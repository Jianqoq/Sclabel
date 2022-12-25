from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, QSize, QPoint, QEasingCurve, QParallelAnimationGroup


# apply shadow effect to the frameless window
def shadow(src):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(40)
    shadow.setColor(QColor(0, 0, 0, 150))
    shadow.setOffset(0)
    src.setGraphicsEffect(shadow)

# apply animation to the progressbar
def displayProgressbar(self):
    anmiation = QPropertyAnimation(self.win.progressBar, b"pos", self.win.frame)
    anmiation2 = QPropertyAnimation(self.win.progressBar, b"size", self.win.frame)
    anmiation2.setEndValue(QSize(387, 15))
    anmiation2.setStartValue(QSize(0, 15))
    anmiation.setStartValue(QPoint(215, 400))
    anmiation.setEndValue(QPoint(0, 385))
    anmiation.setDuration(500)
    anmiation.setEasingCurve(QEasingCurve.InOutCubic)
    anmiation2.setEasingCurve(QEasingCurve.InOutCubic)
    anmiation2.setDuration(500)
    group = QParallelAnimationGroup()
    group.addAnimation(anmiation)
    group.addAnimation(anmiation2)
    self.win.progressBar.show()
    group.start()
