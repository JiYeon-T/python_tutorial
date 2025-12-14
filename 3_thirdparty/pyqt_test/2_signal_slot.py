from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
import sys


# 1.PyQt 内置控件有可以直接使用的信号, 比如 button 的 clicked..
# 2.除了接收Qt自带的信号之外，我们也可以自行定义信号，在合适的时机，自行 发射信号
# 自定义信号需要使用pyqtSignal来声明信号，并且需要在类中的函数之外声明(需要全局变量/类变量)
def handleCalc():
    """槽函数"""
    #print('统计按钮被按下')
    info = textEdit.toPlainText()   # 获取框中输入的信息
    # 统计薪资 2w 以上的人
    salary_info = get_salary_larger_than_2w(info)

    # 弹出通知对话框
    #QMessageBox.about(parent, caption, text)
    QMessageBox.about(window,
                      "统计结果",
                      f'''薪资大于2w:\n{salary_info[0]}
                        \n薪资小于2w:\n{salary_info[1]}''')

def get_salary_larger_than_2w(info):
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
        parts = line.split(' ') # 输入用空格分开,eg:张三 2000 35
        #去掉列表中的空字符串, 数据处理
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name +'\n'  # 统计结果一行一行的显示
        else:
            salary_below_20k += name +'\n'
    return salary_above_20k, salary_below_20k

def calculate_salary_test():
    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    window = QMainWindow()  # 主窗口
    window.resize(500, 400)
    window.move(500, 300)   # 相对于父控件的位置，由于主窗口没有父控件，变成了相对屏幕左上角的位置
    window.setWindowTitle("薪资统计")

    textEdit = QPlainTextEdit(window)   # window 是textEdit 的父控件
    textEdit.setPlaceholderText("请输入信息")    # 占位信息
    textEdit.move(10, 25)   # 相对于 标题栏的下面的左上角的位置
    textEdit.resize(300, 350)

    button = QPushButton('统计', window)        # 父控件 window
    button.move(380, 80)
    button.clicked.connect(handleCalc)      # 设置槽函数
    window.show()
    app.exec_() #死循环，等待, 除法按下结束才会关闭

################### step2 将这个窗口有关的都封装起来 ############################
# 这样写代码的模块性好, 方便维护
# 可扩展性好，写其它窗口时候:class Query()....
# 尽量不要引入全局变量
class States():
    def __init__(self):
        # 主窗口控件
        self.window = window = QMainWindow()  # 主窗口
        self.window.resize(500, 400)
        self.window.move(500, 300)  # 相对于父控件的位置，由于主窗口没有父控件，变成了相对屏幕左上角的位置
        self.window.setWindowTitle("薪资统计")
        # 文本编辑窗口控件
        self.textEdit = QPlainTextEdit(self.window)  # window 是textEdit 的父控件
        self.textEdit.setPlaceholderText("请输入信息")  # 占位信息
        self.textEdit.move(10, 25)  # 相对于 标题栏的下面的左上角的位置
        self.textEdit.resize(300, 350)
        #按键控件
        self.button = QPushButton('统计', self.window)  # 父控件 window
        self.button.move(380, 80)
        self.button.clicked.connect(self.handleCalc)  # 设置槽函数

    # 这个窗口的槽函数们
    def handleCalc(self):
        """槽函数"""
        # print('统计按钮被按下')
        info = self.textEdit.toPlainText()  # 获取框中输入的信息
        # 统计薪资 2w 以上的人
        salary_info = self.get_salary_larger_than_2w(info)

        # 弹出通知对话框
        # QMessageBox.about(parent, caption, text)
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

def calculate_salary_test2():
    app = QApplication(sys.argv)
    s = States()
    s.window.show()
    app.exec_() #死循环，等待, 除法按下结束才会关闭
    # sys.exit(app.exec_())

class MyWindow(QWidget):
    # 声明自定义信号的时候，必须在类中定义，而不能在函数中定义
    my_signal = pyqtSignal(str) # 类属性, 参数为变量的类型

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

if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

























