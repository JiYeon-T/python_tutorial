
# https://blog.csdn.net/bb8886/article/details/131940247
# https://blog.csdn.net/bb8886/article/details/131940247


# 1. 使用模块实现单例
# singleton 模块定义 singleton 对象,类似与全局遍历
class Singleton(object):
    def foo(self):
        pass

singleton = Singleton()

# 其他模块引用时:
def singleton_test1():
    # from mysingleton import singleton
    a = singleton
    b = singleton
    print(id(a), id(b))

# 2.通过装饰器实现:
def singleton_func(cls):
    """装饰器"""
    instance = {}
    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

@singleton_func
class Phone(object):
    NAME = "Phone"
    def phone_id(self):
        return id(self)

def singleton_test2():
    p1 = Phone()
    p2 = Phone()
    print(p1.phone_id(), p2.phone_id())
    print(p1.NAME, p2.NAME) # 不能有类变量??
    p1.NAME = "NAME"
    print(p1.NAME, p2.NAME) # 不能有类变量??

# 3.通过实例化方法实现
class SingletoneInstance(object):
    def __call__(self, *args, **kwargs):
        return self

def singletone_test3():
    single_object = SingletoneInstance() # 666
    a = single_object()
    b = single_object()
    print(id(a), id(b))

# 4.使用类装饰器实现单例
class SingletoneDecorator(object):
    _instance = None
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

@SingletoneDecorator
class Computer(object):
    def computer_id(self):
        return id(self)

def singleton_test4():
    c1 = Computer()
    c2 = Computer()
    print(c1.computer_id(), c2.computer_id())

# 5.重写 __new__ 方法实现单例
class SingletonClass(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # cls._instance = super(SingletonClass, cls).__new__(cls) # python2
            cls._instance = super().__new__(cls) # python 3.x

    _is_init = False
    def __init__(self):
        if self._is_init is False:
            self._is_init = True

def singleton_test5():
    c1 = SingletonClass()
    c2 = SingletonClass()
    print(id(c1), id(c2))


if __name__ == '__main__':
    # singleton_test1()
    singleton_test2()
    # singletone_test3()
    # singleton_test4()
    # singleton_test5()