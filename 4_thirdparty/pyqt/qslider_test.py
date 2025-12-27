import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QRadioButton, QPushButton, QGroupBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtWidgets import QStackedWidget, QComboBox, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QAction, QCompleter, QSlider, QDial
from PyQt5.QtWidgets import QDialog, QFileDialog, QInputDialog, QFontDialog, QProgressDialog, QColorDialog
from PyQt5.QtCore import Qt, QFile, pyqtSlot
from PyQt5.QtGui import QPainter, QValidator, QIntValidator, QRegExpValidator


# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QDial.html#PySide2.QtWidgets.PySide2.QtWidgets.QDial


def qslider_test():
    pass

def qdial_test():
    """
    https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QDial.html#PySide2.QtWidgets.PySide2.QtWidgets.QDial

    QDial is used when the user needs to control a value within a program-definable range,
    and the range either wraps around (for example, with angles measured from 0 to 359 degrees)
    or the dialog layout needs a square widget.
    """
    class Win(QMainWindow):

        def __init__(self):
            super().__init__()
            self.setWindowTitle("Dial test")
            self.setGeometry(100, 100, 800, 600)
            self.init_ui()

        def init_ui(self):
            self.dial = QDial()  # 继承自: QAbstractSlider
            self.dial.setGeometry(200, 200, 100, 100)
            self.dial.setNotchesVisible(True)
            self.dial.setRange(1, 100)
            self.dial.setSingleStep(1)
            self.dial.setWrapping(True)  # 转一圈, 每个角落都有刻度
            self.dial.sliderMoved.connect(self._dial_mouse_changed)
            self.dial.sliderPressed.connect(self._dial_pressed)
            self.dial.sliderReleased.connect(self._dial_released)
            self.setCentralWidget(self.dial)

        def _dial_mouse_changed(self, value):
            print('dial text changed:', value)

        def _dial_pressed(self):
            print('dial pressed:', self.dial.sliderPosition())

        def _dial_released(self):
            print('dial released:', self.dial.sliderPosition())

    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    qslider_test()
    qdial_test()
