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
        win = self.win
        win.setupUi(self)
        dpi = self.dpi = self.devicePixelRatioF()

        # get the main window instance
        self.mainwindow = mainwindow
        mainwindow = self.mainwindow
        self.last_file = read_savedfile(mainwindow)

        # init label
        self.label = Mylabel(dpi, self)
        label = self.label

        # get widget pos
        self.originpos = win.pushButton_5.pos()
        self.originpos2 = win.horizontalSlider.pos()

        # init UI
        self.setMouseTracking(True)
        self.setMaximumSize(self.size())
        self.setMinimumSize(self.size())
        win.lineEdit.hide()
        win.lineEdit_2.hide()
        win.dockWidget.hide()
        win.dockWidget_3.hide()
        win.dockWidget.setWindowTitle('Drawing Panel')
        win.dockWidget_3.setWindowTitle('History Annotations')

        # set validator to line edit
        self.validator = QIntValidator()
        validator = self.validator
        win.lineEdit.setValidator(validator)
        win.lineEdit_2.setValidator(validator)

        self.action1 = QAction("Line Color")
        self.action2 = QAction('Rect Brush Color')
        self.action3 = QAction('Cir Brush Color')
        self.action4 = QAction('Delete')
        win.pushButton.setMenu(self.menu())
        win.pushButton_3.setMenu(self.menu2())

        # install event filter
        win.dockWidget.installEventFilter(self)
        win.listWidget_2.installEventFilter(self)
        win.dockWidget_3.installEventFilter(self)
        win.lineEdit_3.installEventFilter(self)
        label.installEventFilter(self)
        self.installEventFilter(self)

        # current screen geometry after high dpi scaling(if device support high dpi)
        self.width = width
        self.height = height

        # set floating window parent to label
        win.dockWidget.setParent(label)
        win.dockWidget_3.setParent(label)

        # label name dialog
        self.dialog = Dialog(label, self)
        dialog = self.dialog
        dialog.setWindowFlag(Qt.FramelessWindowHint)
        dialog.setAttribute(Qt.WA_TranslucentBackground)
        shadow(dialog)

        # init var
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

        # labelling file content
        self.storelabeling = {
                                              'Image path': self.imgname,
                                              'Image_width': 0,
                                              'Image_height': 0,
                                              'Label': []
                                              }
        self.templist = []

        # action signal connect
        self.action1.triggered.connect(lambda: self.rectborder_color_picker(label))
        self.action2.triggered.connect(lambda: self.rectbrush_color_picker(label))
        self.action3.triggered.connect(lambda: self.circle_color_picker(label))
        self.action4.triggered.connect(lambda: self.removeitem(label))

        # connect signal to widgets
        win.lineEdit_3.textEdited.connect(lambda: win.lineEdit_3.setText(self.path))
        win.pushButton_2.clicked.connect(lambda: self.showlineedit(win))
        win.pushButton_5.clicked.connect(lambda: self.showlineedit_2(win))
        win.pushButton_6.clicked.connect(lambda: self.showslider(win))
        win.lineEdit.textEdited.connect(lambda: self.updatevalue(label, win))
        win.horizontalSlider.valueChanged.connect(lambda: self.displayvalue(label, win))
        win.listWidget_2.itemPressed.connect(self.print2)
        win.listWidget_2.doubleClicked.connect(lambda: self.highlight(label, label.storerectbrushcolor, label.storecolor
                                                                      , label.selectedbox_begin, label.selectedbox_end,
                                                                      label.storebegin, label.storeend, win))
        win.pushButton_7.clicked.connect(lambda: self.loadimg(True, win, self.path, label, dpi, self.storelabeling))
        label.signal2.connect(self.print)

    def updatevalue(self, label, win):
        label.width = int(win.lineEdit.text())

    def displayvalue(self, label, win):
        label.radius = win.horizontalSlider.value()
        win.pushButton_6.setText(str(win.horizontalSlider.value()))

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

    def rectborder_color_picker(self, label):
        dialog = QColorDialog()
        color = dialog.getColor(options=QColorDialog.ShowAlphaChannel)
        label.brush = QBrush(color, Qt.SolidPattern) if color.isValid() else False

    def rectbrush_color_picker(self, label):
        dialog = QColorDialog()
        color = dialog.getColor(options=QColorDialog.ShowAlphaChannel)
        label.rectbrushcolor = QBrush(color, Qt.SolidPattern) if color.isValid() else False

    def circle_color_picker(self, label):
        dialog = QColorDialog()
        color = dialog.getColor(options=QColorDialog.ShowAlphaChannel)
        label.circlebrushcolor = QBrush(color, Qt.SolidPattern) if color.isValid() else False

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

    def loadimg(self, check, win, path, label, dpi, storelabeling):
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
                storelabeling['Image path'] = imgname
                self.basename = os.path.splitext(os.path.basename(imgname))[0]
                self.saveloc = rf'{path}\{self.basename}.json'
                win.dockWidget.setFloating(True)
                win.dockWidget_3.setFloating(True)
                self.readimg(imgname, win, label, self.width, self.height, dpi, storelabeling)
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
                    self.readimg(path, win, label, self.width, self.height, dpi, storelabeling)
                    dir = os.path.dirname(os.path.realpath(path))
                    self.saveloc = rf'{dir}\{self.basename}.json'
                    storelabeling['Image path'] = path
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

    def readimg(self, path, win, label, width, height, dpi, storelabeling):
        if path == 0:
            self.close()
            return
        else:
            img = cv2.imread(path)
            if img is not None:
                img = QPixmap(path)
                changed = True if self.w != img.width() else False
                new_w = self.w = int(img.width() // dpi)
                new_h = self.h = int(img.height() // dpi)
                realwidth = new_w if new_w <= width else width
                realheight = new_h if new_w <= height else height
                windowposx = (width - realwidth)//2
                windowposy = (height - realheight)//2
                label.image = img
                storelabeling['Image_width'] = img.width()
                storelabeling['Image_height'] = img.height()
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
                self.readimg(path, win, label, width, height, dpi, storelabeling)
                self.lastname = path

    def eventFilter(self, src, event):
        win = self.win
        label = self.label
        mainwindow = self.mainwindow
        if event.type() == QEvent.DragEnter:
            event.accept()
        elif event.type() == QEvent.Drop:
            self.path = event.mimeData().urls()[0].toLocalFile()
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == win.dockWidget and self.toggle:
            self.closelineedit(win)
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == win.dockWidget and self.toggle2:
            self.closelineedit_2(win)
        elif event.type() == QEvent.MouseButtonPress and QtCore.Qt.LeftButton and src == win.dockWidget and self.toggle3:
            self.closeslider(win)
        elif event.type() == QEvent.ContextMenu and QtCore.Qt.RightButton and\
                src == win.listWidget_2 and self.selected:
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
                label.clear()
                self.updatesaveloc(file)
                self.readimg(file, win, label, self.width, self.height, self.dpi, self.storelabeling)
                autosave(mainwindow, self.lastname, 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
            else:
                autosave(self.mainwindow, 'None', 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                self.templist.clear()
                label.clear()
                label.close()
                self.close()
        elif event.type() == QEvent.KeyPress and event.key() == QtCore.Qt.Key_Plus and self.dir:
            file = self.getnext()
            templist = self.templist
            if file != 0:
                self.lastname = file
                label.clear()
                self.savefile(templist, self.storelabeling, self.saveloc)
                self.updatesaveloc(file)
                self.readimg(file, win, label, self.width, self.height, self.dpi, self.storelabeling)
                autosave(mainwindow, self.lastname, 'Saving setting', 'Last annotation file')
                self.storelabeling['Label'].clear()
                templist.clear()
            else:
                self.savefile(templist, self.storelabeling, self.saveloc)
                self.storelabeling['Label'].clear()
                templist.clear()
                label.clear()
                autosave(mainwindow, 'None', 'Saving setting', 'Last annotation file')
                label.close()
                self.close()
        elif event.type() == QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Plus)\
                and (mainwindow.labelling or self.singal):
            templist = self.templist
            self.savefile(templist, self.storelabeling, self.saveloc)
            self.close()
            win.dockWidget.close()
            win.dockWidget_3.close()
            label.close()
            self.storelabeling['Label'].clear()
            templist.clear()
            mainwindow.show()
        elif event.type() == QEvent.Close:
            mainwindow.win.pushButton_3.setEnabled(True)
            mainwindow.show()
            self.close()
            win.dockWidget.close()
            win.dockWidget_3.close()
        elif event.type() == QEvent.KeyPress and event.key() == QtCore.Qt.Key_Escape:
            mainwindow.win.pushButton_3.setEnabled(True)
            label.close()
        elif event.type() == QEvent.Resize and src == label:
            w = self.w
            h = self.h
            wfactor = w / label.geometry().width() if w <= self.width else w / label.geometry().width()
            hfactor = h / label.geometry().height() if h <= self.height else h / label.geometry().height()
            label.wfactor = wfactor
            label.hfactor = hfactor
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

    def highlight(self, label, storerectbrushcolor, storecolor, selectedbox_begin, selectedbox_end, storebegin, storeend, win):
        current_row = win.listWidget_2.currentRow()
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
            win.listWidget_2.clearSelection()

    def additem(self):
        label = self.label
        storebegin = label.newbegin
        storeend = label.newend
        self.templist.append(self.storelabel(storebegin[-1], storeend[-1], self.name))

    def removeitem(self, label):
        win = self.win
        row = win.listWidget_2.currentIndex().row()
        label.rectlist.pop(row)
        label.storeend.pop(row)
        label.storebegin.pop(row)
        label.newend.pop(row)
        label.newbegin.pop(row)
        win.listWidget_2.takeItem(row)
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
        y = pos.y() + dialog.dialog.frame_2.height() - label.pos().y() - label.geometry().height()
        x = pos.x() + dialog.dialog.frame_2.width() - label.pos().x() - label.geometry().width()
        if y > 0 and x < 0:
            dialog.move(pos.x(), pos.y()-y)
        elif y < 0 and x > 0:
            dialog.move(pos.x() - x - 20, pos.y())
        elif x > 0 and y > 0:
            dialog.move(pos.x() - x - 20, pos.y()-y)
        else:
            dialog.move(pos)
        dialog.show()

    def go2lastsaved(self, win, basename, dpi, storelabeling):
        label = self.label
        last_file = self.last_file
        dir = os.path.dirname(last_file)
        self.path = dir
        m = os.scandir(dir)
        for file in m:
            path = os.path.join(dir, file.name)
            if os.path.samefile(path, last_file):
                basename = os.path.splitext(os.path.basename(path))[0]
                win.dockWidget.setFloating(True)
                win.dockWidget_3.setFloating(True)
                self.readimg(path, win, label, self.width, self.height, dpi, storelabeling)
                win.dockWidget.show()
                win.dockWidget_3.show()
                label.show()
                self.storelabeling['Image path'] = path
                break
        self.filename = (os.path.join(dir, file.name) for file in m)
        self.saveloc = f'{self.path}\{basename}.json'
        self.dir = True
        self.singal = False


class Dialog(QDialog):
    def __init__(self, parent, mainwindow):
        super().__init__(parent)
        dialog = self.dialog = Ui_Dialog()
        dialog.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.mainwin = mainwindow
        listWidget = dialog.listWidget
        listWidget.itemPressed.connect(lambda: self.setlabel(self.mainwin, listWidget))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.additem(self.dialog)
            self.dialog.lineEdit_4.clear()

    def setlabel(self, mainwin, listWidget):
        data = listWidget.currentItem()
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
        text = dialog.lineEdit_4.text()
        if text:
            dialog.listWidget.addItem(text)


class Dialog3(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        dialog = self.dialog = Dialog2.Ui_Dialog()
        dialog.setupUi(self)
        font = QtGui.QFont()
        font.setPixelSize(12)
        buttonBox = dialog.buttonBox
        dpi = parent.dpi
        storelabeling = parent.storelabeling
        buttonBox.accepted.connect(lambda: parent.go2lastsaved(parent.win, parent.basename, dpi, storelabeling))
        buttonBox.rejected.connect(lambda: parent.loadimg(False, parent.win, parent.path, parent.label, dpi, storelabeling))
        buttonBox.button(QDialogButtonBox.Ok).setFont(font)
        buttonBox.button(QDialogButtonBox.Cancel).setFont(font)
