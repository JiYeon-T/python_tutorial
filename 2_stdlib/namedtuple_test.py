import collections
import sys
from collections import namedtuple
from typing import NamedTuple
import timeit  # TODO:Tool for measuring execution time of small code snippets.
# https://cloud.tencent.com/developer/news/1383097
# 具名元组
# 在Python中，NamedTuple是一种特殊形式的元组，它为元组内的每个元素赋予了名字，从而使得访问更加直观且代码更具自解释性。
# 这种数据结构结合了元组的不可变性和字典的键值对应特性，非常适合用来表示具有固定属性的小型对象集合，比如数据库查询结果、配置项等。


def namedtuple_example1():
    """基础操作"""

    class Point(NamedTuple):
        x : float
        y : float
    p = Point(3.1, 4.5)
    # 由于NamedTuple是不可变的，一旦创建后其内容就不能更改。访问元素就像访问普通元组一样 ，但可以通过属性名进行 ，这大大增强了代码的可读性：
    # 可以直接通过属性名称访问, 类似于字典
    print(f"x:{p.x} y:{p.y}")
    # p.x = 2  # AttributeError: can't set attribute
    # 通过这种方式，NamedTuple不仅提供了清晰的数据结构表示 ，还保证了数据的安全性，防止了意外的修改。
    # 在需要表示不可变的、具有特定意义的数据组合时 ，它是首选的数据结构之一。

def namedtuple_api_example():
    """api"""

    Student = namedtuple('Student', 'name serialnum school gradelevel')
    li = Student._make(["李白", 123, "清华学校", "A"])  # 使用可迭代对象创建 namedtuple
    print(type(li), repr(li), sep=", ")
    print(f"dict:{li._asdict()}")
    wang = li._replace(name="王安石")  # TODO: 为什么不会改变原对象???
    print(type(li), repr(li), sep=", ")
    print(type(wang), repr(wang), sep=", ")

def namedtuple_example2():
    """进阶技巧：继承与扩展
    在这个例子中 ，ColorPoint继承自BasePoint，并新增了一个字段color，同时重写了__str__方法以提供更友好的字符串表示。
    """

    class BasePoint(NamedTuple):
        x : float
        y : float

    class ColorPoint(BasePoint):
        color : str = 'black'  # 默认参数

        def __str__(self):
            return f"point({self.x},{self.y}) color:{self.color}"
    # c = ColorPoint(1.0, 2.0)
    # print(c)

    class DistancePoint(ColorPoint):
        """除了简单地添加字段，我们还可以利用类方法或静态方法来扩展功能，
        比如实现一些计算逻辑或验证规则
        NOTE:
        通过这些进阶技巧 ，NamedTuple不仅能保持数据的纯净性和不可变性，
        还能通过继承和扩展，变得更加灵活和强大，适用于更广泛的场景。
        """

        def distance_to_origin(self):
            """计算到原点的距离"""
            return self.x * self.y / 2
    # c2 = DistancePoint(1.5, 2.5)
    # print(c2.distance_to_origin())

        @classmethod
        def from_polar(cls, radius:float, angle_deg:float, color='black'):
            """使用极坐标创建点实例"""
            import math
            x = radius * math.cos(angle_deg)
            y = radius * math.sin(angle_deg)
            return cls(x, y)
    # c3 = DistancePoint.from_polar(50, 30)
    # print(c3, c3.distance_to_origin(), sep=",")
    # c3.x = 1  # AttributeError: can't set attribute

def namedtuple_example3():
    """
    在处理结构化数据时，如果数据具有固定的字段且不需要动态增减，NamedTuple相比dict和list有显著优势。
    例如，在表示数据库记录或API响应结构时：
    提升代码可读性
    易于理解的属性访问
    与dict对比：
    NamedTuple提供了字段名的同时保持了元组的不可变性，使得数据更安全，适合存储不需要修改的结构化信息。
    而dict允许动态添加和删除键值对，适合更多变的数据结构。
    与list对比：
    列表适合存储有序但无固定结构的数据集合。当集合中的每个元素都具有相同的结构和语义时，NamedTuple则更加合适，
    因为它提供了类型安全和更清晰的访问方式。
    性能考量：
    虽然直接比较性能可能因具体应用场景而异，NamedTuple通常比同等大小的dict占用更少的内存，因为它们不需要存储键的哈希表。
    此外 ，访问 NamedTuple 的属性通常比访问 dict 的键更快。
    通过这些实战应用 ，可以看到NamedTuple在特定场景下能有效优化数据结构，提高代码的清晰度和运行效率，是Python编程中不可或缺的高级特性之一。
    """
    class LogEntry(NamedTuple):
        timestamp : float
        level : str
        message : str
    log = LogEntry(123456789, 'INFO', 'Application started')
    if log.level == 'ERROR':
        print(f"ERROR at {log.timestamp} {log.message}")

def namedtuple_example4():
    """
    Python 3.5 引入了类型注解，而NamedTuple与类型注解的结合能够增强代码的自我文档化能力及静态检查的可能性。
    通过在定义NamedTuple时指定字段类型 ，可以明确预期的数据类型，辅助IDE和类型检查器提供更好的代码补全和错误提示：
    """
    class InventoryItem(NamedTuple):
        name : str
        quantity : int
        unit_price : float
    # 上述代码中，name、quantity和unit_price字段分别指定了字符串、整数和浮点数类型，提高了代码的清晰度和维护性。
    # item = InventoryItem('Widget', 1, 2.0)

    #TODO:
    # 4.2 利用match case模式匹配
    # Python 3.10 引入的match-case语句为处理不同类型的值提供了更优雅的方式，尤其适合与NamedTuple配合使用。通过模式匹配，可以针对NamedTuple的不同字段值编写分支逻辑：
    # def process_item(item : InventoryItem):
    #     match item:
    #         case InventoryItem(name='Widget', quantity=q, unit_price=p):
    #             print(f"Processing Widget with quantity {q} at ${p:.2f} each.")
    #         case InventoryItem(quantity=q) if q > 50:
    #             print(f"Large order of {q} items detected!")
    #         case _:
    #             print("Handling general inventory item.")
    # process_item(InventoryItem(name='Widget', quantity=75, unit_price=49.99))
    # 这里，match-case不仅检查了InventoryItem的类型，
    # 还进一步匹配了具体的字段值和条件，使得逻辑表达更为直接和简洁。
    # 通过模式匹配，代码可读性更强，维护成本更低。

def namedtuple_example5():
    """
    性能测试:
    通过使用Python的内置函数sys.getsizeof()，可以大致评估两种结构的内存占用：

    NamedTuple相比普通元组，在存储相同数据时会占用更多的内存。
    原因在于NamedTuple为了提供字段名访问的能力，内部需要额外存储类型信息和字段名。
    尽管这个开销对于单个实例来说微乎其微 ，但在处理大量数据时差异可能会变得明显。
    """
    Point = collections.namedtuple('Point', ['x', 'y'])  # 返回一个类
    print(f'doc:{Point.__doc__}')
    print(f"type:{type(Point)}")  # type:<class 'type'>

    named_tuple = Point(x=1, y=2)
    print(f"size:{sys.getsizeof(named_tuple)}")

    plain_tuple = (1, 2) # 普通元组
    print(f"size:{sys.getsizeof(plain_tuple)}")  # 为什么 size 一样???

    # 5.2 访问速度比较
    # 尽管NamedTuple在内存占用上不占优势，但在访问速度上 ，尤其是在频繁访问的情况下，它通常表现得更为高效。
    # 这是因为通过属性访问（.x,.y）通常比索引访问（[0],[1]）更快速 ，尤其是在现代解释器中 ，属性访问往往经过优化。
    # 为了量化这一差异，可以通过简单的计时测试来比较：
    def access_plain_tuple():
        _sum = plain_tuple[0] + plain_tuple[1]

    def access_named_tuple():
        _sum = named_tuple.x + named_tuple.y

    print(f"plain tuple:{timeit.timeit(access_named_tuple, number=1000000)}")
    print(f"named tuple:{timeit.timeit(access_named_tuple, number=1000000)}")

if __name__ == '__main__':
    # namedtuple_example1()
    namedtuple_api_example()
    # namedtuple_example2()
    # namedtuple_example3()
    # namedtuple_example4()
    # namedtuple_example5()







