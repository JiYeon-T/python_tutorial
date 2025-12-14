import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QRadioButton, QPushButton, QGroupBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout

# from PyQt5.QtCore import Qt
# from PyQt5.QtUiTools import QUiLoader
from PyQt5.QtCore import QFile
# 界面布局
# UI 设计师
# 界面随着主窗口拉伸

class MyVLayoutWindow(QWidget):
    """控件布局测试"""
    def __init__(self):
        super(MyVLayoutWindow, self).__init__()
        # 设置大小
        self.resize(300, 300)
        # 设置标题
        self.setWindowTitle("垂直布局")
        layout = QVBoxLayout()

        # 会将你放在layout中的空间压缩成默认的大小，上述代码表示1:1:2:2分割
        # 作用是在布局中增加一个伸缩量(相当于Qt中的弹簧)，里面的参数表示QSpaceItem的个数，默认值为0
        layout.addStretch(1) # 添加弹簧
        self.btn1 = QPushButton("按钮1")
        layout.addWidget(self.btn1)

        layout.addStretch(1)
        self.btn2 = QPushButton("按钮2")
        layout.addWidget(self.btn2)

        layout.addStretch(2)
        self.btn3 = QPushButton("按钮3")
        layout.addWidget(self.btn3)
        layout.addStretch(2)

        self.setLayout(layout) # 设置当前控件的布局

class MyMixLayoutWindow(QWidget):
    """多种组合布局格式使用"""
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.init_ui()

    def init_ui(self):
        # 最外层的垂直布局，包含两部分：爱好和性别.....
        container = QVBoxLayout()

        # 创建第一个组，添加多个组件
        hobby_box = QGroupBox("爱好")
        v_layout = QVBoxLayout() # 垂直布局
        btn1 = QRadioButton("篮球")
        btn2 = QRadioButton("足球")
        btn3 = QRadioButton("乒乓球")
        btn4 = QRadioButton("橄榄球")
        # 将 widget 添加到 layout 中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        v_layout.addWidget(btn4)
        # hobby_box 设置 layout
        hobby_box.setLayout(v_layout)

        # 创建第二个组
        gender_box = QGroupBox("性别")
        h_layout = QHBoxLayout() # 水平布局
        btn5 = QRadioButton("男")
        btn6 = QRadioButton("女")
        h_layout.addWidget(btn5)
        h_layout.addWidget(btn6)
        gender_box.setLayout(h_layout) # 设置 box 的布局

        container.addWidget(hobby_box) # 将两个组添加到容器中
        container.addWidget(gender_box)

        self.setLayout(container)


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:green;")

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉2要显示的内容", self)
        self.setStyleSheet("background-color:red;")

class StackedLayoutWindowTest(QWidget):
    """抽屉布局的窗口"""
    def __init__(self):
        super().__init__()
        print("init")
        self.resize(400, 600)
        self.create_stack_layout()
        self.init_ui()

    def create_stack_layout(self):
        # 创建堆叠(抽屉)布局
        self.stacked_layout = QStackedLayout()
        win1 = Window1()
        win2 = Window2()
        # 空间到布局器中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)
        print("create stack layout")

    def init_ui(self):
        self.setFixedSize(300, 270)
        # 创建整体布局器
        container = QVBoxLayout() # 垂直布局

        # 创建 要显示具体内容的 widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout) # 抽屉布局
        widget.setStyleSheet("background-color:grey;")
        # 创建两个按钮用来切换 stacklayout
        btn1 = QPushButton("抽屉1")
        btn2 = QPushButton("抽屉2")
        btn1.clicked.connect(self.btn1_pressed_slot)
        btn2.clicked.connect(self.btn2_pressed_slot)

        # 添加 button
        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)

        # 设置当前控件(类)的 layout, 然后才可以显示 layout 中的控件
        self.setLayout(container)
        print("init ui")

    def btn1_pressed_slot(self):
        """根据抽屉布局器的索引值来决定显示哪个window"""
        self.stacked_layout.setCurrentIndex(0)
        print("btn1")

    def btn2_pressed_slot(self):
        """根据抽屉布局器的索引值来决定显示哪个window"""
        self.stacked_layout.setCurrentIndex(1)
        print("btn2")


if __name__ =='__main__':
    app = QApplication(sys.argv)
    # w = MyVLayoutWindow()
    # w = MyMixLayoutWindow()
    w = StackedLayoutWindowTest()
    print("run")
    w.show()
    app.exec_()