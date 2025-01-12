TODO:
- airtest SubProcess.Popen 类学习, 实现了一个串口接收的类->发送到队列中
- python 拓展模块：
functiontools
warning 
metaclass


# 需求
- 官方文档:
https://airtest.doc.io.netease.com/en/IDEdocs/faq/2_common%20problems/
https://airtest.readthedocs.io/zh-cn/latest/README_MORE.html
https://poco-chinese.readthedocs.io/en/latest/source/doc/poco-example/index.html

- pyqt:
pyqt apps:
https://app.gumroad.com/l/pysqtsamples
https://blog.csdn.net/TianYanRen111/article/details/128713183
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMainWindow.html

- 代码架构:
OTA 升级工具代码模块:
GUI : Module
PROTO : Module
BT

- airtest log 文件夹会越来越大，越要定期清除

- 软件添加"帮助"选项，Q&A，
帮助文档直接写到资源文件中，指定格式，
代码中 readline() 判断每一行开头的第一个字符是否是“数字”+“.”，是的话这一行就是标题行，加粗；
1.手机输入法无法使用问题
Q:为什么我的电脑运行完该软件后手机上无法使用手动输入功能了?
A:手动启用系统自带输入法功能

- adb 获取蓝牙有关信息?
直接通过 adb 解绑系统蓝牙中已绑定设备，都不用 poco/airtest 判断？
有没有 adb 命令可以删除蓝牙配对记录?

- **升级完成后蓝牙设置里解绑**

- requirements.txt

- 需要将 adb 一起打包放到软件同级目录下

- 要时刻判断是否出现断联，如果出现就要左滑退出，然后重新进入；

- 支持手机热插拔

- 实时监测是否有手机插入/拔出
方案1:轮询？是否有新的手机插入/拔出？ adb devices 结果保存，然后对比差异？
方案2:通过检查计算机上的 usb 设备个数，能不能订阅 usb 断开之类的事件? 断开之后判断是哪个设备断开；

- 使用归一化坐标系, 尽量保证软件兼容不同手机
OTA 升级工具，通过 adb 命令获取每台手机的分辨率, 保存到本地类中，airtest swipe() 使用绝对坐标系, swipe() 最好不要使用图片，而是直接通过坐标变化的方式实现。每个手机类保存各自的分辨率，保证脚本兼容性；
SingleAirtest(){
   w = None;
   h = None;
}

- airtest report 功能利用起来, 保存日志
多线程/多进程同时操作多台设备时，poco airtest 的报告会冲突？是不是说明不能多线程操作？
需要考虑多进程

- 多线程/多进程同时写入 log 是否会冲突? 考虑将不同设备的 airtest log 保存到不同的目录中方便分析
(这里主要是异常时的手机截图)
每个进程保存的 log 目录 log/设备mac或者psn
升级成功后删除 airtest log 目录，否则会导致 log 过大。

- 界面上增加"检查版本号"选项, 
hint:“传输升级完成后检查手表版本号是否升级到指定版本” 选项，功能默认关闭
实现:界面上需要输入要升级到的版本号
传包完成后, 指定30 min定时器, 尝试连接设备获取版本号:"AT+SWV?", 然后进行判断

- OTA 升级工具锁定功能
输入指定的密码解锁后才可以操作，避免工人误操作。

- 软件 Title 不能固定，要按照当前项目名称切换。否则不同项目不好区分，每次都修改 .ui 文件麻烦。

- airtest monkey 自动测试升级以及测试结果上报（后话）
- 产线接入 MES 系统（后话）
- 本地数据库(保存设备升级信息)
- UI 自动测试工具:
全自动 UI 测试流程:
OTA + 冒烟测试 + jenknins

- python unittest
Poco是自动化测试框架，不负责单元测试部分。如果想要进行系统地管理你的测试或编写更高级的测试代码，
请参考我们的单元测试部分 PocoUnit. PocoUnit是一个提供了完善设施的专门为游戏和应用设计的单元测试框架，
用法与python标准库 unittest 完全兼容。
https://airtest.doc.io.netease.com/en/tutorial/4_Android_automated_testing_one/

- 另一测试工具:Uiautomator2
https://blog.csdn.net/m0_70618214/article/details/130130745

- adb 控制手机
https://blog.csdn.net/killsime/article/details/135280379