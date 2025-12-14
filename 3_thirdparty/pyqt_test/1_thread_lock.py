import sys
import threading as th
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
import time

# 1.线程锁的使用：防止多次进入同一个线程
# 这种方式还是不行, 只是表面上防止进入了, 实际上已经开启了很多线程, 只是其它线程暂时都还在阻塞等待锁被释放罢了


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.sendThreadLock = th.Lock() # 线程锁
        self.sendButton = QPushButton("发送", self)
        self.window().resize(500, 500)
        self.sendButton.move(100, 200)

        self.sendButton.clicked.connect(self.send_button_function)


    def send_button_function(self):
        """ button 的槽函数 """
        def fun():
            """ 线程入口函数 """
            self.sendThreadLock.acquire() # 线程锁防止重入
            for ix in range(10):
                print(ix)
                time.sleep(1)
            self.sendThreadLock.release()

        # 创建新线程防止UI界面卡顿
        th1 = th.Thread(target=fun, name="sendThread")
        th1.setDaemon(True) # 主线程结束（UI界面）, 子线程结束, 否则子线程一直不退出，成为僵尸线程
        th1.start()

def hello():
    """ 线程入口函数 """
    import time
    for ix in range(50):
        print(f"hello:{ix}")
        time.sleep(1)
    else:
        print("线程结束")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)  # 整个 UI 界面的控件，信号管理等
    win = Window()
    win.show()
    sys.exit(app.exec_()) # 死循环，等待, 除非按下结束才会关闭