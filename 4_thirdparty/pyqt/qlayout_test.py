import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QRadioButton, QPushButton, QGroupBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtWidgets import QStackedWidget, QComboBox
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QPainter
# from PyQt5.QtUiTools import QUiLoader

# 界面布局
# UI 设计师
# 界面随着主窗口拉伸控件大小以及位置也跟着改变
# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QLayout.html
# https://doc.qt.io/archives/qtforpython-5/overviews/layout.html#layout-management


class VLayoutWindow(QWidget):
    """控件布局测试"""

    def __init__(self):
        super(VLayoutWindow, self).__init__()
        # self.resize(300, 300)  # 设置大小
        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle("垂直布局")  # 设置标题
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

        self.setLayout(layout)  # 设置当前控件的布局


class MixLayoutWindow(QWidget):
    """组合布局格式使用"""

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
        h_layout = QHBoxLayout()  # 水平布局
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


class StackedLayoutWindow(QWidget):
    """
    抽屉布局的窗口
    https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QStackedLayout.html
    C++:
    https://doc.qt.io/qt-6/zh/qstackedlayout.html
    QStackedLayout 类提供了一个部件堆栈，在该堆栈中，一次只能看到一个部件
    QStackedLayout 没有为用户提供切换页面的内在方法。这通常是通过QComboBox 或QListWidget 来实现的，
    后者存储了 QStackedLayout 页面的标题。
    """

    def __init__(self):
        super().__init__()
        print("init")
        self.resize(400, 600)
        self.init_ui()

    def create_stackedlayout(self):
        """"""
        self.stacked_layout = QStackedLayout()  # 创建堆叠(抽屉)布局
        # test: 显示所有 widget
        # self.stacked_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        win1 = Window1()  # stacked Layout 中添加两个控件
        win2 = Window2()

        self.stacked_layout.addWidget(win1)  # 空间到布局器中
        # self.stacked_layout.addStretch(1)  # 仅 BoxLayout 支持该方法
        # self.stacked_layout.setSpacing(10)
        # 一个 QStackedLayout 可以填充多个子部件（"页面"）。例如
        # QStackedLayout 没有为用户提供切换页面的内在方法。这通常是通过QComboBox 或QListWidget 来实现的，
        # 后者存储了 QStackedLayout 页面的标题。例如
        self.stacked_layout.addWidget(win2)
        # self.stacked_layout.setTitle(f"abc")  # 报错,
        print("create stack layout")

    def init_ui(self):
        self.create_stackedlayout()
        self.setFixedSize(300, 270)
        container = QVBoxLayout()  # 创建整体布局器 垂直布局
        # 创建 要显示具体内容的 widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)  # 抽屉布局
        widget.setStyleSheet("background-color:grey;")
        # 创建两个按钮用来切换 stacklayout
        btn1 = QPushButton("抽屉1")
        btn2 = QPushButton("抽屉2")
        btn1.clicked.connect(self.btn1_pressed_slot)
        btn2.clicked.connect(self.btn2_pressed_slot)

        container.addWidget(widget)  # 添加 button
        container.addWidget(btn1)
        container.addWidget(btn2)

        # 设置当前控件(类)的 layout, 然后才可以显示 layout 中的控件
        self.setLayout(container)
        print(f"init ui {container}")

    def btn1_pressed_slot(self):
        """根据抽屉布局器的索引值来决定显示哪个window"""
        self.stacked_layout.setCurrentIndex(0)
        print(f"btn1 {repr(self.layout().contentsRect())}")
        # print(f"{repr(self.layout())}")
        # print(f"widget count:{self.layout().count()}")
        print(f"margins:{self.layout().getContentsMargins()}")

    def btn2_pressed_slot(self):
        """根据抽屉布局器的索引值来决定显示哪个window"""
        self.stacked_layout.setCurrentIndex(1)
        print(f"btn2 {self.layout().contentsRect()}")

    def delete_layout_item(self):
        """
        The following code fragment shows a safe way to remove all items from a layout:
        """
        child = self.layout().takeAt(0)
        while child:
            del child


def layout_example():
    app = QApplication(sys.argv)
    # w = VLayoutWindow()
    # w = MixLayoutWindow()
    w = StackedLayoutWindow()
    print("run")
    w.show()
    app.exec_()


def pyqt_layout_example2():

    class App(QDialog):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_menu_test"
            self.left = 100
            self.top = 100
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            # We set the window size using the setGeometry(left,top,width,height) method.
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.crate_groupbox()

            # If you’re intrigued by layouts,
            # PyQt5 also offers the flexibility to create vertical layouts using a qvboxlayout.
            # QVBoxLayout Default:Vertical layout
            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.horizontalGroupBox)

            windowLayout.addWidget(QPushButton("垂直布局第2个元素", self))
            windowLayout.addWidget(QPushButton("垂直布局第3个元素", self))
            windowLayout.addWidget(QPushButton("垂直布局第4个元素", self))
            windowLayout.addWidget(QPushButton("垂直布局第5个元素", self))
            self.setLayout(windowLayout)

            self.show()

        def crate_groupbox(self):
            # Box Creation: A box with a title and a horizontal layout is established with:
            # QGroupBox - Default horizontal layout
            self.horizontalGroupBox = QGroupBox("What's your favorite color?")
            layout = QHBoxLayout()

            buttonBlue = QPushButton('Blue', self)
            buttonBlue.clicked.connect(self.on_click)
            layout.addWidget(buttonBlue)

            buttonRed = QPushButton('Red', self)
            buttonRed.clicked.connect(self.on_click)
            layout.addWidget(buttonRed)

            buttonGreen = QPushButton('Green', self)
            buttonGreen.clicked.connect(self.on_click)
            layout.addWidget(buttonGreen)

            buttonBlack = QPushButton('水平布局的第4个item', self)
            buttonBlack.clicked.connect(self.on_click)
            layout.addWidget(buttonBlack)

            buttonPink = QPushButton('水平布局的第5个item long long long', self)
            buttonPink.clicked.connect(self.on_click)
            layout.addWidget(buttonPink)

            self.horizontalGroupBox.setLayout(layout)

        # @Slot()
        def on_click(self):
            print("Clicked")

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def pyqt_grid_layout_test():

    class App(QDialog):
        """PyQt5 supports a grid layout, which is named QGridLayout.
        Widgets can be added to a grid in both the horizontal and vertical direction.
        An example of a grid layout with widgets is shown below:"""

        def __init__(self):
            super().__init__()
            self.title = "pyqt_grid_layout_test"
            self.left = 100
            self.top = 100
            self.width = 320
            self.height = 100
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            # We set the window size using the setGeometry(left,top,width,height) method.
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.create_gridlayout()

            windowLayout = QVBoxLayout()
            windowLayout.addWidget(self.horizontalGroupBox)
            windowLayout.addWidget(QPushButton('='))
            self.setLayout(windowLayout)
            # print(f'spacing:{self.layout().spacing()}')

            self.show()

        def create_gridlayout(self):
            self.horizontalGroupBox = QGroupBox('栅格布局的计算器') # 默认水平布局

            # In the method createGridLayout() we create the grid with a title and set the size.
            layout = QGridLayout()
            # layout.setColumnStretch(1, 2)  # TODO:???
            # layout.setColumnStretch(2, 2)
            layout.setHorizontalSpacing(5)
            layout.setVerticalSpacing(20)

            layout.addWidget(QPushButton('1'), 0, 0) # add widgets to the layout
            layout.addWidget(QPushButton('2'), 0, 1)
            layout.addWidget(QPushButton('3'), 0, 2)
            layout.addWidget(QPushButton('4'), 1, 0)
            layout.addWidget(QPushButton('5'), 1, 1)
            layout.addWidget(QPushButton('6'), 1, 2)
            layout.addWidget(QPushButton('7'), 2, 0)
            layout.addWidget(QPushButton('8'), 2, 1)
            layout.addWidget(QPushButton('0'), 2, 2)

            self.horizontalGroupBox.setLayout(layout)

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


def layout_test3():
    """
    This function can be used to iterate over a layout.
    The following code will draw a rectangle for each layout item in the
    layout structure of the widget.
    """

    def paintLayout(self, painter, item):
        layout = item.layout()

        if layout:
            for layout_item in layout:
                self.paintLayout(painter, layout_item)

        painter.drawRect(item.geometry())

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.layout():
            self.paintLayout(painter, self.layout())


def qlayoutitem_example1():
    """
    https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QLayoutItem.html
    C++:
    https://doc.qt.io/qt-6/zh/qlayoutitem.html
    This is used by custom layouts.
    """
    # def heightForWidth(self, w):
    #     if cache_dirty or cached_width != w:
    #         h = calculateHeightForWidth(w)
    #         self.cached_hfw = h
    #         return h
    #     return cached_hfw
    # TODO: 网站上没有给出相关示例
    pass


def qstackedwidget_example():
    """
    https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QStackedWidget.html
    https://doc.qt.io/archives/qtforpython-5/overviews/layout.html#layout-management
    C++:
    https://doc.qt.io/qt-6/zh/qstackedwidget.html
    详细说明
    QStackedWidget 可用于创建类似于QTabWidget 所提供的用户界面。
    它是一个建立在QStackedLayout 类之上的便捷布局 widget。
    与 QStackedLayout 类似，QStackedWidget 也可以通过多个子 widget（"页面"）来构建和填充
    QStackedWidget 没有为用户提供切换页面的内在方法。
    这通常是通过QComboBox 或QListWidget 来实现的，后者存储了 QStackedWidget 页面的标题。
    """
    class Win(QWidget):
        def __init__(self):
            super().__init__()
            self.resize(400, 600)
            self.init_ui()

        def init_ui(self):
            """"""
            first_widget = QWidget()
            label1 = QLabel(first_widget)
            label1.resize(self.width(), (int)(self.height() / 2) )
            label1.setStyleSheet("background-color:green;")
            second_widget = QWidget()
            label2 = QLabel(second_widget)
            label2.resize(self.width(), (int)(self.height() / 2) )
            label2.setStyleSheet("background-color:grey;")
            third_widget = QWidget()
            stackedwidget = QStackedWidget()
            stackedwidget.addWidget(first_widget)  # 向 stackedwidget 中添加组件
            stackedwidget.addWidget(second_widget)
            stackedwidget.addWidget(third_widget)
            # self.stackedwidget.setCurrentIndex(1)  # 设置初始显示页面

            global_layout = QVBoxLayout()  # 添加布局
            self.setLayout(global_layout)

            page_combobox = QComboBox()  # 配合 combobox 使用
            page_combobox.addItem('Page1')
            page_combobox.addItem('Page2')
            page_combobox.addItem('Page3')
            page_combobox.activated.connect(stackedwidget.setCurrentIndex)

            global_layout.addWidget(page_combobox)
            global_layout.addWidget(stackedwidget)

    app = QApplication(sys.argv)
    w = Win()
    w.show()
    app.exec_()

def qborderlayout_example():
    """
    https://doc.qt.io/archives/qtforpython-5/overviews/qtwidgets-layouts-borderlayout-example.html#border-layout-example
    """
    pass


if __name__ =='__main__':
    # layout_example()
    # pyqt_layout_example2()
    # pyqt_grid_layout_test()
    qstackedwidget_example()
