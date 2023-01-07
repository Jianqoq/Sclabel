import configparser
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QPen
from cython_libary import calculation
from UI.cap_pic_ui import *
from functions.Image_process import *


class MyLabel2(QLabel):
    def __init__(self, temploc, temp, img_width,
                 img_height, half_width, half_height, main_win,
                 quality, hide, parent=None):
        super(MyLabel2, self).__init__(parent=parent)
        self.mainwindow = main_win
        self.factor1 = main_win.dpi
        self.name2 = main_win.name
        self.save = main_win.readpath
        self.hide2 = hide
        self.x0 = 0
        self.y0 = 0
        main_win_width = int(main_win.width)
        main_win_height = int(main_win.height)
        self.main_win_width = main_win_width
        self.main_win_height = main_win_height
        self.x1, self.y1 = calculation.label2_event_pos(main_win_width, main_win_height, self.factor1)
        self.path = main_win.path
        self.pixmap = None
        self.name = None
        self.tempfile = None
        self.temploc = temploc
        self.temp = temp
        self.new_width = int(img_width - self.x1 // self.factor1)
        self.new_high = int(img_height - self.y1 // self.factor1)
        self.half_width = half_width
        self.half_height = half_height
        self.flag = False
        self.quality = quality
        self.count = 0
        self.check = False
        self.nparray = None
        self.toggle = False
        self.pressed = False
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
            x = event.pos().x()
            y = event.pos().y()
            factor = self.factor1
            self.tempfile, self.name, self.nparray = readimage(self.temploc, int(x*factor), int(y*factor),
                                                               self.main_win_width, self.main_win_height,
                                                               self.imagedict[self.index],
                                                               self.imagedict[self.index][2])
            pixmap = self.pixmap = QPixmap(self.name)
            pixmap.setDevicePixelRatio(factor)
            self.setPixmap(pixmap)
            self.resize(int(pixmap.width()//factor),
                        int(pixmap.height()//factor))
            self.pressed = True
            self.move(x, y)
        elif event.buttons() == Qt.RightButton and self.name and self.check:
            factor = self.factor1
            self.rectlist.clear()
            self.initpos = QPoint()
            self.finalpos = QPoint()
            self.tempfile.close()
            os.unlink(self.name)
            pixmap = self.pixmap = QPixmap(self.temploc)
            pixmap.setDevicePixelRatio(factor)
            self.resize(int(pixmap.width()//factor),
                        int(pixmap.height()//factor))
            self.move(0, 0)
            self.setPixmap(pixmap)
            self.pressed = False
            self.check = False
            x0 = event.globalPos().x()
            y0 = event.globalPos().y()
            self.rect = QRect(x0, y0, self.x1, self.y1)
            self.repaint()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Return and not self.pressed:
            index = self.index
            new_path = self.checkrepeatname(self.save, self.name2, self.imagedict[index][1])
            savefullimg(self.temploc, new_path, self.imagedict[index], self.imagedict[index][2])
            self.dolabelling(new_path, self.mainwindow)

        elif event.key() == Qt.Key_Return and self.nparray is not None:
            index = self.index
            self.tempfile.close()
            os.unlink(self.name)
            self.temp.cleanup()
            path = self.checkrepeatname(self.save, self.name2, self.imagedict[index][1])
            if not os.path.exists(self.save):
                os.makedirs(self.save)
            cv2.imwrite(path, self.nparray, [self.imagedict[index][0], self.imagedict[index][2]])
            if self.mainwindow is None:
                self.parent().close()
            self.dolabelling(path, self.mainwindow)
        elif event.key() == Qt.Key_Escape and not self.toggle:
            if self.check:
                self.tempfile.close()
                self.temp.cleanup()
                os.unlink(self.name)
            self.toggle = True
            self.parent().close() if not self.hide2 else (self.mainwindow.show(), self.parent().close())

    def mouseMoveEvent(self, event):
        if not self.check:
            x0 = event.globalPos().x()
            y0 = event.globalPos().y()
            self.rect = QRect(x0, y0, self.x1, self.y1)
            self.update()
            self.x0 = x0
            self.y0 = y0

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.check:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
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

    def dolabelling(self, path, mainwindow):
        if mainwindow.win.checkBox_2.isChecked():
            self.parent().close()
            mainwindow.directannotate(path)
            mainwindow.labelling = True
        else:
            self.parent().close()
            mainwindow.show()


class OpenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win1 = QMainWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.new_win = New_Ui_MainWindow()
        self.setFocusPolicy(Qt.NoFocus)
