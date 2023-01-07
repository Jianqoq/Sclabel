from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, QSize, Qt, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QFrame, QWidget, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QVBoxLayout, QCheckBox, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 346)
        MainWindow.setStyleSheet("")
        font = QFont()
        setFamily = font.setFamily
        setPixelSize = font.setPixelSize
        setBold = font.setBold
        setItalic = font.setItalic
        setWeight = font.setWeight
        centralwidget = QWidget(MainWindow)
        centralwidget.setStyleSheet("")
        centralwidget.setObjectName("centralwidget")
        frame_2 = self.frame_2 = QFrame(centralwidget)
        frame_2.setGeometry(QRect(40, 30, 321, 290))
        frame_2.setMinimumSize(QSize(40, 40))
        frame_2.setMaximumSize(QSize(500, 600))
        frame_2.setStyleSheet("\n"
"QFrame#frame_2{\n"
"background-color: rgb(209, 209, 209);\n"
"border-radius: 5px;\n"
"}\n"
"")
        frame_2.setFrameShape(QFrame.StyledPanel)
        frame_2.setFrameShadow(QFrame.Raised)
        frame_2.setObjectName("frame_2")
        frame = self.frame = QFrame(frame_2)
        frame.setGeometry(QRect(1, 30, 319, 259))
        frame.setStyleSheet("QFrame#frame{\n"
"background-color: rgb(94, 94, 94);\n"
"border: 0.5px solid rgb(209, 209, 209);;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"}")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setObjectName("frame")
        line = self.line = QFrame(frame)
        line.setGeometry(QRect(1, 59, 321, 1))
        line.setStyleSheet("background-color: rgb(108, 108, 108);")
        line.setFrameShadow(QFrame.Sunken)
        line.setLineWidth(1)
        line.setFrameShape(QFrame.HLine)
        line.setObjectName("line")
        layoutWidget = QWidget(frame)
        layoutWidget.setGeometry(QRect(10, 60, 231, 191))
        layoutWidget.setObjectName("layoutWidget")
        horizontalLayout = QHBoxLayout(layoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setObjectName("horizontalLayout")
        gridLayout = self.gridLayout = QGridLayout()
        gridLayout.setObjectName("gridLayout")
        label_2 = self.label_2 = QLabel(layoutWidget)
        setFamily("Segoe UI")
        setPixelSize(10)
        label_2.setFont(font)
        label_2.setStyleSheet("color: rgb(211, 211, 211);")
        label_2.setAlignment(Qt.AlignCenter)
        label_2.setObjectName("label_2")
        gridLayout.addWidget(label_2, 1, 0, 1, 1)
        label = self.label = QLabel(layoutWidget)
        label.setMinimumSize(QSize(50, 0))
        setFamily("Segoe UI")
        setPixelSize(10)
        label.setFont(font)
        label.setStyleSheet("color: rgb(211, 211, 211);")
        label.setAlignment(Qt.AlignCenter)
        label.setObjectName("label")
        gridLayout.addWidget(label, 0, 0, 1, 1)
        horizontalLayout.addLayout(gridLayout)
        _2 = QVBoxLayout()
        _2.setObjectName("_2")
        lineEdit_2 = self.lineEdit_2 = QLineEdit(layoutWidget)
        lineEdit_2.setMinimumSize(QSize(0, 40))
        setFamily("Bahnschrift SemiBold")
        setPixelSize(7)
        setBold(False)
        setItalic(False)
        setWeight(7)
        lineEdit_2.setFont(font)
        lineEdit_2.setFocusPolicy(Qt.ClickFocus)
        lineEdit_2.setLayoutDirection(Qt.LeftToRight)
        lineEdit_2.setStyleSheet("QLineEdit#lineEdit_2{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);font: 63 7pt \"Bahnschrift SemiBold\";\n"
"color: rgb(236, 236, 236);}\n"
"QLineEdit#lineEdit_2:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);font: 63 8pt \"Bahnschrift SemiBold\";\n"
"color: rgb(236, 236, 236);}")
        lineEdit_2.setAlignment(Qt.AlignCenter)
        lineEdit_2.setObjectName("lineEdit_2")
        _2.addWidget(lineEdit_2)
        lineEdit = self.lineEdit = QLineEdit(layoutWidget)
        lineEdit.setMinimumSize(QSize(0, 40))
        setFamily("Bahnschrift SemiBold")
        setPixelSize(7)
        setBold(False)
        setItalic(False)
        setWeight(7)
        lineEdit.setFont(font)
        lineEdit.setFocusPolicy(Qt.ClickFocus)
        lineEdit.setStyleSheet("QLineEdit#lineEdit{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);font: 63 7pt \"Bahnschrift SemiBold\";\n"
"color: rgb(236, 236, 236);}\n"
"QLineEdit#lineEdit:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);font: 63 8pt \"Bahnschrift SemiBold\";\n"
"color: rgb(236, 236, 236);}")
        lineEdit.setAlignment(Qt.AlignCenter)
        lineEdit.setObjectName("lineEdit")
        _2.addWidget(lineEdit)
        horizontalLayout.addLayout(_2)
        layoutWidget1 = self.layoutWidget1 = QWidget(frame)
        layoutWidget1.setGeometry(QRect(250, 60, 71, 191))
        layoutWidget1.setObjectName("layoutWidget1")
        verticalLayout = self.verticalLayout = QVBoxLayout(layoutWidget1)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        checkBox = self.checkBox = QCheckBox(layoutWidget1)
        
        setFamily("Segoe UI")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        checkBox.setFont(font)
        checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        checkBox.setObjectName("checkBox")
        verticalLayout.addWidget(checkBox)
        checkBox_2 = self.checkBox_2 = QCheckBox(layoutWidget1)
        
        setFamily("Segoe UI")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        checkBox_2.setFont(font)
        checkBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        checkBox_2.setObjectName("checkBox_2")
        verticalLayout.addWidget(checkBox_2)
        layoutWidget2 = QWidget(frame)
        layoutWidget2.setGeometry(QRect(11, 8, 301, 47))
        layoutWidget2.setObjectName("layoutWidget2")
        horizontalLayout_2 = QHBoxLayout(layoutWidget2)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        create = self.create = QPushButton(layoutWidget2)
        create.setMinimumSize(QSize(0, 45))
        
        setFamily("Segoe UI")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        create.setFont(font)
        create.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 5px;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgba(0, 151, 193, 240);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     border-radius: 5px;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(237, 95, 95);\n"
"}")
        create.setObjectName("create")
        horizontalLayout_2.addWidget(create)
        settings = self.settings = QPushButton(layoutWidget2)
        settings.setMinimumSize(QSize(0, 45))
        
        setFamily("Segoe UI")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        settings.setFont(font)
        settings.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 5px;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     border-radius: 5px;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(189, 189, 189);\n"
"}")
        settings.setObjectName("settings")
        horizontalLayout_2.addWidget(settings)
        pushButton_3 = self.pushButton_3 = QPushButton(layoutWidget2)
        pushButton_3.setMinimumSize(QSize(0, 45))
        
        setFamily("Segoe UI")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        pushButton_3.setFont(font)
        pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 5px;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(156, 156, 156);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     border-radius: 5px;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(189, 189, 189);\n"
"}")
        pushButton_3.setObjectName("pushButton_3")
        horizontalLayout_2.addWidget(pushButton_3)
        frame_3 = self.frame_3 = QFrame(frame_2)
        frame_3.setGeometry(QRect(0, 0, 211, 29))
        frame_3.setFrameShape(QFrame.StyledPanel)
        frame_3.setFrameShadow(QFrame.Raised)
        frame_3.setObjectName("frame_3")
        pushButton = self.pushButton = QPushButton(frame_2)
        pushButton.setGeometry(QRect(266, 0, 55, 29))
        pushButton.setMinimumSize(QSize(0, 0))
        pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    border:none;\n"
"    background-color: transparent;\n"
"    image: url(:/image/close (6).png);\n"
"border-top-right-radius: 5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border:none;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(255, 49, 49);\n"
"    image: url(:/image/close (5).png);\n"
"border-top-right-radius: 5px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    border:none;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(255, 137, 137);\n"
"border-top-right-radius: 5px;\n"
"}")
        pushButton.setText("")
        pushButton.setObjectName("pushButton")
        line_2 = self.line_2 = QFrame(frame_2)
        line_2.setGeometry(QRect(3, 30, 315, 1))
        line_2.setStyleSheet("background-color: rgb(230, 230, 230);")
        line_2.setFrameShadow(QFrame.Raised)
        line_2.setLineWidth(3)
        line_2.setFrameShape(QFrame.HLine)
        line_2.setObjectName("line_2")
        pushButton_2 = self.pushButton_2 = QPushButton(frame_2)
        pushButton_2.setGeometry(QRect(211, 0, 55, 29))
        pushButton_2.setMinimumSize(QSize(0, 0))
        pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    border:none;\n"
"    background-color: transparent;\n"
"    image: url(:/image/minimize (5).png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border:none;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(134, 134, 134);\n"
"    image: url(:/image/minimize (6).png);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    border:none;\n"
"    color: rgb(224, 224, 224);\n"
"    background-color: rgb(179, 179, 179);\n"
"    image: url(:/image/minimize (6).png);\n"
"}")
        pushButton_2.setText("")
        pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(centralwidget)

        self.retranslateUi(MainWindow)
        pushButton.clicked.connect(MainWindow.close) # type: ignore
        pushButton_2.clicked.connect(MainWindow.showMinimized) # type: ignore
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.label.setText(_translate("MainWindow", "Height"))
        self.lineEdit_2.setText(_translate("MainWindow", "640"))
        self.lineEdit.setText(_translate("MainWindow", "640"))
        self.checkBox.setText(_translate("MainWindow", "Hide"))
        self.checkBox_2.setText(_translate("MainWindow", "Labeling"))
        self.create.setText(_translate("MainWindow", "Create"))
        self.settings.setText(_translate("MainWindow", "Settings"))
        self.pushButton_3.setText(_translate("MainWindow", "Annotation"))

import Icon.icon_rc
