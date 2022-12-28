from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from cython_libary import draw
from functions import Draw
from cython_libary import Find_edge


class Mylabel(QWidget):
    signal2 = pyqtSignal(QPointF, QPointF, name='valChanged')

    def __init__(self, parent):
        super(Mylabel, self).__init__()
        self.begin = QPointF()
        self.end = QPointF()
        self.leftedge = False
        self.topedge = False
        self.rightedge = False
        self.bottomedge = False
        self.pressed = False
        self.start = False
        self.edge = False
        self.tlcorner = False
        self.brcorner = False
        self.currentboxx = None
        self.selected = False
        self.prev = None
        self.size2 = self.rect()
        self.currentbox_index = None
        self.image = QPixmap()
        self.parent = parent
        self.brush = QBrush(Qt.red, Qt.SolidPattern)
        self.width = 3
        self.radius = 10
        self.wfactor = 1
        self.hfactor = 1
        self.circlewidth = 3
        self.circlebrushcolor = QBrush(Qt.green, Qt.SolidPattern)
        self.rectbrushcolor = QBrush(QColor(100, 10, 10, 40))
        self.rectlist = []
        self.storebegin = []
        self.storeend = []
        self.storecolor = []
        self.storewidth = []
        self.storecirclewidth = []
        self.storecirclebrushcolor = []
        self.storerectbrushcolor = []
        self.storecircleradius = []
        self.newbegin = []
        self.newend = []
        self.selectedbox_begin = []
        self.selectedbox_end = []
        self.setMouseTracking(True)

    def update_item(self, beginpoint, endpoint, index):
        self.rectlist[index] = QRectF(beginpoint, endpoint)
        self.storebegin[index] = beginpoint
        self.storeend[index] = endpoint
        self.newbegin[self.currentboxx] = beginpoint * self.parent.dpi
        self.newend[self.currentboxx] = endpoint * self.parent.dpi
        if self.selected:
            self.selectedbox_begin[0] = beginpoint
            self.selectedbox_end[0] = endpoint

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        qp.drawPixmap(self.rect(), self.image)
        qp.setRenderHints(QPainter.HighQualityAntialiasing)
        qp.setRenderHint(QPainter.SmoothPixmapTransform)
        br2 = self.brush
        pen = QPen()
        draw.drawcurrentrect(self.pressed, self.edge, pen, qp,
                             br2, self.width, self.rectbrushcolor,
                             self.begin, self.end)
        draw.drawhisrect(pen, qp, self.rectlist, self.storecolor, self.storewidth,
                         self.storerectbrushcolor, self.storecirclewidth, self.storecirclebrushcolor,
                         self.storebegin, self.storecircleradius, self.storeend)

    def mousePressEvent(self, event):
        if not self.selected and event.buttons() == Qt.LeftButton and not self.pressed:
            self.begin = self.end = event.pos()
            self.pressed = True
            self.update()
        elif self.selected and self.edge and event.buttons() == Qt.LeftButton and not self.pressed:
            self.begin = self.end = event.pos()
            self.pressed = True
            self.start = False
            self.update()
        elif self.selected and not self.edge and event.buttons() == Qt.LeftButton and not self.pressed:
            self.start = True

    def mouseMoveEvent(self, event):
        prev = self.prev
        edge = self.edge
        currentboxx = self.currentboxx
        selected = self.selected
        pressed = self.pressed
        parent = self.parent

        if edge and not selected:
            self.storerectbrushcolor[currentboxx] = QBrush(QColor(200, 200, 200, 40))
            self.storecolor[currentboxx] = QColor(248, 255, 106, 255)
            self.update()

        if pressed and not edge and not selected:
            self.end = event.pos()
            self.update()

        elif pressed and selected:
            self.end = event.pos()
            self.update()

        if not selected and edge and pressed and currentboxx is not None:
            beginpoint = self.storebegin[currentboxx]
            endpoint = self.storeend[currentboxx]
            if self.leftedge:
                beginpoint = QPointF(event.pos().x(), beginpoint.y())
                self.update_item(beginpoint, endpoint, currentboxx)
                self.update()
                return
            elif self.topedge:
                beginpoint = QPointF(beginpoint.x(), event.pos().y())
                self.update_item(beginpoint, endpoint, currentboxx)
                self.update()
                return
            elif self.rightedge:
                endpoint = QPointF(event.pos().x(), endpoint.y())
                self.update_item(beginpoint, endpoint, currentboxx)
                self.update()
                return
            elif self.bottomedge:
                endpoint = QPointF(endpoint.x(), event.pos().y())
                self.update_item(beginpoint, endpoint, currentboxx)
                self.update()
                return
            elif self.tlcorner:
                beginpoint = event.pos()
                self.update_item(beginpoint, endpoint, currentboxx)
                self.update()
                return
            elif self.brcorner:
                endpoint = event.pos()
                self.update_item(beginpoint, endpoint, currentboxx)
                self.update()
                return

        elif selected and edge and pressed and currentboxx is not None:
            beginpoint = self.storebegin[parent.index]
            endpoint = self.storeend[parent.index]
            if self.leftedge:
                beginpoint = QPointF(event.pos().x(), beginpoint.y())
                self.update_item(beginpoint, endpoint, parent.index)
                self.update()
                return
            elif self.topedge:
                beginpoint = QPointF(beginpoint.x(), event.pos().y())
                self.update_item(beginpoint, endpoint, parent.index)
                self.update()
                return
            elif self.rightedge:
                endpoint = QPointF(event.pos().x(), endpoint.y())
                self.update_item(beginpoint, endpoint, parent.index)
                self.update()
                return
            elif self.bottomedge:
                endpoint = QPointF(endpoint.x(), event.pos().y())
                self.update_item(beginpoint, endpoint, parent.index)
                self.update()
                return
            elif self.tlcorner:
                beginpoint = event.pos()
                self.update_item(beginpoint, endpoint, parent.index)
                self.update()
                return
            elif self.brcorner:
                endpoint = event.pos()
                self.update_item(beginpoint, endpoint, parent.index)
                self.update()
                return

        if prev is not None and prev != currentboxx and not selected:
            self.storerectbrushcolor[prev] = self.rectbrushcolor
            self.storecolor[prev] = self.brush
            self.update()

        if selected and not pressed and not self.start and\
                (Find_edge.checklefttop(self, event.pos().x(), event.pos().y(), self.radius, self.selectedbox_begin, self.selectedbox_end)
            or Find_edge.checkrightbottom(self, event.pos().x(), event.pos().y(), self.radius, self.selectedbox_begin, self.selectedbox_end)):
            if self.topedge or self.bottomedge:
                self.edge = True
                self.setCursor(Qt.SizeVerCursor)
            elif self.leftedge or self.rightedge:
                self.edge = True
                self.setCursor(Qt.SizeHorCursor)
            elif self.tlcorner or self.brcorner:
                self.edge = True
                self.setCursor(Qt.ClosedHandCursor)

        elif not selected and not pressed and \
           (Find_edge.checklefttop(self, event.pos().x(), event.pos().y(), self.radius, self.storebegin, self.storeend)
            or Find_edge.checkrightbottom(self, event.pos().x(), event.pos().y(), self.radius, self.storebegin, self.storeend)):
            if self.topedge or self.bottomedge:
                self.edge = True
                self.setCursor(Qt.SizeVerCursor)
            elif self.leftedge or self.rightedge:
                self.edge = True
                self.setCursor(Qt.SizeHorCursor)
            elif self.tlcorner or self.brcorner:
                self.edge = True
                self.setCursor(Qt.ClosedHandCursor)

        elif not pressed:
            if currentboxx is not None and not selected:
                self.storerectbrushcolor[currentboxx] = self.rectbrushcolor
                self.storecolor[currentboxx] = self.brush
            self.rightedge = False
            self.bottomedge = False
            self.topedge = False
            self.leftedge = False
            self.edge = False
            self.tlcorner = False
            self.brcorner = False
            self.unsetCursor()

    def mouseReleaseEvent(self, event):
        parent = self.parent
        if not self.selected and not self.edge and event.button() == Qt.LeftButton:
            Draw.store_data(self.storebegin, self.storeend, self.rectlist, self.begin,
                            self.end, self.storecolor, self.brush, self.storewidth,
                            self.width, self.storecirclewidth, self.circlewidth,
                            self.storecirclebrushcolor, self.circlebrushcolor,
                            self.storerectbrushcolor, self.rectbrushcolor,
                            self.storecircleradius, self.radius,
                            self.newbegin, self.newend)
            self.currentboxx = len(self.rectlist) - 1
            index = len(self.rectlist) - 1
            self.signal2.emit(QPointF(self.newbegin[index].x()*self.wfactor, self.newbegin[index].y()*self.hfactor),
                              QPointF(self.newend[index].x()*self.wfactor, self.newend[index].y()*self.hfactor))
            parent.popupdialog(event.globalPos(), parent.dialog, self)
            self.pressed = False
            self.update()
        elif self.edge and event.button() == Qt.LeftButton:
            currentboxx = self.currentboxx
            beginx = format(self.newbegin[currentboxx].x()*self.wfactor, '.3f')
            beginy = format(self.newbegin[currentboxx].y()*self.hfactor, '.3f')
            endx = format(self.newend[currentboxx].x()*self.wfactor, '.3f')
            endy = format(self.newend[currentboxx].y()*self.hfactor, '.3f')
            parent.templist[currentboxx]['Init Pos'] = (beginx, beginy)
            parent.templist[currentboxx]['final Pos'] = (endx, endy)
            name = parent.win.listWidget_2.item(currentboxx).data(Qt.UserRole)[0]
            parent.win.listWidget_2.item(currentboxx).setText(f'{name}'
                                                                        f'  Begin: ({beginx},{beginy})'
                                                                        f'  End: ({endx},{endy})')
            self.pressed = False
            self.update()
        self.start = False

    def clear(self):
        self.rectlist.clear()
        self.storebegin.clear()
        self.storeend.clear()
        self.newbegin.clear()
        self.newend.clear()
        self.storerectbrushcolor.clear()
        self.storecolor.clear()
        self.storecirclewidth.clear()
        self.storecircleradius.clear()
        self.storecirclebrushcolor.clear()
        self.parent.win.listWidget_2.clear()
        self.currentboxx = None
        self.prev = None
        self.selected = False
        self.parent.index = None
