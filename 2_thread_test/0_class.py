

def property_decorator_test1():
    """"""

    class Test(object):

        def __init__(self):
            self.a = 1
            self._b = 2
            # self.__c = 3  # private class member, 只能在类内部访问
            self.c = 3  # private class member, 只能在类内部访问

        @property
        def c(self):
            """property 装饰器"""
            return self.__c

        @c.setter
        def c(self, val):  # set 方法, 可以用 obj.set_c 调用该方法, 像调用属性一样
            self.c = val

        @c.deleter
        def c(self):  # obj.del_c
            """当执行del obj.value时，value.deleter方法会被调用，
            输出"Deleting the value"并删除内部的_value属性"""
            print("del __c attribute")
            del self.c

    t = Test()
    # print(t.a)
    # print(t._b)
    # print(t.__c) # AttributeError: 'Test' object has no attribute '__c'
    print("c={0}".format(t.c))
    del t.c
    print("c={0}".format(t.get_c))

# TODO:


if __name__ == '__main__':
    property_decorator_test1()