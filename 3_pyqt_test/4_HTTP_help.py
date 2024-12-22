import sys, time
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon
import requests     # 写一个 HTTP 调试助手

class HttpClient():
    def __init__(self):
        # 加载 ui 文件, 局部变量
        qfile = QFile("ui/2_http.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 从 UI 定义中动态创建窗口对象
        self.ui = QUiLoader().load(qfile)
        # boxMethod 按键
        self.ui.boxMethod.addItems(['GET', 'POST', 'PUT', 'DELETE'])
        # 信号处理，设置槽函数
        self.ui.buttonSend.clicked.connect(self.sendRequest)
        self.ui.buttonAddHeader.clicked.connect(self.addOneHeader)
        self.ui.buttonDelHeader.clicked.connect(self.delOneHeader)
        self.ui.buttonClear.clicked.connect(self.clearDisplay)

    def sendRequest(self):
        pass

    def addOneHeader(self):
        pass

    def delOneHeader(self):
        pass
    def clearDisplay(self):
        pass

def http_client_test():
    app = QApplication([])  # 整个 UI 界面的控件，信号管理等
    s = HttpClient()
    s.ui.window.show()
    app.exec_() #死循环，等待, 除法按下结束才会关闭

if __name__ =='__main__':
    pass
















