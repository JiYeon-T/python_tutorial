class Test():
    classVarible = 0

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3 # private class member



t = Test()
print(t.classVarible)
print(t.a)
print(t._b)
# print(t.__c) # AttributeError: 'Test' object has no attribute '__c'



if __name__ == '__main__':
    pass