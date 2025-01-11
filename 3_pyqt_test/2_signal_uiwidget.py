#################################################
# pyqt---子线程进行gui操作导致界面崩溃
# http://681314.com/A/uEw0hrUlmP
#################################################
import sys
import time
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox

###########################################################################################################################
# 在 PyQt或 Qt 通常中您不能直接在子线程中执行与 GUI 相关的操作。这可能会导致应用程序崩溃或不可预测的行为。所有与 GUI 相关的操作都应该在主线程中执行。
# 如果您需要在子线程完成某些操作后显示一个消息框可以使用 PyQt 提供的信号和槽机制来在主线程中执行 GUI 更新。
# 以下是如何实现这个机制的示例:
# 在您的线程类中定义一个信号。
# 如果您使用 Python 的内置 `threading` 模块来创建线程而不是使用 PyQt 的 `QThread`您仍然必须确保 GUI 相关的操作例如显示消息框仅在主线程中执行。
# 在 PyQt 中直接从非主线程修改 GUI 是不安全的。
# 即使您使用 `threading.Thread`仍可以使用 PyQt 的信号和槽机制来安全地更新 GUI。
###########################################################################################################################

class YourThread(QThread):
    """子线程"""
    show_warning_signal = pyqtSignal(str, str, str)

    def run(self):
        # 执行线程其他操作
        while True:
            # 当需要显示消息时发出信号,而不是直接操作控件
            self.show_warning_signal.emit("Wow", "Warning", "12345679")
            time.sleep(10)

class YourMainWindow(QWidget):
    """自己的窗口类"""
    def __init__(self):
        super().__init__()
        self.thread = YourThread()
        self.thread.show_warning_signal.connect(self.display_waring)
        self.thread.start()

    def display_waring(self, text1, text2, text3):
        """
        连接信号的槽函数,用于操作控件,显示警告信息
        通过上述方法您可以确保消息框的显示是在主线程中完成的从而避免了由于直接在子线程中进行 GUI 操作而导致的崩溃。
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("错误警告")
        msg_box.setText(f"name:{text1} level:{text2} info:{text3}")
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("PyQt崩溃问题测试")
    w = YourMainWindow()
    w.setWindowTitle("PyQt崩溃问题测试")
    w.show()
    app.exec_()