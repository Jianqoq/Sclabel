from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5 import QtGui


class Messagebox(QMessageBox):
    def __init__(self, error):
        super(Messagebox, self).__init__()
        self.box = QMessageBox()
        self.box.setText(error)
        font = QtGui.QFont()
        font.setPixelSize(12)
        self.box.setWindowTitle('Error')
        self.box.setFont(font)
        self.box.exec_()
        self.box.findChild(QPushButton).setFont(font)
