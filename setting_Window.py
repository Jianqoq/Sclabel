from main import *
from threading import *
import UI.setting
from PyQt5.QtWidgets import QFileDialog, QWidget
from functions.Image_process import *


class SettingWindow(QWidget):
    def __init__(self, main_win_pos, size, dpi, main_win):
        super(SettingWindow, self).__init__()
        self.win = UI.setting.Ui_Form()
        self.setObjectName('Settings')
        self.ui = self.win.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(QRect(0, 0, 0, 0))
        self.mainwin = main_win
        self.configname = self.mainwin.configname
        self.path = rf'C:\Users\{os.getlogin()}\Documents\Sclabel'
        self.init_text()
        self.win.progressBar.hide()
        self.win.pushButton_2.setEnabled(False)
        self.win.pushButton.clicked.connect(lambda: self.getdir(self.win.lineEdit))
        self.win.pushButton_2.clicked.connect(self.confirm)
        self.win.pushButton_5.clicked.connect(lambda: displayProgressbar(self))
        self.win.pushButton_3.clicked.connect(self.cancel_button)
        self.win.pushButton_5.clicked.connect(self.threading1)
        self.win.pushButton_4.clicked.connect(self.ok_button)
        self.win.pushButton_6.clicked.connect(lambda: self.getdir(self.win.lineEdit_4))
        self.win.pushButton_7.clicked.connect(lambda: self.getdir(self.win.lineEdit_6))
        self.win.pushButton_11.clicked.connect(lambda: self.getdir(self.win.lineEdit_7))
        self.win.pushButton_8.clicked.connect(lambda: self.openfolder(10))
        self.win.pushButton_9.clicked.connect(lambda: self.openfolder(9))
        self.win.pushButton_10.clicked.connect(lambda: self.openfolder(8))
        self.win.pushButton_12.clicked.connect(lambda: self.openfolder(12))
        self.win.lineEdit.textChanged.connect(self.enableapply)
        self.win.lineEdit_2.textEdited.connect(self.enableapply)
        self.win.lineEdit_3.textEdited.connect(self.enableapply)
        self.win.lineEdit_4.textChanged.connect(self.enableapply)
        self.win.lineEdit_6.textChanged.connect(self.enableapply)
        self.win.lineEdit_7.textChanged.connect(self.enableapply)
        self.win.horizontalSlider.valueChanged.connect(self.enableapply)
        self.win.horizontalSlider.valueChanged.connect(self.updateslider)
        self.win.comboBox_2.currentIndexChanged.connect(self.enableapply)
        self.imgdict = None
        self._winx = int(-self.size().width()//dpi + size.width()//dpi + main_win_pos.x())
        self._winy = int(-self.size().height()//dpi + size.height()//dpi + main_win_pos.y())
        self.name = 'image'
        self.window_pos()
        self.move(self._winx, self._winy)

    @property
    def winx(self):
        return self._winx

    @winx.setter
    def winx(self, args):
        arg1, arg2, arg3 = args
        if isinstance(arg1, QPoint) and isinstance(arg2, QSize) and isinstance(arg3, float):
            self._winx = int(self.size().width()//args - arg2.width() + arg1.x())
        else:
            raise ValueError

    @property
    def winy(self):
        return self._winy

    @winy.setter
    def winy(self, args):
        arg1, arg2, arg3 = args
        if isinstance(arg1, QPoint) and isinstance(arg2, QSize) and isinstance(arg3, float):
            self._winy = int(self.size().height() // arg3 - arg2.height() + arg1.y())
        else:
            raise ValueError

    def window_pos(self):
        if self._winx < 0:
            self._winx = 0
        else:
            self._winy = 0

    def openfolder(self, num):
        if num == 8:
            open_dir(self.win.lineEdit.text())
        elif num == 9:
            open_dir(self.win.lineEdit_6.text())
        elif num == 10:
            open_dir(self.win.lineEdit_4.text())
        elif num == 12:
            open_dir(self.win.lineEdit_7.text())

    def threading1(self):
        Thread(target=self.dataaugment).start()

    def enableapply(self):
        self.win.pushButton_2.setEnabled(True)

    def dataaugment(self):
        dataaugment(self.win.lineEdit_6.text(), self.win.lineEdit_4.text(), self.win.lineEdit_3.text(),
                    self.win.lineEdit_5, self.win.progressBar, self.mainwin.imgdict[self.mainwin.image_format],
                    self.mainwin.slidervalue)

    def ok_button(self):
        self.confirm()
        self.cancel_button()

    def cancel_button(self):
        self.close()

    def getdir(self, lineedit):
        folder = QFileDialog.getExistingDirectory()
        lineedit.setText(folder) if folder else False

    # update config file and update MainWindow variables without quitting the whole software
    def confirm(self):
        self.name = self.win.lineEdit_2.text()
        self.dir = self.win.lineEdit.text()
        self.dir2 = self.win.lineEdit_4.text()
        self.name2 = self.win.lineEdit_3.text()
        self.aug_load = self.win.lineEdit_6.text()
        self.format = str(self.win.comboBox_2.currentIndex())
        self.labellication = self.win.lineEdit_7.text()
        self.mainwin.slidervalue = self.win.horizontalSlider.value()
        self.mainwin.imageformat = self.format
        self.mainwin.readpath = self.dir
        self.mainwin.name = self.name
        self.mainwin.save = self.dir2
        self.mainwin.Aug_name = self.name2
        self.mainwin.Aug_load = self.aug_load

        if not self.name or not self.dir or not self.dir2 or not self.name2 or not self.aug_load:
            Messagebox('Input name can\'t be empty')
        else:
            self.updatesettings(self.dir, self.dir2, self.name, self.name2, self.aug_load, self.format,
                                self.labellication, self.configname)
            self.win.pushButton_2.setEnabled(False)

    def updateslider(self):
        value = self.win.horizontalSlider.value()
        self.win.label_9.setText(str(value))

    def updatesettings(self, dir, dir2, name, name2, aug_load, suffix, dir3, configname):
        updatefilename(self.path, dir, 'Saving setting', 'Location', configname)
        updatefilename(self.path, dir2, 'Saving setting', 'Save Location', configname)
        updatefilename(self.path, name, 'Saving setting', 'Image name', configname)
        updatefilename(self.path, name2, 'Saving setting', 'Augment Image name', configname)
        updatefilename(self.path, aug_load, 'Saving setting', 'augment data load', configname)
        updatefilename(self.path, str(self.win.horizontalSlider.value()), 'Saving setting', 'Quality', configname)
        updatefilename(self.path, suffix, 'Saving setting', 'Image Format', configname)
        updatefilename(self.path, dir3, 'Saving setting', 'Label Location', configname)

    def init_text(self):
        config = configparser.ConfigParser()
        config.read(rf'{self.path}\{self.configname}')
        self.win.lineEdit.setText(config.items('Saving setting')[0][1])
        self.win.lineEdit_2.setText(config.items('Saving setting')[1][1])
        self.win.lineEdit_4.setText(config.items('Saving setting')[2][1])
        self.win.lineEdit_3.setText(config.items('Saving setting')[3][1])
        self.win.lineEdit_6.setText(config.items('Saving setting')[4][1])
        self.win.label_9.setText(config.items('Saving setting')[10][1])
        self.win.horizontalSlider.setValue(int(config.items('Saving setting')[10][1]))
        self.win.comboBox_2.setCurrentIndex(int(config.items('Saving setting')[11][1]))
        self.win.lineEdit_7.setText(config.items('Saving setting')[12][1])
