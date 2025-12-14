import time
# https://www.runoob.com/python3/python-decorators.html


def decorator_base_test():
    """
    Python 装饰器
    装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。
    装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。
    装饰器的语法使用 @decorator_name 来应用在函数或方法上。
    Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。
    装饰器的应用场景：
    日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
    性能分析: 可以使用装饰器来测量函数的执行时间。
    权限控制: 装饰器可用于限制对某些函数的访问权限。
    缓存: 装饰器可用于实现函数结果的缓存，以提高性能。
    语法
    def decorator_function(original_function):
        def wrapper(*args, **kwargs):
            # 这里是在调用原始函数前添加的新功能
            before_call_code()

            result = original_function(*args, **kwargs)

            # 这里是在调用原始函数后添加的新功能
            after_call_code()

            return result
        return wrapper

    # 使用装饰器
    @decorator_function
    def target_function(arg1, arg2):
        pass  # 原始函数的实现
    # 装饰器也可以带参数:
    # 类装饰器
    """
    def time_logger(origin_fun):
        """装饰器
        decorator 是一个装饰器函数，它接受一个函数 func 作为参数，并返回一个内部函数 wrapper，
        在 wrapper 函数内部，你可以执行一些额外的操作，然后调用原始函数 func，并返回其结果。
        :decorator_function 是装饰器，它接收一个函数 original_function 作为参数。
        :wrapper 是内部函数，它是实际会被调用的新函数，它包裹了原始函数的调用，并在其前后增加了额外的行为。
        当我们使用 @decorator_function 前缀在 target_function 定义前，
        Python会自动将 target_function 作为参数传递给 decorator_function，
        然后将返回的 wrapper 函数替换掉原来的 target_function。
        """
        def wrapper(*args, **kwargs):
            """wrapper 是内部函数，它是实际会被调用的新函数，它包裹了原始函数的调用，并在其前后增加了额外的行为。"""
            start = time.time()
            result = origin_fun(*args, **kwargs)
            end = time.time()
            print(f"time usage:{end -start} sec")
            return result
        return wrapper

    @time_logger
    def print_hello(n):
        for i in range(n):
            print("hello %d" % i)

    def decorator_test1():
        print(print_hello(3))
    # decorator_test1()

    def repeat(n):
        """带参数的装饰器 repeat """
        def decrator(original_fun):
            def wrapper(*args, **kwargs):
                result = None
                for _ in range(n):
                    print(f"This is {_ + 1} time:", end=":")
                    result = original_fun(*args, **kwargs)
                return result
            return wrapper
        return decrator

    @repeat(5)
    def greet(name):
        print(f"Hello {name}")

    def decorator_test2():
        greet("Bob")
    # decorator_test2()

    # TODO:也可以同时使用多个装饰器, 但是为什么不生效??
    # 多个装饰器的堆叠
    @time_logger
    @repeat(5)
    def hello(name):
        print(f"Hello {name}")
        time.sleep(0.1)

    def decorator_test3():
        greet("Alan")
    # decorator_test3()

    # 除了函数装饰器，Python 还支持类装饰器。
    # 类装饰器（Class Decorator）是一种用于动态修改类行为的装饰器，它接收一个类作为参数，并返回一个新的类或修改后的类。
    # 类装饰器可以用于：
    # 添加/修改类的方法或属性
    # 拦截实例化过程
    # 实现单例模式、日志记录、权限检查等功能
    # 类装饰器有两种常见形式：
    # 1.函数形式的类装饰器（接收类作为参数，返回新类）
    # 2.类形式的类装饰器（实现 __call__ 方法，使其可调用）
    class DecratorClass(object):
        """类装饰器"""
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            # 在调用原始函数之前/之后执行的代码
            print("Before")
            result = self.func(*args, **kwargs)
            # 在调用原始函数之后执行的代码
            print("After")
            return result

    @DecratorClass
    def my_function():
        print("Decrator class test")
    # my_function()

    # 内置装饰器
    # Python 提供了一些内置的装饰器，例如：
    # @staticmethod: 将方法定义为静态方法，不需要实例化类即可调用。
    # @classmethod: 将方法定义为类方法，第一个参数是类本身（通常命名为 cls）。
    # @property: 将方法转换为属性，使其可以像属性一样访问。
    class MyClass:

        def __init__(self, name=None):
            self.__name = name

        @staticmethod
        def static_method():
            print("This is a static method")

        @classmethod
        def class_method(cls, text=None):
            print(f"This is a class method {text}")

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, new_name):
            self.__name = new_name

        @name.getter
        def name(self):
            return self.__name

    def decorator_test4():
        MyClass.static_method()
        MyClass.class_method()

        c = MyClass()
        c.name = 'Alice'
        print(f"name:{c.name}")  # 可以向属性一样调用类的方法
    # decorator_test4()

    # 多个装饰器的堆叠，当有多个装饰器时可以堆叠使用
    # TODO:


def property_test():
    """
    @property 测试
    属性访问器的作用是为了数据安全,
    定义后，属性的访问方式由 obj.setx() -> obj.x = val
    obj.getx() -> obj.x
    obj.delx() -> del obj.x
    roperty是标准库提供的一个类，一个property实例映射一个普通类属性，
    我们可以在创建property时指定其对应属性的各种访问器，以下是官方例子的一个改版
    """
    class PropertyTest:

        # def __init__(self, x=None):
        #     self.__x = x

        def getx(self):
            """获取器"""
            print(f"invoke getter method")
            return self.__x

        def setx(self, val):
            """设置器"""
            print(f"invoke setter method")
            if val < 0:
                raise ValueError(f"必须大于0 {val}")
            self.__x = val

        def delx(self):
            """删除器"""
            print(f"invoke delete method")
            del self.__x

        # 创建 property 实例:
        x = property(fget=getx, fset=setx, fdel=delx, doc='I am x property')

    c = PropertyTest()
    c.x = 12
    print(f'x = {c.x}')
    del c.x

def decorator_property_test():
    """
    @property 装饰器
    """

    class PropertyTest(object):

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, val):
            print("invoke setter method")
            self.__x = val

        @x.getter
        def x(self):
            print("invoke getter method")
            return self.__x

        @x.deleter
        def x(self):
            print("invoke delete method")
            del self.__x

    c = PropertyTest()
    c.x = 123
    print(f'x = {c.x}')
    del c.x


def property_test2():
    """ 使用自己实现的 property """

    class MyProperty(object):
        """自己实现一个 property 类??"""
        def __init__(self, fget=None, fset=None, fdel=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel

        def __get__(self, instance, owner):
            return self.fget(instance)

        def __set__(self, instance, value):
            self.fset(instance, value)

        def __delete__(self, instance):
            self.fdel(instance)

    class C(object):

        def getx(self):
            print(f"invoke getter method")
            return self.x

        def setx(self, value):
            print(f"invoke setter method")
            self.x = value

        def delx(self):
            print(f"invoke delete method")
            del self.x

        x = MyProperty(fget=getx, fset=setx, fdel=delx)

    # TODO: 这个测试用例一直失败, 循环打印 setter
    c = C()
    c.x = 1
    print(f"x={c.x}")
    del c.x

if __name__ == '__main__':
    # decorator_base_test()
    # property_test()
    # property_test2()  # TODO:
    decorator_property_test()