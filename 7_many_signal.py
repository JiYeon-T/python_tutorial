from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTextBrowser
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys
import time
import threading as th
from PySide2.QtCore import Signal, QObject

# 3.使用信号，在主线程里面操作界面，子线程发送信号
# 信号类
# 一种信号定义为 该类的 一个 静态属性，值为Signal 实例对象即可。
# 可以定义多个 Signal 静态属性，对应这种类型的对象可以发出的 多种 信号。
class MySignals(QObject):
    """定义一种信号, 两个参数, 类型分别是: QTextBrowser 和 字符串"""
    #test_print_signal = Signal(QTextBrowser, str)
    text_print_signal = Signal(str)
    # 还可以定义其它信号, 当只有一个控件的时候，就可以不指定第一个参数
    # 具体内容与 UI 界面有关
    update_table = Signal(int, int, str)    # 行, 列, 内容,

class SpiderMan:
    def __init__(self):
        self.ui = QUiLoader().load('ui/6_jindu.ui')
        # 设置槽函数
        self.ui.button0.clicked.connect(self.crawlClicked)
        #step1: 实例化一个信号对象
        # 主线程 和 子线程之间使用这个信号通信
        self.ms = MySignals()

        # step2: 定义信号的处理函数
        self.ms.text_print_signal.connect(self.print_to_gui)
        self.ms.update_table.connect(self.update_table_signal_process)

        # 对空间进行管理
        self.control = []   # [[self.ui.label0, self.ui.text0, self.ui.button0], ... ], 对控件进行管理
        self.control = [[self.ui.label0, self.ui.text0, self.ui.button0],
                        [self.ui.label1, self.ui.text1, self.ui.button1],
                        [self.ui.label2, self.ui.text2, self.ui.button2],
                        [self.ui.label3, self.ui.text3, self.ui.button3],
                        [self.ui.label4, self.ui.text4, self.ui.button4],
                        [self.ui.label5, self.ui.text5, self.ui.button5],
                        [self.ui.label6, self.ui.text6, self.ui.button6],
                        [self.ui.label7, self.ui.text7, self.ui.button7],
                        [self.ui.label8, self.ui.text8, self.ui.button8]]
        self.rowMax = 8
        self.colMax = 2

    # 自定义信号处理函数, text_print() 参数
    # 通过另外一个参数确定在哪个文本框控件打印
    # 这个函数是在主线程执行的
    def print_to_gui(self, text):
        self.ui.text0.append(str(text))  # 这样使不好的

    def update_table_signal_process(self, row, col, content):
        """信号逻辑处理放到这个地方"""
        # 有没有办法对空间进行管理
        # if row==0 and col==1:
        #     self.ui.text0.setText(str(content))
        #
        # elif row == 1 and col == 1:
        #     self.ui.text1.setText(str(content))
        # 对控件进行管理后
        if row<=self.rowMax and col<=self.colMax:
            #有效信号
            self.control[row][col].setText = content
            # 根据控件不同,还需要对不同的控件调用不同的接口
            #eg:
            # if col == 2:
            #     self.control[row][col].setButtonText(content)
        else:
            print("invalid signal." + row + "-" + col + "-" + content)


    # 槽函数, 子线程中启动
    def crawlClicked(self):
        # 线程入口函数
        def start_crawl():
            for i in range(1, 6):
                # step3:当需要更新 UI 界面的时候就发出信号
                # 多个控件可以输出内容时，需要指定
                # 发出信号
                self.ms.text_print_signal.emit(f"爬取到第{i}个文件...")  # 调用 Signal 的emit()方法
                self.ms.update_table.emit(1, 1, "God job" + str(i))
                time.sleep(1)  # 阻塞期间连窗口都无法拖动，跟卡住了一样

        # 启动一个新的线程
        th1 = th.Thread(target=start_crawl)
        th1.start()     # 与 Qt 的主线程分离开




if __name__ == '__main__':
    # 注意，在新的线程里面操作界面会出现很多莫名其妙的 bug, 必须通过子线程发送信号的方式更新界面
    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    s = SpiderMan()
    s.ui.show()
    sys.exit(app.exec_())  # 死循环，等待, 除法按下结束才会关闭