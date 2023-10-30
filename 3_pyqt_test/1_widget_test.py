import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QTextBrowser, QLabel, QComboBox, QDesktopWidget
from PyQt5.QtWidgets import QListWidget, QTableWidget, QTableWidgetItem, QRadioButton, QCheckBox, QButtonGroup
from PyQt5.QtWidgets import QTableWidget, QTabWidget, QProgressBar, QSpinBox, QFileDialog, QDateEdit
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMessageBox, QInputDialog, QAction
# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtCore import QFile
# from PySide2.QtGui import QIcon
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGroupBox, QMainWindow, QVBoxLayout
# TODO:
# from PyQt5.QtBluetooth import

class States():
    def __init__(self):
        # 从文件中(QtDesigner 生成的)加载 UI 定义
        self.ui = QUiLoader().load(QFile("./ui/0_kongjian_test.ui"))
        #QMessageBox.about( self.ui.centralwidget, '操作成功', '继续下一步')

def qt_designer_test():
    app = QApplication([])
    # app.setWindowIcon(QIcon('res/logo.jpg'))
    s = States()
    s.ui.show()
    sys.exit(app.exec_())

def button_test():
    """add a button"""
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("ButtonTest")

    btn = QPushButton("按钮") # QPushButton(str, parent: QWidget = None)
    btn.setParent(w) # 设置对象的父类

    w.show() # 显示界面
    app.exec_()

def label_test():
    """add a label"""
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("LabelTest")
    w.resize(600, 400) # 设置主要窗口大小
    label = QLabel("标签", w) # QLabel(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    w.show()
    app.exec_()

def qlineedit_test():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("LineEditTest")
    w.resize(600, 400) # 设置主要窗口大小

    account_label = QLabel("账号:", w)
    account_label.setGeometry(20, 20, 50, 20) # 设置位置以及大小 (x, y, w, h)
    account_edit = QLineEdit("请输入账号", w)
    account_edit.setGeometry(60, 20, 200, 20)

    key_label = QLabel("密码", w)
    key_label.setGeometry(20, 60, 50, 20)
    key_edit = QLineEdit("输入密码", w)
    key_edit.setGeometry(60, 60, 200, 20)

    btn = QPushButton("登陆", w)
    btn.setGeometry(20, 100, 70, 20)

    w.show()
    app.exec_()

def modify_position_test():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("LabelTest")
    w.resize(600, 400) # 设置主要窗口大小

    label = QLabel("标签", w) # QLabel(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())

    # QDesktopWidget()获取当前屏幕的组件
    # availableGeometry()屏幕可用的位置坐标
    # center()屏幕中间
    center_pointer = QDesktopWidget().availableGeometry().center()
    print(center_pointer) # 屏幕中心点的位置坐标
    x = center_pointer.x()
    y = center_pointer.y()
    # w.move(x, y) # widget 的左上角处于屏幕中间位置
    #########################################
    # 这里补个小知识
    # 代码注释后面写上todo可以用于后续方便更新定位
    #########################################
    # w.move(x - 300, y -200) # 窗口中间位于屏幕中间
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect())) # typle
    x1, y1, w1, h1 = w.frameGeometry().getRect() # 元组拆包
    w.move(int(x-w1/2), int(y-h1/2)) # 屏幕中间

    # 设置窗口图标
    icon = QIcon("D:\\Files\\GitFile\\python_tutorial\\3_pyqt_test\\res\\logo3.ico")
    print(type(icon))
    w.setWindowIcon(icon)

    w.show()
    app.exec_()


if __name__ =='__main__':
    # qt_designer_test()
    # button_test()
    # label_test()
    # qlineedit_test()
    modify_position_test()