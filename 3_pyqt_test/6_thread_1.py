from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTextBrowser
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys
import time
import threading as th
from PySide2.QtCore import Signal, QObject
# 多线程操作(可以使用 python 的线程库，也可以使用 pyqt 封装的线程库)
# qt 主循环的线程
# 后台服务程序线程
# eg1: HTTP 调试器

# 2.打印进度
# 如果只使用一个线程，只有等到所有的都结束完以后，才会执行 pyqt 渲染的任务,
# 这样等到所有的执行完以后才会显示进度
# 因此要使用多线程
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/6_jindu.ui')
        # 设置槽函数
        self.ui.doCrawl.clicked.connect(self.crawlClicked)

    # 槽函数
    def crawlClicked(self):
        """"""
        for i in range(1, 6):
            self.ui.infoBox.append(f'爬取到第 {i} 个文件...')
            time.sleep(1)       # 阻塞期间连窗口都无法拖动，跟卡住了一样


# 使用多线程
# python 函数中可以定义函数
class Spider:
    def __init__(self):
        self.ui = QUiLoader().load('ui/6_jindu.ui')
        # 设置槽函数
        self.ui.doCrawl.clicked.connect(self.crawlClicked)

    # 槽函数
    def crawlClicked(self):
        # 函数中定义函数
        def run():
            for i in range(1, 6):
                self.ui.infoBox.append(f'爬取到第 {i} 个文件...')  # 这样使不好的
                time.sleep(1)  # 阻塞期间连窗口都无法拖动，跟卡住了一样
        # 启动一个新的线程
        th1 = th.Thread(target=run)
        th1.start()     # 与 Qt 的主线程分离开

# 3.使用信号，在主线程里面操作界面，子线程发送信号
# 信号类
class MySignals(QObject):
    """定义一种信号, 两个参数, 类型分别是: QTextBrowser 和 字符串"""
    #test_print_signal = Signal(QTextBrowser, str)
    text_print_signal = Signal(str)
    # 还可以定义其它信号, 当只有一个控件的时候，就可以不指定第一个参数
    update_table = Signal(str)

class SpiderMan:
    def __init__(self):
        self.ui = QUiLoader().load('ui/6_jindu.ui')
        # 设置槽函数
        self.ui.doCrawl.clicked.connect(self.crawlClicked)
        #step1: 实例化一个信号对象
        # 主线程 和 子线程之间使用这个信号通信
        self.ms = MySignals()
        # step2: 定义信号的处理函数
        self.ms.text_print_signal.connect(self.print_to_gui)

    # 自定义信号处理函数, text_print() 参数
    # 通过另外一个参数确定在哪个文本框控件打印
    # 这个函数是在主线程执行的
    def print_to_gui(self, text):
        self.ui.infoBox.append(str(text))  # 这样使不好的

    # 槽函数, 子线程中启动
    def crawlClicked(self):
        # 启动一个新的线程
        th1 = th.Thread(target=self.start_crawl)
        th1.start()     # 与 Qt 的主线程分离开

    # 线程入口函数
    def start_crawl(self):
        for i in range(1, 6):
            # step2:当需要打印内容的时候就发出信号
            #self.ms.text_print.emit(self.ui.infoBox1, '输出内容')  # 多个控件可以输出内容时，需要指定
            # 发出信号
            self.ms.text_print_signal.emit(f"爬取到第{i}个文件...")    # 调用 Signal 的emit()方法
            time.sleep(1)  # 阻塞期间连窗口都无法拖动，跟卡住了一样

# 注意，在新的线程里面操作界面会出现很多莫名其妙的 bug
app = QApplication([])  # 整个 UI 界面的控件，信号管理等
s = SpiderMan()
s.ui.show()
app.exec_() #死循环，等待, 除法按下结束才会关闭

if __name__ =='__main__':
    pass













