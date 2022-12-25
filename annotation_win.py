import ctypes
import cv2
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QColorDialog, QMenu, QAction, QDialog, QDialogButtonBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIntValidator
from UI.class_dialog import *
from annotation_rect import *
from UI.rect_settingpanel import *
from functions.graphic_effect import *
from functions.file_manipulation import  *
from UI import Dialog2
from UI.Message_Box import *


class QLineEditMask(QMainWindow):
    def __init__(self, width, height, mainwindow):
        super(QLineEditMask, self).__init__()
        self.win = Ui_Form()
        self.win.setupUi(self)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setMaximumSize(self.size())
        self.setMinimumSize(self.size())
        self.dpi = self.devicePixelRatioF()
        self.win.lineEdit.hide()
        self.win.lineEdit_2.hide()
        self.win.dockWidget.hide()
        self.win.dockWidget_3.hide()
        self.validator = QIntValidator()
        self.win.lineEdit.setValidator(self.validator)
        self.win.lineEdit_2.setValidator(self.validator)
        self.action1 = QAction("Line Color")
        self.action2 = QAction('Rect Brush Color')
        self.action3 = QAction('Cir Brush Color')
        self.action4 = QAction('Delete')
        self.win.pushButton.setMenu(self.menu())
        self.win.pushButton_3.setMenu(self.menu2())
        self.action1.triggered.connect(self.rectborder_color_picker)
        self.action2.triggered.connect(self.rectbrush_color_picker)
        self.action3.triggered.connect(self.circle_color_picker)
        self.action4.triggered.connect(self.removeitem)
        self.win.dockWidget.installEventFilter(self)
        self.win.listWidget_2.installEventFilter(self)
        self.win.dockWidget_3.installEventFilter(self)
        self.win.lineEdit_3.installEventFilter(self)
        self.installEventFilter(self)
        self.width = width
        self.height = height
        self.label = Mylabel(self)
        self.dialog = Dialog(self)
        shadow(self.dialog)
        self.dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.dialog.setAttribute(Qt.WA_TranslucentBackground)
        self.mainwindow = mainwindow
        self.last_file = read_savedfile(self.mainwindow)
        self.name = None
        self.toggle = False
        self.toggle2 = False
        self.toggle3 = False
        self.toggle4 = False
        self.selected = False
        self.path = None
        self.filename = None
        self.imgname = None
        self.basename = None
        self.saveloc = None
        self.color = None
        self.displayed = False
        self.dir = False
        self.singal = False
        self.toggle5 = False
        self.count = 0
        self.storelabeling = {
                              'Image path': self.imgname,
                              'Image_width': 0,
                              'Image_height': 0,
                              'Label': []
                              }
        self.templist = []
        self.originpos = self.win.pushButton_5.pos()
        self.originpos2 = self.win.horizontalSlider.pos()
        self.win.pushButton_2.clicked.connect(self.showlineedit)
        self.win.pushButton_5.clicked.connect(self.showlineedit_2)
        self.win.pushButton_6.clicked.connect(self.showslider)
        self.win.lineEdit.textEdited.connect(self.update)
        self.win.lineEdit_2.textEdited.connect(self.update2)
        self.win.horizontalSlider.valueChanged.connect(self.displayvalue)
        self.win.listWidget_2.itemPressed.connect(self.print2)
        self.win.pushButton_7.clicked.connect(lambda: self.loadimg(True))
        self.label.signal2.connect(self.print)

    def update(self):
        self.label.width = int(self.win.lineEdit.text())

    def update2(self):
        self.label.circlewidth = int(self.win.lineEdit_2.text())

    def displayvalue(self):
        self.label.radius = self.win.horizontalSlider.value()
        self.win.pushButton_6.setText(str(self.win.horizontalSlider.value()))

    def menu(self):
        menu = QMenu()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPixelSize(10)
        font.setBold(True)
        font.setWeight(75)
        menu.setFont(font)
        menu.addAction('Rect')
        menu.addAction('Poly')
        return menu

    def menu2(self):
        menu = QMenu()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPixelSize(10)
        font.setBold(True)
        font.setWeight(75)
        menu.setFont(font)
        menu.addAction(self.action1)
        menu.addAction(self.action2)
        menu.addAction(self.action3)
        return menu

    def rectborder_color_picker(self):
        dialog = QColorDialog()
        color = dialog.getColor(options=QColorDialog.ShowAlphaChannel)
        self.label.brush = QBrush(color, Qt.SolidPattern) if color.isValid() else False

    def rectbrush_color_picker(self):
        dialog = QColorDialog()
        color = dialog.getColor(options=QColorDialog.ShowAlphaChannel)
        self.label.rectbrushcolor = QBrush(color, Qt.SolidPattern) if color.isValid() else False

    def circle_color_picker(self):
        dialog = QColorDialog()
        color = dialog.getColor(options=QColorDialog.ShowAlphaChannel)
        self.label.circlebrushcolor = QBrush(color, Qt.SolidPattern) if color.isValid() else False

    def showlineedit(self):
        if not self.toggle2 and not self.toggle3:
            self.win.lineEdit.resize(self.win.pushButton_4.size().width(), self.win.pushButton_4.size().height())
            animation = QPropertyAnimation(self.win.lineEdit, b"pos", self.win.dockWidget)
            animation.setStartValue(self.win.pushButton_4.pos())
            animation.setEndValue(self.win.pushButton_2.pos())
            animation.setDuration(150)
            animation2 = QPropertyAnimation(self.win.pushButton_2, b"pos", self.win.dockWidget)
            animation2.setStartValue(self.win.pushButton_2.pos())
            distance = self.win.pushButton_4.pos().y() - self.win.pushButton_2.pos().y()
            animation2.setEndValue(QPoint(self.win.pushButton_2.pos().x(), self.win.pushButton_2.pos().y() - distance))
            animation2.setDuration(150)
            self.win.lineEdit.show()
            animation.start()
            animation2.start()
            self.toggle = True

    def closelineedit(self):
        animation = QPropertyAnimation(self.win.lineEdit, b"pos", self.win.dockWidget)
        animation.setStartValue(self.win.pushButton_2.pos())
        animation.setEndValue(self.win.pushButton_4.pos())
        animation.setDuration(150)
        animation2 = QPropertyAnimation(self.win.pushButton_2, b"pos", self.win.dockWidget)
        animation2.setStartValue(self.win.pushButton_2.pos())
        animation2.setEndValue(QPoint(self.win.lineEdit.pos()))
        animation2.setDuration(150)
        animation.start()
        animation2.start()
        self.win.lineEdit.hide()
        self.toggle = False

    def showlineedit_2(self):
        if not self.toggle3 and not self.toggle:
            self.win.lineEdit_2.resize(self.win.pushButton_4.size().width(), self.win.pushButton_4.size().height())
            animation = QPropertyAnimation(self.win.lineEdit_2, b"pos", self.win.dockWidget)
            animation.setStartValue(self.win.pushButton_4.pos())
            animation.setEndValue(self.win.pushButton_5.pos())
            animation.setDuration(150)
            animation2 = QPropertyAnimation(self.win.pushButton_5, b"pos", self.win.dockWidget)
            animation2.setStartValue(self.win.pushButton_5.pos())
            animation2.setEndValue(QPoint(self.win.pushButton_5.pos().x() + 120, self.win.pushButton_5.pos().y()))
            animation2.setDuration(150)
            self.win.lineEdit_2.show()
            animation.start()
            animation2.start()
            self.toggle2 = True

    def closelineedit_2(self):
        animation = QPropertyAnimation(self.win.lineEdit_2, b"pos", self.win.dockWidget)
        animation.setStartValue(self.win.lineEdit_2.pos())
        animation.setEndValue(self.win.pushButton_4.pos())
        animation.setDuration(150)
        animation2 = QPropertyAnimation(self.win.pushButton_5, b"pos", self.win.dockWidget)
        animation2.setStartValue(self.win.pushButton_5.pos())
        animation2.setEndValue(QPoint(self.originpos))
        animation2.setDuration(150)
        animation.start()
        animation2.start()
        self.win.lineEdit.hide()
        self.toggle2 = False

    def showslider(self):
        if not self.toggle2 and not self.toggle:
            animation = QPropertyAnimation(self.win.horizontalSlider, b"pos", self.win.dockWidget)
            animation.setStartValue(self.win.horizontalSlider.pos())
            animation.setEndValue(self.win.checkBox.pos())
            animation.setDuration(150)
            animation2 = QPropertyAnimation(self.win.checkBox, b"pos", self.win.dockWidget)
            animation2.setStartValue(self.win.checkBox.pos())
            animation2.setEndValue(QPoint(10, 190))
            animation2.setDuration(150)
            animation.start()
            animation2.start()
            self.win.pushButton_6.setEnabled(False)
            self.win.pushButton_6.setText(str(self.win.horizontalSlider.value()))
            self.toggle3 = True

    def closeslider(self):
        animation = QPropertyAnimation(self.win.horizontalSlider, b"pos", self.win.dockWidget)
        animation.setStartValue(self.win.horizontalSlider.pos())
        animation.setEndValue(self.originpos2)
        animation.setDuration(150)
        animation2 = QPropertyAnimation(self.win.checkBox, b"pos", self.win.dockWidget)
        animation2.setStartValue(self.win.checkBox.pos())
        animation2.setEndValue(self.win.horizontalSlider.pos())
        animation2.setDuration(150)
        animation.start()
        animation2.start()
        self.win.pushButton_6.setEnabled(True)
        self.win.pushButton_6.setText('Circle Radius')
        self.toggle3 = False

    def loadimg(self, check):
        if os.path.exists(self.last_file) and check:
            Dialog3(self).show()
        else:
            try:
                m = os.scandir(self.path)
                self.filename = (os.path.join(self.path, file.name) for file in m)
                try:
                    imgname = next(self.filename)
                except BaseException as e:
                    Messagebox('Directory is empty.')
                    return
                self.storelabeling['Image path'] = imgname
                self.basename = os.path.splitext(os.path.basename(imgname))[0]
                self.saveloc = rf'{self.path}\{self.basename}.json'
                self.readimg(imgname)
                self.dir = True
                self.singal = False
            except OSError as e:
                if e.errno == 20:
                    self.readimg(self.path)
                    self.basename = os.path.splitext(os.path.basename(self.path))[0]
                    dir = os.path.dirname(os.path.realpath(self.path))
                    self.saveloc = rf'{dir}\{self.basename}.json'
                    self.storelabeling['Image path'] = self.path
                    self.dir = False
                    self.singal = True
                elif e.errno == 2:
                    print('Invalid path')

    def updatesaveloc(self, filename):
        self.storelabeling['Image path'] = filename
        self.basename = os.path.splitext(os.path.basename(filename))[0]
        self.saveloc = f'{self.path}\{self.basename}.json'

    def readimg(self, path):
        if path == 0:
            self.close()
            return
        else:
            img = cv2.imread(path)
            if img is not None:
                autosave(self.mainwindow, path, 'Saving setting', 'Last annotation file')
                img = QPixmap(path)
                img.setDevicePixelRatio(self.dpi)
                realwidth = int(img.width()//self.dpi)
                realheight = int(img.height()//self.dpi)
                self.setMaximumSize(realwidth, realheight)
                self.setMinimumSize(realwidth, realheight)
                self.storelabeling['Image_width'] = img.width()
                self.storelabeling['Image_height'] = img.height()
                self.label.setPixmap(img)
                self.label.resize(realwidth, realheight)
                self.win.frame.resize(realwidth, realheight)
                self.setGeometry(0, 0, realwidth, realheight)
                windowposx = (self.width - realwidth)//2
                windowposy = (self.height - realheight)//2
                self.move(windowposx, windowposy)
                self.label.move(0, 0)
                dockwidth = self.win.dockWidget.width()
                dockposy = (self.height - self.win.dockWidget.height())//2
                dockposy2 = (self.height - self.win.dockWidget_3.height())//2
                self.win.dockWidget.setFloating(True)
                self.win.dockWidget_3.setFloating(True)
                if windowposx - dockwidth < 0:
                    self.win.dockWidget.move(0, dockposy)
                else:
                    self.win.dockWidget.move(windowposx - dockwidth, dockposy)
                if windowposx + realwidth >= self.width:
                    self.win.dockWidget_3.move(windowposx + realwidth - self.win.dockWidget_3.width(), dockposy2)
                else:
                    self.win.dockWidget_3.move(windowposx + realwidth, dockposy2)
                if not self.displayed:
                    self.win.dockWidget.show()
                    self.win.dockWidget_3.show()
                self.displayed = True
            else:
                path = self.getnext()
                self.readimg(path)

    def eventFilter(self, src, event):
        if event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle:
            self.closelineedit()
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle2:
            self.closelineedit_2()
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle3:
            self.closeslider()
        elif event.type() == QEvent.ContextMenu and QtCore.Qt.RightButton and src == self.win.listWidget_2 and self.selected:
            self.selected = False
            menu = QMenu()
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPixelSize(9)
            font.setWeight(75)
            menu.addAction(self.action4)
            menu.setFont(font)
            menu.exec_(event.globalPos())
        elif src == self.win.lineEdit_3:
            if event.type() == QEvent.DragEnter and QtCore.Qt.LeftButton:
                event.accept()
            elif event.type() == QEvent.Drop:
                path = event.mimeData().urls()[0].toLocalFile()
                src.setText(path)
                self.path = path
                return True
        elif event.type() == QEvent.KeyPress and event.key() == QtCore.Qt.Key_Plus and self.dir:
            file = self.getnext()
            if file != 0:
                self.readimg(file)
                self.savefile()
                autosave(self.mainwindow, file, 'Saving setting', 'Last annotation file')
                self.updatesaveloc(file)
                self.storelabeling['Label'].clear()
                self.templist.clear()
                self.label.clear()
                self.label.setFocus()
            else:
                self.savefile()
                autosave(self.mainwindow, 'None', 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
                self.label.clear()
                self.close()
        elif event.type() == QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Plus)\
                and (self.mainwindow.labelling or self.singal):
            self.savefile()
            self.close()
            self.win.dockWidget.close()
            self.win.dockWidget_3.close()
            self.label.close()
            self.storelabeling['Label'].clear()
            self.templist.clear()
            self.mainwindow.show()
        elif event.type() == QEvent.Close:
            self.mainwindow.win.pushButton_3.setEnabled(True)
            self.win.dockWidget.close()
            self.win.dockWidget_3.close()
        return super().eventFilter(src, event)

    def getnext(self):
        try:
            return next(self.filename)
        except StopIteration:
            return 0

    def print(self, var1, var2, var3):
        list_widget2 = self.win.listWidget_2
        text = f'{var1}  Begin: ({var2.x()},{var2.y()})  End: ({var3.x()},{var3.y()})'
        list_widget2.addItem(text)
        index = list_widget2.count()-1
        list_widget2.item(index).setData(Qt.UserRole, (var1, var2, var3))

    def print2(self):
        self.selected = True

    def additem(self):
        storebegin = self.label.newbegin
        storeend = self.label.newend
        self.templist.append(self.storelabel(storebegin[-1], storeend[-1], self.name))

    def removeitem(self):
        row = self.win.listWidget_2.currentIndex().row()
        index = self.win.listWidget_2.currentIndex().data(Qt.UserRole)[0]
        self.label.rectlist[index] = None
        self.label.storeend[index] = None
        self.label.storebegin[index] = None
        self.label.newend[index] = None
        self.label.newbegin[index] = None
        self.win.listWidget_2.takeItem(row)
        self.templist[index] = None
        self.label.update()

    def storelabel(self, initpos: QPoint, finalpos: QPoint, name):
        labelingdict = {
            "Name": name,
            "Init Pos": (initpos.x(), initpos.y()),
            "final Pos": (finalpos.x(), finalpos.y()),
        }
        return labelingdict

    def savefile(self):
        if len(self.templist) > 0:
            for index, point in enumerate(self.templist):
                if point is not None:
                    self.storelabeling['Label'].append(self.templist[index])
            with open(self.saveloc, mode='w') as file:
                json.dump(self.storelabeling, file, indent=4)
                file.close()
        else:
            print('No Point')

    def popupdialog(self, pos):
        position = self.dialog.dialog.frame_2.pos()
        y = pos.y() + self.dialog.dialog.frame_2.height() + position.y() - self.pos().y()-self.geometry().height()
        x = pos.x() + self.dialog.dialog.frame_2.width() + position.x() - self.pos().x() - self.geometry().width()
        if y > 0 and x < 0:
            self.dialog.move(pos.x(), pos.y()-y + position.y())
        elif x > 0 and y < 0:
            self.dialog.move(pos.x() - x, pos.y())
        elif x > 0 and y > 0:
            self.dialog.move(pos.x() - x, pos.y()-y + position.y()+10)
        else:
            self.dialog.move(pos)
        self.dialog.show()

    def go2lastsaved(self):
        dir = os.path.dirname(self.last_file)
        self.path = dir
        m = os.scandir(dir)
        for file in m:
            path = os.path.join(dir, file.name)
            if os.path.samefile(path, self.last_file):
                self.readimg(path)
                self.storelabeling['Image path'] = path
                self.basename = os.path.splitext(os.path.basename(path))[0]
                break
        self.filename = (os.path.join(dir, file.name) for file in m)
        self.saveloc = f'{self.path}\{self.basename}.json'
        self.dir = True
        self.singal = False


class Dialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.mainwin = parent
        self.dialog.listWidget.itemPressed.connect(self.setlabel)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.additem()
            self.dialog.lineEdit_4.clear()

    def setlabel(self):
        data = self.dialog.listWidget.currentItem()
        self.mainwin.name = data.text()
        self.mainwin.additem()
        self.close()

    def additem(self):
        self.dialog.listWidget.addItem(self.dialog.lineEdit_4.text())


class Dialog3(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.dialog = Dialog2.Ui_Dialog()
        self.dialog.setupUi(self)
        font = QtGui.QFont()
        font.setPixelSize(12)
        self.dialog.buttonBox.accepted.connect(parent.go2lastsaved)
        self.dialog.buttonBox.rejected.connect(lambda: parent.loadimg(False))
        self.dialog.buttonBox.button(QDialogButtonBox.Ok).setFont(font)
        self.dialog.buttonBox.button(QDialogButtonBox.Cancel).setFont(font)


os.environ['QT_SCALE_FACTOR'] = str(ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100)
os.environ['QT_FONT_DPI'] = str(ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100)
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
