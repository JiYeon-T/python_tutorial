import sys  # 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法
from math import asin  # from … import 语句, Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中
import threading as th  # 给模块起别名 使用 as 关键字为模块或函数起别名：
from os import * # from … import *  # 把一个模块的所有内容全都导入到当前的命名空间也是可行的,
# "不推荐，容易引起命名冲突。"

# 如果路径问题是在无法解决，可以通过添加搜索路径的方式, 但是并不推荐
# sys.path.append("D:\\test")
# import test

# 模块的搜索路径
# 当导入一个模块时，Python 会按照以下顺序查找模块：
# 1.当前目录。
# 2.环境变量 PYTHONPATH 指定的目录。
# 3.Python 标准库目录。
# 4. .py 文件中指定的目录。

# https://www.runoob.com/python3/python3-module.html

def module_base_test():
    """python 模块(单个的 .py 文件)"""
    def print_path():
        for i, v in enumerate(sys.path):
            print(f"[{i}]:{v}")
    # print_path()

    # 一个模块被另一个程序第一次引入时，其主程序将运行。
    # 如果我们想在模块被引入时，模块中的某一程序块不执行，
    # 我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
    #  每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
    # 说明：__name__ 与 __main__ 底下是双下划线

    # 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
    # print(dir(sys))
    # print(sys.ps1) # 变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:
    # print(sys.ps2)

    # 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，
    # 主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
    # __path__ # 这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦
    # __all__ # 包中的所有的模块名需要写在里面

    # __name__ 属性
    # 一个模块被另一个程序第一次引入时，其主程序将运行。
    # 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行。
    # 说明：每个模块都有一个 __name__ 属性。
    # 如果模块是被直接运行，__name__ 的值为 __main__。
    # 如果模块是被导入的，__name__ 的值为模块名。

    # dir() 函数
    # 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
    def module_test2():
        # from test_module import moudle_import_test
        import test_module
        # moudle_import_test()
        print(dir(test_module))
    module_test2()

def package_base_test():
    """包测试
    目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，
    主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
    最简单的情况，放一个空的 :file:__init__.py就可以了。
    当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。

    通常我们并不主张使用 * 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。
    不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。
    记住，使用 from Package import specific_submodule 这种方法永远不会有错。
    事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。
    """
    from stream_package.audio import codec, decode, encode
    from stream_package.video import mp4, wav
    def test1():
        c = encode.Encoder()
    test1()

if __name__ == '__main__':
    # module_base_test()
    package_base_test()