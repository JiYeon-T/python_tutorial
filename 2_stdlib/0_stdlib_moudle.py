


def python_stdlib_test():
    """Python3 标准库概览
    以上我们看到的只是 Python3 标准库中的一部分模块，
    还有很多其他模块可以在官方文档中查看完整的标准库文档：
    https://docs.python.org/zh-cn/3/library/index.html
    标准模块
    Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
    模块名	功能描述
    math	数学运算（如平方根、三角函数等）
    os	操作系统相关功能（如文件、目录操作）
    sys	系统相关的参数和函数
    random	生成随机数
    datetime	处理日期和时间
    json	处理 JSON 数据
    re	正则表达式操作
    collections	提供额外的数据结构（如 defaultdict、deque）
    itertools	提供迭代器工具
    functools	高阶函数工具（如 reduce、lru_cache）
    """
    import sys # sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。
    import os # os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
    import time # time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。
    import datetime # datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等
    import random # random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。
    import math # math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。
    import re # re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。
    import json # json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。
    import urllib # urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。
    import shutil # 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
    import glob # glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表
    from urllib.request import urlopen # 理从 urls 接收的数据的 urllib.request
    import smtplib #发送电子邮件的 smtplib
    import zlib # 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
    from timeit import Timer # timeit事件度量库
    import pstats # pstats 模块提供了针对更大代码块的时间度量工具。
    import doctest
    import unittest

    # import sys # 系统相关模块
    # sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，
    # 以及与 stdin、stdout 和 stderr 相关的信息。
    print(sys.argv) # 是一个 list,包含所有的命令行参数.
    print(repr(sys.stdout)) # 分别表示标准输入输出,错误输出的文件对象.
    print(repr(sys.stdin))
    print(repr(sys.stderr))
    # print(sys.stdin.readline()) # 从标准输入读一行
    sys.stdout.write("a\n")
    # sys.exit(-1) # 退出程序(大多脚本的定向终止都使用 sys.exit())
    print("available moudls", sys.modules) # 是一个dictionary，表示系统中所有可用的module
    print(sys.platform) # 得到运行的操作系统环境
    print(sys.path) # sys.path 是一个list,指明所有查找module，package的路径

    # import os # 操作系统相关的调用和操作
    # os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
    print("environ", os.environ) # 一个 dictionary 包含环境变量的映射关系
    print("environment PATH", os.environ["PATH"]) # 可以得到环境变量HOME的值
    directory = "."
    os.chdir(directory) # 改变当前目录 os.chdir('d:\\outlook') 注意windows下用到转义
    print("current working directory", os.getcwd()) # 得到当前目录
    # print("egid:{} gid:".format(os.getegid(), os.getgid())) # 得到有效组id/组 id
    # print("euid:{} uid:{}".format(os.geteuid(), os.getuid())) # 得到用户/有效用户id
    # print("groups:", os.getgroups()) # 得到用户组名称列表
    print("login:", os.getlogin()) # 到用户登录名称
    print("env path:",os.getenv("PATH")) # 得到环境变量
    # os.putenv("") # 设置环境变量
    # print("umask", os.umask()) # 设置umask(Set the current numeric umask and return the previous umask)
    # os.system("dir") # 利用系统调用，运行cmd命令
    print("dirs:", os.listdir())

    # 内置模块(不用import就可以直接使用)常用内置函数：
    # help(object) # 在线帮助, obj可是任何类型
    print("callable:", callable(object)) # 查看一个obj是不是可以像函数一样调用
    # print(repr(object)) # 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝

    # shutil
    # shutil.copy("foo.txt", 'archive.db')
    # shutil.move('foo.txt', 'foo2.txt')

    # glob
    print(glob.glob('*.py'))

    # re
    # 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
    re.findall(r'\bf[a-z]*', 'which foot or hand fell fasttest')

    print("supported functions:", dir(math)) # 打印模块里定义过得名字
    # math 模块为浮点运算提供了对底层 C 函数库的访问:
    print("PI:",math.pi)
    print("sample:", random.sample(range(100), 10))

    # 有几个模块用于访问互联网以及处理网络通信协议。
    # 其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及
    # 用于发送电子邮件的 smtplib:
    # for line in urlopen("https://www.baidu.com"):
    #     line = line.decode('utf-8') # # Decoding the binary data to text.
    #     if 'EST' in line or 'EDT' in line: # look for Eastern Time
    #         print(line)
    #     print("url recv:", line)

    # 需要本地有一个在运行的邮件服务器。
    # server = smtplib.SMTP('localhost')
    # server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    #                 """To: jcaesar@example.org
    #                 From: soothsayer@example.org
    #
    #                 Beware the Ides of March.
    #                 """)

    # datetime:
    print(datetime.datetime.now())
    print(type(datetime.datetime.today()))
    now = datetime.datetime.today()
    print(now.strftime("%Y-%m-%d %H:%M:%S")) # 格式化日期
    birthday = datetime.date(1998, 2, 15) # 该模块还支持时区处理
    # now = datetime.date()
    print("now:", repr(now))
    print("%d-%d-%d" % (now.year, now.month, now.day))
    # now = datetime.date(datetime.date.year, month=datetime.date.month, day=datetime.date.day)
    today = datetime.date(now.year, month=now.month, day=now.day)
    diff = today - birthday
    print("lived days:", diff.days, diff) # 返回天数
    today = datetime.date.today() # 今天
    timestamp = time.time() # 当前时间戳
    print("today", today)
    yesterday = today - datetime.timedelta(days=1) # 昨天
    print("yesterday", yesterday)
    last_month = today.month - 1 if today.month - 1 else 12
    print("last_month:", last_month) # 上个月时间戳
    print("timestamp:", timestamp)
    print("date:", datetime.datetime.fromtimestamp(timestamp)) # 时间戳转datetime
    print("timestamp:", time.mktime(today.timetuple())) # datetime转时间戳
    today_str = today.strftime("%Y-%m-%d") # datetime转字符串
    print("today str:", today_str)
    today = datetime.datetime.strptime(today_str, "%Y-%m-%d") # 字符串转datetime
    print("东八区:", today + datetime.timedelta(hours=8)) # 补时差

    s = b'witch whish has which witches wrist watch 111111111111111111111111111111111111'
    print("len:", len(s))
    print("checksum:", zlib.crc32(s)) # CRC-32 checksum of data.
    pressed = zlib.compress(s)
    print("compressed size:", len(pressed))
    decompressed = zlib.decompress(pressed)
    print("decompress:", decompressed)
    print("checksum:", zlib.crc32(decompressed))

    # timeit(python 内置模块, 无需单独安装)
    # timeit 模块用于测试一小段代码的执行时间, 可以用于测试性能问题
    # TODO: 其他性能测试模块 pstats 和 cProfile
    list_stmt = "[x for x in range(1000)]" # 测试代码
    generator_stmt = "(x for x in range(1000))"
    setup = "pass" # 没有额外的初始化代码
    number = 10000 # 代码要重复执行的次数
    list_execution_time = timeit.timeit(list_stmt, setup, number=number)
    print('execution_time: %f seconds' % list_execution_time)
    # repeat() 方法会返回一个列表，其中包含多次测量的结果，以便更好地评估代码性能。其基本语法为：
    generator_execution_time = timeit.repeat(list_stmt, setup, repeat=3, number=number)
    print('execution_time: {} seconds'.format(generator_execution_time))

    # 测试模块
    # doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
    # https://docs.python.org/zh-cn/3.12/library/doctest.html
    # C++ doctest:
    # https://blog.csdn.net/liao20081228/article/details/76984975
    def average(value):
        """
        Computes the arithmetic mean of a list of numbers.
        >>> print(average([x for x in range(10000)]))
        40.0
        """
        return sum(value) / len(value)
    # doctest.testmod() # # 自动验证嵌入测试
    average([x for x in range(10000)])
    # unittest
    # unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
    class TestStatisticalFunctions(unittest.TestCase):
        """测试用例"""
        def test_average(self):
            self.assertEqual(average([20, 30, 70]), 40.0)
            self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
            self.assertRaises(ZeroDivisionError, average, [])
            self.assertRaises(TypeError, average, 20, 30, 70)
    # TestStatisticalFunctions()
    # unittest.main()

if __name__ == '__main':
    python_stdlib_test()