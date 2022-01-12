import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QTextBrowser, QLabel, QComboBox
from PyQt5.QtWidgets import QListWidget, QTableWidget, QTableWidgetItem


class States():
    def __init__(self):
        # 从文件中加载 UI 定义
        self.ui = QUiLoader().load(QFile("./ui/0_kongjian_test.ui"))


if __name__ =='__main__':
    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    # app.setWindowIcon(QIcon('res/logo.jpg'))
    s = States()
    s.ui.show()
    sys.exit(app.exec_())  # 死循环，等待, 除法按下结束才会关闭