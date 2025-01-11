# import audio # import 包名.模块名

# 导入模块
# from audio import codec, decode, encode #from 包名 import 模块名1,模块名2,……,模块名n
from audio import *

# 直接导出包中的类/方法, 一个文件中可以导出多个类/方法的
# from audio.codec import Codec,Util, get_raw_data


def test1():
    cd = codec.Codec()
    util = codec.Util()
    codec.get_raw_data()

def test2():
    """直接导出包中的类/方法, 一个文件中可以导出多个类/方法的"""
    cd = Codec()
    util = Util()
    get_raw_data()

def test3():
    """定义了 __all__ 变量后, 使用 from module import * 导入模块后
     __all__ 中声明的变量会被导入, 没有声明的不会被导入
     但是使用直接导入模块的方法仍然可以导入 __all__ 中未声明的模块
     即 from audio import codec, decode, encode 仍然可以使用
     """
    cd = codec.Codec()
    util = codec.Util()
    codec.get_raw_data()

    decorder = decode.Decoder()
    decorder.print_time() # 对象的方法
    decode.decorder_test_fun() # 模块中开放的方法

    # dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
    # 返回的列表容纳了在一个模块里定义的所有模块，变量和函数。
    print(dir(codec)) # __name__ 模块名称, __file__ 导入文件名
    print(dir(codec))
    print(dir(codec))
    # globals() 和 locals() 函数
    # 根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
    # 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
    # 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
    # 两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。
    print("locals:", locals())
    print("globals:", globals())

    # 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
    #
    # 因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。
    # 该函数会重新导入之前导入过的模块。
    reload(codec)

if __name__ == '__main__':
    # codec = audio.Codec()
    # test1()
    # test2()
    test3()

# https://blog.csdn.net/Wei_sx/article/details/143461086
# https://www.runoob.com/python/python-modules.html