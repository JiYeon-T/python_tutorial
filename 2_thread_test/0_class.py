class Test(object):
    classVarible = 0

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3 # private class member, 只能在类内部访问

    @property
    def get_c(self):
        """property 装饰器"""
        return self.__c

    @get_c.setter
    def set_c(self, val):
        self.__c = val

    @get_c.deleter
    def del_c(self):
        del self.__c

t = Test()
print(t.classVarible)
print(t.a)
print(t._b)
# print(t.__c) # AttributeError: 'Test' object has no attribute '__c'
print("c={0}".format(t.get_c))


if __name__ == '__main__':
    pass