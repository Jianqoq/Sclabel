import cv2
import json
from PyQt5.QtWidgets import QMainWindow, QColorDialog, QMenu, QAction, QDialog, QDialogButtonBox
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
        self.dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.dialog.setAttribute(Qt.WA_TranslucentBackground)
        shadow(self.dialog)
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
        self.lastname = None
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
        self.action1.triggered.connect(self.rectborder_color_picker)
        self.action2.triggered.connect(self.rectbrush_color_picker)
        self.action3.triggered.connect(self.circle_color_picker)
        self.action4.triggered.connect(lambda: self.removeitem(self.label))
        self.win.lineEdit_3.textEdited.connect(lambda: self.win.lineEdit_3.setText(self.path))
        self.win.pushButton_2.clicked.connect(lambda: self.showlineedit(self.win))
        self.win.pushButton_5.clicked.connect(lambda: self.showlineedit_2(self.win))
        self.win.pushButton_6.clicked.connect(lambda: self.showslider(self.win))
        self.win.lineEdit.textEdited.connect(self.update)
        self.win.lineEdit_2.textEdited.connect(self.update2)
        self.win.horizontalSlider.valueChanged.connect(self.displayvalue)
        self.win.listWidget_2.itemPressed.connect(self.print2)
        self.win.listWidget_2.doubleClicked.connect(lambda: self.highlight(self.label, self.label.storerectbrushcolor,
                                                                           self.label.storecolor, self.label.selectedbox_begin,
                                                                           self.label.selectedbox_end, self.label.storebegin,
                                                                           self.label.storeend))
        self.win.pushButton_7.clicked.connect(lambda: self.loadimg(True, self.win, self.path, self.label))
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

    def showlineedit(self, win):
        if not self.toggle2 and not self.toggle3:
            win.lineEdit.resize(win.pushButton_4.size().width(), win.pushButton_4.size().height())
            animation = QPropertyAnimation(win.lineEdit, b"pos", win.dockWidget)
            animation.setStartValue(win.pushButton_4.pos())
            animation.setEndValue(win.pushButton_2.pos())
            animation.setDuration(150)
            animation2 = QPropertyAnimation(win.pushButton_2, b"pos", win.dockWidget)
            animation2.setStartValue(win.pushButton_2.pos())
            distance = win.pushButton_4.pos().y() - win.pushButton_2.pos().y()
            animation2.setEndValue(QPoint(win.pushButton_2.pos().x(), win.pushButton_2.pos().y() - distance))
            animation2.setDuration(150)
            win.lineEdit.show()
            animation.start()
            animation2.start()
            self.toggle = True

    def closelineedit(self, win):
        animation = QPropertyAnimation(win.lineEdit, b"pos", win.dockWidget)
        animation.setStartValue(win.pushButton_2.pos())
        animation.setEndValue(win.pushButton_4.pos())
        animation.setDuration(150)
        animation2 = QPropertyAnimation(win.pushButton_2, b"pos", win.dockWidget)
        animation2.setStartValue(win.pushButton_2.pos())
        animation2.setEndValue(QPoint(win.lineEdit.pos()))
        animation2.setDuration(150)
        animation.start()
        animation2.start()
        win.lineEdit.hide()
        self.toggle = False

    def showlineedit_2(self, win):
        if not self.toggle3 and not self.toggle:
            win.lineEdit_2.resize(win.pushButton_4.size().width(), win.pushButton_4.size().height())
            animation = QPropertyAnimation(win.lineEdit_2, b"pos", win.dockWidget)
            animation.setStartValue(win.pushButton_4.pos())
            animation.setEndValue(win.pushButton_5.pos())
            animation.setDuration(150)
            animation2 = QPropertyAnimation(win.pushButton_5, b"pos", win.dockWidget)
            animation2.setStartValue(win.pushButton_5.pos())
            animation2.setEndValue(QPoint(win.pushButton_5.pos().x() + 120, win.pushButton_5.pos().y()))
            animation2.setDuration(150)
            win.lineEdit_2.show()
            animation.start()
            animation2.start()
            self.toggle2 = True

    def closelineedit_2(self, win):
        animation = QPropertyAnimation(win.lineEdit_2, b"pos", win.dockWidget)
        animation.setStartValue(win.lineEdit_2.pos())
        animation.setEndValue(win.pushButton_4.pos())
        animation.setDuration(150)
        animation2 = QPropertyAnimation(win.pushButton_5, b"pos", win.dockWidget)
        animation2.setStartValue(win.pushButton_5.pos())
        animation2.setEndValue(QPoint(self.originpos))
        animation2.setDuration(150)
        animation.start()
        animation2.start()
        win.lineEdit.hide()
        self.toggle2 = False

    def showslider(self, win):
        if not self.toggle2 and not self.toggle:
            animation = QPropertyAnimation(win.horizontalSlider, b"pos", win.dockWidget)
            animation.setStartValue(win.horizontalSlider.pos())
            animation.setEndValue(win.checkBox.pos())
            animation.setDuration(150)
            animation2 = QPropertyAnimation(win.checkBox, b"pos", win.dockWidget)
            animation2.setStartValue(win.checkBox.pos())
            animation2.setEndValue(QPoint(10, 190))
            animation2.setDuration(150)
            animation.start()
            animation2.start()
            win.pushButton_6.setEnabled(False)
            win.pushButton_6.setText(str(win.horizontalSlider.value()))
            self.toggle3 = True

    def closeslider(self, win):
        animation = QPropertyAnimation(win.horizontalSlider, b"pos", win.dockWidget)
        animation.setStartValue(win.horizontalSlider.pos())
        animation.setEndValue(self.originpos2)
        animation.setDuration(150)
        animation2 = QPropertyAnimation(win.checkBox, b"pos", win.dockWidget)
        animation2.setStartValue(win.checkBox.pos())
        animation2.setEndValue(win.horizontalSlider.pos())
        animation2.setDuration(150)
        animation.start()
        animation2.start()
        win.pushButton_6.setEnabled(True)
        win.pushButton_6.setText('Circle Radius')
        self.toggle3 = False

    def loadimg(self, check, win, path, label):
        if os.path.exists(self.last_file) and check:
            Dialog3(self).show()
        else:
            try:
                m = os.scandir(path)
                self.filename = (os.path.join(path, file.name) for file in m)
                try:
                    imgname = next(self.filename)
                except BaseException as e:
                    Messagebox('Directory is empty.')
                    return
                self.storelabeling['Image path'] = imgname
                self.basename = os.path.splitext(os.path.basename(imgname))[0]
                self.saveloc = rf'{path}\{self.basename}.json'
                win.dockWidget.setFloating(True)
                win.dockWidget_3.setFloating(True)
                self.readimg(imgname, self.win, self.label, self.width, self.height)
                self.dir = True
                self.singal = False
                win.dockWidget.show()
                win.dockWidget_3.show()
                label.show()
                self.hide()
            except OSError as e:
                if e.errno == 20:
                    win.dockWidget.setFloating(True)
                    win.dockWidget_3.setFloating(True)
                    self.basename = os.path.splitext(os.path.basename(path))[0]
                    self.readimg(path, self.win, self.label, self.width, self.height)
                    dir = os.path.dirname(os.path.realpath(path))
                    self.saveloc = rf'{dir}\{self.basename}.json'
                    self.storelabeling['Image path'] = path
                    self.dir = False
                    self.singal = True
                    label.show()
                    win.dockWidget.show()
                    win.dockWidget_3.show()
                    self.hide()
                elif e.errno == 2:
                    print('Invalid path')

    def updatesaveloc(self, filename):
        self.storelabeling['Image path'] = filename
        self.basename = os.path.splitext(os.path.basename(filename))[0]
        self.saveloc = f'{self.path}\{self.basename}.json'

    def readimg(self, path, win, label, width, height):
        if path == 0:
            self.close()
            return
        else:
            img = cv2.imread(path)
            if img is not None:
                img = QPixmap(path)
                changed = True if self.w != img.width() else False
                self.w = int(img.width() // self.dpi)
                new_w = self.w
                self.h = int(img.height() // self.dpi)
                new_h = self.h
                realwidth = new_w if new_w <= width else width
                realheight = new_h if new_w <= height else height
                windowposx = (width - realwidth)//2
                windowposy = (height - realheight)//2
                label.image = img
                self.storelabeling['Image_width'] = img.width()
                self.storelabeling['Image_height'] = img.height()
                label.setGeometry(windowposx, windowposy, new_w, new_h)
                label.setWindowTitle(self.basename)
                dockwidth = win.dockWidget.width()
                dockposy = (height - win.dockWidget.height())//2
                dockposy2 = (height - win.dockWidget_3.height())//2
                x = (width + realwidth)//2
                if changed and windowposx - dockwidth < 0:
                    win.dockWidget.move(0, dockposy)
                elif changed:
                    win.dockWidget.move(windowposx - dockwidth, dockposy)
                if changed and x + realwidth >= width:
                    win.dockWidget_3.move(width - win.dockWidget_3.width(), dockposy2)
                elif changed:
                    win.dockWidget_3.move(windowposx + realwidth, dockposy2)
                label.repaint()
            else:
                path = self.getnext()
                self.readimg(path, win, label, width, height)
                self.lastname = path

    def eventFilter(self, src, event):

        if event.type() == QEvent.DragEnter:
            event.accept()
        elif event.type() == QEvent.Drop:
            self.path = event.mimeData().urls()[0].toLocalFile()
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle:
            self.closelineedit(self.win)
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle2:
            self.closelineedit_2(self.win)
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == self.win.dockWidget and self.toggle3:
            self.closeslider(self.win)
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
                self.lastname = file
                self.label.clear()
                self.updatesaveloc(file)
                self.readimg(file, self.win, self.label, self.width, self.height)
                autosave(self.mainwindow, self.lastname, 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
            else:
                autosave(self.mainwindow, None, 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
                self.label.clear()
                self.label.close()
                self.close()
        elif event.type() == QEvent.KeyPress and event.key() == QtCore.Qt.Key_Plus and self.dir:
            file = self.getnext()
            if file != 0:
                self.lastname = file
                self.label.clear()
                self.savefile(self.templist, self.storelabeling, self.saveloc)
                self.updatesaveloc(file)
                self.readimg(file, self.win, self.label, self.width, self.height)
                autosave(self.mainwindow, self.lastname, 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
            else:
                self.savefile(self.templist, self.storelabeling, self.saveloc)
                self.storelabeling['Label'].clear()
                self.templist.clear()
                self.label.clear()
                autosave(self.mainwindow, None, 'Saving setting', 'Last annotation file')
                self.label.close()
                self.close()
        elif event.type() == QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Plus)\
                and (self.mainwindow.labelling or self.singal):
            self.savefile(self.templist, self.storelabeling, self.saveloc)
            self.close()
            self.win.dockWidget.close()
            self.win.dockWidget_3.close()
            self.label.close()
            self.storelabeling['Label'].clear()
            self.templist.clear()
            self.mainwindow.show()
        elif event.type() == QEvent.Close:
            self.mainwindow.win.pushButton_3.setEnabled(True)
            self.close()
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

    def highlight(self, label, storerectbrushcolor, storecolor, selectedbox_begin, selectedbox_end, storebegin, storeend):
        current_row = self.win.listWidget_2.currentRow()
        prev_index = self.index
        if not label.selected:
            index = current_row
            self.index = index
            storerectbrushcolor[index] = QBrush(QColor(200, 200, 200, 40))
            storecolor[index] = QColor(248, 255, 106, 255)
            selectedbox_begin.append(storebegin[index])
            selectedbox_end.append(storeend[index])
            label.repaint()
            label.selected = True
        elif label.selected and current_row != prev_index:
            index = current_row
            storerectbrushcolor[prev_index] = label.rectbrushcolor
            storecolor[prev_index] = label.brush
            storerectbrushcolor[index] = QBrush(QColor(200, 200, 200, 40))
            storecolor[index] = QColor(248, 255, 106, 255)
            selectedbox_begin[0] = storebegin[index]
            selectedbox_end[0] = storeend[index]
            label.repaint()
            self.index = index
        elif label.selected and current_row == prev_index:
            storerectbrushcolor[prev_index] = label.rectbrushcolor
            storecolor[prev_index] = label.brush
            selectedbox_begin.pop()
            selectedbox_end.pop()
            label.repaint()
            label.selected = False
            self.win.listWidget_2.clearSelection()

    def additem(self):
        storebegin = self.label.newbegin
        storeend = self.label.newend
        self.templist.append(self.storelabel(storebegin[-1], storeend[-1], self.name))

    def removeitem(self, label):
        row = self.win.listWidget_2.currentIndex().row()
        label.rectlist.pop(row)
        label.storeend.pop(row)
        label.storebegin.pop(row)
        label.newend.pop(row)
        label.newbegin.pop(row)
        self.win.listWidget_2.takeItem(row)
        self.templist.pop(row)
        label.update()

    def storelabel(self, initpos: QPoint, finalpos: QPoint, name):
        labelingdict = {
            "Name": name,
            "Init Pos": (initpos.x(), initpos.y()),
            "final Pos": (finalpos.x(), finalpos.y()),
        }
        return labelingdict

    def savefile(self, templist, storelabeling, saveloc):
        if templist:
            for index, point in enumerate(templist):
                if point is not None:
                    storelabeling['Label'].append(templist[index])
            with open(saveloc, mode='w') as file:
                json.dump(storelabeling, file, indent=4)
                file.close()
        else:
            with open(saveloc, mode='w') as file:
                json.dump(storelabeling, file, indent=4)
                file.close()

    def popupdialog(self, pos, dialog, label):
        y = pos.y() + dialog.dialog.frame_2.height() - label.pos().y()- label.geometry().height()
        x = pos.x() + dialog.dialog.frame_2.width() - label.pos().x() - label.geometry().width()
        if y > 0 and x < 0:
            dialog.move(pos.x(), pos.y()-y)
        elif x > 0 and y < 0:
            dialog.move(pos.x() - x - 20, pos.y())
        elif x > 0 and y > 0:
            dialog.move(pos.x() - x - 20, pos.y()-y)
        else:
            dialog.move(pos)
        dialog.show()

    def go2lastsaved(self, win, basename):
        dir = os.path.dirname(self.last_file)
        self.path = dir
        m = os.scandir(dir)
        for file in m:
            path = os.path.join(dir, file.name)
            if os.path.samefile(path, self.last_file):
                basename = os.path.splitext(os.path.basename(path))[0]
                win.dockWidget.setFloating(True)
                win.dockWidget_3.setFloating(True)
                self.readimg(path, win, self.label, self.width, self.height)
                win.dockWidget.show()
                win.dockWidget_3.show()
                self.label.show()
                self.storelabeling['Image path'] = path
                break
        self.filename = (os.path.join(dir, file.name) for file in m)
        self.saveloc = f'{self.path}\{basename}.json'
        self.dir = True
        self.singal = False


class Dialog(QDialog):
    def __init__(self, parent, mainwindow):
        super().__init__(parent)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.mainwin = mainwindow
        self.dialog.listWidget.itemPressed.connect(lambda: self.setlabel(self.mainwin))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.additem(self.dialog)
            self.dialog.lineEdit_4.clear()

    def setlabel(self, mainwin):
        data = self.dialog.listWidget.currentItem()
        mainwin.name = data.text()
        mainwin.additem()
        text = f'{mainwin.name}  Begin: ({mainwin.var1.x()},{mainwin.var1.y()})' \
               f'  End: ({mainwin.var2.x()},{mainwin.var2.y()})'
        list_widget2 = mainwin.win.listWidget_2
        list_widget2.addItem(text)
        index = list_widget2.count()-1
        list_widget2.item(index).setData(Qt.UserRole, (mainwin.name, mainwin.var1, mainwin.var2))
        self.close()

    def additem(self, dialog):
        if dialog.lineEdit_4.text():
            dialog.listWidget.addItem(dialog.lineEdit_4.text())


class Dialog3(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.dialog = Dialog2.Ui_Dialog()
        self.dialog.setupUi(self)
        font = QtGui.QFont()
        font.setPixelSize(12)
        self.dialog.buttonBox.accepted.connect(lambda: parent.go2lastsaved(parent.win, parent.basename))
        self.dialog.buttonBox.rejected.connect(lambda: parent.loadimg(False, parent.win, parent.path, parent.label))
        self.dialog.buttonBox.button(QDialogButtonBox.Ok).setFont(font)
        self.dialog.buttonBox.button(QDialogButtonBox.Cancel).setFont(font)
