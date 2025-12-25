import random
import time
import sys
import os
from PySide2.QtWidgets import QApplication,QWidget,QTextEdit, QMainWindow, QPushButton
from PySide2.QtWidgets import QDialog, QVBoxLayout, QMessageBox, QLineEdit, QAction, QTableWidget, QTableWidgetItem
from PySide2.QtWidgets import QHBoxLayout, QGroupBox, QGridLayout, QTextBrowser, QInputDialog, QFileDialog
from PySide2.QtWidgets import QLabel, QColorDialog, QFontDialog, QSizePolicy, QHBoxLayout
from PySide2.QtWidgets import QComboBox, QTreeView, QFileSystemModel, QFormLayout, QSpinBox
from PySide2.QtWidgets import QDialogButtonBox, QWizard, QWizardPage, QPlainTextEdit
from PySide2.QtCore import Signal, Slot, QObject, QRect, Qt, QDate, QDateTime, QRegExp, QSortFilterProxyModel, QTime
from PySide2.QtCore import Property

from PySide2.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QBrush, QFont
from PySide2.QtGui import QStandardItemModel

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
# webkit
# TODO:from PySide2.QtWebKit import *
import threading
import queue

# 参考资料链接：
# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/
# https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMainWindow.html
# https://doc.qt.io/qtforpython-6.2/PySide6/QtGui/QTextCharFormat.html


def pyqt_basic_test1():

    print(f"ui loop start argv:{sys.argv}")
    # 只要是Qt制作的app，必须有且只有一个 QApplication 对象
    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    window = QMainWindow() # 主窗口
    window.resize(500, 400)
    window.move(500, 300)  # 相对于父控件的位置，由于主窗口没有父控件，变成了相对屏幕左上角的位置
    window.setWindowTitle("薪资统计")

    textEdit = QPlainTextEdit(window)   # window 是textEdit 的父控件
    textEdit.setPlaceholderText("请输入信息")  # 占位信息
    textEdit.move(0, 0)  # 相对于标题栏的下面的左上角的位置
    textEdit.resize(300, 350)
    print(f"text:{textEdit.toPlainText()}")

    button = QPushButton('统计', window)        # 父控件 window
    button.move(400, 0)

    window.show()

    # 最后一个窗口关闭后，程序才停止
    # 类中的一个循环监听方法, 监测我在打开的页面中做了什么
    app.exec_()  #死循环，等待, 除非按下结束才会关闭
    print(" exit")


def calculate_salary_test():
    """计算工资水平
    ################### step2 将这个窗口有关的成员都封装起来 ############################
    # 这样写代码的模块性好, 方便维护
    # 可扩展性好，写其它窗口时候:class Query()....
    # 尽量不要引入全局变量
    """
    class SalaryCalculator:
        """类"""
        def handle_calc(self):
            """槽函数"""
            # print('统计按钮被按下')
            info = self.textEdit.toPlainText()  # 获取框中输入的信息
            # 统计薪资 2w 以上的人
            salary_info = self.get_salary_larger_than_2w(info)

            # 弹出通知对话框
            # QMessageBox.about(parent, caption, text)
            # 当前作用域 -> 上一级作用域 -> 当前文件夹 -> builtin python 库
            QMessageBox.about(self.window,
                              "统计结果",
                              f'''薪资大于2w:\n{salary_info[0]}
                                \n薪资小于2w:\n{salary_info[1]}''')

        def get_salary_larger_than_2w(self, info):
            """
            :fun: 统计薪资 2w 以上的人
            :param info: info, <class 'str'>
            :return: <class 'tuple'> (salary_above_20k, salary_below_20k)
            """
            salary_above_20k = ''
            salary_below_20k = ''
            for line in info.splitlines():
                if not line.strip():
                    continue
                parts = line.split(' ')  # 输入用空格分开,eg:张三 2000 35
                # 去掉列表中的空字符串, 数据处理
                parts = [p for p in parts if p]
                name, salary, age = parts
                if int(salary) >= 20000:
                    salary_above_20k += name + '\n'  # 统计结果一行一行的显示
                else:
                    salary_below_20k += name + '\n'
            return salary_above_20k, salary_below_20k

        def init_ui(self):
            self.window = QMainWindow()  # 主窗口
            self.window.resize(500, 400)
            self.window.move(500, 300)  # 相对于父控件的位置，由于主窗口没有父控件，变成了相对屏幕左上角的位置
            self.window.setWindowTitle("薪资统计")

            self.textEdit = QPlainTextEdit(self.window)  # window 是textEdit 的父控件
            self.textEdit.setPlaceholderText("请输入信息")  # 占位信息
            self.textEdit.move(10, 25)  # 相对于 标题栏的下面的左上角的位置
            self.textEdit.resize(300, 350)

            button = QPushButton('统计', self.window)  # 父控件 window
            button.move(380, 80)
            button.clicked.connect(self.handle_calc)  # 设置槽函数

    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    calculator = SalaryCalculator()
    calculator.init_ui()
    calculator.window.show()
    app.exec_()  #死循环，等待, 除法按下结束才会关闭

def pyqt_window_test():

    class App(QWidget):
        """"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_window_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            # We set the window size using the setGeometry(left,top,width,height) method.
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.show() # Finally show() is called to display the window.

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


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
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.
            button = QPushButton("PySide2 Button", self)
            button.setToolTip("This is button Tip:Click to print log")
            button.move(100, 70)
            # If an event takes place, each PyQt5 widget can emit a signal.
            # A signal does not execute any action, that is done by a slot.
            # PyQt supports many type of signals, not just clicks.
            button.clicked.connect(self.on_clock) # 连接槽函数
            self.show() # Finally show() is called to display the window.

        @Slot()
        def on_clock(self):
            print("Pyside2 button clicked")

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def pyqt_messagebox_test():
    class App(QWidget):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_messagebox_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI() # 构造函数中显示 UI

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.show()
            print("Enter?")
            # This function will block()
            buttonReply = QMessageBox.question(self, "PyQt Message", "Dou You like pyqt?", \
                                               QMessageBox.Yes | QMessageBox.No | QMessageBox.Open, QMessageBox.No)
            # 可选的更多的按钮
            # QMessageBox.Cancel	QMessageBox.Ok	QMessageBox.Help
            # QMessageBox.Open	QMessageBox.Save	QMessageBox.SaveAll
            # QMessageBox.Discard	QMessageBox.Close	QMessageBox.Apply
            # QMessageBox.Reset	QMessageBox.Yes	QMessageBox.YesToAll
            # QMessageBox.No	QMessageBox.NoToAll	QMessageBox.NoButton
            # QMessageBox.RestoreDefaults	QMessageBox.Abort	QMessageBox.Retry
            # QMessageBox.Ignore
            if buttonReply == QMessageBox.Yes:
                print("Yes clicked")
            elif buttonReply == QMessageBox.No:
                print("No clicked")
            elif buttonReply == QMessageBox.Open:
                print("Open clicked")
            # ... # 等等其他事件
            else:
                print("No one clicked")
            # self.show()
            print("Enter finished")

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_lineedit_test():
    class App(QMainWindow):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_lineedit_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            # create a textbox in the window
            self.textbox = QLineEdit(self)
            self.textbox.move(20, 20) # absolutely move position
            self.textbox.resize(1000, 80)

            # create a button in the window
            self.button = QPushButton('Show Text', self)
            self.button.move(100, 100)
            self.button.clicked.connect(self.on_clock)
            self.show()

        @Slot()
        def on_clock(self):
            print("Pyside2 button clicked")
            textboxVal = self.textbox.text()
            QMessageBox.question(self, 'Message', 'You Typed:' + textboxVal, QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.clear()

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def pyqt_table_test():
    class App(QWidget):
        """
        """
        def __init__(self):
            super(App, self).__init__()
            self.title = "pyqt_table_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)  # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height)  # We set the window size using the setGeometry(left,top,width,height) method.

            self.__crateTable()

            #  # Add box layout, add table to box layout and add box layout to widget
            layout = QVBoxLayout()
            layout.addWidget(self.tableWidget)
            self.setLayout(layout)

            self.show()

        def __crateTable(self):
            self.tableWidget = QTableWidget()
            self.tableWidget.move(200, 200)
            # Tables can have multiple rows and columns.
            # This can be specified with setRowCount() and setColumnCount().
            self.tableWidget.setRowCount(4)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setItem(0, 0, QTableWidgetItem("提示(0,0)"))
            self.tableWidget.setItem(0, 1, QTableWidgetItem("提示(0,1)"))
            self.tableWidget.setItem(1, 0, QTableWidgetItem("提示(1,0)"))
            self.tableWidget.setItem(1, 1, QTableWidgetItem("提示(1,1)"))
            self.tableWidget.setItem(2, 0, QTableWidgetItem("提示(2,0)"))
            self.tableWidget.setItem(2, 1, QTableWidgetItem("提示(2,1)"))
            self.tableWidget.setItem(3, 0, QTableWidgetItem("提示(3,0)"))
            self.tableWidget.setItem(3, 1, QTableWidgetItem("提示(3,1)"))
            self.tableWidget.move(0, 0)

            # table selection change
            self.tableWidget.doubleClicked.connect(self.on_click)

        @Slot()
        def on_click(self):
            for currentTableItem in self.tableWidget.selectedItems():
                print("clicked item:({0},{1}) {2}".format(currentTableItem.row(), \
                                                          currentTableItem.column(), \
                                                          currentTableItem.text()))

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_inputdialog_test():
    class App(QWidget):
        """"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_menu_test"
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            # self.getInteger()
            # self.getDouble()
            # self.getChoice()
            self.getText()
            self.show()

        def getInteger(self):
            """Parameters in order: self, window title, label (before input box), default value, minimum, maximum and step size."""
            int, okPressed = QInputDialog.getInt(self, "获取整数", "Percentage", 50, minValue=0,  maxValue=100, step=1)
            if okPressed:
                print(int)

        def getDouble(self):
            """The last parameter (10) is the number of decimals behind the comma."""
            double, okPressed = QInputDialog.getDouble(self, "获取浮点数", "Value", 50.00, minValue=0,  maxValue=100, decimals=10)
            if okPressed:
                print(double)

        def getChoice(self):
            """Get an item from a dropdown box:"""
            items = ("Red", "Blue", "Green")
            item, okPressed = QInputDialog.getItem(self, "获取选项", "Color:", items, 0, False)
            if okPressed and item:
                print(item)

        def getText(self):
            """Get a string using QInputDialog.getText()"""
            defaultValue = ""
            text, okPressed = QInputDialog.getText(self, "获取文本", "名字", QLineEdit.Normal, text=defaultValue)
            if okPressed and text != "":
                print(text)

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_dialog_test():
    class App(QWidget):
        """The methods used are QFileDialog.getOpenFileName(), QFileDialog.getOpenFileNames(),
        QFileDialog.getSaveFileName(). The method parameters let you specify the default directory,
        filetypes and the default filename."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_menu_test"
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            # self.openFileNameDialog()
            # self.openFileNamesDialog()
            self.saveFileDialog()

            self.show()

        def openFileNameDialog(self):
            """如果这个设置为按钮的槽函数不就是打开文件的功能了吗"""
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog # ???
            fileName, _ = QFileDialog.getOpenFileName(self, \
                                                      "获取打开文件", \
                                                      "", \
                                                      "All Files (*);;Python Files (*.py);;C Files(*.c)", \
                                                      options = options)
            if fileName:
                print(fileName)

        def openFileNamesDialog(self):
            """"""
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog # ???
            files, _ = QFileDialog.getOpenFileNames(self,
                                                    "获取打开得文件", "",
                                                    "All Files (*);;Python Files (*.py);;C Files(*.c)",
                                                    options = options)
            if files:
                print(files)

        def saveFileDialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog # ???
            fileName, _ = QFileDialog.getSaveFileName(self, "获取保存文件", "",
                                                      "All Files (*);;Python Files (*.py);;C Files(*.c)",
                                                      options = options)
            if fileName:
                print(fileName)

        @Slot()
        def on_click(self):
            print("Clicked")

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_image_test():
    class App(QWidget):
        """PyQt5 (and Qt) support images by default.
        In this article we’ll show you how to add an image to a window.
        An image can be loaded using the QPixmap class."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            pixmap = self.loadImage("apple.png")
            label = QLabel(self)
            label.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
            self.show()

        def loadImage(self, path):
            """Adding an image to a PyQt5 window is as simple as creating a label and adding an image
            to that label. You can load an image into a QPixmap. A QPixmap can be used to display an
            image in a PyQt window.
            To load an image from a file, you can use the QPixmap.load() method. This will return a
            True or False value depending on whether the image was successfully loaded.
            Once you have loaded an image into a QPixmap, you can then display it by creating a QLabel
            and setting the pixmap property of the label to the QPixmap."""
            pixmap = QPixmap(path)
            print(pixmap.width(), pixmap.height())
            return pixmap

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_painter_test():
    """画布以及画笔功能"""
    class PaintWidget(QWidget):
        """Auto Paint Widget"""
        def paintEvent(self, event):
            """随机画点, 重写父类的方法"""
            qp = QPainter(self)
            qp.setPen(Qt.black)
            size = self.size()
            for i in range(1024): # 随机画 1024 个点
                x = random.randint(1, size.width() - 1) # 确保在 window 范围内
                y = random.randint(1, size.height() - 1)
                # To add individual pixels, employ the drawPoint(x, y) method.
                qp.drawPoint(x, y)

    class App(QMainWindow):
        """"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_painter_test"
            self.left = 10
            self.top = 10
            self.width = 440
            self.height = 280
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            # Setting a window’s background is quite straightforward:
            self.setAutoFillBackground(True)
            p = self.palette()
            p.setColor(self.backgroundRole(), Qt.white)
            self.setPalette(p)

            # Initiate paint widget and paint
            self.m = PaintWidget(self)
            self.m.move(0, 0)
            self.m.resize(self.width, self.height)

            self.show()

        # To add individual pixels, employ the drawPoint(x, y) method.

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_image_test():
    class App(QWidget):
        """PyQt5 (and Qt) support images by default.
        In this article we’ll show you how to add an image to a window.
        An image can be loaded using the QPixmap class."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            button = QPushButton("自定义颜色", self)
            button.setToolTip("打开调色板")
            button.move(10, 10)
            button.clicked.connect(self.on_click)
            self.show()

        @Slot()
        def on_click(self):
            self.openColorDialog()

        def openColorDialog(self):
            color = QColorDialog.getColor()
            if color.isValid():
                print(color.name())
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_qcolor_test():
    """Working with QColor in PyQt5 is an essential task when developing GUI applications
    that require a diverse range of colors. Defining and using colors effectively can enhance
    the user interface of your applications.
    In PyQt5, colors are primarily defined using the QColor(r, g, b) method. This method
    employs the RGB color model, which stands for Red, Green, and Blue. By adjusting the
    values of r, g, and b, which range from 0 to 255, you can produce an extensive spectrum
    of colors.
    Specifically, in a QPainter widget, which is a vital widget for drawing graphics in
    PyQt5, you can designate a color using the setBrush method."""
    class App(QMainWindow):
        """"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 440
            self.height = 280
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            # set window background color:white
            self.setAutoFillBackground(True)
            p = self.palette()
            p.setColor(self.backgroundRole(), Qt.white)
            self.setPalette(p)

            # Add paint widget and paint
            self.m = PaintWidget(self)
            self.m.move(0, 0)
            self.m.resize(self.width, self.height)

            self.show()

    class PaintWidget(QWidget):
        """绘图"""
        def paintEvent(self, event):
            qp = QPainter(self)

            qp.setPen(Qt.black)
            size = self.size()
            # Colored rectangles
            qp.setBrush(QColor(200, 0, 0)) # read
            qp.drawRect(0, 0, 100, 100)

            qp.setBrush(QColor(0, 200, 0)) # green
            qp.drawRect(100, 0, 100, 100)

            qp.setBrush(QColor(0, 0, 200)) # blue
            qp.drawRect(200, 0, 100, 100)
            # method. It showcases how to draw a variety of colors on a QPainter widget
            # using the setBrush and QColor methods:
            for i in range(0, 100):
                qp.setBrush(QColor(i*10, 0, 0)) # QBrush
                qp.drawRect(10*i, 100+32*0, 10, 32)

                qp.setBrush(QColor(i*10, i*10, 0))
                qp.drawRect(10*i, 100+32*1, 10, 32)

                qp.setBrush(QColor(i*2, i*10, i*1))
                qp.drawRect(10*i, 10+32*2, 10, 32)

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_drag_and_drop_test():
    class App(QWidget):
        """Like any modern GUI toolkit, PyQt supports drag and drop.
        A widget parameter must be set using the setDragEnabled(True) method call.
        A custom widget should then be set to accept a drop with setAcceptDrops(True)."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 320
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            editBox = QLineEdit("Drag this", self)
            editBox.setDragEnabled(True)
            editBox.move(10, 10) # (x,y)
            editBox.resize(200, 32) # (width,height)

            dragWidget = CustomLabel('Drop here', self)
            dragWidget.move(200, 200)

            self.show()

        @Slot()
        def on_click(self):
            self.openColorDialog()

    class CustomLabel(QLabel):
        """The textbox is created with the call QLineEdit(). A custom class (CustomLabel) is
        created that accepts drag and drop. Both events are defined as methods and have their
        logic executed if the event occurs."""
        def __init__(self, title, parent):
            super().__init__(title, parent)
            self.setAcceptDrops(True) # NOTE:
        def dragEnterEvent(selfself, e):
            if e.mimeData().hasFormat('text/plain'): # QMimeData
                e.accept()
            else:
                e.ignore()

        def dropEvent(self, e):
            self.setText(e.mimeData().text())



    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def pyqt_pyqt_fontdailog_test():
    class App(QWidget):
        """PyQt5 comes with a font dialog that you may have seen in a text editor.
        This is the typical dialog where you can select font, font size, font style and so on.
        Of course the look and feel depends on the operating system."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_pyqt_fontdailog_test"
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            button = QPushButton("选择字体", self)
            button.setToolTip('打开字体库')
            button.move(50, 50)
            button.clicked.connect(self.on_click)
            self.show()

        @Slot()
        def on_click(self):
            self.openFontDialog()

        def openFontDialog(self):
            ok, font = QFontDialog.getFont()
            if ok:
                print(font.toString())

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def pyqt_matplotlib_test():
    class App(QWidget):
        """Matplotlib offers powerful visualizations that can be seamlessly integrated into a
        PyQt5 application. For this, specific libraries and imports are required.."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 640
            self.height = 400
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            self.canvas = PlotCanvas(self, width=5, height=4)
            self.canvas.move(0, 0)

            button = QPushButton('Sample Button', self)
            button.setToolTip("解释 button")
            button.move(self.width-140, self.height-100)
            button.resize(140, 100)
            button.clicked.connect(self.on_click)

            self.show()

        @Slot()
        def on_click(self):
            self.canvas.plot()

    class PlotCanvas(FigureCanvas):
        """The primary component here is a widget named ‘PlotCanvas’
        which houses the Matplotlib visualization."""
        def __init__(self, parent=None, width=5, height=4, dpi=100):
            fig = Figure(figsize=(width, height), dpi=dpi)
            FigureCanvas.__init__(self, fig) # 调用父类的构造函数
            # super().__init__(PlotCanvas, fig)
            self.axes = fig.add_subplot(111) # Add an `~.axes.Axes` to the figure as part of a subplot arrangement.
            self.setParent(parent)
            FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
            FigureCanvas.updateGeometry(self)
            self.plot()

        def plot(self):
            # TODO: 怎么清空画布?????
            data = [random.random() for i in range(25)]
            ax = self.figure.add_subplot(111)
            ax.plot(data, 'r-')
            ax.set_title('坐标系')
            self.draw()

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_browser_test():
    """TODO：浏览器"""
    class App(QWidget):
        """QWebView uses the Webkit rendering engine
            The web browser engine is used by Safari, App Store and many OS X applications.
            The load() method opens the url (QUrl) in the argument.
            You can create a QUrl using: QUrl(url).
            The show() method is required to display the widget."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.
            # TODO: QtWebKit
            # https://www.webkit.org/
            # https://pythonspot.com/pyqt5-browser/
            # https://pythonspot.com/pyqt5-webkit-browser/
            self.show()

        @Slot()
        def on_click(self):
            self.openColorDialog()

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def pyqt_treeview_test():
    """QTreeView 还需要深入理解"""
    class App(QWidget):
        """"""
        FROM, SUBJECT, DATE = range(3)  # list column index
        def __init__(self):
            super().__init__()
            self.title = "pyqt_treeview_test"
            self.left = 10
            self.top = 10
            self.width = 640
            self.height = 240
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.
            # print(FROM, SUBJECT, DATE)

            self.dataGroupBox = QGroupBox("收件箱(邮箱标题)") #

            self.dataView = QTreeView() # TODO:QTreeView -> QWidget 的派生类
            self.dataView.setRootIsDecorated(False)
            self.dataView.setAlternatingRowColors(True)
            # self.dataView.setAllColumnsShowFocus()

            dataLayout = QHBoxLayout() # 每个邮件都是水平布局
            dataLayout.addWidget(self.dataView)
            self.dataGroupBox.setLayout(dataLayout)

            self.model = self.createMailModel(self)
            self.dataView.setModel(self.model)
            self.addMailItem(self.model, 'service@github.com', 'Your Github Donation', '03/25/2017 02:05 PM')
            self.addMailItem(self.model, 'support@github.com', 'Github Projects', '02/02/2017 03:05 PM')
            self.addMailItem(self.model, 'service@phone.com', 'Your Phone Bill', '01/01/2017 04:05 PM')

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(self.dataGroupBox)
            self.setLayout(mainLayout)

            self.show()

        def createMailModel(self, parent):
            """设置表格格式以及表头
            Model Structure: The model’s structure is detailed using:"""
            model = QStandardItemModel(0, 3, parent)
            model.setHeaderData(self.FROM, Qt.Horizontal, "FROM") # 设置列表头
            model.setHeaderData(self.SUBJECT, Qt.Horizontal, "SUBJECT")
            model.setHeaderData(self.DATE, Qt.Horizontal, "DATE")
            return model

        def addMailItem(self, model, mailFrom, subject, date):
            """插入邮件
            Data Ingestion: Data is appended to the tree view with:"""
            model.insertRow(0)
            model.setData(model.index(0, self.FROM), mailFrom) # ???
            model.setData(model.index(0, self.SUBJECT), subject) # ???
            model.setData(model.index(0, self.DATE), date) # ???

        @Slot()
        def on_click(self):
            self.addMailItem(self.model, random.randint(1, 100), random.randint(100, 1000), random.randint(1000, 10000))

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def pyqt_directory_view_test():
    class App(QWidget):
        """PyQt can show a directory structure using a QTreeView.
        For the treeview to show as a directory tree, we need to set its model to a
        QFileSystemModel instance. That is achieved by calling the setModel method for
        the tree instance."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_directory_view_test"
            self.left = 10
            self.top = 10
            self.width = 640
            self.height = 480
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            self.model = self.createFileSystemModel()

            self.tree = QTreeView()
            self.tree.setModel(self.model)
            # We can set additional options on the tree object:
            # sorting enabled (setSortingEnabled), animation and indention.
            self.tree.setAnimated(False)
            self.tree.setIndentation(20)
            self.tree.setSortingEnabled(True)
            self.tree.setWindowTitle("Dir View")
            self.tree.resize(self.size())

            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.tree)
            self.setLayout(windowLayout)

            self.show()

        @Slot()
        def on_click(self):
            self.openColorDialog()

        def createFileSystemModel(self):
            """创建文件夹 Model"""
            model = QFileSystemModel()
            # The path is specified using the models setRootPath() method,
            # where the parameter is the full path to the directory By default its the root.
            model.setRootPath('')
            return model

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_qformlayout_test():
    class App(QDialog):
        """A form can be created using the class QFormLayout. This is the easiest way
        to create a form where widgets (input) have descriptions (labels)."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_qformlayout_test"
            self.left = 10
            self.top = 10
            self.width = 50
            self.height = 50
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            # QDialogButtonBox
            self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

            mainLayout = QVBoxLayout()
            self.formGroupBox = self.createFormGroupBox()
            mainLayout.addWidget(self.formGroupBox)
            mainLayout.addWidget(self.buttonBox)
            self.setLayout(mainLayout)

            self.show()

        def createFormGroupBox(self):
            """设置 Form"""
            formGroupBox = QGroupBox("Form layout")
            layout = QFormLayout()
            # The Form Layout is created using the class QFormLayout.
            # We can add rows to the form using the method addRow.
            # The method is defined as
            layout.addRow(QLabel("名字"), QLineEdit())
            layout.addRow(QLabel("国家"), QComboBox())
            layout.addRow(QLabel("年龄"), QSpinBox())
            formGroupBox.setLayout(layout)
            return formGroupBox

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_boxlayout_test():
    """An instance of the QBoxLayout in PyQt5 provides a versatile method to manage widget
    layouts. It allocates space into distinct boxes, with each box entirely filled by a
    specific widget. The orientation - vertical or horizontal - is determined by the type
    of class used to create the object."""
    class App(QDialog):
        """"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 200
            self.height = 200
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.
            btn1 = QPushButton("Button1")
            btn2 = QPushButton("Button2")
            btn3 = QPushButton("Button3")
            btn4 = QPushButton("Button4")

            # For vertical placement of widgets, QVBoxLayout is employed. Similarly,
            # QHBoxLayout is used for horizontal placement of widgets. It’s essential
            # to note that QVBoxLayout inherits from the overarching QBoxLayout class.
            mainLayout = QVBoxLayout()
            mainLayout.addWidget(btn1)
            mainLayout.addWidget(btn2)
            mainLayout.addWidget(btn3)
            mainLayout.addWidget(btn4)
            self.setLayout(mainLayout)

            self.show()

        @Slot()
        def on_click(self):
            self.openColorDialog()

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

def pyqt_qWizardPage_test():
    """A wizard is a screen you often see during installations, you have back and next
    buttons, and are guided through a process.
    In PyQt5 these are called pages, every page can have some content. The buttons will
    guide you through these pages."""
    class QIComboBox(QComboBox):
        """自己定义的 comboBox 类"""
        def __init__(self, parent=None):
            super().__init__(parent)

    class Page1(QWizardPage):
        """页面1"""
        def __init__(self, parent=None):
            super().__init__(parent)
            self.comboBox = QIComboBox(self)
            self.comboBox.addItem("Python", "/path/to/filename1")
            self.comboBox.addItem("PyQt5", "/path/to/filename2")
            layout = QVBoxLayout()
            layout.addWidget(self.comboBox)
            self.setLayout(layout)
            print("Page1 contructor")

    class Page2(QWizardPage):
        """页面 2"""
        def __init__(self, parent=None):
            super().__init__(parent)
            self.label1 = QLabel("123")
            self.label2 = QLabel("456")
            self.textView = QTextBrowser()
            self.textView.setText("""A wizard is a screen you often see during installations, you have back and next buttons, and are guided through a process.
In PyQt5 these are called pages, every page can have some content. The buttons will guide you through these pages.""")
            layout = QVBoxLayout()
            layout.addWidget(self.label1)
            layout.addWidget(self.label2)
            layout.addWidget(self.textView)
            self.setLayout(layout)
            print("Page2 contructor")

    class MagicWizard(QWizard):
        """"""
        def __init__(self, parent=None):
            super().__init__(parent)
            self.title = "安装向导页面切换测试"
            self.addPage(Page1(self))
            self.addPage(Page2(self))
            self.setWindowTitle(self.title)
            self.resize(640, 480)
            print("安装向导页面切换测试")

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            self.show()

    app = QApplication(sys.argv)
    ex = MagicWizard()
    ex.show()
    sys.exit(app.exec_())


def pyqt_scroll_area_test():
    """滑动区域以及滚动条"""
    import sys
    from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea

    class MainWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            # 创建 QScrollArea 对象
            scroll_area = QScrollArea(self)
            scroll_area.setWidgetResizable(True)  # 允许内容改变大小

            # 创建布局
            layout = QVBoxLayout()

            container_layout = QVBoxLayout()
            for i in range(50):  # 添加多个按钮作为示例内容
                btn = QPushButton(f"Button {i}", self)
                container_layout.addWidget(btn)

            # 创建容器小部件，并将布局设置到容器小部件上
            container = QWidget()
            container.setLayout(container_layout)
            scroll_area.setWidget(container)  # 将容器小部件设置到滚动区域中

            # 将滚动区域添加到主窗口中
            self.setLayout(layout)
            self.layout().addWidget(scroll_area)
            self.setGeometry(300, 300, 300, 200)  # 设置主窗口的几何形状
            self.setWindowTitle('QScrollArea Example')  # 设置窗口标题

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

def get_layout_children():
    """获取 layout 中的所有控件
    An instance of the QBoxLayout in PyQt5 provides a versatile method to manage widget
    layouts. It allocates space into distinct boxes, with each box entirely filled by a
    specific widget. The orientation - vertical or horizontal - is determined by the type
    of class used to create the object."""
    class App(QDialog):
        """"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_image_test"
            self.left = 10
            self.top = 10
            self.width = 200
            self.height = 200
            self.mainLayout = None
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.
            btn1 = QPushButton("Button1")
            btn2 = QPushButton("Button2")
            btn3 = QPushButton("Button3")
            btn4 = QPushButton("Button4")
            btn1.clicked.connect(self.on_click)

            # For vertical placement of widgets, QVBoxLayout is employed. Similarly,
            # QHBoxLayout is used for horizontal placement of widgets. It’s essential
            # to note that QVBoxLayout inherits from the overarching QBoxLayout class.
            self.mainLayout = QVBoxLayout()
            self.mainLayout.addWidget(btn1)
            self.mainLayout.addWidget(btn2)
            self.mainLayout.addWidget(btn3)
            self.mainLayout.addWidget(btn4)
            self.setLayout(self.mainLayout)

            self.show()

        @Slot()
        def on_click(self):
            # self.openColorDialog()
            print(self.mainLayout.count())
            for i in range(self.mainLayout.count()):
                print(str(self.mainLayout.itemAt(i)), f"type:{self.mainLayout.itemAt(i)}")
                # self.mainLayout.itemAt(i).setText(f"New Button {i}")
                # self.mainLayout.removeItem(self.mainLayout.itemAt(i))
                self.mainLayout.itemAt(i).widget().setText(f"New btn {i}")

            self.mainLayout.removeWidget(self.mainLayout.itemAt(1).widget())
            # self.mainLayout.removeItem(self.mainLayout.itemAt(1))
            print(self.mainLayout.count())

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # pyqt_basic_test1()
    # calculate_salary_test()
    # pyqt_signal_test1()
    # pyqt_window_test()
    # pyqt_mainwindow_test()
    # pyqt_pushbutton_test()
    # pyqt_signal_test()
    # pyqt_messagebox_test()
    # pyqt_lineedit_test()
    # pyqt_menu_test()
    # pyqt_table_test()
    # pyqt_horizontal_layout_test()
    # pyqt_dialog_test()
    # pyqt_grid_layout_test()
    # pyqt_inputdialog_test()
    # pyqt_image_test()
    # pyqt_painter_test()
    # pyqt_image_test()
    # pyqt_qcolor_test()
    # pyqt_drag_and_drop_test()
    # pyqt_pyqt_fontdailog_test()
    # pyqt_matplotlib_test()
    # pyqt_browser_test()
    # pyqt_treeview_test()
    pyqt_directory_view_test()
    # pyqt_qformlayout_test()
    # pyqt_boxlayout_test()
    # pyqt_qWizardPage_test()
    # pyqt_scroll_area_test()
    # get_layout_children()