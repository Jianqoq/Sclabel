from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLabel
from cython_libary import draw
from functions import Draw
from cython_libary import Find_edge


class Mylabel(QLabel):
    signal2 = pyqtSignal(int, QPoint, QPoint, name='valChanged')

    def __init__(self, parent=None):
        super(Mylabel, self).__init__(parent)
        self.begin = QPoint()
        self.end = QPoint()
        self.setFocusPolicy(Qt.StrongFocus)
        self.leftedge = False
        self.topedge = False
        self.rightedge = False
        self.bottomedge = False
        self.pressed = False
        self.edge = False
        self.tlcorner = False
        self.brcorner = False
        self.currentboxx = None
        self.currentbox_index = None
        self.parent = parent
        self.brush = QBrush(Qt.red, Qt.SolidPattern)
        self.width = 3
        self.radius = 10
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
        self.setMouseTracking(True)
        self.free_cursor_on_side = 0

    def update_item(self, beginpoint, endpoint):
        self.rectlist[self.currentboxx] = QRect(beginpoint, endpoint)
        self.storebegin[self.currentboxx] = beginpoint
        self.storeend[self.currentboxx] = endpoint
        self.newbegin[self.currentboxx] = beginpoint * self.parent.dpi
        self.newend[self.currentboxx] = endpoint * self.parent.dpi

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        qp.setRenderHints(QPainter.HighQualityAntialiasing)
        br2 = self.brush
        pen = QPen()
        draw.drawcurrentrect(self.pressed, self.edge, pen, qp,
                             br2, self.width, self.rectbrushcolor,
                             self.begin, self.end)
        draw.drawhisrect(pen, qp, self.rectlist, self.storecolor, self.storewidth,
                         self.storerectbrushcolor, self.storecirclewidth, self.storecirclebrushcolor,
                         self.storebegin, self.storecircleradius, self.storeend)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton and not self.pressed:
            self.begin = self.end = event.pos()
            self.pressed = True
            self.update()
        elif event.buttons() == Qt.LeftButton and not self.pressed and self.edge:
            self.currentbox_index = self.currentboxx

    def mouseMoveEvent(self, event):
        if self.edge:
            self.storerectbrushcolor[self.currentboxx] = QBrush(QColor(200, 200, 200, 40))
            self.storecolor[self.currentboxx] = QColor(248, 255, 106, 255)
            self.update()
        if self.pressed and not self.edge:
            self.end = event.pos()
            self.update()
        if self.edge and self.pressed and self.currentboxx is not None:
            beginpoint = self.storebegin[self.currentboxx]
            endpoint = self.storeend[self.currentboxx]
            if self.leftedge:
                beginpoint = QPoint(event.pos().x(), beginpoint.y())
                self.update_item(beginpoint, endpoint)
                self.update()
                return
            elif self.topedge:
                beginpoint = QPoint(beginpoint.x(), event.pos().y())
                self.update_item(beginpoint, endpoint)
                self.update()
                return
            elif self.rightedge:
                endpoint = QPoint(event.pos().x(), endpoint.y())
                self.update_item(beginpoint, endpoint)
                self.update()
                return
            elif self.bottomedge:
                endpoint = QPoint(endpoint.x(), event.pos().y())
                self.update_item(beginpoint, endpoint)
                self.update()
                return
            elif self.tlcorner:
                beginpoint = event.pos()
                self.update_item(beginpoint, endpoint)
                self.update()
                return
            elif self.brcorner:
                endpoint = event.pos()
                self.update_item(beginpoint, endpoint)
                self.update()
                return

        if (Find_edge.checklefttop(self, event.pos().x(), event.pos().y(), self.radius, self.storebegin, self.storeend)
            or Find_edge.checkrightbottom(self, event.pos().x(), event.pos().y(), self.radius, self.storebegin,
                                          self.storeend)) and not self.pressed:
            if self.topedge:
                self.edge = True
                self.setCursor(Qt.SizeVerCursor)
            elif self.leftedge:
                self.edge = True
                self.setCursor(Qt.SizeHorCursor)
            elif self.bottomedge:
                self.edge = True
                self.setCursor(Qt.SizeVerCursor)
            elif self.rightedge:
                self.edge = True
                self.setCursor(Qt.SizeHorCursor)
            elif self.tlcorner:
                self.edge = True
                self.setCursor(Qt.ClosedHandCursor)
            elif self.brcorner:
                self.edge = True
                self.setCursor(Qt.ClosedHandCursor)

        elif not self.pressed:
            self.rightedge = False
            self.bottomedge = False
            self.topedge = False
            self.leftedge = False
            self.edge = False
            self.tlcorner = False
            self.brcorner = False
            self.unsetCursor()
            if self.currentboxx is not None:
                self.storerectbrushcolor[self.currentboxx] = self.rectbrushcolor
                self.storecolor[self.currentboxx] = self.brush

    def mouseReleaseEvent(self, event):
        if not self.edge:
            Draw.store_data(self.storebegin, self.storeend, self.rectlist, self.begin, self.end, self.storecolor, self.brush,
                            self.storewidth, self.width, self.storecirclewidth, self.circlewidth, self.storecirclebrushcolor,
                            self.circlebrushcolor, self.storerectbrushcolor, self.rectbrushcolor, self.storecircleradius,
                            self.radius, self.newbegin, self.newend)
            self.currentboxx = len(self.rectlist) - 1
            index = len(self.rectlist) - 1
            self.signal2.emit(index, self.newbegin[index], self.newend[index])
            self.parent.popupdialog(event.globalPos())
        elif self.edge:
            beginx = self.newbegin[self.currentboxx].x()
            beginy = self.newbegin[self.currentboxx].y()
            endx = self.newend[self.currentboxx].x()
            endy = self.newend[self.currentboxx].y()
            self.parent.templist[self.currentboxx]['Init Pos'] = (beginx, beginy)
            self.parent.templist[self.currentboxx]['final Pos'] = (endx, endy)
            self.parent.win.listWidget_2.item(self.currentboxx).setText(f'{len(self.rectlist) - 1}'
                                                                    f'  Begin: ({beginx},{beginy})'
                                                                    f'  End: ({endx},{endy})')
        self.pressed = False
        self.update()

    def clear(self):
        self.rectlist.clear()
        self.storebegin.clear()
        self.storeend.clear()
        self.newbegin.clear()
        self.newend.clear()