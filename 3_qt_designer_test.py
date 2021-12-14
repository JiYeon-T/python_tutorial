from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon

class States():
    def __init__(self):
        # 从文件中加载 UI 定义
        # q_file_stats = QFile("ui/stats.ui") #ui 目录下
        # q_file_stats.open(QFile.ReadOnly)
        # q_file_stats.close()

        # 从 UI 定义中动态创建一个窗口对象, QUiLoader().load()的返回值就是 QtDesigner 创建的主窗口对象
        # 注意: 里面的控件对象 变成了 self.ui 对象的属性了(成员)
        # eg: self.ui.button, self.ui.textEdit
        # 可以打断点在这里调试: self.ui 是 QWidget 类型
        self.ui = QUiLoader().load("ui/3_spider_ui.ui")

        # signal - slot
        self.ui.button.clicked.connect(self. handleCalc)  # 关联槽函数

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

app = QApplication([])  # 整个 UI 界面的控件，信号管理等
#app.setWindowIcon(QIcon('res/logo.jpg'))
s = States()
s.window.show()
app.exec_() #死循环，等待, 除法按下结束才会关闭

if __name__ =='__main__':
    pass
