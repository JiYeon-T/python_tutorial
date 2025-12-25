
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtNfc import QNearFieldManager  # TODO:
from PyQt5.QtBluetooth import QBluetooth  # TODO:

# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QApplication.html


def basic_example():
    use_gui = not '-no-gui' in sys.argv
    # The color specification must be set before you create the QApplication object.
    QApplication.setColorSpec(QApplication.ManyColor)
    app = QApplication(sys.argv) if use_gui else QCoreApplication(sys.argv)

    app.aboutQt()
    # app.alert(QWidget())
    # _update_all_widgets()
    # QApplication.desktop()
    QApplication.beep()
    w = QApplication.focusWidget()
    print(f"{app.styleSheet()}")

    return app.exec_()


def _update_all_widgets():
    """更新所有控件"""
    for widget in QApplication.allWidgets():
        widget.update()

# def _exit_action():
#     exitAct = QAction(tr("E&xit"), self)
#     exitAct.setShortcut(tr("Ctrl+Q"))
#     exitAct.setStatusTip(tr("Exit the application"))
#     exitAct.triggered.connect(qApp.closeAllWindows)


if __name__ =='__main__':
    basic_example()

