import configparser
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen
from functions.calculation import *
from UI.cap_pic_ui import *
from functions.Image_process import *


class MyLabel2(QLabel):
    def __init__(self, filename, temploc, temp, save, name,
                 posx, posy, window, factor, new_width,
                 new_high, half_width, half_height, main_win,
                 quality, path, parent=None):
        super(MyLabel2, self).__init__(parent=parent)
        self.x0 = 0
        self.y0 = 0
        self.x1 = int(posx)
        self.y1 = int(posy)
        self.path = path
        self.pixmap = None
        self.name = None
        self.tempfile = None
        self.temploc = temploc
        self.temp = temp
        self.new_width = new_width
        self.new_high = new_high
        self.half_width = half_width
        self.half_height = half_height
        self.flag = False
        self.quality = quality
        self.filename = filename
        self.factor1 = factor
        self.name2 = name
        self.save = save
        self.count = 0
        self.check = False
        self.nparray = None
        self.toggle = False
        self.pressed = False
        self.window = window
        self.mainwindow = main_win
        self.imagedict = None
        self.start = False
        self.index = self.getformat()
        self.rect = QRect(0, 0, 0, 0)
        self.rectlist = []
        self.initpos = QPoint()
        self.finalpos = QPoint()
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton and not self.check:
            self.check = True
            self.rect = QRect(0, 0, 0, 0)
            x = event.pos().x()
            y = event.pos().y()
            self.tempfile, self.name, self.nparray = readimage(self.temploc,
                                                               int(x*self.factor1),
                                                               int(y*self.factor1),
                                                               self.x1, self.y1,
                                                               self.imagedict[self.index],
                                                               self.imagedict[self.index][2])
            self.pixmap = QPixmap(self.name)
            self.pixmap.setDevicePixelRatio(self.factor1)
            self.setPixmap(self.pixmap)
            self.resize(int(self.pixmap.width()//self.factor1),
                        int(self.pixmap.height()//self.factor1))
            self.pressed = True
            self.move(x, y)
        elif event.buttons() == Qt.RightButton and self.name and self.check:
            self.rectlist.clear()
            self.initpos = QPoint()
            self.finalpos = QPoint()
            self.tempfile.close()
            os.unlink(self.name)
            self.pixmap = QPixmap(self.temploc)
            self.pixmap.setDevicePixelRatio(self.factor1)
            self.resize(int(self.pixmap.width()//self.factor1),
                        int(self.pixmap.height()//self.factor1))
            self.move(0, 0)
            self.setPixmap(self.pixmap)
            self.pressed = False
            self.check = False

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Return and not self.pressed:
            new_path = self.checkrepeatname(self.save, self.name2, self.imagedict[self.index][1])
            savefullimg(self.temploc, new_path, self.imagedict[self.index], self.imagedict[self.index][2])
            self.dolabelling(new_path)

        elif event.key() == Qt.Key_E and self.nparray is not None:
            self.tempfile.close()
            os.unlink(self.name)
            self.temp.cleanup()
            path = self.checkrepeatname(self.save, self.name2, self.imagedict[self.index][1])
            if not os.path.exists(self.save):
                os.makedirs(self.save)
            cv2.imwrite(path, self.nparray, [self.imagedict[self.index][0], self.imagedict[self.index][2]])
            if self.mainwindow is None:
                self.window.close()
            self.dolabelling(path)
        elif event.key() == Qt.Key_Escape and not self.toggle:
            if self.check:
                self.tempfile.close()
                self.temp.cleanup()
                os.unlink(self.name)
            self.toggle = True
            if self.mainwindow is None:
                self.window.close()
            else:
                self.mainwindow.show()
                self.window.close()

    def mouseMoveEvent(self, event):
        if not self.check:
            self.x0 = event.globalPos().x()
            self.y0 = event.globalPos().y()
            x, y = label2_event_pos(self.x1, self.y1, self.factor1)
            self.rect = QRect(self.x0, self.y0, x, y)
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.drawRect(self.rect)

    def getformat(self):
        config = configparser.ConfigParser()
        config.read(rf'{self.path}\{self.mainwindow.configname}')
        return config.get('Saving setting', 'image format')

    def checkrepeatname(self, dir: str, name: str, suffix: str):
        file = f'{dir}/{name}{str(self.count)}{suffix}'
        while os.path.exists(file):
            self.count += 1
            file = f'{dir}/{name}{str(self.count)}{suffix}'
        return file

    def dolabelling(self, path):
        if self.mainwindow.win.checkBox_2.isChecked():
            self.window.close()
            self.mainwindow.directannotate(path)
            self.mainwindow.labelling = True
        else:
            self.window.close()
            self.mainwindow.show()


class OpenWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.win1 = QMainWindow()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.new_win = New_Ui_MainWindow()
        self.setFocusPolicy(Qt.NoFocus)