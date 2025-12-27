import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QRadioButton, QPushButton, QGroupBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtWidgets import QStackedWidget, QComboBox, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QAction, QCompleter, QSlider
from PyQt5.QtWidgets import QDialog, QFileDialog, QInputDialog, QFontDialog, QProgressDialog, QColorDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtCore import Qt, QFile, pyqtSlot
from PyQt5.QtGui import QPainter, QValidator, QIntValidator, QRegExpValidator


# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QDialog.html
# https://doc.qt.io/qt-6/zh/qdialog.html
# QDialog Inherited by: QAbstractPrintDialog, QPageSetupDialog, QPrintDialog, QPrintPreviewDialog, QColorDialog,
# QErrorMessage, QFileDialog, QFontDialog, QInputDialog, QMessageBox, QProgressDialog, QWizard
# 另请参阅 QDialogButtonBox,QTabWidget,QWidget,QProgressDialog 和标准对话框示例。
# https://doc.qt.io/qt-6/zh/qtwidgets-dialogs-standarddialogs-example.html
# https://code.qt.io/cgit/qt/qtbase.git/tree/examples/widgets/dialogs/standarddialogs/dialog.cpp?h=6.10


def qdialog_test():

    class MyDialog(QDialog):
        """定义对话框类"""
        def __init__(self):
            super().__init__()
            self.setWindowTitle(f'自定义对话框')
            self.resize(300, 200)
            self.move(200, 200)

            self.label = QLabel('自定义错误提示', self)
            self.label.setMargin(50)
            # 在执行自定义对话框时，为了关闭对话框并返回适当的值，
            # 请将默认按钮（例如确定按钮）连接到accept() 槽，
            # 将取消按钮连接到reject() 槽。另外，
            # 也可以使用Accepted 或Rejected 调用done() 槽。
            self.ok_button = QPushButton('确认', self)
            self.ok_button.clicked.connect(self._accept)  #
            self.cancel_button = QPushButton('取消', self)
            self.cancel_button.clicked.connect(self._reject)

            # 对话框的默认按钮是用户按 Enter（返回）键时按下的按钮。该按钮用于表示用户接受对话框的设置并希望关闭对话框。
            # self.ok_button.setDefault(True)

            # 如果用户在对话框中按 Esc 键，将调用QDialog::reject()。这将导致窗口关闭：close event 不能被ignored 。

            layout = QVBoxLayout()
            layout.addWidget(self.label)
            layout.addWidget(self.ok_button)
            layout.addWidget(self.cancel_button)
            self.setLayout(layout)

        @pyqtSlot()
        def _accept(self):
            self.accept()
            # 将模式对话框的结果代码设置为i(QMessageBox::StandardButton 枚举的值。)
            # self.setResult(QMessageBox.StandardButton.FirstButton)

        @pyqtSlot()
        def _reject(self):
            self.reject()
            # self.setResult(QMessageBox.StandardButton.LastButton)

    class Win(QMainWindow):

        def __init__(self):
            super().__init__()
            self.init_ui()
            self.setGeometry(500, 500, 800, 600)

        def init_ui(self):
            self.button = QPushButton('modal', self)
            # self.setCentralWidget(button)  # 错误实现:这个 button 会占满整个父类(屏幕)
            self.button.clicked.connect(self.modal_dialog_slot)
            self.button.move(int(self.width()/2), int(self.height()/2))

            self.modeless_button = QPushButton('modeless', self)
            self.modeless_button.clicked.connect(self.modeless_dialog_slot)
            self.modeless_button.move(int(self.width()/2), int(self.height()/2) + 100)

            self.my_dialog()
        @pyqtSlot()
        def modal_dialog_slot(self):
            """create dialog, 模态对话框使用 exec() 显示
            阻塞直到对话框关闭

            显示模式对话框的最常用方法是调用open() 函数。或者，也可以调用setModal(true) 或setWindowModality() ，
            然后再调用show() 。在这两种情况下，一旦显示对话框，控件就会立即返回给调用者。您必须连接到finished() 信号，
            才能知道对话框何时关闭以及return value 。或者，也可以连接accepted() 和rejected() 信号。

            在执行自定义对话框时，为了关闭对话框并返回适当的值，
            请将默认按钮（例如确定按钮）连接到accept() 槽，
            将取消按钮连接到reject() 槽。
            另外，也可以使用Accepted 或Rejected 调用done() 槽。

            模态对话框常用于需要返回值的情况，
            例如，显示用户按下的是OK 还是Cancel 。可以通过调用accept() 或reject() 槽关闭对话框，exec()
            将根据情况返回Accepted 或Rejected 。调用exec() 会返回对话框的结果。如果对话框未被销毁，
            也可以通过result() 获得结果。

            要修改对话框的关闭行为，可以重新实现函数accept()、reject() 或done()。
            只有在保留对话框位置或覆盖标准关闭或拒绝行为时，才应重新实现closeEvent() 函数。
            """
            # self.button.setEnabled(False)  # 关闭按钮, 否则重复点击会弹出很多窗口

            self.dialog = QDialog(self)
            self.dialog.setWindowTitle('模态对话框')
            self.dialog.setGeometry(int(self.width()/4), int(self.height()/4), int(self.width()/2), int(self.height()/2))
            # self.dialog.setSizeGripEnabled(True)  # 右下角控制大小的按钮, 此属性表示是否启用了尺寸控件
            # 显示模式对话框的最常用方法是调用open() 函数。
            # 也可以调用setModal(true) 或setWindowModality() ，然后再调用show() 。
            # 在这两种情况下，一旦显示对话框，控件就会立即返回给调用者。
            # 您必须连接到finished() 信号，才能知道对话框何时关闭以及return value 。
            # 或者，也可以连接accepted() 和rejected() 信号。
            # self.setWindowModality(Qt.WindowModality.WindowModal)  # 不阻塞,
            self.setWindowModality(Qt.WindowModality.ApplicationModal)  # 不阻塞

            # 该属性用于确定show() 应弹出模式对话框还是无模式对话框。
            # 设置模式对话框后, show() 接口同样会阻塞:
            # 默认情况下，该属性为false ，show() 会以无模式方式弹出对话框。
            # 将此属性设置为 true 相当于将QWidget::windowModality 设置为Qt::ApplicationModal 。
            # exec() 会忽略此属性的值，并始终以模态方式弹出对话框。
            # self.dialog.setModal(False)

            self.dialog.accepted.connect(self._accepted_slt)
            self.dialog.rejected.connect(self._rejected_slt)  # 如果没有选择任何按钮直接 x 掉, 也会收到 rejected 信号
            self.dialog.finished.connect(self._finished_slt)
            self.dialog.show()


            # The most common way to display a modal dialog is to call its exec() function.
            # When the user closes the dialog, exec() will provide a useful return value .
            # ret = self.dialog.exec()  # 阻塞直到对话框关闭
            # print(f"ret:{ret}")

            # To close the dialog and return the appropriate value, you must connect a default button,
            # e.g. an OK button to the accept() slot and a Cancel button to the reject() slot.
            # Alternatively, you can call the done() slot with Accepted or Rejected
            # self.button.setEnabled(True)
            print(f"dialog Exit")

        def _add_buttons(self):
            pass

        def extension_dialog(self):
            """
            可扩展性是以两种方式显示对话框的能力：显示最常用选项的部分对话框和显示所有选项的完整对话框。
            通常情况下，可扩展对话框最初显示为部分对话框，但带有一个More 切换按钮。如果用户按下More 按钮，对话框就会展开。
            """


        @pyqtSlot()
        def _accepted_slt(self):
            print(f'_accepted_slt')

        @pyqtSlot()
        def _rejected_slt(self):
            print(f'_rejected_slt')

        @pyqtSlot()
        def _finished_slt(self):
            print(f'_finished_slt')

        @pyqtSlot()
        def modeless_dialog_slot(self):
            """非模态对话框使用 show() 方法显示
            立即返回，对话框独立运行

            无模式对话框是一种独立于同一应用程序中其他窗口运行的对话框。文字处理程序中的查找和替换对话框通常是无模式的，
            这样用户就可以同时与应用程序的主窗口和对话框进行交互。例如:Notepad++ 等文字搜索软件

            警告： 使用open() 或show() 时，不应在堆栈中创建模式对话框，以免控件返回调用者后立即将其销毁。
            """
            # An alternative is to call setModal (true) or setWindowModality() , then show() .
            # Unlike exec() , show() returns control to the caller immediately.
            self.dialog2 = QDialog()
            self.dialog2.setWindowTitle('非模态对话框')
            # When an application modal dialog is opened, the user must finish interacting with the
            # dialog and close it before they can access any other window in the application.
            # Window modal dialogs only block access to the window associated with the dialog,
            # allowing the user to continue to use other windows in an application.
            # self.dialog2.setModal(True)
            # self.dialog2.setWindowModality(Qt.WindowModality.ApplicationModal)
            # self.dialog2.set
            self.dialog2.show()  # // 立即返回，对话框独立运行

        def my_dialog(self):
            dialog = MyDialog()
            ret = dialog.exec()  # 阻塞直到返回
            print(f"reference:{QMessageBox.Accepted}  {QMessageBox.Rejected}")
            print(f'ret:{repr(ret)} {ret}')

    app = QApplication(sys.argv)
    ex = Win()
    ex.show()
    sys.exit(app.exec_())



def qfiledialog_test():
    class App(QWidget):
        """The methods used are QFileDialog.getOpenFileName(), QFileDialog.getOpenFileNames(),
        QFileDialog.getSaveFileName(). The method parameters let you specify the default directory,
        filetypes and the default filename."""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_menu_test"
            self.left = 200
            self.top = 200
            self.width = 800
            self.height = 600
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title) # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height) # We set the window size using the setGeometry(left,top,width,height) method.

            button = QPushButton('Unknown', self)
            button.move(int(self.width / 2), int(self.height / 2))

            # button.clicked.connect(self.saveFileDialog)
            button.clicked.connect(self.openFileNameDialog)
            # button.clicked.connect(self.openFileNamesDialog)


        def openFileNameDialog(self):
            """如果这个设置为按钮的槽函数不就是打开文件的功能了吗"""
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog # ???
            fileName, _ = QFileDialog.getOpenFileName(self, \
                                                      "获取打开文件", \
                                                      "", \
                                                      "All Files (*);;Python Files (*.py);;C Files(*.c)", \
                                                      options = options)
            if fileName:
                print(fileName)

        def openFileNamesDialog(self):
            """"""
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog  # ???
            files, _ = QFileDialog.getOpenFileNames(self,
                                                    "获取打开得文件", "",
                                                    "All Files (*);;Python Files (*.py);;C Files(*.c)",
                                                    options = options)
            if files:
                print(files)

        def saveFileDialog(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog # ???
            fileName, _ = QFileDialog.getSaveFileName(self,
                                                      "获取保存文件", "",
                                                      "All Files (*);;Python Files (*.py);;C Files(*.c)",
                                                      options = options)
            if fileName:
                print(fileName)

        @pyqtSlot()
        def on_click(self):
            print("Clicked")

    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


def qprogressdialog_test():
    pass


def qmessagebox_test():
    """QMessageBox 也是 QDialog 的子类
    标准对话框如QMessageBox提供了预定义的消息提示功能。‌
    https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QMessageBox.html
    """
    class App(QWidget):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_messagebox_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI() # 构造函数中显示 UI

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            print("Enter?")
            # self._question_messagebox()
            # self.criticial_messagebox()
            # self.my_dialog()
            QMessageBox.aboutQt(self)

            print("Enter finished")

        def _question_messagebox(self):
            """问题对话框"""
            # This function will block()
            buttonReply = QMessageBox.question(self, "PyQt Message", "Dou You like pyqt?", \
                                               QMessageBox.Yes | QMessageBox.No | QMessageBox.Open,
                                               QMessageBox.No)
            # 可选的更多的按钮
            # QMessageBox.Cancel	QMessageBox.Ok	QMessageBox.Help
            # QMessageBox.Open	QMessageBox.Save	QMessageBox.SaveAll
            # QMessageBox.Discard	QMessageBox.Close	QMessageBox.Apply
            # QMessageBox.Reset	QMessageBox.Yes	QMessageBox.YesToAll
            # QMessageBox.No	QMessageBox.NoToAll	QMessageBox.NoButton
            # QMessageBox.RestoreDefaults	QMessageBox.Abort	QMessageBox.Retry
            # QMessageBox.Ignore
            if buttonReply == QMessageBox.Yes:
                print("Yes clicked")
            elif buttonReply == QMessageBox.No:
                print("No clicked")
            elif buttonReply == QMessageBox.Open:
                print("Open clicked")
            else:  # 等等其他事件
                print("No one clicked")

        def criticial_messagebox(self):
            # QMessageBox.critical(self, '异常', '内存不足')
            # 信息对话框
            QMessageBox.information(self, '请补充信息', '填充姓名')

    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


def custome_dialog_test():
    class CustomDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("自定义对话框")
            self.setGeometry(100, 100, 300, 200)

            self.label = QLabel("输入内容:")
            self.input_field = QLineEdit()

            self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            self.button_box.accepted.connect(self.accept)
            self.button_box.rejected.connect(self.reject)

            layout = QVBoxLayout()
            layout.addWidget(self.label)
            layout.addWidget(self.input_field)
            layout.addWidget(self.button_box)

            self.setLayout(layout)

        def get_input(self):
            return self.input_field.text()

    app = QApplication([])
    dialog = CustomDialog()
    if dialog.exec_() == QDialog.Accepted:
        print("用户输入:", dialog.get_input())
    else:
        print("对话框被取消")


if __name__ == '__main__':
    # qdialog_test()
    # qfiledialog_test()
    qmessagebox_test()
    # custome_dialog_test()