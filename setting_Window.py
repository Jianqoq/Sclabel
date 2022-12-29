from main import *
from threading import *
import UI.setting
from PyQt5.QtWidgets import QFileDialog, QWidget
from functions.Image_process import *


class SettingWindow(QWidget):
    def __init__(self, main_win_pos, size, main_win):
        super(SettingWindow, self).__init__()
        self.win = UI.setting.Ui_Form()
        win = self.win
        win.setupUi(self)
        self.setObjectName('Settings')
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(QRect(0, 0, 0, 0))
        self.mainwin = main_win
        self.configname = self.mainwin.configname
        self.path = rf'C:\Users\{os.getlogin()}\Documents\Sclabel'
        self.init_text()
        win.progressBar.hide()
        win.pushButton_2.setEnabled(False)
        
        # connect signals
        win.pushButton.clicked.connect(lambda: self.getdir(win.lineEdit))
        win.pushButton_2.clicked.connect(self.confirm)
        win.pushButton_5.clicked.connect(lambda: displayProgressbar(self))
        win.pushButton_3.clicked.connect(self.cancel_button)
        win.pushButton_5.clicked.connect(self.threading1)
        win.pushButton_4.clicked.connect(self.ok_button)
        win.pushButton_6.clicked.connect(lambda: self.getdir(win.lineEdit_4))
        win.pushButton_7.clicked.connect(lambda: self.getdir(win.lineEdit_6))
        win.pushButton_11.clicked.connect(lambda: self.getdir(win.lineEdit_7))
        win.pushButton_8.clicked.connect(lambda: self.openfolder(10))
        win.pushButton_9.clicked.connect(lambda: self.openfolder(9))
        win.pushButton_10.clicked.connect(lambda: self.openfolder(8))
        win.pushButton_12.clicked.connect(lambda: self.openfolder(12))
        win.lineEdit.textChanged.connect(self.enableapply)
        win.lineEdit_2.textEdited.connect(self.enableapply)
        win.lineEdit_3.textEdited.connect(self.enableapply)
        win.lineEdit_4.textChanged.connect(self.enableapply)
        win.lineEdit_6.textChanged.connect(self.enableapply)
        win.lineEdit_7.textChanged.connect(self.enableapply)
        win.horizontalSlider.valueChanged.connect(self.enableapply)
        win.horizontalSlider.valueChanged.connect(self.updateslider)
        win.comboBox_2.currentIndexChanged.connect(self.enableapply)

        self.imgdict = None
        self.name = 'image'

        # init setting window display pos
        self_size = self.size()
        self.winx = int(main_win_pos.x() + size.width()//2 - self_size.width()//2)
        self.winy = int(main_win_pos.y() + size.height()//2 - self_size.height()//2)
        self.window_pos()
        self.move(self.winx, self.winy)

    def window_pos(self):
        if self.winx < 0 and self.winy < 0:
            self.winx = 0
            self.winy = 0
        if self.winx < 0:
            self.winx = 0
        elif self.winy < 0:
            self.winy = 0

    def openfolder(self, num):
        if num == 8:
            open_dir(self.win.lineEdit.text(), True)
        elif num == 9:
            open_dir(self.win.lineEdit_6.text(), True)
        elif num == 10:
            open_dir(self.win.lineEdit_4.text(), True)
        elif num == 12:
            open_dir(self.win.lineEdit_7.text(), True)

    def threading1(self):
        Thread(target=self.dataaugment).start()

    def enableapply(self):
        self.win.pushButton_2.setEnabled(True)

    def dataaugment(self):
        win = self.win
        mainwin = self.mainwin
        dataaugment(win.lineEdit_6.text(), win.lineEdit_4.text(), win.lineEdit_3.text(),
                    win.lineEdit_5, win.progressBar, mainwin.imgdict[mainwin.image_format],
                    mainwin.slidervalue)

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
        win = self.win
        mainwin = self.mainwin
        self.name = win.lineEdit_2.text()
        dir = win.lineEdit.text()
        dir2 = win.lineEdit_4.text()
        name2 = win.lineEdit_3.text()
        aug_load = win.lineEdit_6.text()
        format = str(win.comboBox_2.currentIndex())
        labellication = win.lineEdit_7.text()
        mainwin.slidervalue = win.horizontalSlider.value()
        mainwin.imageformat = format
        mainwin.readpath = dir
        mainwin.name = self.name
        mainwin.save = dir2
        mainwin.Aug_name = name2
        mainwin.Aug_load = aug_load

        if not self.name or not dir or not dir2 or not name2 or not aug_load:
            Messagebox('Input name can\'t be empty')
        else:
            self.updatesettings(dir, dir2, self.name, name2, aug_load, format,
                                labellication, self.configname)
            win.pushButton_2.setEnabled(False)

    def updateslider(self):
        win = self.win
        value = win.horizontalSlider.value()
        win.label_9.setText(str(value))

    def updatesettings(self, dir, dir2, name, name2, aug_load, suffix, dir3, configname):
        path = self.path
        updatefilename(path, dir, 'Saving setting', 'Location', configname)
        updatefilename(path, dir2, 'Saving setting', 'Save Location', configname)
        updatefilename(path, name, 'Saving setting', 'Image name', configname)
        updatefilename(path, name2, 'Saving setting', 'Augment Image name', configname)
        updatefilename(path, aug_load, 'Saving setting', 'augment data load', configname)
        updatefilename(path, str(self.win.horizontalSlider.value()), 'Saving setting', 'Quality', configname)
        updatefilename(path, suffix, 'Saving setting', 'Image Format', configname)
        updatefilename(path, dir3, 'Saving setting', 'Label Location', configname)

    def init_text(self):
        win = self.win
        config = configparser.ConfigParser()
        config.read(rf'{self.path}\{self.configname}')
        win.lineEdit.setText(config.items('Saving setting')[0][1])
        win.lineEdit_2.setText(config.items('Saving setting')[1][1])
        win.lineEdit_4.setText(config.items('Saving setting')[2][1])
        win.lineEdit_3.setText(config.items('Saving setting')[3][1])
        win.lineEdit_6.setText(config.items('Saving setting')[4][1])
        win.label_9.setText(config.items('Saving setting')[10][1])
        win.horizontalSlider.setValue(int(config.items('Saving setting')[10][1]))
        win.comboBox_2.setCurrentIndex(int(config.items('Saving setting')[11][1]))
        win.lineEdit_7.setText(config.items('Saving setting')[12][1])
