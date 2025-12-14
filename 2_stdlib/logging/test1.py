#
# ##### 1.python 运行日志——logging 模块
#
# 参考博客
# https://www.cnblogs.com/yyds/p/6901864.html
#
# ```
# # 几乎所有开发语言都会内置日志相关功能，或者会有比较优秀的第三方库来提供日志操作功能，比如：log4j（log for java），log4php(log for php), 等。
# # 它们功能强大、使用简单。Python自身也提供了一个用于记录日志的标准库模块--logging。
# # 当为某个应用程序指定一个日志级别后，应用程序会记录所有日志级别大于或等于指定日志级别的日志信息，
# # 而不是仅仅记录指定级别的日志信息，nginx、php等应用程序以及这里要提高的python的logging模块都是这样的。
# ```
#
# Logger(记录器) + Handler(处理器) + Filter(过滤器) + Formatter(格式化器)
#
# - logging模块四大组件:Logger, Handler, Formatter, Filter
#
# 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络(服务器数据实时可视化？)等；
# 不同的处理器（handler）可以将日志输出到不同的位置；
# 日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
# 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
# 每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。
#
# （1）logger 记录器
#
# Logger是一个树形层级结构，在使用接口debug，info，warn，error，critical之前必须创建Logger实例，即创建一个记录器，如果没有显式的进行创建，则默认创建一个**root logger**，并应用默认的日志级别(WARN)，处理器Handler(StreamHandler，即将日志信息打印输出在标准输出上)，和格式化器Formatter(默认的格式即为第一个简单使用程序中输出的格式)。
#
# ```python
# logger = logging.getLogger(logger_name)
# ```
#
# 创建 logger 实例后，可以使用以下方法进行日志级别设置，增加处理器Handler 等操作；
#
# Handler 处理器类型有很多种：StreamHandler, FileHandler, NullHandler
#
# ```
# logger.setLevel(logging.ERROR)
# logger.addHandler(handler_name) # 增加处理器
# logger.removeHandler(handler_name) # 删除处理器
# # streamHandler
# sh = logging.StreamHandler(stream=None)
# fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)
# ```
#
# 格式化器
#
# ```python
# formatter = logging.Formatter(fmt=None, datefmt=None)
# ```
#
# 过滤器
#
# Handlers和Loggers可以使用Filters来完成比级别更复杂的过滤。Filter基类只允许特定Logger层次以下的事件。例如用‘A.B’初始化的Filter允许Logger ‘A.B’, ‘A.B.C’, ‘A.B.C.D’, ‘A.B.D’等记录的事件，logger‘A.BB’, ‘B.A.B’ 等就不行。 如果用空字符串来初始化，所有的事件都接受。**着什么意思？？？**
#
# ```python
# filter = logging.Filter(name='')
# ```
#
# logging 模块的配置方法：
#
# 自定义配置(可选)。logging标准模块支持三种配置方式: dictConfig，fileConfig，listen。其中，dictConfig是通过一个字典进行配置Logger（logging.basicConfig()），Handler，Filter，Formatter；fileConfig则是通过一个文件进行配置(logging.fileConfig())；而listen则监听一个网络端口，通过接收网络数据来进行配置。当然，除了以上集体化配置外，也可以直接调用Logger，Handler等对象中的方法在代码中来显式配置（创建Logger并进行配置）。
#
# logging.basicConfig()可选参数：
#
# | filename | 创建一个FileHandler, 使用指定的文件名，而不是使用 StreamHandler |
# | -------- | ---------------------------------------- |
# | filemode | 如果指明了文件名，指出文件打开模式，没有指明则使用filemode        |
# | format   | handler 使用指明的格式化字符串                      |
# | datefmt  | 日期/时间格式                                  |
# | level    | 指明 root logger 的级别                       |
# | stream   | 使用指定的流初始化 StreamHandler, **与参数 filename 不兼容** |
#
# ```python
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# LOG_FILENAME = "log_test.log"
# logging.basicConfig(filename="abc.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# ```
#
# logging 输出格式有关的关键字：
#
# | 字段/属性名称         | 使用格式                | 描述                                       |
# | --------------- | ------------------- | ---------------------------------------- |
# | asctime         | %(asctime)s         | 日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896 |
# | created         | %(created)f         | 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值   |
# | relativeCreated | %(relativeCreated)d | 日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的） |
# | msecs           | %(msecs)d           | 日志事件发生事件的毫秒部分                            |
# | levelname       | %(levelname)s       | 该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'） |
# | levelno         | %(levelno)s         | 该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）      |
# | name            | %(name)s            | 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger  |
# | message         | %(message)s         | 日志记录的文本内容，通过 `msg % args`计算得到的           |
# | pathname        | %(pathname)s        | 调用日志记录函数的源码文件的全路径                        |
# | filename        | %(filename)s        | pathname的文件名部分，包含文件后缀                    |
# | module          | %(module)s          | filename的名称部分，不包含后缀                      |
# | lineno          | %(lineno)d          | 调用日志记录函数的源代码所在的行号                        |
# | funcName        | %(funcName)s        | 调用日志记录函数的函数名                             |
# | process         | %(process)d         | 进程ID                                     |
# | processName     | %(processName)s     | 进程名称，Python 3.1新增                        |
# | thread          | %(thread)d          | 线程ID                                     |
# | threadName      | %(threadName)s      | 线程名称                                     |
#
# - 不同文件之间如何共享 logging(多个文件共用logging 模块时重复打印问题解决)
#
# **NOTE:不要对所有模块都是用 root logger, 这回导致重复打印**
#
# eg:
#
# my_project_module.py
#
# ```python
# import logging
# logging.basicConfig(filename='my_projet_module.log') # root logger 只可以有一个
# ```
#
# main.py
#
# ```python
# import logging
# import myprojectmodule # 运行 my)project_module.py 中的代码, 将生成 'package_test.log' 文件
# logging.basicConfig(filename='mian.log') # 无效
# ```
#
# **如果想在不同的文件中使用不同的 logger, 就需要创建一个新的 logger**
#
# ```python
# (1)可以使用 logger.getLogger(name) 创建一个新的logger, 如果这个名字已经存在，则不创建新的 Logger ,继续使用
# ```
#




import logging

# create Logger
logger_name = "test_logger_1"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create Handler
log_path = "log_test.log"
# fh = logging.FileHandler(log_path)
fh = logging.StreamHandler()
fh.setLevel(logging.DEBUG) # 低于 INFO 的 log 不处理

# create Formatter
# fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
fmt = "%(asctime)-15s %(levelname)s [%(thread)d|%(threadName)s] %(message)s"
# datefmt = "%a %d %b %Y %H:%M:%S"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add Handler and Formatter to Logger
fh.setFormatter(formatter)
logger.addHandler(fh)


def logger_example1():
    # import 一个模块的时候, 模块外面的这些代码是会被执行的.
    logger.debug("test1 debug log")
    logger.info("test1 info log")
    logger.warning("test1 warning log")
    logger.error("test1 error log")
    logger.critical("test1 critical log")


if __name__ == '__main__':
    logger_example1()
