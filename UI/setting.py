from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import QRect, QSize, Qt, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QFrame, QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton,\
        QSizePolicy, QProgressBar, QSlider, QComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        font = QFont()
        setFamily = font.setFamily
        setPixelSize = font.setPixelSize
        setBold = font.setBold
        setItalic = font.setItalic
        setWeight = font.setWeight
        Form.setObjectName("Form")
        Form.resize(551, 591)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(551, 591))
        Form.setMaximumSize(QSize(551, 591))
        Form.setStyleSheet("")
        frame = self.frame = QFrame(Form)
        frame.setGeometry(QRect(0, 0, 551, 591))
        frame.setStyleSheet("QFrame#frame{\n"
"background-color: rgb(94, 94, 94);\n"
"}")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Plain)
        frame.setObjectName("frame")
        layoutWidget = self.layoutWidget = QWidget(frame)
        layoutWidget.setGeometry(QRect(360, 530, 181, 61))
        layoutWidget.setObjectName("layoutWidget")
        horizontalLayout = self.horizontalLayout = QHBoxLayout(layoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(7)
        horizontalLayout.setObjectName("horizontalLayout")
        pushButton_4 = self.pushButton_4 = QPushButton(layoutWidget)
        pushButton_4.setMinimumSize(QSize(0, 35))
        
        setFamily("Yu Gothic UI Semibold")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        pushButton_4.setFont(font)
        pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(126, 126, 126);\n"
"    border-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(155, 155, 155);\n"
"    border-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(183, 183, 183);\n"
"    border-color: rgb(192, 192, 192);\n"
"}")
        pushButton_4.setObjectName("pushButton_4")
        horizontalLayout.addWidget(pushButton_4)
        pushButton_3 = self.pushButton_3 = QPushButton(layoutWidget)
        pushButton_3.setMinimumSize(QSize(0, 35))
        
        setFamily("Yu Gothic UI Semibold")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        pushButton_3.setFont(font)
        pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(139, 139, 139);\n"
"    border-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(155, 155, 155);\n"
"    border-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(183, 183, 183);\n"
"    border-color: rgb(192, 192, 192);\n"
"}")
        pushButton_3.setObjectName("pushButton_3")
        horizontalLayout.addWidget(pushButton_3)
        pushButton_2 = self.pushButton_2 = QPushButton(layoutWidget)
        pushButton_2.setMinimumSize(QSize(0, 35))
        
        setFamily("Yu Gothic UI Semibold")
        setPixelSize(11)
        setBold(True)
        setWeight(75)
        pushButton_2.setFont(font)
        pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(0, 107, 157);\n"
"    border-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(0, 122, 179);\n"
"    border-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(0, 144, 211);\n"
"    border-color: rgb(192, 192, 192);\n"
"}\n"
"QPushButton#pushButton_2:disabled{\n"
"    color: rgb(230, 230, 230);\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"border-style: solid;\n"
"     padding: 6px;\n"
"    background-color: rgb(210, 210, 210);\n"
"    border-color: rgb(192, 192, 192);\n"
"}")
        pushButton_2.setObjectName("pushButton_2")
        horizontalLayout.addWidget(pushButton_2)
        widget = self.widget = QWidget(frame)
        widget.setGeometry(QRect(10, 11, 531, 501))
        widget.setObjectName("widget")
        verticalLayout_2 = self.verticalLayout_2 = QVBoxLayout(widget)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.setSpacing(0)
        verticalLayout_2.setObjectName("verticalLayout_2")
        horizontalLayout_2 = self.horizontalLayout_2 = QHBoxLayout()
        horizontalLayout_2.setSpacing(7)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        label = self.label = QLabel(widget)
        label.setMinimumSize(QSize(72, 0))
        label.setMaximumSize(QSize(300, 52))
        
        setFamily("Segoe UI")
        setPixelSize(13)
        setBold(True)
        setWeight(75)
        label.setFont(font)
        label.setStyleSheet("color: rgb(255, 255, 255);")
        label.setWordWrap(False)
        label.setObjectName("label")
        horizontalLayout_2.addWidget(label)
        lineEdit = self.lineEdit = QLineEdit(widget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lineEdit.sizePolicy().hasHeightForWidth())
        lineEdit.setSizePolicy(sizePolicy)
        lineEdit.setMinimumSize(QSize(0, 30))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(12)
        setBold(True)
        setItalic(False)
        font.setUnderline(False)
        setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        lineEdit.setFont(font)
        lineEdit.setStyleSheet("QLineEdit#lineEdit{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);\n"
"color: rgb(236, 236, 236);\n"
"}\n"
"color: rgb(217, 217, 217);\n"
"QLineEdit#lineEdit:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);}")
        lineEdit.setObjectName("lineEdit")
        horizontalLayout_2.addWidget(lineEdit)
        pushButton = self.pushButton = QPushButton(widget)
        pushButton.setEnabled(True)
        pushButton.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton.setFont(font)
        pushButton.setStyleSheet("QPushButton#pushButton{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/image/dot.png"), QIcon.Normal, QIcon.Off)
        pushButton.setIcon(icon)
        pushButton.setIconSize(QSize(12, 12))
        pushButton.setObjectName("pushButton")
        horizontalLayout_2.addWidget(pushButton)
        pushButton_10 = self.pushButton_10 = QPushButton(widget)
        pushButton_10.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton_10.setFont(font)
        pushButton_10.setStyleSheet("QPushButton#pushButton_10{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_10:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_10:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_10.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/image/folder-open.png"), QIcon.Normal, QIcon.Off)
        pushButton_10.setIcon(icon1)
        pushButton_10.setIconSize(QSize(20, 20))
        pushButton_10.setObjectName("pushButton_10")
        horizontalLayout_2.addWidget(pushButton_10)
        verticalLayout_2.addLayout(horizontalLayout_2)
        horizontalLayout_8 = self.horizontalLayout_8 = QHBoxLayout()
        horizontalLayout_8.setSpacing(7)
        horizontalLayout_8.setObjectName("horizontalLayout_8")
        label_8 = self.label_8 = QLabel(widget)
        
        setFamily("Segoe UI")
        setPixelSize(13)
        setBold(True)
        setWeight(75)
        label_8.setFont(font)
        label_8.setStyleSheet("color: rgb(255, 255, 255);")
        label_8.setObjectName("label_8")
        horizontalLayout_8.addWidget(label_8)
        lineEdit_6 = self.lineEdit_6 = QLineEdit(widget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lineEdit_6.sizePolicy().hasHeightForWidth())
        lineEdit_6.setSizePolicy(sizePolicy)
        lineEdit_6.setMinimumSize(QSize(0, 30))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(12)
        setBold(True)
        setItalic(False)
        setWeight(75)
        font.setStyleStrategy(QFont.PreferDefault)
        lineEdit_6.setFont(font)
        lineEdit_6.setStyleSheet("QLineEdit#lineEdit_6{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);\n"
"color: rgb(236, 236, 236);}\n"
"QLineEdit#lineEdit_6:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);\n"
"color: rgb(236, 236, 236);}")
        lineEdit_6.setObjectName("lineEdit_6")
        horizontalLayout_8.addWidget(lineEdit_6)
        pushButton_7 = self.pushButton_7 = QPushButton(widget)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pushButton_7.sizePolicy().hasHeightForWidth())
        pushButton_7.setSizePolicy(sizePolicy)
        pushButton_7.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton_7.setFont(font)
        pushButton_7.setStyleSheet("QPushButton#pushButton_7{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_7:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_7:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_7.setText("")
        pushButton_7.setIcon(icon)
        pushButton_7.setIconSize(QSize(12, 12))
        pushButton_7.setObjectName("pushButton_7")
        horizontalLayout_8.addWidget(pushButton_7)
        pushButton_9 = self.pushButton_9 = QPushButton(widget)
        pushButton_9.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton_9.setFont(font)
        pushButton_9.setStyleSheet("QPushButton#pushButton_9{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_9:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_9:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_9.setText("")
        pushButton_9.setIcon(icon1)
        pushButton_9.setIconSize(QSize(20, 20))
        pushButton_9.setObjectName("pushButton_9")
        horizontalLayout_8.addWidget(pushButton_9)
        verticalLayout_2.addLayout(horizontalLayout_8)
        horizontalLayout_3 = self.horizontalLayout_3 = QHBoxLayout()
        horizontalLayout_3.setSpacing(7)
        horizontalLayout_3.setObjectName("horizontalLayout_3")
        label_2 = self.label_2 = QLabel(widget)
        
        setFamily("Segoe UI")
        setPixelSize(13)
        setBold(True)
        setWeight(75)
        label_2.setFont(font)
        label_2.setStyleSheet("color: rgb(255, 255, 255);")
        label_2.setObjectName("label_2")
        horizontalLayout_3.addWidget(label_2)
        lineEdit_2 = self.lineEdit_2 = QLineEdit(widget)
        lineEdit_2.setMinimumSize(QSize(0, 30))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(12)
        setBold(True)
        setWeight(75)
        font.setStyleStrategy(QFont.PreferDefault)
        lineEdit_2.setFont(font)
        lineEdit_2.setStyleSheet("QLineEdit#lineEdit_2{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);\n"
"color: rgb(236, 236, 236);\n"
"}\n"
"QLineEdit#lineEdit_2:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);\n"
"color: rgb(236, 236, 236);}")
        lineEdit_2.setObjectName("lineEdit_2")
        horizontalLayout_3.addWidget(lineEdit_2)
        label_9 = self.label_9 = QLabel(widget)
        
        setFamily("Segoe UI")
        setPixelSize(9)
        label_9.setFont(font)
        label_9.setStyleSheet("color: rgb(255, 255, 255);")
        label_9.setObjectName("label_9")
        horizontalLayout_3.addWidget(label_9)
        horizontalSlider = self.horizontalSlider = QSlider(widget)
        horizontalSlider.setMaximum(100)
        horizontalSlider.setOrientation(Qt.Horizontal)
        horizontalSlider.setTickPosition(QSlider.NoTicks)
        horizontalSlider.setTickInterval(1)
        horizontalSlider.setObjectName("horizontalSlider")
        horizontalLayout_3.addWidget(horizontalSlider)
        label_7 = self.label_7 = QLabel(widget)
        
        setFamily("Segoe UI")
        setPixelSize(9)
        label_7.setFont(font)
        label_7.setStyleSheet("color: rgb(255, 255, 255);")
        label_7.setObjectName("label_7")
        horizontalLayout_3.addWidget(label_7)
        comboBox_2 = self.comboBox_2 = QComboBox(widget)
        comboBox_2.setMinimumSize(QSize(70, 24))
        
        setFamily("Arial")
        setPixelSize(8)
        comboBox_2.setFont(font)
        comboBox_2.setStyleSheet("QComboBox{border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);}\n"
"QComboBox:hover{border-radius: 5px;\n"
"background-color: rgb(214, 214, 214);\n"
"}")
        comboBox_2.setObjectName("comboBox_2")
        comboBox_2.addItem("")
        comboBox_2.addItem("")
        comboBox_2.addItem("")
        comboBox_2.addItem("")
        comboBox_2.addItem("")
        horizontalLayout_3.addWidget(comboBox_2)
        verticalLayout_2.addLayout(horizontalLayout_3)
        horizontalLayout_6 = QHBoxLayout()
        horizontalLayout_6.setSpacing(7)
        horizontalLayout_6.setObjectName("horizontalLayout_6")
        label_6 = self.label_6 = QLabel(widget)
        label_6.setMinimumSize(QSize(71, 0))
        
        setFamily("Segoe UI")
        setPixelSize(13)
        setBold(True)
        setWeight(75)
        label_6.setFont(font)
        label_6.setStyleSheet("color: rgb(255, 255, 255);")
        label_6.setObjectName("label_6")
        horizontalLayout_6.addWidget(label_6)
        lineEdit_4 = self.lineEdit_4 = QLineEdit(widget)
        lineEdit_4.setMinimumSize(QSize(0, 30))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(12)
        setBold(True)
        setItalic(False)
        setWeight(75)
        font.setStyleStrategy(QFont.PreferDefault)
        lineEdit_4.setFont(font)
        lineEdit_4.setStyleSheet("QLineEdit#lineEdit_4{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);\n"
"color: rgb(236, 236, 236);}\n"
"QLineEdit#lineEdit_4:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);\n"
"color: rgb(236, 236, 236);}")
        lineEdit_4.setText("")
        lineEdit_4.setObjectName("lineEdit_4")
        horizontalLayout_6.addWidget(lineEdit_4)
        pushButton_6 = self.pushButton_6 = QPushButton(widget)
        pushButton_6.setEnabled(True)
        pushButton_6.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton_6.setFont(font)
        pushButton_6.setStyleSheet("QPushButton#pushButton_6{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_6:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_6:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_6.setText("")
        pushButton_6.setIcon(icon)
        pushButton_6.setIconSize(QSize(12, 12))
        pushButton_6.setObjectName("pushButton_6")
        horizontalLayout_6.addWidget(pushButton_6)
        pushButton_8 = self.pushButton_8 = QPushButton(widget)
        pushButton_8.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton_8.setFont(font)
        pushButton_8.setStyleSheet("QPushButton#pushButton_8{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_8:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_8:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_8.setText("")
        pushButton_8.setIcon(icon1)
        pushButton_8.setIconSize(QSize(20, 20))
        pushButton_8.setObjectName("pushButton_8")
        horizontalLayout_6.addWidget(pushButton_8)
        verticalLayout_2.addLayout(horizontalLayout_6)
        horizontalLayout_7 = QHBoxLayout()
        horizontalLayout_7.setSpacing(7)
        horizontalLayout_7.setObjectName("horizontalLayout_7")
        label_5 = self.label_5 = QLabel(widget)
        
        setFamily("Segoe UI")
        setPixelSize(13)
        setBold(True)
        setWeight(75)
        label_5.setFont(font)
        label_5.setStyleSheet("color: rgb(255, 255, 255);")
        label_5.setObjectName("label_5")
        horizontalLayout_7.addWidget(label_5)
        lineEdit_3 = self.lineEdit_3 = QLineEdit(widget)
        lineEdit_3.setMinimumSize(QSize(0, 30))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(12)
        setBold(True)
        setItalic(False)
        setWeight(75)
        font.setStyleStrategy(QFont.PreferDefault)
        lineEdit_3.setFont(font)
        lineEdit_3.setStyleSheet("QLineEdit#lineEdit_3{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);\n"
"color: rgb(236, 236, 236);}\n"
"QLineEdit#lineEdit_3:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);\n"
"color: rgb(236, 236, 236);}\n"
"")
        lineEdit_3.setObjectName("lineEdit_3")
        horizontalLayout_7.addWidget(lineEdit_3)
        verticalLayout_2.addLayout(horizontalLayout_7)
        horizontalLayout_4 = QHBoxLayout()
        horizontalLayout_4.setSpacing(7)
        horizontalLayout_4.setObjectName("horizontalLayout_4")
        label_10 = self.label_10 = QLabel(widget)
        
        setFamily("Segoe UI")
        setPixelSize(13)
        setBold(True)
        setWeight(75)
        label_10.setFont(font)
        label_10.setStyleSheet("color: rgb(255, 255, 255);")
        label_10.setObjectName("label_10")
        horizontalLayout_4.addWidget(label_10)
        lineEdit_7 = self.lineEdit_7 = QLineEdit(widget)
        lineEdit_7.setMinimumSize(QSize(0, 30))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(12)
        setBold(True)
        setItalic(False)
        setWeight(75)
        font.setStyleStrategy(QFont.PreferDefault)
        lineEdit_7.setFont(font)
        lineEdit_7.setStyleSheet("QLineEdit#lineEdit_7{border-radius: 5px;     padding: 6px;    background-color: rgb(143, 143, 143);\n"
"color: rgb(236, 236, 236);}\n"
"QLineEdit#lineEdit_7:hover{border-radius: 5px;\n"
"background-color: rgb(169, 169, 169);\n"
"color: rgb(236, 236, 236);}")
        lineEdit_7.setText("")
        lineEdit_7.setObjectName("lineEdit_7")
        horizontalLayout_4.addWidget(lineEdit_7)
        pushButton_11 = self.pushButton_11 = QPushButton(widget)
        pushButton_11.setEnabled(True)
        pushButton_11.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton_11.setFont(font)
        pushButton_11.setStyleSheet("QPushButton#pushButton_11{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_11:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_11:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_11.setText("")
        pushButton_11.setIcon(icon)
        pushButton_11.setIconSize(QSize(12, 12))
        pushButton_11.setObjectName("pushButton_11")
        horizontalLayout_4.addWidget(pushButton_11)
        pushButton_12 = self.pushButton_12 = QPushButton(widget)
        pushButton_12.setMinimumSize(QSize(30, 20))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(8)
        setBold(True)
        setWeight(75)
        pushButton_12.setFont(font)
        pushButton_12.setStyleSheet("QPushButton#pushButton_12{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_12:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_12:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_12.setText("")
        pushButton_12.setIcon(icon1)
        pushButton_12.setIconSize(QSize(20, 20))
        pushButton_12.setObjectName("pushButton_12")
        horizontalLayout_4.addWidget(pushButton_12)
        verticalLayout_2.addLayout(horizontalLayout_4)
        horizontalLayout_5 = QHBoxLayout()
        horizontalLayout_5.setSpacing(8)
        horizontalLayout_5.setObjectName("horizontalLayout_5")
        label_4 = self.label_4 = QLabel(widget)
        
        setFamily("Segoe UI")
        setPixelSize(13)
        setBold(True)
        setWeight(75)
        label_4.setFont(font)
        label_4.setStyleSheet("color: rgb(255, 255, 255);")
        label_4.setObjectName("label_4")
        horizontalLayout_5.addWidget(label_4)
        pushButton_5 = self.pushButton_5 = QPushButton(widget)
        pushButton_5.setMinimumSize(QSize(0, 25))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(12)
        setBold(True)
        setWeight(75)
        font.setStyleStrategy(QFont.PreferDefault)
        pushButton_5.setFont(font)
        pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"border-radius: 3px;background-color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"border-radius: 3px;    \n"
"    background-color: rgb(191, 197, 197);\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"border-radius: 3px;\n"
"    background-color: rgb(213, 213, 213);\n"
"}")
        pushButton_5.setObjectName("pushButton_5")
        horizontalLayout_5.addWidget(pushButton_5)
        verticalLayout_2.addLayout(horizontalLayout_5)
        verticalLayout = QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        lineEdit_5 = self.lineEdit_5 = QLineEdit(widget)
        lineEdit_5.setMinimumSize(QSize(0, 20))
        
        setFamily("Arial")
        setPixelSize(7)
        lineEdit_5.setFont(font)
        lineEdit_5.setMouseTracking(True)
        lineEdit_5.setFocusPolicy(Qt.NoFocus)
        lineEdit_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        lineEdit_5.setReadOnly(True)
        lineEdit_5.setObjectName("lineEdit_5")
        verticalLayout.addWidget(lineEdit_5)
        progressBar = self.progressBar = QProgressBar(widget)
        progressBar.setMaximumSize(QSize(800, 15))
        
        setFamily("Bahnschrift SemiBold")
        setPixelSize(7)
        setBold(True)
        setWeight(75)
        progressBar.setFont(font)
        progressBar.setStyleSheet("QProgressBar{\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 7px;\n"
"border: 1px solid;\n"
"border-width:1.5px;\n"
"    border-color: rgb(51, 51, 51);\n"
"background-color: rgb(223, 223, 223);\n"
"\n"
"}\n"
"QProgressBar:chunk{\n"
"color: rgb(236, 236, 236);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 161, 118);\n"
"}\n"
"")
        progressBar.setProperty("value", 50)
        progressBar.setAlignment(Qt.AlignCenter)
        progressBar.setTextVisible(True)
        progressBar.setObjectName("progressBar")
        verticalLayout.addWidget(progressBar)
        verticalLayout_2.addLayout(verticalLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Setting"))
        self.pushButton_4.setText(_translate("Form", "Ok"))
        self.pushButton_3.setText(_translate("Form", "Cancel"))
        self.pushButton_2.setText(_translate("Form", "Apply"))
        self.label.setText(_translate("Form", "Srceenshot Location:"))
        self.lineEdit.setText(_translate("Form", "123"))
        self.label_8.setText(_translate("Form", "Data Augment Load:"))
        self.label_2.setText(_translate("Form", "Saving Name:"))
        self.lineEdit_2.setText(_translate("Form", "Image"))
        self.label_9.setText(_translate("Form", "Quality:"))
        self.label_7.setText(_translate("Form", "Format:"))
        self.comboBox_2.setItemText(0, _translate("Form", "JPG"))
        self.comboBox_2.setItemText(1, _translate("Form", "PNG"))
        self.comboBox_2.setItemText(2, _translate("Form", "TIFF"))
        self.comboBox_2.setItemText(3, _translate("Form", "BMP"))
        self.comboBox_2.setItemText(4, _translate("Form", "JP2"))
        self.label_6.setText(_translate("Form", "Augment Images Location:"))
        self.label_5.setText(_translate("Form", "Augment Image Name:"))
        self.label_10.setText(_translate("Form", "Labeling Location:"))
        self.label_4.setText(_translate("Form", "Image Data Augment:"))
        self.pushButton_5.setText(_translate("Form", "Generate"))
import Icon.icon_rc
