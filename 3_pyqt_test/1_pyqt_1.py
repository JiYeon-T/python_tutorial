from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

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

window.show()

app.exec_() #死循环，等待, 除法按下结束才会关闭

if __name__ =='__main__':
    pass

