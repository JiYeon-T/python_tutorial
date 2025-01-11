import sys # 与 python 解释器有关的
from PyQt5.QtWidgets import QApplication # pyqt5 后台管理的命脉, 用于用户界面应用程序的控制流和主要设置
from PyQt5.QtWidgets import  QWidget, QMainWindow, QPushButton, QPlainTextEdit

def pyqt_test1():
    print(f"ui loop start argv:{sys.argv}")
    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    window = QMainWindow() # 主窗口
    window.resize(500, 400)
    window.move(500, 300)   # 相对于父控件的位置，由于主窗口没有父控件，变成了相对屏幕左上角的位置
    window.setWindowTitle("薪资统计")

    textEdit = QPlainTextEdit(window)   # window 是textEdit 的父控件
    textEdit.setPlaceholderText("请输入信息")    # 占位信息
    textEdit.move(0, 0) # 相对于 标题栏的下面的左上角的位置
    textEdit.resize(300, 350)
    print(f"text:{textEdit.toPlainText()}")

    button = QPushButton('统计', window)        # 父控件 window
    button.move(400, 0)

    window.show()

    app.exec_() #死循环，等待, 除非按下结束才会关闭
    print(" exit")

def pyqt5_loop_test():
    """pyqt main loop"""
    # 只要是Qt制作的app，必须有且只有一个QApplication对象
    app = QApplication(sys.argv) # sys.argv 命令行参数
    app.setApplicationName("TestApp")
    w = QWidget() # 创建窗口
    w.setWindowTitle("My first Pyqt") # 设置窗口标题
    # w.resize(500)
    w.show() # 显示窗口
    # 最后一个窗口关闭后，程序才停止
    # 类中的一个循环监听方法, 监测我在打开的页面中做了什么
    app.exec_()

if __name__ =='__main__':
    pyqt5_loop_test()

