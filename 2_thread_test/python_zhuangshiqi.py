# 装饰器测试

class People:
    CLASS_NAME = "People"

    def __init__(self, name, salary=2500):
        self.__salary = salary
        self.name = name
        self.first = name[0:1]
        self.last = name[-1:]

    @classmethod
    def print_class_name(cls):
        """
        内置装饰器 @classmethod, 用于定义类方法, 第一个参数通常被定义为 cls, 表示类本身, 而不是实例
        (1)类方法内部能放调用实例方法/访问实例变量
        (2)类和实例都可以直接调用类方法
        (3)如果需要在类方法内部调用实例方法, 可以通过传入对象作为参数实现
        应用场景:
        (1)在类级别操作类的属性/状态
        (2)提供不依赖于实例状态的工厂方法
        (3)在实例化对象之前对类进行初始化
        """
        print(cls.CLASS_NAME)

    @classmethod
    def print_class_name_v2(cls, instance):
        """
        不支持重载???
        :param cls
        :param instance
        """
        print(instance.name + " " + cls.CLASS_NAME)

    @staticmethod
    def compose_group():
        """
        内置装饰器 @staticmethod 用于定义静态方法, 静态方法是类中的方法, 与类的实例无关， 也无法访问类的实例变量/实例方法
        静态方法通过类名调用，而不是通过对象/实例调用
        调用该方法时不需要创建类实例
        """
        print(" compose a group")

    @property
    def fullname(self):
        """
        内部装饰器: @property 可以像成员一样调用方法
        """
        return self.first + self.last

    @fullname.setter
    def fullname(self, name):
        """
        设置 fullname 属性时进行的操作
        当设置 B 属性时 并且你希望同事更新 A 属性, 这个就可以通过添加 setter 实现
        :param name
        """
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """
        删除 fullname 属性时执行的操作
        """
        self.first = None
        self.last = None

    # @fullname.getter
    # def fullname(self):


if __name__ == '__main__':
    People.print_class_name()
    p = People("xiao li")
    p.print_class_name()
    People.print_class_name_v2(p)

    People.compose_group()

    p.first = 'a'
    print(p.fullname)

    del p.fullname
    if isinstance(p.first, str):
        print("name:{}".format(p.first + p.last))
    else:
        print("None name")

