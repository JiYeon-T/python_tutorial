import sys
import time
import queue
import threading

from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QDialog
from PySide2.QtWidgets import QVBoxLayout




################################ 信号和槽函数 ############################################
# from PySide2.QtCore import Slot #pyqtSlot
## Pyside2 与 pyqt5 的区别(解决代码移植问题):
# pyside2 没有 Pyqtslot
# 在PySide2中，确实没有与PyQt5中pyqtSlot装饰器直接对应的装饰器。
# 在PySide2中，信号和插槽机制使用了自己的装饰器名称即 Slot装饰器

# PySide2和PyQt5在信号和插槽的实现上有所不同。PyQt5使用pyqtSlot装饰器来定义槽函数，
# 而PySide2则使用Slot装饰器来实现相同的功能。这意味着，如果你从PyQt5迁移到PySide2，
# 你可能需要将pyqtSlot装饰器替换为 Slot装饰器
# 例如，在PyQt5中，你可能会这样定义一个槽函数：

# @pyqtSlot()
# def handleCalc():
#     QMessageBox.about(window, '关于', '点击按钮1次')

# 而在PySide2中，你应该这样定义：
# @Slot()
# def handleCalc():
#     QMessageBox.about(window, '关于', '点击按钮1次')

# 请注意，虽然装饰器名称不同，但两者在功能上是等价的，都用于将槽函数与信号连接起来。
# 此外，PySide2和PyQt5在信号和插槽机制上还有其他一些细微的差异，比如参数传递和返回值处理等。
# 在使用时，建议查阅相应的文档以确保正确实现]^。

def pyqt_signal_example():
    """PyQT 信号以及槽函数的使用"""
    class Dialog(QDialog):
        """QDialog 继承自 QWidget"""
        def __init__(self):
            super(Dialog, self).__init__()
            self.title = "Button - Signal - Slot test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480

            button = QPushButton("Click")
            # button.setGeometry(self.left, self.top, self.width, self.height)
            button.clicked.connect(self.slot_method)

            mainLayout = QVBoxLayout() # layout
            mainLayout.addWidget(button)
            # mainLayout.setGeometry(QRect(self.left, self.top, self.width, self.height))

            self.setLayout(mainLayout)
            self.setWindowTitle(self.title)

        @Slot()
        def slot_method(self):
            print("slot method called")

    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())


def signal_basic_test():
    """"""

    class MyWindow(QWidget):
        """
        1.PyQt 内置控件有可以直接使用的信号, 比如 button 的 clicked..
        2.除了接收Qt自带的信号之外，我们也可以自行定义信号，在合适的时机，自行 发射信号
        自定义信号需要使用pyqtSignal来声明信号，并且需要在类中的函数之外声明(需要全局变量/类变量)
        """
        # 声明自定义信号的时候，必须在类中定义(作为类变量)，而不能在函数中定义
        my_signal = Signal(str)  # 类属性, 参数为变量的类型

        def __init__(self):
            super().__init__()
            self.init_ui()
            self.pressed_cnt = 0

        def init_ui(self):
            self.resize(600, 400)
            btn = QPushButton("开始检测", self)
            btn.setGeometry(200, 200, 100, 30)
            btn.clicked.connect(self.btn_check) # 设置槽函数

            self.display_edit = QLineEdit("cnt:0", self)
            self.display_edit.resize(100, 100)
            self.display_edit.move(200, 0)

            self.my_signal.connect(self.my_slot) # 设置自己信号的槽函数

        def btn_check(self):
            """btn 的槽函数"""
            print("check")
            self.pressed_cnt += 1
            if self.pressed_cnt % 2 == 0:
                self.my_signal.emit(f"cnt:{self.pressed_cnt}")

        def my_slot(self, msg):
            """自己定义的信号的槽函数"""
            print("myslot")
            # 在槽函数(主线程)中操作 UI 控件没有问题
            self.display_edit.clear()
            self.display_edit.setText(str(msg))

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()


def pyqt_signal_test1():
    """
    https://pythonspot.com/pyqt5-signals-and-slots/
    """
    class QtSignal(QObject):
        """要转发的信号"""
        signal = Signal(list)
        def __int__(self, parent=None):
            super(QtSignal, self).__int__(parent)

    qt_signal = QtSignal()
    msg_queue = queue.Queue(maxsize=100)

    def input_thread_entry():
        """生产者
        Q:线程如何退出?
        A: (1)设置为 daemon, 主线程结束, 子线程自动结束;
        (2) 不要用 while True, 改为:while running, 队列中携带退出消息, 将 running=False;
        TODO: 这个 input() 线程如何优雅地退出???
        """
        if 1:
        # try :
            while True:
                in_str = input("请输入要显示的字符\n")
                print("send Msg:{}".format(in_str))
                item = []
                item.append(in_str)
                msg_queue.put(item)
        # except Exception as e:
        #     print(e)
        # finally:
        #     pass

    def qt_msg_proxy_thread_entry():
        """消费者"""
        try:
            while True:
                msg = msg_queue.get(block=True, timeout=None)
                print("Got msg:{}".format(msg))
                # 通过信号和槽函数向 ui 线程发送信息
                qt_signal.signal.emit(msg)
        except Exception as e:
            print(e)
        finally:
            pass

    def ui_thread_entry():
        win = None
        def signal_process(msg_list):
            """信号对应的槽函数"""
            if not win:
                return
            win.clear()
            for msg in msg_list:
                win.setText(msg)

        qt_signal.signal.connect(signal_process)

        app = QApplication(sys.argv)
        # container = QWidget()
        win = QTextEdit(text="This is a text view")
        win.show()
        app.exec_()
        print(f'UI exit')

    # NOTE:线程通信 UI 放到单独的线程中,
    # 这种方式不太行, UI 退出了, 主线程以及其他线程都没有退出, 要让 UI 作为主线程
    # ui_thread = threading.Thread(target=ui_thread_entry, daemon=True)
    # ui_thread.start()
    # time.sleep(1)

    input_thread = threading.Thread(target=input_thread_entry, daemon=True)
    input_thread.start()

    qt_msg_proxy_thread = threading.Thread(target=qt_msg_proxy_thread_entry, daemon=True)
    qt_msg_proxy_thread.start()

    # while True:
    #     time.sleep(10000)

    # UI 作为主线程
    ui_thread_entry()


def many_signal_test():
    # 3.使用信号，在主线程里面操作界面，子线程发送信号更新 UI
    # 信号类
    # 一种信号定义为该类的 一个静态属性，值为Signal 实例对象即可。
    # 可以定义多个 Signal 静态属性，对应这种类型的对象可以发出的 多种信号。
    class MySignals(QObject):
        """定义一种信号, 两个参数, 类型分别是: QTextBrowser 和 字符串"""
        # test_print_signal = Signal(QTextBrowser, str)
        text_print_signal = Signal(str)
        # 还可以定义其它信号, 当只有一个控件的时候，就可以不指定第一个参数
        # 具体内容与 UI 界面有关
        update_table = Signal(int, int, str)  # 行, 列, 内容,

    class SpiderMan:
        def __init__(self):
            self.ui = QUiLoader().load('ui/6_jindu.ui')
            # 设置槽函数
            self.ui.button0.clicked.connect(self.crawlClicked)
            # step1: 实例化一个信号对象
            # 主线程 和 子线程之间使用这个信号通信
            self.ms = MySignals()

            # step2: 定义信号的处理函数
            self.ms.text_print_signal.connect(self.print_to_gui)
            self.ms.update_table.connect(self.update_table_signal_process)

            # 对控件进行管理
            self.control = []  # [[self.ui.label0, self.ui.text0, self.ui.button0], ... ], 对控件进行管理
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

        # 自定义槽函数, text_print() 参数
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
            if row <= self.rowMax and col <= self.colMax:
                # 有效信号
                self.control[row][col].setText = content
                # 根据控件不同,还需要对不同的控件调用不同的接口
                # eg:
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
                    self.ms.text_print_signal.emit(f"爬取到第{i}个文件...")
                    self.ms.update_table.emit(1, 1, "God job" + str(i))  # 发出信号
                    time.sleep(1)  # 如果在子线程操作 UI 阻塞期间连窗口都无法拖动，跟卡住了一样

            # 启动一个新的线程
            th1 = threading.Thread(target=start_crawl)
            th1.start()  # 与 Qt 的主线程分离开

    # NOTE:在新的线程里面操作界面会出现很多莫名其妙的 bug(非法操作!!!!!), 必须通过子线程发送信号的方式更新界面
    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    s = SpiderMan()
    s.ui.show()
    sys.exit(app.exec_())  # 死循环，等待, 除法按下结束才会关闭


def slot_long_time_test():
    """"""

    class Window(QWidget):
        """
        线程锁的使用：防止多次进入同一个线程
        """

        def __init__(self):
            super().__init__()
            self.sendThreadLock = threading.Lock()
            self.sendButton = QPushButton("发送", self)
            self.window().resize(500, 500)
            self.sendButton.move(100, 200)

            self.sendButton.clicked.connect(self.send_button_function)

        def send_button_function(self):
            """ button 的槽函数
            如果槽函数中有耗时操作, 可以使用子线程"""

            def entry():
                """ 子线程中打印信息 """
                self.sendThreadLock.acquire()  # 线程锁防止重入
                for ix in range(10):
                    print(ix)
                    time.sleep(1)
                self.sendThreadLock.release()

            # 创建新线程防止UI界面卡顿
            # TODO:这种方式还是不行, 只是表面上防止进入了, 实际上已经开启了很多线程, 只是其它线程暂时都还在阻塞等待锁被释放罢了
            th1 = threading.Thread(target=entry, name="sendThread")
            th1.setDaemon(True)  # 主线程结束（UI界面）, 子线程结束, 否则子线程一直不退出，成为僵尸线程
            th1.start()

    app = QApplication(sys.argv)  # 整个 UI 界面的控件，信号管理等
    win = Window()
    win.show()
    sys.exit(app.exec_()) # 死循环，等待, 除非按下结束才会关闭


if __name__ == '__main__':
    pyqt_signal_example()
    # signal_basic_test()
    # pyqt_signal_test1()
    # many_signal_test()
    # slot_long_time_test()