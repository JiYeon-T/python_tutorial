import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QRadioButton, QPushButton, QGroupBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtWidgets import QStackedWidget, QComboBox, QToolButton, QRadioButton
from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import Qt, QFile, pyqtSlot
from PyQt5.QtGui import QPainter, QIcon


# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QPushButton.html


def pyqt_pushbutton_test():
    class App(QWidget):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_pushbutton_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.init_ui()

            self.pushed_cnt = 0

        def init_ui(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.
            # button = QPushButton("PySide2 Button", self)
            self.button = QPushButton("&Button", self)  # 直接设置快捷键
            # self.button.setShortcut('Ctrl+S')  # 设置快捷键
            self.button.setCheckable(True)  # If you need toggle behavior
            # self.button.setAutoRepeat(True)  # auto-repeats the activation signal when being pushed down
            self.button.setToolTip("This is button Tip:Click to print log")
            # self.button.setIcon(QIcon('This is icon str'))  # TODO: 设置 Icon, QIcon & QPixmap
            # self.button.setAutoDefault(True)  # 选中状态的按键, 按下回车等同于按按键
            # self.button.setFlat(True)  # 设置为 True 后只有按键被按下才显示按键背景
            # 还提供 button.pressed 和 released 信号
            # self.button.setMenu(QMenu('菜单列表'))
            # self.add_menu()
            # self.button.initStyleOption()
            self.button.move(100, 70)

            # If an event takes place, each PyQt5 widget can emit a signal.
            # A signal does not execute any action, that is done by a slot.
            # PyQt supports many type of signals, not just clicks.
            self.button.clicked.connect(self.on_clock) # 连接槽函数
            self.show() # Finally show() is called to display the window.

        @pyqtSlot()
        def on_clock(self):
            self.pushed_cnt += 1
            if self.button.isChecked():
                print(f"Pyside2 button clicked {self.pushed_cnt}")
                self.button.showMenu()
            else:
                print(f'pop up')

        def add_menu(self):
            """实现菜单功能的按键和普通的按键功能有点冲突, 符合逻辑
            正常情况下不能放到一起使用"""
            menu = QMenu('菜单列表')
            menu.addAction('下一曲')
            menu.addAction('上一曲')
            menu.addAction('播放')
            menu.addAction('暂停')
            self.button.setMenu(menu)

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def qtoolbutton_test():
    # TODO:
    pass


def qradiobutton_test():
    # TODO:
    pass


def qcheckbox_test():
    pass

if __name__ == '__main__':
    pyqt_pushbutton_test()

