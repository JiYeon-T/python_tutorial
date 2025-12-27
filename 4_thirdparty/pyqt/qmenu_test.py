import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMenu, QAction, QMenuBar, QVBoxLayout
# from PyQt5.QtCore import
from PyQt5.QtGui import QIcon

# https://doc.qt.io/archives/qtforpython-5/overviews/qtwidgets-mainwindows-menus-example.html#menus-example
# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QMenu.html

def qmenubar_test():

    class App(QMainWindow):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_menu_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI()  # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.
            self.statusBar().showMessage('Tips')

            mainMenu = self.menuBar()  # MainWindow 的菜单栏, QMenuBar 类型
            fileMenu = mainMenu.addMenu('文件')
            editMenu = mainMenu.addMenu('编辑')
            viewMenu = mainMenu.addMenu('视图')
            searchMenu = mainMenu.addMenu('搜索')
            toolsMenu = mainMenu.addMenu('工具')
            helpMenu = mainMenu.addMenu('帮助')

            # 为每个 menu 添加 QAction
            openButton = QAction('Open', self)
            openButton.setShortcut('Ctrl+O')
            openButton.setStatusTip('打开文件')
            fileMenu.addAction(openButton)

            editButton = QAction('Edit', self)
            editButton.setShortcut('Ctrl+E')
            editButton.setStatusTip('编辑文件')
            fileMenu.addAction(editButton)

            saveButton = QAction('Save', self)
            saveButton.setShortcut('Ctrl+S')
            saveButton.setStatusTip('保存文件')
            fileMenu.addAction(saveButton)

            fileMenu.addSeparator()

            saveasButton = QAction('Saveas', self)
            # saveasButton.setShortcut('Ctrl+S')
            saveasButton.setStatusTip('另存为')
            fileMenu.addAction(saveasButton)

            fileMenu.addSeparator()  # 添加分隔符

            exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
            exitButton.setShortcut('Ctrl+Q')  # 设置快捷键
            exitButton.setStatusTip('退出程序')  # 设置状态栏提示
            fileMenu.addAction(exitButton)

            # layout = QVBoxLayout()
            # layout.addWidget(mainMenu)
            # self.setLayout(layout)

    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


def qmenu_test():
    """
    不用单独测试, QMenuBar的 addMenu() 方法添加的就是 QMenu 对象
    该对象具有 addAction() 等方法
    class <QMenu>
    https://doc.qt.io/archives/qtforpython-5/overviews/qtwidgets-mainwindows-menus-example.html#menus-example
    """
    pass


if __name__ == '__main__':
    qmenubar_test()
    # qmenu_test()
