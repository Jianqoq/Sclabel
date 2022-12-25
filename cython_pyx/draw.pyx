from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QBrush
import cython

@cython.wraparound(False)
@cython.boundscheck(False)
def store_data(list beginlist, list endlist, list rectlist, begin, end, list storecolor,
               color, list storewidth, int width, list storecirclewidth, int circlewidth,
               list storecirclebrushcolor, circlebrushcolor, list storebrushcolor, brushcolor,
               list storecircleradius, int radius):
    beginlist.append(begin)
    endlist.append(end)
    rectlist.append(QRect(begin, end))
    storecolor.append(color)
    storewidth.append(width)
    storecirclewidth.append(circlewidth)
    storecirclebrushcolor.append(circlebrushcolor)
    storebrushcolor.append(brushcolor)
    storecircleradius.append(radius)


def get_points(point, int index, list endlist, pos):
        cdef int vertdistance = point.y() - endlist[index].y()
        cdef int hordistance = point.x() - endlist[index].x()
        newpoint = point - pos
        cdef int radius = QPoint.manhattanLength(pos - point)
        return vertdistance, hordistance, newpoint, radius

@cython.wraparound(False)
@cython.boundscheck(False)
def drawhisrect(pen, qp, list rectlist, list storecolor, list storewidth, list storerectbrushcolor, list storecirclewidth,
                list storecirclebrushcolor, list storebegin, list storecircleradius, list storeend):

    cdef int length = len(rectlist)
    cdef int index, width, radius
    if length > 0:
        for index, rect in enumerate(rectlist):
            if rect is not None:
                color = storecolor[index]
                width = storewidth[index]
                pen.setBrush(color)
                pen.setWidth(width)
                qp.setPen(pen)
                color = storerectbrushcolor[index]
                qp.setBrush(color)
                qp.drawRect(rect)
                width = storecirclewidth[index]
                pen.setWidth(width)
                color = storecirclebrushcolor[index]
                qp.setBrush(color)
                qp.setPen(pen)
                beginpoint = storebegin[index]
                radius = storecircleradius[index]
                qp.drawEllipse(beginpoint, radius, radius)
                color = storecolor[index]
                pen.setBrush(color)
                brushcolor = storecirclebrushcolor[index]
                qp.setBrush(brushcolor)
                width = storecirclewidth[index]
                pen.setWidth(width)
                qp.setPen(pen)
                endpoint = storeend[index]
                qp.drawEllipse(endpoint, radius, radius)
    else:
        return


def drawcurrentrect(bint pressed, bint edge, pen, qp, br2, int width, rectbrushcolor, begin, end):
    if pressed and not edge:
        pen.setBrush(br2)
        pen.setWidth(width)
        qp.setPen(pen)
        qp.setBrush(rectbrushcolor)
        qp.drawRect(QRect(begin, end))
        return
    else:
        return