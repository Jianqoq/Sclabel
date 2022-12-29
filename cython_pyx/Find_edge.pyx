from PyQt5.QtCore import *
from cython_libary import draw
import cython

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef bint checklefttop(object self, int x, int y, int radius2, list storebegin, list storeend):

    cdef short int vertdistance, hordistance, index, x_diff, y_diff, new_y, new_x
    cdef float radius, store_y, store_x

    if storebegin:
            for index, point in enumerate(storebegin):
                if point is not None:
                    vertdistance, hordistance, newpoint, radius = draw.get_points(point, index, storeend, QPointF(x, y))
                    x_diff = abs(point.x() - x)
                    y_diff = abs(point.y() - y)
                    store_y = storeend[index].y()
                    store_x = storeend[index].x()
                    new_y = newpoint.y()
                    new_x = newpoint.x()
                    if radius <= radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.tlcorner = True
                        self.brcorner = False
                        toggle(self, '5')
                        return True
                    elif new_x <= radius2 and new_y <= radius2 and vertdistance < 0 and hordistance < 0:
                        if x_diff <= 5 and y < store_y-10:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '4')
                            return True
                        elif y_diff <= 5 and x < store_x-radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '3')
                            return True
                    elif new_x <= radius2 and new_y > -radius2 and vertdistance >= 0 and hordistance < 0:
                        if x_diff <= 5 and y > store_y+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '4')
                            return True
                        elif y_diff <= 5 and x < store_x-radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '3')
                            return True
                    elif new_x > -radius2 and new_y <= radius2 and vertdistance < 0 and hordistance >= 0:
                        if x_diff <= 5 and y < store_y-radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '4')
                            return True
                        elif y_diff <= 5 and x > store_x+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '3')
                            return True
                    elif new_x > -radius2 and new_y > -radius2 and vertdistance >= 0 and hordistance >= 0:
                        if x_diff <= 5 and y > store_y+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '4')
                            return True
                        elif y_diff <= 5 and x > store_x+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            toggle(self, '3')
                            return True
            return False

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef bint checkrightbottom(object self, int x, int y, int radius2, list storebegin, list storeend):

    cdef short int vertdistance, hordistance, index, x_diff, y_diff, new_y, new_x
    cdef float radius
    cdef float store_y, store_x

    if storeend:
        for index, point in enumerate(storeend):
            if point is not None:
                vertdistance, hordistance, newpoint, radius = draw.get_points(point, index, storebegin, QPointF(x, y))
                x_diff = abs(point.x() - x)
                y_diff = abs(point.y() - y)
                store_y = storebegin[index].y()
                store_x = storebegin[index].x()
                new_y = newpoint.y()
                new_x = newpoint.x()
                if radius <= radius2:
                    self.prev = self.currentboxx
                    self.currentboxx = index
                    self.brcorner = True
                    self.tlcorner = False
                    toggle(self, '5')
                    return True
                elif new_x >= -radius2 and new_y >= -radius2 and vertdistance > 0 and hordistance >= 0:
                    if x_diff <= 5 and y >= store_y - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '2')
                        return True
                    elif y_diff <= 5 and x >= store_x - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '1')
                        return True
                elif new_x >= -radius2 and new_y < radius2 and vertdistance <= 0 and hordistance >= 0:
                    if x_diff <= 5 and y <= store_y + radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '2')
                        return True
                    elif y_diff <= 5 and x >= store_x - 10:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '1')
                        return True
                elif new_x < 10 and new_y >= -radius2 and vertdistance > 0 and hordistance < 0:
                    if x_diff <= 5 and y >= store_y - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '2')
                        return True
                    elif y_diff <= 5 and x <= store_x + radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '1')
                        return True
                elif new_x < radius2 and new_y < radius2 and vertdistance <= 0 and hordistance < 0:
                    if x_diff <= 5 and y <= store_y + radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '2')
                        return True
                    elif y_diff <= 5 and x <= store_x - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        toggle(self, '1')
                        return True

    return False

cpdef void toggle(object self, str number):
    cdef dict dictionary = {
    '1': False,
    '2': False,
    '3': False,
    '4': False,
    '5': False
    }
    dictionary[number] = True
    self.bottomedge = dictionary['1']
    self.rightedge = dictionary['2']
    self.topedge = dictionary['3']
    self.leftedge = dictionary['4']
    return
