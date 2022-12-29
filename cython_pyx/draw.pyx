from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import QBrush
import cython
from time import time

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef void store_data(list beginlist, list endlist, list rectlist, begin, end, list storecolor,
               color, list storewidth, int width, list storecirclebrushcolor, circlebrushcolor,
                list storebrushcolor, brushcolor, list storecircleradius, float radius, newbegin, newend):
    beginlist.append(begin)
    endlist.append(end)
    rectlist.append(QRectF(begin, end))
    storecolor.append(color)
    storewidth.append(width)
    storecirclebrushcolor.append(circlebrushcolor)
    storebrushcolor.append(brushcolor)
    storecircleradius.append(radius)
    newend.append(end*1.5)
    newbegin.append(begin*1.5)


def get_points(point, int index, list endlist, pos):
        cdef float vertdistance = point.y() - endlist[index].y()
        cdef float hordistance = point.x() - endlist[index].x()
        newpoint = point - pos
        cdef float radius = QPointF.manhattanLength(pos - point)
        return vertdistance, hordistance, newpoint, radius

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef void drawhisrect(pen, qp, list rectlist, list storecolor, list storewidth, list storerectbrushcolor,
                list storecirclebrushcolor, list storebegin, list storecircleradius, list storeend):

    cdef int index, width, radius
    if rectlist:
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
                width = storewidth[index]
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
                width = storewidth[index]
                pen.setWidth(width)
                qp.setPen(pen)
                endpoint = storeend[index]
                qp.drawEllipse(endpoint, radius, radius)
        return
    else:
        return


cpdef void drawcurrentrect(bint pressed, bint edge, pen, qp, br2, int width, rectbrushcolor, begin, end):
    if pressed and not edge:
        pen.setBrush(br2)
        pen.setWidth(width)
        qp.setPen(pen)
        qp.setBrush(rectbrushcolor)
        qp.drawRect(QRectF(begin, end))
        return
    else:
        return
