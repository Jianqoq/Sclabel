from setting_Window import *
from UI.main_window import *
from annotation_win import *
from functions.graphic_effect import *
from functions.file_manipulation import *
from cap_pic_show import *
import sys
import ctypes
from PyQt5.QtWidgets import QApplication


class Win(QMainWindow):
    signal = pyqtSignal(int, int, name='valChanged2')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.win = Ui_MainWindow()
        win = self.win
        win.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        shadow(self)
        self.dpi = self.devicePixelRatioF()
        self.path = rf'C:\Users\{os.getlogin()}\Documents\Sclabel'
        path = self.path
        self.offset = None
        self.check = None
        self.height = None
        self.width = None
        self.name = None
        self.save = None
        self.readpath = None
        self.pos2 = None
        self.temp = None
        self.x = None
        self.y = None
        self.filename = None
        self.settingw = None
        self.Aug_load = None
        self.Aug_name = None
        self.posx = 0
        self.posy = 0
        self.lastpos = None
        self.slidervalue = 0
        self.image_format = None
        self.imglabel = None
        self.label = None
        self.labelcheckbox = None
        self.labelling = False
        self.configname = 'config.ini'
        readdir(self, path, os.getlogin())

        # initialize var
        self.init_var(path, win)

        slidervalue = self.slidervalue
        compression = self.compression = int(round(100/slidervalue, 0))
        self.imgdict = {
            '0': (int(cv2.IMWRITE_JPEG_QUALITY), '.jpg', slidervalue),
            '1': (int(cv2.IMWRITE_PNG_COMPRESSION), '.png', compression),
            '2': (int(cv2.IMWRITE_TIFF_COMPRESSION), '.tiff', compression),
            '3': (None, '.bmp', None),
            '4': (None, '.jp2', None),
        }

        onlyint = self.onlyint = QIntValidator()
        win.lineEdit.setValidator(onlyint)
        win.lineEdit_2.setValidator(onlyint)

        win.frame_3.installEventFilter(self)
        win.settings.clicked.connect(lambda: self.settingwin(self.pos(), win.frame_2))
        win.create.clicked.connect(lambda: self.cap_opennewwin(win, self.slidervalue))
        win.pushButton_3.clicked.connect(lambda: self.annotation(win))
        win.checkBox.toggled.connect(lambda: self.update4(path, 'check', win.checkBox.isChecked()))
        win.checkBox_2.toggled.connect(lambda: self.update3(path, 'labeling function', win.checkBox_2.isChecked()))
        win.lineEdit.textEdited.connect(lambda: w_update(self, 'Saving setting', 'width', win.lineEdit))
        win.lineEdit_2.textEdited.connect(lambda: h_update(self, 'Saving setting', 'height', win.lineEdit_2))

        self.move(self.posx, self.posy)

        self.show()

    def annotation(self, win):
        self.window2 = QLineEditMask(geo.width(), geo.height(), self)
        window2 = self.window2
        window2.show()
        point = win.frame.mapToGlobal(win.frame.pos())
        x = point.x() + win.frame.width()//2 - window2.geometry().width()//2
        y = point.y() + win.frame.height()//2 - window2.geometry().height()//2 - 60
        window2.move(x, y)
        win.pushButton_3.setEnabled(False)
        self.labelling = True

    def directannotate(self, path):
        self.window2 = QLineEditMask(geo.width(), geo.height(), self)
        window = self.window2
        saveloc = get_label_filename(path)
        window.storelabeling['Image path'] = path
        window.saveloc = saveloc
        window.win.dockWidget.show()
        window.win.dockWidget_3.show()
        window.readimg(path, window.win, window.label, geo.width(), geo.height())
        window.dir = False
        window.singal = True
        window.win.dockWidget.setFloating(True)
        window.win.dockWidget_3.setFloating(True)
        window.label.show()
        window.hide()

    def init_var(self, path, win):
        config = configparser.ConfigParser()
        config.read(rf'{path}\{self.configname}')
        readpath = self.readpath = config.get('Saving setting', 'Location')
        self.name = config.get('Saving setting', 'Image name')
        save = self.save = config.get('Saving setting', 'Save Location')
        self.Aug_name = config.get('Saving setting', 'Augment Image name')
        Aug_load = self.Aug_load = config.get('Saving setting', 'Augment Data load')
        width = self.width = config.get('Saving setting', 'width')
        height = self.height = config.get('Saving setting', 'height')
        self.posx = int(config.get('Saving setting', 'last_posx'))
        self.posy = int(config.get('Saving setting', 'last_posy'))
        check = self.check = config.get('Saving setting', 'check')
        self.slidervalue = int(config.get('Saving setting', 'Quality'))
        self.image_format = config.get('Saving setting', 'Image Format')
        imglabel = self.imglabel = config.get('Saving setting', 'Label Location')
        labelcheckbox = self.labelcheckbox = config.get('Saving setting', 'Labeling Function')

        win.lineEdit.setText(width)
        win.lineEdit_2.setText(height)
        self.checkTrue(check, win.checkBox)
        self.checkTrue(labelcheckbox, win.checkBox_2)
        open_dir(readpath, False)
        open_dir(save, False)
        open_dir(Aug_load, False)
        open_dir(imglabel, False)

    def checkTrue(self, key, checkbox):
        checkbox.setChecked(True) if key == 'True' else checkbox.setChecked(False)

    def update3(self, path, key, statement: bool):
        checkbox_update(path, key, statement)
        self.labelcheckbox = statement

    def update4(self, path, key, statement: bool):
        checkbox_update(path, key, statement)
        self.check = statement

    @QtCore.pyqtSlot(int, int)
    def updatelabelinfo(self, width, height):
        label = self.label
        if label is not None:
            label.x1 = width
            label.y1 = height
        else:
            self.width = width
            self.height = height

    def settingwin(self, pos, frame_2):
        pos = pos + frame_2.pos()
        self.settingw = SettingWindow(pos, frame_2.size(), self)
        settingw = self.settingw
        settingw.show()

    def cap_opennewwin(self, win, slidervalue):
        self.temp = tempfile.TemporaryDirectory()
        temp = self.temp
        name = temp.name
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        temploc = rf'{name}/image.jpg'
        if win.checkBox.isChecked():
            self.hide()
        window_capture(temploc, 0, 0, w, h)
        self.open_window(temploc, temp, slidervalue, win)

    def keyPressEvent(self, event):
        self.cap_opennewwin(self.win, self.slidervalue) if event.key() == 39 else False

    def eventFilter(self, source, event):
        win = self.win
        offset = self.offset
        if source == win.frame_3 and event.type() == QtCore.QEvent.MouseMove and QtCore.Qt.LeftButton and offset:
            self.pos2 = self.pos() + event.globalPos() - offset
            self.move(self.pos2)
            self.offset = event.globalPos()
            event.accept()
        elif source == win.frame_3 and event.type() == QtCore.QEvent.MouseButtonPress and QtCore.Qt.LeftButton:
            self.offset = event.globalPos()
        elif source == win.frame_3 and event.type() == QtCore.QEvent.MouseButtonRelease and QtCore.Qt.LeftButton:
            lastpos(self.path, self.pos2) if self.pos2 is not None else False

        return super().eventFilter(source, event)

    def open_window(self, temploc, temp, quality, win):
        factor = self.dpi
        image = QPixmap(temploc)
        image.setDevicePixelRatio(factor)
        x = image.width()
        y = image.height()
        self.window = OpenWindow()
        wind = self.window
        wind.filename = temploc
        wind.new_win.setupUi(wind)
        newx = int(x // factor)
        newy = int(y // factor)
        win_instance = self if win.checkBox.isChecked() else None
        self.label = MyLabel2(temploc, temp, x, y, newx, newy, win_instance, quality, wind)
        label = self.label
        label.setPixmap(image)
        self.updateidct()
        label.imagedict = self.imgdict
        label.setFocusPolicy(Qt.StrongFocus)
        label.resize(newx, newy)
        label.setMouseTracking(True)
        wind.setGeometry(0, 0, x, y)
        wind.show()

    def updateidct(self):
        slidervalue = self.slidervalue
        self.compression = int(round(100/slidervalue, 0))
        compression = self.compression
        self.imgdict = {
            '0': (int(cv2.IMWRITE_JPEG_QUALITY), '.jpg', slidervalue),
            '1': (int(cv2.IMWRITE_PNG_COMPRESSION), '.png', compression),
            '2': (int(cv2.IMWRITE_TIFF_COMPRESSION), '.tiff', compression),
            '3': (None, '.bmp', None),
            '4': (None, '.jp2', None),
        }


os.environ['QT_SCALE_FACTOR'] = str(ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100)
os.environ['QT_FONT_DPI'] = str(ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100)
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    geo = app.desktop().screenGeometry(0)
    win = Win()
    app.exec()
