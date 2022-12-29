from PyQt5.QtCore import *
from cython_libary import draw
import cython

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef bint checklefttop(object self, int x, int y, int radius2, list storebegin, list storeend):

    cdef short int vertdistance, hordistance, index, xdis, ydis, xdis2, ydis2, ydis3, ydis4, x_diff, y_diff
    cdef float radius, store_y, store_x

    if storebegin:
            for index, point in enumerate(storebegin):
                if point is not None:
                    vertdistance, hordistance, newpoint, radius = draw.get_points(point, index, storeend, QPointF(x, y))
                    x_diff = abs(point.x() - x)
                    y_diff = abs(point.y() - y)
                    store_y = storeend[index].y()
                    store_x = storeend[index].x()
                    if radius <= radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.tlcorner = True
                        self.brcorner = False
                        self.leftedge = False
                        self.topedge = False
                        self.rightedge = False
                        self.bottomedge = False
                        return True
                    elif newpoint.x() <= radius2 and newpoint.y() <= radius2 and vertdistance < 0 and hordistance < 0:
                        if x_diff <= 5 and y < store_y-10:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            self.bottomedge = False
                            return True
                        elif y_diff <= 5 and x < store_x-radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            self.bottomedge = False
                            self.rightedge = False
                            return True
                    elif newpoint.x() <= radius2 and newpoint.y() > -radius2 and vertdistance >= 0 and hordistance < 0:
                        if x_diff <= 5 and y > store_y+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            self.bottomedge = False
                            return True
                        elif y_diff <= 5 and x < store_x-radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            self.bottomedge = False
                            self.rightedge = False
                            return True
                    elif newpoint.x() > -radius2 and newpoint.y() <= radius2 and vertdistance < 0 and hordistance >= 0:
                        if x_diff <= 5 and y < store_y-radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            self.bottomedge = False
                            return True
                        elif y_diff <= 5 and x > store_x+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            self.bottomedge = False
                            self.rightedge = False
                            return True
                    elif newpoint.x() > -radius2 and newpoint.y() > -radius2 and vertdistance >= 0 and hordistance >= 0:
                        if x_diff <= 5 and y > store_y+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            self.bottomedge = False
                            return True
                        elif y_diff <= 5 and x > store_x+radius2:
                            self.prev = self.currentboxx
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            self.rightedge = False
                            self.bottomedge = False
                            return True
            return False

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef bint checkrightbottom(object self, int x, int y, int radius2, list storebegin, list storeend):

    cdef short int vertdistance, hordistance, index, x_diff, y_diff
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
                if radius <= radius2:
                    self.prev = self.currentboxx
                    self.currentboxx = index
                    self.brcorner = True
                    self.tlcorner = False
                    self.bottomedge = False
                    self.rightedge = False
                    self.leftedge = False
                    self.topedge = False
                    return True
                elif newpoint.x() >= -radius2 and newpoint.y() >= -radius2 and vertdistance > 0 and hordistance >= 0:
                    if x_diff <= 5 and y >= store_y - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        self.topedge = False
                        return True
                    elif y_diff <= 5 and x >= store_x - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        self.leftedge = False
                        return True
                elif newpoint.x() >= -radius2 and newpoint.y() < radius2 and vertdistance <= 0 and hordistance >= 0:
                    if x_diff <= 5 and y <= store_y + radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        self.topedge = False
                        return True
                    elif y_diff <= 5 and x >= store_x - 10:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        self.leftedge = False
                        return True
                elif newpoint.x() < 10 and newpoint.y() >= -radius2 and vertdistance > 0 and hordistance < 0:
                    if x_diff <= 5 and y >= store_y - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        self.topedge = False
                        return True
                    elif y_diff <= 5 and x <= store_x + radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        self.leftedge = False
                        return True
                elif newpoint.x() < radius2 and newpoint.y() < radius2 and vertdistance <= 0 and hordistance < 0:
                    if x_diff <= 5 and y <= store_y + radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        self.topedge = False
                        return True
                    elif y_diff <= 5 and x <= store_x - radius2:
                        self.prev = self.currentboxx
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        self.leftedge = False
                        return True

    return False

