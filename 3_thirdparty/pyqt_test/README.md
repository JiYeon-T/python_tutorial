This is a pyqt5 study nodebook.


# 在使用 pyqt 的过程中，概率出现界面卡死的现象，
# 原因:只能在 UI 线程中操作 UI 控件, 其他线程不可以, 即使是定时器也不可以

# 可以实现信号与槽在多个线程中的相互传递数据。
# 用法很简单，创建一个进程类，不同触发时刻分别调用即可。

# TODO: python 多进程实现以及应用
# python multiprocessing:
# https://docs.python.org/zh-cn/3/library/multiprocessing.html


##### 常见控件

##### pyqt
###### 控件

- QPushButton:

```python
button.connect(handleCalc) # 信号 -> 槽函数
button.setText(text) # 改变文本eg:按下变成成停止, 而不是一直是停止
button.setEnabled(False)
button.setEnabled(True) # 继承自 QWidget
button.setIcon(QIcon('logo.png'))	# 设置软件左上角小图标
button.setIconSize(QSize(30, 30))
```

- QLineEdit：只能单行编辑的文本框

```python
edit.textChanged.connect(handleTextChange)
passwordEdit.returnPressed.connect(onLogin) # 回车按下, 进行登录操作, 不需要鼠标点击 
text = edit.text()
edit.setPlaceHolderText('请输入名字')
edit.setText('你好')
edit.clear()
edit.copy()
edit.paste()
```

- QPlainTextEdit:多行纯文本编辑框

```python
edit.textChanged.connect(handleTextChange)
edit.cursorPositionChanged.connect(handleChanged)
text = edit.toPlainText()
textCursor = edit.textCursor()
selectionText = textCursor.selectedText() # 获取选中的文本
edit.setPlainText("Hello, world")
edit.appendPlainText() # 末尾添加\r\n
edit.insertPlainText() # 不会自动换行
edit.clear()
edit.copy()
edit.paste()
edit.document().setMaximumBlockCount(1000) # 为了防止 文本占用太多资源，设置文本框的最大行数
```

- QTextBrowser文本浏览框，只能浏览文本（通常用来显示log日志， 或者不需要用户编辑的大段内容）获取文本, 设置文本, 清除文本, 剪切复制等等

```python
textBrowser.append('hello, world')
textBrowser.ensureCursorVisable() # 使得新添加的文本在最当前的位置, 自动添加换行
textBrowser.insertPlainText('光标处插入文本')
```

- QLabel:标签 可以用来显示文本,图片, 动画等

```python
label.setText()
QLabel 的 pixmap 属性设置中选择图片文件指定既可以使用 label 显示图片
label.setPicture()
label.setPixelMap()
```

- QComboBox:组合选择框

```python
cbox.currentIdexChanged.connect(handleSelectionChange) # 选择了不同的 handleSelection
cbox.addItem('添加一个选项')
cbox.additems(['a', 'b', 'c'])
cbox.clear()
method = cvox.currentText() # 获取当前选中的文本
```

- QListWidget 列表控件

```python
listWidget.addItem("表格1")
listWidget.takeItem(1) # 删除第一行（从下标0开始）
listWidget.clear()
listWidget.currentItem().text() # 获取当前选中掉个对象的文本
```

- QTableWidget:表格控件, 表格单元中可以显示文本或者富文本图片等

QTableWidgetItem #表格中每个单元格类型

**表格控件通常用来从数据库中提取数据进行显示**

```python
table.insertRow(0)
table.insertRow(2)
table.removeRow(0)
table.removeRow(2)
table.setItem(row, 0, QTableWidgetItem("添加的单元格对象"))
table.item() # 返回单元格对象(QTableWidgetItem类型)
table.item(2, 4).setText('设置单元格文本')
item = QTableWidgetItem('不允许修改的单元格')
item.setFlags(Qt.ItemIsEnabled)	# 参数名字不允许修改
table.setItem(row, 0, item)
item.setTextAlignment(Qt.AlignCenter) # 单元格对齐
table.setItem(row, 0, item)
QTableWidget{ # 设置表格框以及单元格线的颜色, QML 格式
	border：1px solid green;
	gridline-color:rgb(71, 191, 255) 
}
table.item(0, 0).text()
rowcount = table.rowCount()
currentrow = table.currentRow() # 获取当前选中的是哪一行
table.setRowCount(10)
table.setColumnCount(10)
table.clearContents() # 清除表格中的内容
table.setRowCount(0) # 同时删除表格
table.setColumnWidth(0, 100)
table.horizontalHeader().setStretchLastSection(True) # 表格窗口的大小随着父窗口自动缩小
table.cellChanged.connect(cfgItemChanged) # 当某一个单元格变化时, 使用信号处理
def cfgItemChanged(row, col):
	cfgName = table.item(row, 0).text() # 首列为配置名称
	cfgValue = table.item(row, col).text()
# 表格控件的边界线颜色可以通过QSS属性gridline-color指定，
QTableWidget {
	gridline-color:green;
}
```

Web Browser : HTML + CSS + Java Script
Software : QML + QSS

- QRadioButton:单选按钮

```python
同一个父窗口里的多个单选按钮可以选中一项；
多组单选应该有不同的父控件或者layout；或者放到QButtonGroup中；
buttongroup.buttonClicked.connect(handleButtonClicked)
在该信号处理函数中调用:
buttongroup.checkedButton().text() # 获得选中的按钮的文本进而知道哪个按键被选中, check = 选中
```

- QCheckBox: 勾选按钮，可以多选，可以通过 exclusive 属性变成单选

```python
通常放到一个按钮组中
buttongroup.buttonClicked.connect(handleButtonClicked)
单选时，判断哪个被选中
buttongroup.checkedButton().text()
多选时，需要使用 isChecked() 方法
```

**tab 页控件：界面分成好几个页面**

**NOTE:**

**如果我们要在tab页上布局， 你可能会在对象查看器中直接右键点击该tab，可以你会发现 右键菜单里面没有布局项**

这是 Qt designer 非常坑爹的地方，我当时足足花了一个小时才找到方法。

1. 首先需要你在tab页上添加一个控件
2. 然后点击 在对象查看器 右键点击上层 TabWidget ，这时，你就会发现有布局菜单了


- QProgressBar:进度条

```python
progressBar.setRange(0, 5)
progressBar.setValue(3)
progressBar.reset()
progressBar.setRange(0, 0) # 显示忙碌状态
```

##### 信号的使用

界面显示放到主线程中，数据处理放到其它任务线程中，线程之间通过信号传递信息，否则跨线程直接操作界面很导致卡死等问题(UI线程阻塞等待其它线程执行到当然会导致卡死)；

```python
QSpinBox ：数字输入框
number = box.value()
box.setValue(100)
```

- QDateEdit:日期控件

```python
qdate = dateEdit.date()
dateStr = qdate.toString('yyyy-mm-dd') # 转成字符串
y = qdate.year()
m = qdate.month()
d = qdate.day()
```

- QFileDialog: 选择文件或者目录

```python
filePath = QFileDialog.getExistingDirectory(self.ui, "选择存储路径") # 选择目录：getExistingDirectory()是个静态方法，可以通过类直接调用
filePath, _ = QFileDialog.getOpenFileName(
    self.ui, 	# 父窗口对象
    "选择要上传的图片", # 标题
    r"d:\\data"		# 起始目录
    "图片类型（*.png *.jpg *.bmp)" # 选择过滤项
) # 选择文件，静态方法getOpenFileName（）返沪一个元组（文件路径, 文件类型）
filePath, _ = QFileDialog.getSaveFileName(
    self.ui, # 父串口对象
    "保存对象", # 标题
    r“d:\\\data”, # 起始目录
    "json类型(*.json)" # 选择类型过滤项, 过滤内容在括号中
)
filePaths, _ = QFileDialog.getOpenFileNames(
    self.ui,
    "选择要上传的图片"
    r"d:\\\data",
    "图片类型（*.png *.jpg *.bmp)"
) # 选择多个文件，返回值是 filePaths 一个列表
```

- QTreeWidget:树控件

QTreeWidgetItem:树节点控件



- QMessageBox:弹出框

```python
QMessageBox.critical( # 静态方法
    self.ui,
    '错误',
    '请选择爬取数据存储途径'
)
QMessageBox.warning(
    self.ui,
    '阅读太快',
    '阅读时长必须超过1分钟'
)
QMessageBox.infomation(
    self.ui,
    '操作成功',
    '继续下一步'
)
QMessageBox.about(
    self.ui,
    '操作成功',
    '继续下一步'
)
choice = QMessageBox.question( # 提示选择框， 是或者不是
    self.ui,
    '确认',
    '确认要删除文本吗?'
)
if choice == QMessageBox.Yes:
	print("选了Yes")
if choice == QMessageBox.No:
	print("选了No")
```

- QInputDialog:输入信息框

```python
title, okPressed = QInputDialog.getText( # 返回值分别是输入输入 和 是否点击了 OK 按钮（True / False）
    self,
    "输入目录名称",
    "名称"
    QLineEdit.Normal,
    ""
)
if not okPressed:
	print("你取消了输入")
QInputDialog.getMultiLineText()
QInputDialog.getInt()
QInputDialog.getIem()
items = ["A", 'B', 'C', 'D'] # 弹出对话框，让用户选择
item, ok = QInputDialog().getItem(self,
    "请选择",
    "季节",
    items,
    0, 
    False
)
if ok and not item.isEmpty():
	itemLabel.setText(item)
```



**菜单添加**

