from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import QBrush



def store_data(beginlist: list, endlist: list, rectlist: list, begin: QPointF, end: QPointF, storecolor: list,
               color: QBrush, storewidth: list, width: int, storecirclebrushcolor: list, circlebrushcolor: QBrush, storebrushcolor: list, brushcolor: QBrush,
               storecircleradius: list, radius: int, newbegin, newend):
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


def get_points(point: QPointF, index: int, endlist: list, pos: QPointF):
        vertdistance = point.y() - endlist[index].y()
        hordistance = point.x() - endlist[index].x()
        newpoint = point - pos
        radius = QPointF.manhattanLength(pos - point)
        return vertdistance, hordistance, newpoint, radius


def drawhisrect(pen, qp, rectlist, storecolor, storewidth, storerectbrushcolor, storecirclebrushcolor,
             storebegin, storecircleradius,storeend):

    if rectlist:
        for index, rect in enumerate(rectlist):
            if rect is not None:
                pen.setBrush(storecolor[index])
                pen.setWidth(storewidth[index])
                qp.setPen(pen)
                qp.setBrush(storerectbrushcolor[index])
                qp.drawRect(rect)
                pen.setBrush(storecolor[index])
                pen.setWidth(storewidth[index])
                qp.setBrush(storecirclebrushcolor[index])
                qp.setPen(pen)
                qp.drawEllipse(storebegin[index], storecircleradius[index], storecircleradius[index])
                pen.setBrush(storecolor[index])
                qp.setBrush(storecirclebrushcolor[index])
                pen.setWidth(storewidth[index])
                qp.setPen(pen)
                qp.drawEllipse(storeend[index], storecircleradius[index], storecircleradius[index])
    else:
        return


def drawcurrentrect(pressed, edge, pen, qp, br2, width, rectbrushcolor, begin, end):
    if pressed and not edge:
        pen.setBrush(br2)
        pen.setWidth(width)
        qp.setPen(pen)
        qp.setBrush(rectbrushcolor)
        qp.drawRect(QRectF(begin, end))
    else:
        return
