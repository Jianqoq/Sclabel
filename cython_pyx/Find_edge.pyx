from PyQt5.QtCore import *
import draw
import cython

@cython.wraparound(False)
@cython.boundscheck(False)
def checklefttop(object self, int x, int y, int radius2, list storebegin, list storeend):

    cdef short int vertdistance, hordistance, index, xdis, ydis, xdis2, ydis2, ydis3, ydis4
    cdef int length = len(storebegin)
    cdef int circleradius = radius2

    if length > 0:
            for index, point in enumerate(self.storebegin):
                if point is not None:
                    vertdistance, hordistance, newpoint, radius = draw.get_points(point, index, self.storeend, QPoint(x, y))
                    if radius <= self.radius and not self.pressed:
                        self.currentboxx = index
                        self.tlcorner = True
                        self.brcorner = False
                        self.leftedge = False
                        self.topedge = False
                        return True
                    elif newpoint.x() <= self.radius and newpoint.y() <= self.radius and vertdistance < 0 and \
                            hordistance < 0 and radius > self.radius:
                        if abs(point.x() - x) <= 5 and not self.pressed and y < self.storeend[index].y()-10:
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            return True
                        elif abs(point.y() - y) <= 5 and not self.pressed and x < self.storeend[index].x()-self.radius\
                                and radius > self.radius:
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            self.bottomedge = False
                            return True
                    elif newpoint.x() <= self.radius and newpoint.y() > -self.radius and vertdistance >= 0 and hordistance < 0 and radius > self.radius:
                        if abs(point.x() - x) <= 5 and not self.pressed and y > self.storeend[index].y()+self.radius\
                                and radius > self.radius:
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            return True
                        elif abs(point.y() - y) <= 5 and not self.pressed and x < self.storeend[index].x()-self.radius\
                                and radius > self.radius:
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            self.bottomedge = False
                            return True
                    elif newpoint.x() > -self.radius and newpoint.y() <= self.radius and vertdistance < 0 and hordistance >= 0 and radius > self.radius:
                        if abs(point.x() - x) <= 5 and not self.pressed and y < self.storeend[index].y()-self.radius\
                                and radius > self.radius:
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            return True
                        elif abs(point.y() - y) <= 5 and not self.pressed and x > self.storeend[index].x()+self.radius\
                                and radius > self.radius:
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            self.bottomedge = False
                            return True
                    elif newpoint.x() > -self.radius and newpoint.y() > -self.radius and vertdistance >= 0 and hordistance >= 0 and radius > self.radius:
                        if abs(point.x() - x) <= 5 and not self.pressed and y > self.storeend[index].y()+self.radius\
                                and radius > self.radius:
                            self.currentboxx = index
                            self.leftedge = True
                            self.topedge = False
                            self.rightedge = False
                            return True
                        elif abs(point.y() - y) <= 5 and not self.pressed and x > self.storeend[index].x()+self.radius\
                                and radius > self.radius:
                            self.currentboxx = index
                            self.topedge = True
                            self.leftedge = False
                            return True
            return False

@cython.wraparound(False)
@cython.boundscheck(False)
def checkrightbottom(object self, int x, int y, int radius2, list storebegin, list storeend):

    cdef short int vertdistance, hordistance, index
    cdef int length = len(storeend)
    cdef int circleradius = radius2

    if length > 0:
        for index, point in enumerate(storeend):
            if point is not None:
                vertdistance, hordistance, newpoint, radius = draw.get_points(point, index, storebegin, QPoint(x, y))
                if radius <= circleradius and not self.pressed:
                    self.currentboxx = index
                    self.brcorner = True
                    self.tlcorner = False
                    self.bottomedge = False
                    self.rightedge = False
                    return True
                elif newpoint.x() >= -self.radius and newpoint.y() >= -circleradius and vertdistance > 0 and hordistance >= 0 and radius > circleradius:
                    if abs(point.x() - x) <= 5 and not self.pressed and y >= storebegin[index].y() - circleradius:
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        return True
                    elif abs(point.y() - y) <= 5 and not self.pressed and x >= storebegin[index].x() - circleradius\
                            and radius > circleradius:
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        return True
                elif newpoint.x() >= -circleradius and newpoint.y() < circleradius and vertdistance <= 0 and hordistance >= 0 and radius > circleradius:
                    if abs(point.x() - x) <= 5 and not self.pressed and y <= storebegin[index].y() + circleradius:
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        return True
                    elif abs(point.y() - y) <= 5 and not self.pressed and x >= storebegin[index].x() - 10\
                            and radius > circleradius:
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        return True
                elif newpoint.x() < 10 and newpoint.y() >= -circleradius and vertdistance > 0 and hordistance < 0 and radius > circleradius:
                    if abs(point.x() - x) <= 5 and not self.pressed and y >= storebegin[index].y() - circleradius:
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        return True
                    elif abs(point.y() - y) <= 5 and not self.pressed and x <= storebegin[index].x() + circleradius\
                            and radius > circleradius:
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        return True
                elif newpoint.x() < circleradius and newpoint.y() < circleradius and vertdistance <= 0 and hordistance < 0 and radius > circleradius:
                    if abs(point.x() - x) <= 5 and not self.pressed and y <= storebegin[index].y() + circleradius:
                        self.currentboxx = index
                        self.rightedge = True
                        self.bottomedge = False
                        self.leftedge = False
                        return True
                    elif abs(point.y() - y) <= 5 and not self.pressed and x <= storebegin[index].x() - circleradius \
                            and radius > circleradius:
                        self.currentboxx = index
                        self.bottomedge = True
                        self.rightedge = False
                        self.topedge = False
                        return True

    return False

