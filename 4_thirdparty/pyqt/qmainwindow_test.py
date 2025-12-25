import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMenu, QDockWidget, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSettings

def pyqt_mainwindow_test():

    class App(QMainWindow):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_mainwindow_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            # We set the window size using the setGeometry(left,top,width,height) method.
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.add_menubar()
            self.add_toolbar()
            self.add_dockwidget()
            self.add_statusbar()
            # self.show() # Finally show() is called to display the window.

        def add_menubar(self):
            """添加 MenuBar() 测试"""
            menubar = self.menuBar()  # QMainWindow comes with a default menu bar
            menu_file = QMenu('file', self)
            menu_open = QMenu('open', self)
            menu_close = QMenu('close',self)
            menubar.addMenu(menu_file)
            menubar.addMenu(menu_open)
            # menubar.addMenu(menu_close)
            menubar.addMenu('close')

            # The createPopupMenu() function creates popup menus when the main window receives
            # context menu events. The default implementation generates a menu with the checkable
            # actions from the dock widgets and toolbars. You can reimplement createPopupMenu()
            # for a custom menu.
            # TODO:
            # exception_menu = self.createPopupMenu()
            # exception_menu.setStatusTip('Exception')
            # menubar.addMenu(exception_menu)

        def add_toolbar(self):
            """添加 toolbar"""
            file_toolbar = self.addToolBar('backend')
            file_toolbar.addAction('回退1')
            file_toolbar.addAction('回退2')
            file_toolbar.addAction('回退3')

        def add_dockwidget(self):
            """dockwidget"""
            dock_widget = QDockWidget("请输入路径", self)  # 创建一个停靠窗口
            dock_widget.setWidget(QTextEdit('Please Enter:'))
            # 设置停靠区域
            dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | \
                                        Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
            dock_widget.setMaximumSize((int)(self.width/2), (int)(self.height/2))  # 限制大小
            self.addDockWidget(Qt.AllDockWidgetAreas, dock_widget)

        def add_statusbar(self):
            """
            You can set a status bar with setStatusBar() ,
            but one is created the first time statusBar() (which returns the main window’s status bar)
            is called.
            """
            # Returns the status bar for the main window.
            # This function creates and returns an empty status bar if the status bar does not exist.
            status_bar = self.statusBar()
            status_bar.showMessage("Message in status bar")

        def restore_settings(self):
            """
            To restore geometry saved using QSettings , you can use code like this:
            """
            settings = QSettings("MyCompany", "MyApp")
            self.restoreGeometry(settings.value("myWidget/geometry"))
            self.restoreState(settings.value("myWidget/windowState"))

        def save_settings(self, event):
            """
            To restore the saved state, pass the return value and version number to restoreState() .
            To save the geometry when the window closes, you can implement a close event like this:
            """
            settings = QSettings("MyCompany", "MyApp")
            settings.setValue("geometry", self.saveGeometry())
            settings.setValue("windowState", self.saveState())
            QMainWindow.closeEvent(self, event)

    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())


def pyqt_mainwindow_example2():
    """
    https://doc.qt.io/archives/qtforpython-5/overviews/qtwidgets-mainwindows-application-example.html#application-example
    """
    pass


if __name__ == '__main__':
    pyqt_mainwindow_test()