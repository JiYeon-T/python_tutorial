This is a pyqt5 study nodebook.



##### 常见控件

##### pyqt
###### 控件
QPushButton:
button.connect(handleCalc) # 信号 -> 槽函数
button.setText(text) # 改变文本eg:按下变成成停止, 而不是一直是停止
button.setEnabled(False)
button.setEnabled(True) # 继承自 QWidget
button.setIcon(QIcon('logo.png'))
button.setIconSize(QSize(30, 30))



QLineEdit：只能单行编辑的文本框
edit.textChanged.connect(handleTextChange)
passwordEdit.returnPressed.connect(onLogin) # 回车按下
text = edit.text()
edit.setPlaceHolderText('请输入名字')
edit.setText('你好')
edit.clear()
edit.copy()
edit.paste()



QPlainTextEdit:多行纯文本编辑框
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



QTextBrowser # 文本浏览框，只能浏览文本（通常用来显示log日志， 或者不需要用户编辑的大段内容）
获取文本, 设置文本, 清除文本, 剪切复制等等
textBrowser.append('hello, world')
textBrowser.ensureCursorVisable() # 使得新添加的文本在最当前的位置, 自动添加换行
textBrowser.insertPlainText('光标处插入文本')



QLabel:标签 可以用来显示文本,图片, 动画等
label.setText()
QLabel 的 pixmap 属性设置中选择图片文件指定既可以使用 label 显示图片
label.setPicture()
label.setPixelMap()

QComboBox:组合选择框
cbox.currentIdexChanged.connect(handleSelectionChange) # 选择了不同的 handleSelection
cbox.addItem('添加一个选项')
cbox.additems(['a', 'b', 'c'])
cbox.clear()
method = cvox.currentText() # 获取当前选中的文本



QListWidget 列表控件

listWidget.addItem("表格1")

listWidget.takeItem(1) # 删除第一行（从下标0开始）

listWidget.clear()

listWidget.currentItem().text() # 获取当前选中掉个对象的文本



QTableWidget:表格控件, 表格单元中可以显示文本或者富文本图片等

QTableWidgetItem #表格中每个单元格类型

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

QTableWidget{ # 设置表格框以及单元格线的颜色

​	border：1px solid green;

​	gridline-color:rgb(71, 191, 255) 

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





