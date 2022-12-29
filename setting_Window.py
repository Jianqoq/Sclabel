from main import *
from threading import *
import UI.setting
from PyQt5.QtWidgets import QFileDialog, QWidget
from functions.Image_process import *


class SettingWindow(QWidget):
    def __init__(self, main_win_pos, size, main_win):
        super(SettingWindow, self).__init__()
        
        # set UI
        self.win = UI.setting.Ui_Form()
        win = self.win
        win.setupUi(self)
        self.setObjectName('Settings')
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(QRect(0, 0, 0, 0))
        win.progressBar.hide()
        win.pushButton_2.setEnabled(False)
        
        self.mainwin = main_win
        self.imgdict = None
        self.name = 'image'
        
        # get config file name
        self.configname = main_win.configname
        configname = self.configname

        # get config file path
        self.path = rf'C:\Users\{os.getlogin()}\Documents\Sclabel'
        path = self.path
        
        # fill widgets with text
        self.init_text(win, path, configname)

        # connect signals
        getdir = self.getdir
        openfolder = self.openfolder
        enableapply = lambda: win.pushButton_2.setEnabled(True)
        win.pushButton_2.clicked.connect(lambda: self.confirm(win, main_win, path, configname))
        win.pushButton_5.clicked.connect(lambda: self.displayProgressbar(win.progressBar, win.frame))
        win.pushButton_3.clicked.connect(lambda: self.close())
        win.pushButton_5.clicked.connect(lambda: self.threading1(win, main_win))
        win.pushButton_4.clicked.connect(lambda: (self.confirm(win, main_win, path, configname), self.close()))
        win.pushButton.clicked.connect(lambda: getdir(win.lineEdit))
        win.pushButton_6.clicked.connect(lambda: getdir(win.lineEdit_4))
        win.pushButton_7.clicked.connect(lambda: getdir(win.lineEdit_6))
        win.pushButton_11.clicked.connect(lambda: getdir(win.lineEdit_7))
        win.pushButton_8.clicked.connect(lambda: openfolder(10, win))
        win.pushButton_9.clicked.connect(lambda: openfolder(9, win))
        win.pushButton_10.clicked.connect(lambda: openfolder(8, win))
        win.pushButton_12.clicked.connect(lambda: openfolder(12, win))
        win.lineEdit.textChanged.connect(enableapply)
        win.lineEdit_2.textEdited.connect(enableapply)
        win.lineEdit_3.textEdited.connect(enableapply)
        win.lineEdit_4.textChanged.connect(enableapply)
        win.lineEdit_6.textChanged.connect(enableapply)
        win.lineEdit_7.textChanged.connect(enableapply)
        win.horizontalSlider.valueChanged.connect(lambda: (enableapply(), self.updateslider(win)))
        win.comboBox_2.currentIndexChanged.connect(enableapply)

        # init setting window display pos
        self_size = self.size()
        winx = int(main_win_pos.x() + size.width()//2 - self_size.width()//2)
        winy = int(main_win_pos.y() + size.height()//2 - self_size.height()//2)
        self.window_pos(winx, winy)

    def window_pos(self, winx, winy):
        if winx < 0 and winy < 0:
            winx = 0
            winy = 0
        if winx < 0:
            winx = 0
        elif winy < 0:
            winy = 0
        self.move(winx, winy)

    def openfolder(self, num, win):
        if num == 8:
            open_dir(win.lineEdit.text(), True)
        elif num == 9:
            open_dir(win.lineEdit_6.text(), True)
        elif num == 10:
            open_dir(win.lineEdit_4.text(), True)
        elif num == 12:
            open_dir(win.lineEdit_7.text(), True)

    def threading1(self, win, mainwin):
        Thread(target=self.dataaugment, args=(win, mainwin,)).start()

    def dataaugment(self, win, mainwin):
        dataaugment(win.lineEdit_6.text(), win.lineEdit_4.text(), win.lineEdit_3.text(),
                    win.lineEdit_5, win.progressBar, mainwin.imgdict[mainwin.image_format],
                    mainwin.slidervalue)

    def getdir(self, lineedit):
        folder = QFileDialog.getExistingDirectory()
        lineedit.setText(folder) if folder else False

    # update config file and update MainWindow variables without quitting the whole software
    def confirm(self, win, mainwin, path, configname):
        name = self.name = win.lineEdit_2.text()
        dir = win.lineEdit.text()
        dir2 = win.lineEdit_4.text()
        name2 = win.lineEdit_3.text()
        aug_load = win.lineEdit_6.text()
        format = str(win.comboBox_2.currentIndex())
        labellication = win.lineEdit_7.text()
        mainwin.slidervalue = win.horizontalSlider.value()
        mainwin.imageformat = format
        mainwin.readpath = dir
        mainwin.name = name
        mainwin.save = dir2
        mainwin.Aug_name = name2
        mainwin.Aug_load = aug_load

        if not name or not dir or not dir2 or not name2 or not aug_load:
            Messagebox('Input name can\'t be empty')
        else:
            self.updatesettings(dir, dir2, name, name2, aug_load, format,
                                labellication, configname, win, path)
            win.pushButton_2.setEnabled(False)

    def updateslider(self, win):
        value = win.horizontalSlider.value()
        win.label_9.setText(str(value))

    def updatesettings(self, dir, dir2, name, name2, aug_load, suffix, dir3, configname, win, path):
        updatefilename(path, dir, 'Saving setting', 'Location', configname)
        updatefilename(path, dir2, 'Saving setting', 'Save Location', configname)
        updatefilename(path, name, 'Saving setting', 'Image name', configname)
        updatefilename(path, name2, 'Saving setting', 'Augment Image name', configname)
        updatefilename(path, aug_load, 'Saving setting', 'augment data load', configname)
        updatefilename(path, str(win.horizontalSlider.value()), 'Saving setting', 'Quality', configname)
        updatefilename(path, suffix, 'Saving setting', 'Image Format', configname)
        updatefilename(path, dir3, 'Saving setting', 'Label Location', configname)

    def init_text(self, win, path, configname):
        config = configparser.ConfigParser()
        config.read(rf'{path}\{configname}')
        win.lineEdit.setText(config.items('Saving setting')[0][1])
        win.lineEdit_2.setText(config.items('Saving setting')[1][1])
        win.lineEdit_4.setText(config.items('Saving setting')[2][1])
        win.lineEdit_3.setText(config.items('Saving setting')[3][1])
        win.lineEdit_6.setText(config.items('Saving setting')[4][1])
        win.label_9.setText(config.items('Saving setting')[10][1])
        win.horizontalSlider.setValue(int(config.items('Saving setting')[10][1]))
        win.comboBox_2.setCurrentIndex(int(config.items('Saving setting')[11][1]))
        win.lineEdit_7.setText(config.items('Saving setting')[12][1])

    def displayProgressbar(self, progressBar, frame):
        anmiation = QPropertyAnimation(progressBar, b"pos", frame)
        anmiation2 = QPropertyAnimation(progressBar, b"size", frame)
        anmiation2.setEndValue(QSize(531, 15))
        anmiation2.setStartValue(QSize(0, 15))
        anmiation.setStartValue(QPoint(265, 451))
        anmiation.setEndValue(QPoint(0, 451))
        anmiation.setDuration(500)
        anmiation.setEasingCurve(QEasingCurve.InOutCubic)
        anmiation2.setEasingCurve(QEasingCurve.InOutCubic)
        anmiation2.setDuration(500)
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(anmiation)
        self.group.addAnimation(anmiation2)
        progressBar.show()
        self.group.start()
