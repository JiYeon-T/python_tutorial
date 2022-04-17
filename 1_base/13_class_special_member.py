import os

# python 中类成员以及成员修饰符 -> 字段，方法，属性
class Sutdent:
    """ 一个测试的学生类 """
    country = 'China'
    def __init__(self, ID=0, name="Null", grade=0):
        self.ID = ID
        self.name = name
        self.grade = grade

    def __call__(self, *args, **kwargs):
        """ 重载 () """
        return (self.ID, self.name, self.grade)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    # def __dict__(self):
    #     """ 类或者对象中的所有成员 """

    # def __str__(self):
    #     """ print 对象时会调用这个方法 """
    #     pass

class Teacher:
    __age_level = 'old'
    country = 'China'
    def __init__(self, ID=0, name='null', salary=0):
        self.ID = ID
        self.name = name
        self.__salary = salary # 私有成员，只有在类的内部才可以访问
        self.students_list = {}
    def __call__(self):
        return (self.ID, self.name, self.__salary)

    def __getitem__(self, index):
        return self.students_list[index]

    def __setitem__(self, key, val):
        self.students_list[key] = val


if __name__ == '__main__':
    # xm = Sutdent()  # 执行 Student 的构造函数
    # print(xm()) # 执行 Student 重载的 () 运算符
    # l = []
    # print(xm.__dict__)
    # print(xm) # print(xm.__str__())

    t = Teacher()
    print(t())
    print(t.name)
    # print(t.__salary)   # ERROR, 对象的私有成员,在对象外部无法直接访问, 子类也无法访问
    print(Teacher.country)
    print(t.country)
    # print(Teacher.__age_level) # ERROR
    # print(t.__age_level) # ERROR
    t['1'] = 'xiaoming'
    print(f"Teacher:{t.name}'s Student1:{t['1']}")
    t.country = "Japan"
    print(t.country)    # 字段并不是所有类对象共享的

    t2 = Teacher()
    print(t2.country)