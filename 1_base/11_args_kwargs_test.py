import os, sys

# python 中元组 以及 字典类型的变量如何作为形参以及实参使用

def fun(time, *args, **kwargs):
    print(time)
    print(args)
    # 那么 args 怎么访问呢?
    print(kwargs)
    a = kwargs.pop('a', False) # 通过这种方式来访问可变参数的字典类型
    if a:
        print("a=", a)
    # print(kwargs["a"])
    print("")

def test():
    fun(1)
    fun(1, 2, 3 )   # 传入元组类型
    fun(1, a=1, b=2)    # 传入字典类型

if __name__ == '__main__':
    test()