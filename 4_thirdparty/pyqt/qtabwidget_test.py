import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QRadioButton, QPushButton, QGroupBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtWidgets import QStackedWidget, QComboBox, QTabWidget
from PyQt5.QtCore import Qt, QFile, QSize
from PyQt5.QtGui import QPainter, QIcon
# from PyQt5.QtUiTools import QUiLoader


def qtabwidget_example():
    """
    https://doc.qt.io/qt-6/zh/qtabwidget.html
    使用 QTabWidget 的常规方法如下：
    创建一个 QTabWidget。
    为标签对话框中的每个页面创建一个QWidget ，但不要为它们指定父窗口部件。
    将子窗口部件插入页面窗口部件，使用布局将其正常定位。
    调用addTab() 或insertTab() 将页面部件放入选项卡部件中，为每个选项卡添加一个合适的标签，并可选择键盘快捷键。
    标签的位置由tabPosition 定义，形状由tabShape 定义
    """
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('QTabWidget 示例')
            self.setGeometry(100, 100, 400, 400)
            self.init_ui()

        def init_ui(self):
            self.tab_widget = QTabWidget()
            self.setCentralWidget(self.tab_widget)

            self.tab1 = QWidget()  # 标签页1,这里不需要指定父对象
            self.tab_widget.addTab(self.tab1, "标签页1")
            self.setup_tab1()

            self.tab2 = QWidget()  # 标签页1
            self.tab_widget.addTab(self.tab2, "标签页2")
            self.setup_tab2()

            # self.tab_widget.setTabText(0, "Hello, world")
            self.tab_widget.setTabWhatsThis(0, 'This is tab1')
            # self.tab_widget.setTabShape(QTab)
            # self.tab_widget.setTabIcon(0, QIcon())
            # self.tab_widget.setIconSize(QSize(30, 30))
            self.tab_widget.setTabPosition(QTabWidget.North)
            self.tab_widget.setTabShape(QTabWidget.Rounded)
            self.tab_widget.setCurrentIndex(1)
            print(f'curr:{self.tab_widget.currentIndex()}')
            print(f'curr:{self.tab_widget.currentWidget()}')
            # self.tab_widget.setDocumentMode(True)
            self.tab_widget.setMovable(True)  # 设置标签栏是否可移动
            # self.tab_widget.setTabBarAutoHide(True)
            self.tab_widget.setTabsClosable(True)
            # self.closeEvent()
            self.tab_widget.tabCloseRequested.connect(self._tab_close_request_slot)
            self.tab_widget.usesScrollButtons()
            # 删除所有页面，但不删除它们。调用该函数等同于调用removeTab() 直到标签部件为空。
            # self.tab_widget.clear()
            # 请注意，即使禁用的标签页/页面也可能是可见的。如果页面已经可见，QTabWidget 将不会隐藏它；
            # 如果所有页面都被禁用，QTabWidget 将显示其中一个页面。
            # self.tab_widget.setTabEnabled(0, False)
            self.tab_widget.setToolTip("提示")
            # 如果visible 为 true，则位于index 位置的页面可见；否则，位于index 位置的页面隐藏。页面的标签页将适当重绘。
            # self.tab_widget.setTabVisible(0, False)
            self.tab_widget.tabBarClicked.connect(self._tab_clicked_slot)  # 单击事件
            # tabBarDoubleClicked, 双击事件
            # tabCloseRequested，关闭请求事件
            print(f'whats this:{self.tab_widget.whatsThis()}')

        def _tab_clicked_slot(self, idx):
            print(f'clicked:{idx}')

        def _tab_close_request_slot(self, idx):
            # 如果在show() 之后调用 addTab()，布局系统将尝试调整以适应窗口部件层次结构的变化，并可能导致闪烁。
            # 为避免这种情况，可以在更改之前将QWidget::updatesEnabled 属性设置为 false；
            # 切记在更改完成后将该属性设置为 true，使窗口部件再次接收绘制事件。
            # addTab(), removeTab(), insertTab() 同理
            print(f'remove tab:{idx}')
            self.setUpdatesEnabled(False)
            # 从窗口部件堆栈中删除位于index 位置的标签页。页面部件本身不会被删除。
            self.tab_widget.removeTab(idx)
            self.setUpdatesEnabled(True)

        def setup_tab1(self):
            layout = QVBoxLayout()
            label = QLabel('这是标签页1的内容')
            buton = QPushButton('按钮1')
            layout.addWidget(label)
            layout.addWidget(buton)
            self.tab1.setLayout(layout)

        def setup_tab2(self):
            layout = QVBoxLayout()
            label = QLabel('这是标签页2的内容')
            buton = QPushButton('按钮2')
            layout.addWidget(label)
            layout.addWidget(buton)
            self.tab2.setLayout(layout)


    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()  # 显示界面
    app.exec_()


def qtabbar_test():
    """
    https://doc.qt.io/qt-6/zh/qtabbar.html
    """
    pass

if __name__ == '__main__':
    # qtabwidget_example()
    qtabbar_test()