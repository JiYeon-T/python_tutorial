## python 基础篇

##### 1.python 运行日志——logging 模块

参考博客
https://www.cnblogs.com/yyds/p/6901864.html

```
# 几乎所有开发语言都会内置日志相关功能，或者会有比较优秀的第三方库来提供日志操作功能，比如：log4j（log for java），log4php(log for php), 等。
# 它们功能强大、使用简单。Python自身也提供了一个用于记录日志的标准库模块--logging。
# 当为某个应用程序指定一个日志级别后，应用程序会记录所有日志级别大于或等于指定日志级别的日志信息，
# 而不是仅仅记录指定级别的日志信息，nginx、php等应用程序以及这里要提高的python的logging模块都是这样的。
```

Logger(记录器) + Handler(处理器) + Filter(过滤器) + Formatter(格式化器)

- logging模块四大组件:Logger, Handler, Formatter, Filter

日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络(服务器数据实时可视化？)等；
不同的处理器（handler）可以将日志输出到不同的位置；
日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。

（1）logger 记录器

Logger是一个树形层级结构，在使用接口debug，info，warn，error，critical之前必须创建Logger实例，即创建一个记录器，如果没有显式的进行创建，则默认创建一个**root logger**，并应用默认的日志级别(WARN)，处理器Handler(StreamHandler，即将日志信息打印输出在标准输出上)，和格式化器Formatter(默认的格式即为第一个简单使用程序中输出的格式)。

```python
logger = logging.getLogger(logger_name)
```

创建 logger 实例后，可以使用以下方法进行日志级别设置，增加处理器Handler 等操作；

Handler 处理器类型有很多种：StreamHandler, FileHandler, NullHandler

```
logger.setLevel(logging.ERROR)
logger.addHandler(handler_name) # 增加处理器
logger.removeHandler(handler_name) # 删除处理器
# streamHandler
sh = logging.StreamHandler(stream=None)
fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)
```

格式化器

```python
formatter = logging.Formatter(fmt=None, datefmt=None)
```

过滤器

Handlers和Loggers可以使用Filters来完成比级别更复杂的过滤。Filter基类只允许特定Logger层次以下的事件。例如用‘A.B’初始化的Filter允许Logger ‘A.B’, ‘A.B.C’, ‘A.B.C.D’, ‘A.B.D’等记录的事件，logger‘A.BB’, ‘B.A.B’ 等就不行。 如果用空字符串来初始化，所有的事件都接受。**着什么意思？？？**

```python
filter = logging.Filter(name='')
```

logging 模块的配置方法：

自定义配置(可选)。logging标准模块支持三种配置方式: dictConfig，fileConfig，listen。其中，dictConfig是通过一个字典进行配置Logger（logging.basicConfig()），Handler，Filter，Formatter；fileConfig则是通过一个文件进行配置(logging.fileConfig())；而listen则监听一个网络端口，通过接收网络数据来进行配置。当然，除了以上集体化配置外，也可以直接调用Logger，Handler等对象中的方法在代码中来显式配置（创建Logger并进行配置）。

logging.basicConfig()可选参数：

| filename | 创建一个FileHandler, 使用指定的文件名，而不是使用 StreamHandler |
| -------- | ---------------------------------------- |
| filemode | 如果指明了文件名，指出文件打开模式，没有指明则使用filemode        |
| format   | handler 使用指明的格式化字符串                      |
| datefmt  | 日期/时间格式                                  |
| level    | 指明 root logger 的级别                       |
| stream   | 使用指定的流初始化 StreamHandler, **与参数 filename 不兼容** |

```python
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
LOG_FILENAME = "log_test.log"
logging.basicConfig(filename="abc.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
```

logging 输出格式有关的关键字：

| 字段/属性名称         | 使用格式                | 描述                                       |
| --------------- | ------------------- | ---------------------------------------- |
| asctime         | %(asctime)s         | 日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896 |
| created         | %(created)f         | 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值   |
| relativeCreated | %(relativeCreated)d | 日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的） |
| msecs           | %(msecs)d           | 日志事件发生事件的毫秒部分                            |
| levelname       | %(levelname)s       | 该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'） |
| levelno         | %(levelno)s         | 该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）      |
| name            | %(name)s            | 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger  |
| message         | %(message)s         | 日志记录的文本内容，通过 `msg % args`计算得到的           |
| pathname        | %(pathname)s        | 调用日志记录函数的源码文件的全路径                        |
| filename        | %(filename)s        | pathname的文件名部分，包含文件后缀                    |
| module          | %(module)s          | filename的名称部分，不包含后缀                      |
| lineno          | %(lineno)d          | 调用日志记录函数的源代码所在的行号                        |
| funcName        | %(funcName)s        | 调用日志记录函数的函数名                             |
| process         | %(process)d         | 进程ID                                     |
| processName     | %(processName)s     | 进程名称，Python 3.1新增                        |
| thread          | %(thread)d          | 线程ID                                     |
| threadName      | %(threadName)s      | 线程名称                                     |

- 不同文件之间如何共享 logging(多个文件共用logging 模块时重复打印问题解决)

**NOTE:不要对所有模块都是用 root logger, 这回导致重复打印**

eg:

my_project_module.py

```python
import logging
logging.basicConfig(filename='my_projet_module.log') # root logger 只可以有一个
```

main.py

```python
import logging
import myprojectmodule # 运行 my)project_module.py 中的代码, 将生成 'stream_package.log' 文件
logging.basicConfig(filename='mian.log') # 无效
```

**如果想在不同的文件中使用不同的 logger, 就需要创建一个新的 logger**

```python
(1)可以使用 logger.getLogger(name) 创建一个新的logger, 如果这个名字已经存在，则不创建新的 Logger ,继续使用
```



##### 2. 字典类型与元组类型 python 函数形参的使用 

##### 3.python 中如何传递引用
如果传入的 tuple 或者 list, 则默认传递的就是引用, 如果想传递拷贝, 则要使用



##### 4.类的特殊成员以及魔法方法(magic method)

类的私有成员

具有特殊函数的成员函数: doc

```python
__doc__	#打印类的描述信息
__call__	# 重载 () 运算符, 魔法方法
# 注：构造方法 __init__ 的执行是由创建对象触发的，即：对象 = 类名() ；
# 而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
__dict__	# 类或者对象中的所有成员
__str__	# 要打印的内容，使用 print 打印对象时, 会调用这个方法
__getitem__ # arr[ix] 
__setitem__ # arr[ix] = val
__add__
__sub__
```

**类的普通字段属于对象；类中的静态字段和方法等属于类**

字段，方法，属性（公有成员， 私有成员）

（1）成员

公有成员，在任何地方都能访问

私有成员，只有在类的内部才能方法，私有成员命名时，前两个字符是下划线。

（2）字段

公有静态字段：类可以访问；类内部可以访问；派生类中可以访问

私有静态字段：仅类内部可以访问；（**派生类无法从父类继承私有字段**）

（3）方法



@staticmethod

staticmethod用于修饰类中的方法,使其可以在不创建类实例的情况下调用方法，这样做的好处是执行效率比较高。

```python
class A:
    @staticmethod
    def print_something():
        print("This is a test @staticmethod")
A.print_something() # 不创建对象, 可以直接使用类来调用的方法
```