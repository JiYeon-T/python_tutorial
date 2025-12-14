## pyqt5 学习

**学习感悟：**

浏览器界面: html(控件) + css(样式，Qt Style sheet) +javascript(逻辑)

桌面软件界面: qt(控件) + qss(样式)

手机 APP 界面:

嵌入式设备界面: touchGFX, LVGL(可视化库), ...




##### 1. pyqt5 的版本问题，尽量使用32位的解释器，增加打包后代码的兼容性，目前使用的是64位的解释器。

![python](D:\install_location\python_files\python.png)

![image-20211017093305309](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017093305309.png)

#####  2. application类

```python
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
app = QApplication([])	# 控件管理等功能
#其它代码
#window.resize(100, 200)	# 单位:pixel, 像素
app.exec_()
```

##### 3. signal 和 slot

信号和槽函数的使用:

##### 4. Qt Designer (界面设计师)

路径:python/lib/site-packages/PySide2/designer.exe

UI界面文件夹

设计好的界面保存后，生成 xxx.ui 的文件，文件格式:xml

##### 5. 动态加载 .ui 文件

**NOTE: **

界面修改十分方便

```python
class States():
    def __init__(self):
        # 从文件中加载 UI 定义
        q_file_stats = QFile("ui/stats.ui") #ui 目录下
        q_file_stats.open(QFile.ReadOnly)
        q_file_stats.close()

        # 从 UI 定义中动态创建一个窗口对象, QUiLoader().load()的返回值就是 QtDesigner 创建的主窗口对象
        # 注意: 里面的控件对象 变成了 self.ui 对象的属性了(成员)
        # eg: self.ui.button, self.ui.textEdit
        # 可以打断点在这里调试: self.ui 是 QWidget 类型
        self.ui = QUiLoader().load(q_file_stats)
        self.ui.button.clicked.connect(self. handleCalc)  # 关联槽函数
```

##### 6. API 接口测试——HTTP接口测试助手

课后作业1：

![image-20211017105845480](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017105845480.png)

课后作业2：爬虫

![image-20211017131907975](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017131907975.png)

homework3:股票分析软件，爬虫，通过requiest库拉取文件，读取到mysql的一张表里，使用数据挖掘的方法对得到的数据进行分析，再通过可视化界面显示。

**使用多线程，使爬虫获取数据在后台进行，显示界面在前台进行**

![image-20211017183148556](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017183148556.png)

![image-20211017183313550](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017183313550.png)

4.homework: 可以做一个图像处理界面, opencv, .......

![image-20211017205734357](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017205734357.png)



##### 7. layout 界面布局

**方法1：正常 UI 设计步骤:**

step1.首先界面布局:vertical(垂直), horizontal（水平）......

step2:然后再每个块里面选择控件

**方法2：先将控件都按照想要的位置放置好**

对整体有了布局之后，调整主窗口的大小，就可以改变其中控件的大小。

##### 8. 调节布局中控件的大小

QWidget->sizepolicy 属性

Layout设计经验: 从小到大

![image-20211017133130104](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017133130104.png)

##### 9.代码打包,发布程序

PyInstaller 将脚本制作成可执行程序。

```python
pip install pyinstaller
pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml
# 生成一个 dist/httpclient/httpclient.exe
# --noconsole 指定不要命令行窗口，否则程序执行的时候会出现一个命令行
# --hidden-import 因为 QtXml 库是动态导入, PyInstaller没法分析出来，需要我们告诉它
# 可执行程序需要的资源需要手动拷贝到 httpclient 目录下
# 作用:把程序有关的库都打包到可执行文件夹
```

**可执行程序需要的资源，表格，图片（资源文件）等都需要“手动拷贝”到 httpclient 目录下**

使用的时候只需要将整个文件夹打包发送即可，



##### 10.图标的添加

主窗口的图标

```python
from PySide2.QtGui import QIcon
app = QApplication([])
#加载 icon
app.setWindowIcon('res/logo.png')
```

可执行文件的图标

```python
# 文件格式必须是.ico 图标文件格式
pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo.ico"
#转换网址
www.zamzar.com/convert/png-to-ico
www.easyicon.net/convert
```

##### 11.为radio button按钮添加分组，否则默认所有都是一组

key1: 添加按钮分组

key2:添加 Group box

key3:使用 QWidget

##### 12.qss 界面显示

显示样式

```python
# qss 样式添加到 style sheet
# selector选择器{属性}
QPushButton{		# 仅仅设置该范围内的按钮的属性
    color:read	#声明， 值
    font-size:15px	#15个像素
}

*	# 选择所有元素
*{
    font-family:微软雅黑;
    font-szie:15px;
    colort:#1d649c;
}
```

##### qss 样式设计

选择元素，样式设计;

https://www.bilibili.com/video/BV1cJ411R7bP?p=16&spm_id_from=pageDriver p16, p17



##### 12.多线程后台任务

**好像可以自己写一个服务器性能测试的脚本/工具**

```python
# 多线程操作(可以使用 python 的线程库，也可以使用 pyqt 封装的线程库)
# qt 主循环的线程
# 后台服务程序线程
# 将访问服务器的函数写道按钮的槽函数里
class W():
    def __init__(self):
        pass
    def send_request(self):
        #...
        thread = Thread(target=self.newThreadFun,
                       args = (s, prepared))
        trhead.join()
       
    def newThreadFun(self, s, prepared):
        """线程入口函数"""
        try:
            r = s.send(prepared)
            self.pretty_print_response(r)
        except:
            self.ui.outputWindow.append(traceback.format_exc())
```

**当在一个新线程里，启动新的线程后，禁用按钮，发送之后，重新启用按钮**

**这样点击了“开始按钮”以后，就无法再使用“开始按钮”，直到发送结束**

##### 13.显示进度

**NOTE:**

#####  注意，在新的线程里面操作界面会出现很多莫名其妙的 bug

**保证在主线程里操作界面,子线程发信号，主线程收到信号，在主线程里操作界面**

![image-20211017201502094](C:\Users\qz\AppData\Roaming\Typora\typora-user-images\image-20211017201502094.png)

定义一个可以发送信号的类，

```python

```



---

**？？？要发信号???**

**在子线程中清空（编辑） UI 主线程 lineedit 的内容，导致 dump？**

**千万不要直接在子线程中操作界面打印，很可能会导致奔溃**
