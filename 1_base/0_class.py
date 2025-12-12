import datetime


def oob_base_test():
    """Python3 面向对象编程 Object Oriented Programing
    """
    class Cat():
        """类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称,
        按照惯例它的名称是 self。
        self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。以保持代码的一致性和可读性。
        """
        __CLASS_NAME = "Cat" # 私有变量(类成员)
        CLASS_TYPE = "Animal" # 公开变量(类成员)
        __obj_cnt = 0 # 私有类成员, 保存实例对象的个数

        def __init__(self, id=1, salary=2000):
            self.__id = id # 两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
            self.__salary = salary # 私有
            self.__obj_cnt += 1 # 对象成员

        def eat(self, a, b):
            """公共方法:父类定义一个方法"""
            print("{} a:{} b:{}".format(self.__class__, a, b))
            return a + b

        def __get_salary(self):
            """
            类的私有方法
            __private_method：两个下划线开头，声明该方法为私有方法，
            只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
            """
            print("Salary:", self.__salary)
            return self.__salary

        def myself(self):
            print(self)
            print("id:{}\ntype:{}\nclass:{}\n".format(id(self), type(self), self.__class__))
            print("Class Name:", self.__CLASS_NAME)
            print("id:{} salary:{}".format(self.__id, self.__salary))

        def __add__(self, other):
            """   # 运算符重载:
            # Python同样支持运算符重载，我们可以对类的专有方法进行重载，
            """
            return Cat(self.__id + other.__id)

        def __str__(self):
            """字符串方法"""
            return "name:{} object at id:{}".format(self.__CLASS_NAME, id(self))

        # 所以逻辑上类方法应当只被类调用
        # 实例方法实例调用，
        # 静态方法两者都能调用。
        # 主要区别在于参数传递上的区别，实例方法悄悄传递的是self引用作为参数，
        # 而类方法悄悄传递的是 cls 引用作为参数。
        def object_method(self):
            """实例方法:
            实例方法可以调用实例属性/方法以及类属性/方法"""
            print("{}".format(self.__salary))

        @staticmethod
        def static_method1():
            """用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，
            类的静态方法可以没有参数，
            可以直接使用类名调用, 也可以通过对象调用。
            静态方法无隐含参数，主要为了类实例也可以直接调用静态方法
            静态方法不可以调用类属性/方法或者实例属性/方法（或者说最好不要调用）
            应用场景:
            a. 当一个方法即不需要访问实例成员/方法,又不需要访问类的成员/方法
            但又最好放在类的内部时 e.g.;
            """
            print("静态方法(不需要访问类成员之类的, 但又最好放在类所在命名空间的方法)")
            # print(Cat.__CLASS_NAME) # 最好不要调用
            # Cat.class_method()

        @staticmethod
        def formate_date(date_str):
            """格式化当前时间的
            方法又仅在该类内部用到"""
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

        @classmethod
        def class_method(cls):
            """类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器
            类方法隐含的参数为类本身 cls
            类方法可以调用类属性/方法, 不能调用实例属性/方法
            应用场景:
            a. 当一个接口仅需要访问类属性/方法时, e.g. get_obj_cnt """
            print("类方法 class:{} name:".format(cls.__class__), cls.__name__)
            print(cls.__CLASS_NAME) # cls 参数可以直接访问类变量/类方法的

        @classmethod
        def get_obj_cnt(cls):
            """类方法:
            获取当前类的实例对象个数"""
            return cls.__obj_cnt


    cat = Cat()
    cat.myself()
    # cat.__get_salary() # ERROR:外部不可以调用类的私有方法
    d = Cat() + Cat() # 类的运算符重载
    d.myself()
    cat.static_method1() # 类的静态方法可以没有参数，可以直接使用类名调用
    Cat.static_method1() # 也可以通过对象调用
    cat.class_method() # 类方法通过对象调用
    Cat.class_method() # 类方法直接通过类名调用
    print("Obj cnt:", Cat.get_obj_cnt())
    print("time:", Cat.formate_date("2024-12-05"))

    # 通过这个例子可以看出, self 和 实例化后的对象是一个东西
    # 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，
    # 而 self.class 则指向类。
    # self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
    # 在 Python中，self 是一个惯用的名称，用于表示类的实例（对象）自身。它是一个指向实例的引用，
    # 使得类的方法能够访问和操作实例的属性。
    # 当你定义一个类，并在类中定义方法时，第一个参数通常被命名为 self，尽管你可以使用其他名称，
    # 但强烈建议使用 self，“以保持代码的一致性和可读性”。
    print("id:{}\ntype:{}\nclass:{}\n".format(id(cat), type(cat), cat.__class__))

    # 多继承：
    # 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
    # python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

    # super() 函数是用于调用父类(超类)的一个方法。
    # super()函数是用于调用父类(超类)的一个方法。
    # super()是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
    # 但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。MRO
    # 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
    # Python3.x 和 Python2.x 的一个区别是:
    # Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
    class WildCat(Cat):
        def __init__(self):
            # # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），
            # 然后把类 FooChild 的对象转换为类 FooParent 的对象
            super().__init__()

        def eat(self, a, b):
            # 先调用父类的方法, 然后再调用子类自己的方法
            # 它会查找所有的超类，以及超类的超类，直到找到所需的特性为止。
            super(WildCat, self).eat(a, b)
            print("{} a:{} b:{}".format(self.__class__, a, b))
            return a * b
    # wc = WildCat()
    # wc.eat(1, 2) #
    # print(Cat.CLASS_TYPE) # 外部可以直接访问公有成员

def multi_parent_test():
    class people:
        """人"""

        # 定义基本属性
        name = ''
        age = 0
        # 定义私有属性,私有属性/方法 在类外部无法直接进行访问
        __weight = 0

        # 定义构造方法
        def __init__(self, name, age, weight):
            self.name = name
            self.age = age
            self.__weight = weight # 私有成员

        def speak(self):
            print("%s 说: 我 %d 岁。" % (self.name, self.age))

    # 单继承示例
    class student(people):
        grade = ''

        def __init__(self, name, age, weight, grade):
            # 调用父类的构造函数
            people.__init__(self, name, age, weight)
            self.grade = grade

        # 覆写父类的方法
        def speak(self):
            print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

    # 另一个类，多继承之前的准备
    class speaker():
        topic = ''
        name = ''

        def __init__(self, name, topic):
            self.name = name
            self.topic = topic

        def speak(self):
            print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))

    # 多继承(既是一个 speaker 又是一个学生)
    # class sample(student, speaker):
    class sample(speaker, student): # 多继承时的优先级问题
        a = ''

        def __init__(self, name, age, weight, grage, topic):
            speaker.__init__(self, name + str("_speaker"), topic)
            student.__init__(self, name + str("_student"), age, weight, grage)
        # TODO: 2个父类都有 name 成员, 这时候子类也只有一个 name 成员?? 如果两次构造函数赋值不同呢??
        # speak() 方法也重载了, sample() 具体调用哪个父类的 speak() 方法, 由多继承的顺序决定(第一个最优先);
        # 好像有何够凹函数的顺序有关系。。。

        def speak(self):
            """当子类重写了这个这个方法后, 优先调用子类的方法"""
            print(f"我是{self.name} 我是一个 smaple")
            super().speak() # 调用父类的被重写的方法

    def test():
        tom = sample("Tom", 25, 128, 100, "我的家乡")
        tom.speak()
        # super(sample, tom).speak()  #用子类对象调用父类已被覆盖的方法
    test()

# 类的专有方法:
# __init__: 构造函数，在生成对象时调用
# __del__: 析构函数，释放对象时使用
# __repr__: 打印，转换
# __setitem__: 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
#运算符重载
# Python同样支持运算符重载，我们可以对类的专有方法进行重载
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
# 反向运算符重载： b = 1 + a
# 例如: __add__运算符重载可以保证V+int的情况下不会报错，
# 但是反过来int+V就会报错，通过反向运算符重载可以解决此问题
# __radd__: 加运算
# __rsub__: 减运算
# __rmul__: 乘运算
# __rdiv__: 除运算
# __rmod__: 求余运算
# __rpow__: 乘方
# 复合重载运算符： a += 1
# 例如: 主要用于列表，例如L1+=L2,默认情况下调用__add__，会生成一个新的列表，
# 当数据过大的时候会影响效率，而此函数可以重载+=，使L2直接增加到L1后面
# __iadd__: 加运算
# __isub__: 减运算
# __imul__: 乘运算
# __idiv__: 除运算
# __imod__: 求余运算
# __ipow__: 乘方

def operatore_overload_test():
    """运算符重载测试"""

    class Vector:
        """二维向量"""

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __str__(self):
            return 'Vector (%d, %d)' % (self.a, self.b)

        def __repr__(self):
            return 'Vector (%d, %d)' % (self.a, self.b)

        def __add__(self, other):
            if other.__class__ is Vector:
                return Vector(self.a + other.a, self.b + other.b)
            elif other.__class__ is int:  # 仅添加到 a 上?
                return Vector(self.a + other, self.b + other)

        def __radd__(self, other):
            """反向算术运算符的重载
            __add__运算符重载可以保证V+int的情况下不会报错，
            但是反过来int+V就会报错，通过反向运算符重载可以解决此问题
            """

            if other.__class__ is int or other.__class__ is float:
                return Vector(self.a + other, self.b + other)
            else:
                raise ValueError("值错误")

        def __iadd__(self, other):
            """复合赋值算数运算符的重载
            主要用于列表，例如L1+=L2,默认情况下调用__add__，会生成一个新的列表，
            当数据过大的时候会影响效率，而此函数可以重载+=，使L2直接增加到L1后面
            """

            if other.__class__ is Vector:
                return Vector(self.a + other.a, self.b + other.b)
            elif other.__class__ is int:
                return Vector(self.a + other, self.b + other)

    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print(f"v1:{v1} v2:{v2}")
    print(v1 + v2)
    print(v1 + 5)
    print(6 + v2)


if __name__ == '__main__':
    # oob_base_test()
    # multi_parent_test()
    operatore_overload_test()