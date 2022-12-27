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
        self.setMouseTracking(True)
        #self.setAcceptDrops(True)
        self.setMaximumSize(self.size())
        self.setMinimumSize(self.size())
        self.dpi = self.devicePixelRatioF()
        self.win.lineEdit.hide()
        self.win.lineEdit_2.hide()
        self.win.dockWidget.hide()
        self.win.dockWidget_3.hide()
        self.win.dockWidget.setWindowTitle('Drawing Panel')
        self.win.dockWidget_3.setWindowTitle('History Annotations')
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
        self.label.installEventFilter(self)
        self.win.dockWidget.setParent(self.label)
        self.win.dockWidget_3.setParent(self.label)
        self.dialog = Dialog(self.label, self)
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
        self.w = 0
        self.h = 0
        self.count = 0
        self.var1 = None
        self.var2 = None
        self.index = None
        self.storelabeling = {
                              'Image path': self.imgname,
                              'Image_width': 0,
                              'Image_height': 0,
                              'Label': []
                              }
        self.templist = []
        self.originpos = self.win.pushButton_5.pos()
        self.originpos2 = self.win.horizontalSlider.pos()
        self.win.lineEdit_3.textEdited.connect(self.drop)
        self.win.pushButton_2.clicked.connect(self.showlineedit)
        self.win.pushButton_5.clicked.connect(self.showlineedit_2)
        self.win.pushButton_6.clicked.connect(self.showslider)
        self.win.lineEdit.textEdited.connect(self.update)
        self.win.lineEdit_2.textEdited.connect(self.update2)
        self.win.horizontalSlider.valueChanged.connect(self.displayvalue)
        self.win.listWidget_2.itemPressed.connect(self.print2)
        self.win.listWidget_2.doubleClicked.connect(self.highlight)
        self.win.pushButton_7.clicked.connect(lambda: self.loadimg(True))
        self.label.signal2.connect(self.print)

    def drop(self):
        self.win.lineEdit_3.setText(self.path)

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
                self.win.dockWidget.setFloating(True)
                self.win.dockWidget_3.setFloating(True)
                self.readimg(imgname)
                self.dir = True
                self.singal = False
                self.win.dockWidget.show()
                self.win.dockWidget_3.show()
                self.label.show()
                self.hide()
            except OSError as e:
                if e.errno == 20:
                    self.win.dockWidget.setFloating(True)
                    self.win.dockWidget_3.setFloating(True)
                    self.readimg(self.path)
                    self.basename = os.path.splitext(os.path.basename(self.path))[0]
                    dir = os.path.dirname(os.path.realpath(self.path))
                    self.saveloc = rf'{dir}\{self.basename}.json'
                    self.storelabeling['Image path'] = self.path
                    self.dir = False
                    self.singal = True
                    self.label.show()
                    self.win.dockWidget.show()
                    self.win.dockWidget_3.show()
                    self.hide()
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
                img = QPixmap(path)
                changed = True if self.w != img.width() else False
                self.w = int(img.width() // self.dpi)
                self.h = int(img.height() // self.dpi)
                realwidth = self.w if self.w <= self.width else self.width
                realheight = self.h if self.w <= self.height else self.height
                windowposx = (self.width - realwidth)//2
                windowposy = (self.height - realheight)//2
                self.label.image = img
                self.storelabeling['Image_width'] = img.width()
                self.storelabeling['Image_height'] = img.height()
                self.label.setGeometry(windowposx, windowposy, self.w, self.h)
                self.label.setWindowTitle(self.basename)
                dockwidth = self.win.dockWidget.width()
                dockposy = (self.height - self.win.dockWidget.height())//2
                dockposy2 = (self.height - self.win.dockWidget_3.height())//2
                x = (self.width + realwidth)//2
                if changed and windowposx - dockwidth < 0:
                    self.win.dockWidget.move(0, dockposy)
                elif changed:
                    self.win.dockWidget.move(windowposx - dockwidth, dockposy)
                if changed and x + realwidth >= self.width:
                    self.win.dockWidget_3.move(self.width - self.win.dockWidget_3.width(), dockposy2)
                elif changed:
                    self.win.dockWidget_3.move(windowposx + realwidth, dockposy2)
                self.label.repaint()
            else:
                path = self.getnext()
                self.readimg(path)

    def eventFilter(self, src, event):

        if event.type() == QEvent.DragEnter:
            event.accept()
        elif event.type() == QEvent.Drop:
            self.path = event.mimeData().urls()[0].toLocalFile()
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle:
            self.closelineedit()
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle2:
            self.closelineedit_2()
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle3:
            self.closeslider()
        elif event.type() == QEvent.ContextMenu and QtCore.Qt.RightButton and\
                src == self.win.listWidget_2 and self.selected:
            self.selected = False
            menu = QMenu()
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPixelSize(9)
            font.setWeight(75)
            menu.addAction(self.action4)
            menu.setFont(font)
            menu.exec_(event.globalPos())
        elif event.type() == QEvent.KeyPress and event.key() == 16777236 and self.dir:
            file = self.getnext()
            if file != 0:
                self.label.clear()
                self.updatesaveloc(file)
                self.readimg(file)
                autosave(self.mainwindow, file, 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
            else:
                autosave(self.mainwindow, 'None', 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
                self.label.clear()
                self.label.close()
                self.close()
        elif event.type() == QEvent.KeyPress and event.key() == QtCore.Qt.Key_Plus and self.dir:
            file = self.getnext()
            if file != 0:
                self.label.clear()
                self.savefile()
                self.updatesaveloc(file)
                self.readimg(file)
                autosave(self.mainwindow, file, 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
            else:
                self.savefile()
                self.storelabeling['Label'].clear()
                self.templist.clear()
                self.label.clear()
                autosave(self.mainwindow, None, 'Saving setting', 'Last annotation file')
                self.label.close()
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
        elif event.type() == QEvent.KeyPress and event.key() == QtCore.Qt.Key_Escape:
            self.mainwindow.win.pushButton_3.setEnabled(True)
            self.label.close()
        elif event.type() == QEvent.Resize and src == self.label:
            wfactor = self.w/self.label.geometry().width() if self.w <= self.width else self.w / self.label.geometry().width()
            hfactor = self.h / self.label.geometry().height() if self.h <= self.height else self.h / self.label.geometry().height()
            self.label.wfactor = wfactor
            self.label.hfactor = hfactor
        return super().eventFilter(src, event)

    def getnext(self):
        try:
            return next(self.filename)
        except StopIteration:

            return 0
        except TypeError:
            Messagebox('Not an Image file')
            return 0

    def print(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def print2(self):
        self.selected = True

    def highlight(self):
        if not self.label.selected:
            index = self.win.listWidget_2.currentRow()
            self.index = index
            self.label.storerectbrushcolor[index] = QBrush(QColor(200, 200, 200, 40))
            self.label.storecolor[index] = QColor(248, 255, 106, 255)
            self.label.selectedbox_begin.append(self.label.storebegin[index])
            self.label.selectedbox_end.append(self.label.storeend[index])
            self.label.repaint()
            self.label.selected = True
        elif self.label.selected and self.win.listWidget_2.currentRow() != self.index:
            index = self.win.listWidget_2.currentRow()
            self.label.storerectbrushcolor[self.index] = self.label.rectbrushcolor
            self.label.storecolor[self.index] = self.label.brush
            self.label.storerectbrushcolor[index] = QBrush(QColor(200, 200, 200, 40))
            self.label.storecolor[index] = QColor(248, 255, 106, 255)
            self.label.selectedbox_begin[0] = self.label.storebegin[index]
            self.label.selectedbox_end[0] = self.label.storeend[index]
            self.label.repaint()
            self.index = index
        elif self.label.selected and self.win.listWidget_2.currentRow() == self.index:
            self.label.storerectbrushcolor[self.index] = self.label.rectbrushcolor
            self.label.storecolor[self.index] = self.label.brush
            self.label.selectedbox_begin.pop()
            self.label.selectedbox_end.pop()
            self.label.repaint()
            self.label.selected = False

    def additem(self):
        storebegin = self.label.newbegin
        storeend = self.label.newend
        self.templist.append(self.storelabel(storebegin[-1], storeend[-1], self.name))

    def removeitem(self):
        row = self.win.listWidget_2.currentIndex().row()
        self.label.rectlist.pop(row)
        self.label.storeend.pop(row)
        self.label.storebegin.pop(row)
        self.label.newend.pop(row)
        self.label.newbegin.pop(row)
        self.win.listWidget_2.takeItem(row)
        self.templist.pop(row)
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
            with open(self.saveloc, mode='w') as file:
                json.dump(self.storelabeling, file, indent=4)
                file.close()

    def popupdialog(self, pos):
        y = pos.y() + self.dialog.dialog.frame_2.height() - self.label.pos().y()-self.label.geometry().height()
        x = pos.x() + self.dialog.dialog.frame_2.width() - self.label.pos().x() - self.label.geometry().width()
        if y > 0 and x < 0:
            self.dialog.move(pos.x(), pos.y()-y)
        elif x > 0 and y < 0:
            self.dialog.move(pos.x() - x - 20, pos.y())
        elif x > 0 and y > 0:
            self.dialog.move(pos.x() - x - 20, pos.y()-y)
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
                self.basename = os.path.splitext(os.path.basename(path))[0]
                self.win.dockWidget.setFloating(True)
                self.win.dockWidget_3.setFloating(True)
                self.readimg(path)
                self.win.dockWidget.show()
                self.win.dockWidget_3.show()
                self.label.show()
                self.storelabeling['Image path'] = path
                break
        self.filename = (os.path.join(dir, file.name) for file in m)
        self.saveloc = f'{self.path}\{self.basename}.json'
        self.dir = True
        self.singal = False


class Dialog(QDialog):
    def __init__(self, parent, mainwindow):
        super().__init__(parent)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.mainwin = mainwindow
        self.dialog.listWidget.itemPressed.connect(self.setlabel)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.additem()
            self.dialog.lineEdit_4.clear()

    def setlabel(self):
        data = self.dialog.listWidget.currentItem()
        self.mainwin.name = data.text()
        self.mainwin.additem()
        text = f'{self.mainwin.name}  Begin: ({self.mainwin.var1.x()},{self.mainwin.var1.y()})' \
               f'  End: ({self.mainwin.var2.x()},{self.mainwin.var2.y()})'
        list_widget2 = self.mainwin.win.listWidget_2
        list_widget2.addItem(text)
        index = list_widget2.count()-1
        list_widget2.item(index).setData(Qt.UserRole, (self.mainwin.name, self.mainwin.var1, self.mainwin.var2))
        self.close()

    def additem(self):
        if self.dialog.lineEdit_4.text():
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
