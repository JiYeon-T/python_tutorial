import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QRadioButton, QPushButton, QGroupBox, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtWidgets import QStackedWidget, QComboBox, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QAction, QCompleter
from PyQt5.QtCore import Qt, QFile, pyqtSlot
from PyQt5.QtGui import QPainter, QValidator, QIntValidator, QRegExpValidator


# https://doc.qt.io/archives/qtforpython-5/PySide2/QtWidgets/QLineEdit.html
# TODO: 如何设置 Lineedit 大小用户可手动调节? 参考 sscom

def pyqt_lineedit_test():
    class App(QMainWindow):
        """QMainWindow 继承 QWidget"""
        def __init__(self):
            super().__init__()
            self.title = "pyqt_lineedit_test"
            self.left = 100
            self.top = 100
            self.width = 640
            self.height = 480
            self.initUI() # init

        def initUI(self):
            self.setWindowTitle(self.title)  # The window title is set using setWindowTitle(title)
            self.setGeometry(self.left, self.top, self.width, self.height)  # We set the window size using the setGeometry(left,top,width,height) method.
            layout = QVBoxLayout()

            # create a textbox in the window
            self.textbox = QLineEdit(self)
            self.textbox.move(20, 20) # absolutely move position
            self.textbox.resize(int(self.width / 2), int(self.height / 2))
            self.textbox.setPlaceholderText('请输入文本')
            self.textbox.setDragEnabled(True)
            # self.textbox.addAction(QAction('Action1'),QLineEdit.TrailingPosition)  # ??
            # self.textbox.setEchoMode(QLineEdit.Password)
            self._add_completer()
            # All following alphabetic characters are uppercased.
            # License number; blanks are # and all (alphabetic) characters are converted to uppercase.
            # self.textbox.setInputMask('<AAAAA-AAAAA-AAAAA-AAAAA-AAAAA')
            self.textbox.setClearButtonEnabled(True)
            # self.textbox.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
            # self.textbox.setReadOnly(True)
            self.textbox.setTextMargins(10, 10, 10, 10)
            # self._add_validator()
            # self.textbox.
            # create a button in the window
            self.button = QPushButton('Show Text', self)
            self.button.move(100, 100)
            self.button.clicked.connect(self._on_clock)

            # layout.addWidget(self.textbox)
            # layout.addWidget(self.button)
            # self.setLayout(layout)

        @pyqtSlot()
        def _on_clock(self):
            print("Pyside2 button clicked")
            text = self.textbox.text()
            self.textbox.displayText()
            QMessageBox.question(self, 'Message', 'You Typed:' + text, QMessageBox.Ok, QMessageBox.Reset)
            # self.textbox.clear()

        def _add_completer(self):
            completer = QCompleter()
            self.textbox.setCompleter(completer)

        def _add_validator(self):
            """
            The line edit’s returnPressed() and editingFinished() signals will only be emitted
            if v validates the line edit’s content as Acceptable .
            在实际应用中，QValidator 可以有效提升输入控件的健壮性和用户体验，避免无效数据进入程序
            TODO:对数输入蓝牙地址等信息的校验可以交给 validator
            """
            # validator = QValidator()  # 可以通过继承该类, 重写 fixup()
            # 自定义验证逻辑时，可以通过继承 QValidator 并重写 validate() 和 fixup() 方法来实现：‌
            # validate() 方法执行核心验证，返回验证结果。
            # fixup() 方法用于清理或修正非法输入（如自动格式化）
            # validator = QRegExpValidator()
            validator = QIntValidator(1, 99)  # 判断输入是否 1-99
            self.textbox.setValidator(validator)
            self.textbox.returnPressed.connect(self._edir_check_pass)

        @pyqtSlot()
        def _edir_check_pass(self):
            print(f"pass:{self.textbox.text()}")

    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    pyqt_lineedit_test()


