import keyword
import math
# 导入模块
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *





# https://www.runoob.com/python3/python3-basic-syntax.html
import sys
import time


def base_info():
    """python 关键字"""
    # print(keyword.kwlist)

    # 内容太多, 一行写不下时使用 \ 进行换行
    item1 = 1
    item2 = 2
    item3 = 3
    sum = item1 + \
          item2 + \
          item3



    # Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    # name = "Lebron James"
    # print("first:{} last:{}".format(name[0], name[-1]))

def str_op():
    """字符串操作测试"""
    # 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
    # 字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
    str = '123456789' # 下标从 0 开始
    print(str) # 输出字符串
    print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
    print(str[0]) # 输出字符串第一个字符
    print(str[2:5]) # 输出从第三个开始到第六个的字符（下标从 0 开始,不包含第6个）
    print(str[2:]) # 输出从第三个开始后的所有字符
    print(str[1:5:2]) # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
    print(str * 2)  # 输出字符串两次
    print(str + '你好') # 连接字符串
    print("This is a new line\nline 2")
    print(r"This is a new line\nline 2") # 反斜杠可以用来转义，使用 r (raw)可以让反斜杠不发生转义

    print("\110")#特殊字符:\yyy 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
    print("\x0A") #\x 16进制表示

    print("hello python".capitalize()) #将字符串的第一个字符转换为大写
    print("hello python".center(40, ',')) #center(width, fillchar) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
    print("hello python".count('a')) # count(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    bytes_arr = "hello python我".encode(encoding='utf-8') # bytes.decode(encoding="utf-8", errors="strict")Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
    print(bytes_arr)
    print(bytes_arr.decode(encoding='utf-8')) # encode(encoding='UTF-8',errors='strict')以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
    print("hello python".startswith('a')) # startswith(substr, beg=0,end=len(string))检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
    print("hello python".endswith('a')) # endswith(suffix, beg=0, end=len(string))检查字符串是否以 suffix 结束，如果 beg 或者 end 指定则检查指定的范围内是否以 suffix 结束，如果是，返回 True,否则返回 False。
    print("hello\tpython".expandtabs(2)) # expandtabs(tabsize=8) 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
    print("hello python".find("hello")) # find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
    print("hello python".rfind("hello")) # rfind(str, beg=0,end=len(string))类似于 find()函数，不过是从右边开始查找.
    print("hello python".index("hello")) # index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在字符串中会报一个异常。
    print("hello python".rindex("hello")) # rindex( str, beg=0, end=len(string))类似于 index()，不过是从右边开始.
    print("hello python".isalnum()) # isalnum() 检查字符串是否由字母和数字组成，即字符串中的所有字符都是字母或数字。如果字符串至少有一个字符，并且所有字符都是字母或数字，则返回 True；否则返回 False。
    print("hello python".isalpha()) # isalpha() 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
    print("hello python".isdigit()) # isdigit() 如果字符串只包含数字则返回 True 否则返回 False..
    print("hello python".islower()) # islower() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
    print("hello python".isnumeric()) # isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False
    print("hello python".isspace()) # isspace() 如果字符串中只包含空白，则返回 True，否则返回 False.
    # 如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回True，否则返回False.
    print("hello python".upper()) # upper() 转换字符串中的小写字母为大写
    print("hello python".istitle()) # istitle() 如果字符串是标题化的(见 title())则返回 True，否则返回 False
    print("hello python".isupper()) # isupper()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
    print(len("aaaa"))
    print("-".join('Hello python')) # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    print("hello python".ljust(50, ',')) # ljust(width[, fillchar])返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
    print("hello python".rjust(50, ',')) # rjust(width,[, fillchar])返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
    print("Hello Python".lower()) # lower()转换字符串中所有大写字符为小写.
    print("hello python".strip()) # strip([chars]) 在字符串上执行 lstrip()和 rstrip()该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    print("hello python".lstrip()) # lstrip() 截掉字符串左边的空格或指定字符。
    print("hello python".rstrip())  #rstrip()删除字符串末尾的空格或指定字符。
    print(max('hello python')) # max(str) 返回字符串 str 中最大的字母。
    print(min('hello python')) #min(str) 返回字符串 str 中最小的字母。
    intab = "aeiou"
    outtab = "12345"
    mytable = str.maketrans(intab, outtab) # 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。
    print("hello python".translate(mytable)) # translate(table, deletechars="") 根据 table 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
    print("hello python".replace('e', 'E')) # replace(old, new [, max])把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
    print("hello python".split('e')) # split(str="", num=string.count(str))以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
    print("hello python".splitlines(keepends=False)) # splitlines([keepends])按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
    print("hello python".swapcase()) # swapcase()将字符串中大写转换为小写，小写转换为大写
    print("hello python".title()) # title() 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
    print("hello python".zfill(50)) # zfill (width)返回长度为 width 的字符串，原字符串右对齐，前面填充0
    print("hello python".isdecimal()) # isdecimal()检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
    print("hello python {0} {1}".format([1, 2], 2)) # 按照指定的格式输出字符串:在括号中的数字用于指向传入对象在 format() 中的位置
    # format 指定格式:!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
    # 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
    print("PI:{!r}".format(math.pi))
    print("PI:{0:.3f}".format(math.pi))

def enter_test():
    """"""
    import sys
    import math
    # in_str = input("\n\n输入 enter 键退出\n\n") # 用户输入
    # sys.stdout.write(in_str + '\n')

    #print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
    print("abc", end="")
    print("path:{}\nargc:{}\nargv:{}".format(sys.path, len(sys.argv), sys.argv))
    # help(sys) # help function
    # print(max.__doc__) # print help information

    dict = {'a':1, 'b':2, 'CCC':3}
    for k,v in dict.items():
        print(k, v, sep=":", end="\n") # seprator

    # 类似于 C/C++ 的 printf，Python 的 print 也能实现格式化输出，
    # 方法是使用 % 操作符，它会将左边的字符串当做格式字符串，将右边的参数代入格式字符串：
    print("%d" % 100)
    # 前面格式串中的转义字符格式与 C/C++ 中一致, 如:%d, %f, %o, %x...
    # 如果要带入多个参数，则需要用()
    # 包裹代入的多个参数，参数与参数之间用逗号隔开，参数的顺序应该对应格式字符串中的顺序
    print("%d + %d = %d" % (100, 200, 300))
    a = 16
    print("sqrt{}={}".format(a, math.sqrt(a)))

def var_type_test():
    """Python3 基本数据类型"""
    # a = 100
    # b = 100.0
    # c = "100"
    a, b, c = 100, 100.0, "100"
    print("a:%d b:%f c:%s" % (a, b, c))

    # isinstance 和 type 的区别在于：
    # type()不会认为子类是一种父类类型。type 主要用于判断未知数据类型
    # isinstance()会认为子类是一种父类类型。isinstance 主要用于判断 A 类是否继承于 B 类
    # print("type:{} {} {}".format(type(a), type(b), type(c))) # 多个变量赋值
    # print("instance:{} {} {}".format(isinstance(a, int), isinstance(b, float), isinstance(c, str)))

    # Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加，
    # True==1、False==0 会返回 True，但可以通过 is 来判断类型。
    d = True
    # print(issubclass(bool, int)) # Python3 中，bool 是 int 的子类
    # print(1 is True)
    # print(0 is False)
    # print(True + 1)
    # print(False + 1) #在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。

    # 使用del语句删除一些对象引用(可以通过使用del语句删除单个或多个对象)
    del a, b, c
    del d

    # 简单的数值运算, TODO:python 中数值的范围????, 肯定不是无限大呀
    # print(2 / 4)
    # print(2 // 4) # 除法，得到一个整数
    # print(3 // 4)
    # print(4 // 4)
    # print(2 ** 5) # 乘方

    e, f = 1 + 2j, complex(3, 4) # python 还支持复数
    # print(e, f, sep=",")
    # print(type(e), type(f), sep=",")

    g, h = True, False # 使用 bool()
    print(type(g)) # 布尔类型的值和类型
    print(type(h))
    print(int(True)) # 布尔类型的整数表现
    print(int(False))
    print(bool(0)) # 使用 bool() 函数进行转换
    print(bool(42))
    print(bool(''))
    print(bool('python'))
    print(bool([]))
    print(bool([1, 2, 3]))
    print(True and False) # 布尔逻辑运算
    print(True or False)
    print(not True)

    print(5 > 3) # 布尔比较运算
    print(2 == 2)
    print(7 < 4)
    if True: # 布尔值在控制流中的应用
        print(True)
    if not False:
        print("not false")

def list_base_test():
    """字符串的索引以及操作方法和字符串一致
    和字符串一样，列表可以被索引和切片"""
    import copy # copy 模块
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # a.clear() # List 内置了有很多方法，例如 append()、pop() 等等
    print(a)
    print(a[::2]) # 通过下标的索引操作, 包前不包后
    print(a[0::2])
    print(a[0:-1:2])

    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长(step)，-1 表示逆向
    print(a[-1::-1])

    def reverse_str_sentence(input_sentence):
        """翻转字符串"""
        inputWords = input_sentence.split(" ")
        print(inputWords)
        output = inputWords[-1::-1] # 反向
        return output
    print(reverse_str_sentence("Nothing is impossible"))

    b = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ] # 列表可以被索引和切片, 但是索引得到列表中的元素, 切片得到的是列表
    print("{} {}".format(b[2], type(b[2]))) # <class 'float'
    print("{} {}".format(b[2:3], type(b[2:3]))) # <class 'list'>

    b.append(a) # 	list.append(obj) 在列表末尾添加新的对象
    print(b)
    print("count:{}".format(b.count(1))) # 	list.count(obj) 统计某个元素在列表中出现的次数
    b.extend(a) # list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    print(b)
    print("index:{}".format(b.index(a)))
    b.insert(0, "OK") # list.insert(index, obj) 将对象插入列表
    print(b)
    b.pop(5) # list.pop([index=-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    print(b)
    b.remove(a) # list.remove(obj)移除列表中某个值的第一个匹配项
    print(b)
    b.reverse() # 	list.reverse() 反向列表中元素
    print(b)
    # print(b.sort()) # list.sort( key=None, reverse=False) 对原列表进行排序
    c = b.copy() # list.copy() 复制列表(深拷贝), 用list自带的copy()方法,把重新开辟内存空间存储新列表。
    d = copy.copy(b) # 拷贝模块(深拷贝)
    e = b[:] # 深拷贝
    f = e # 浅拷贝
    print("b:{} id:{}".format(b, id(b)))
    print("c:{} id:{}".format(c, id(c)))
    print("d:{} id:{}".format(d, id(d)))
    print("e:{} id:{}".format(e, id(e)))
    print("f:{} id:{}".format(f, id(f)))
    b.clear() # list.clear() 清空列表
    print(b)

    #列表推导式 [表达式 for 变量 in 列表] 或者 [表达式 for 变量 in 列表 if 条件]
    print(["ELEM:" + str(x) for x in e])

def tuple_base_test():
    """元组测试
    元组（tuple）与列表类似，不同之处在于元组的元素不能修改(所谓元组的不可变指的是元组所指向的内存中的内容不可变。)。
    元组写在小括号 () 里，元素之间用逗号隔开。
    元组中的元素类型也可以不相同(列表和元组不会把相同的值合并)
    TODO:该数据类型使用场景:???
    不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。
    如果可能，能用tuple代替list就尽量用tuple。
    tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下
    """
    a = (1, ) # Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
    tuple = ('ABC', 786, 2.23, 'DEF', 80.2) #
    tiny_tuple = (123, 'ABC')
    print("type:{}".format(tiny_tuple))
    print(tuple) # 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取
    print(tiny_tuple)
    print(tuple[0])
    print(tuple[1:3])
    print(tuple[2:])
    # print(tuple * 2)
    print(tuple + tiny_tuple) # 元组也可以使用 + 操作符进行拼接
    # tuple[0] = "ABC" # TypeError: 'tuple' object does not support item assignment
    # tuple += "XYZ" # ERROR:can only concatenate tuple (not "str") to tuple
    single_elem_tuple = (1, ) # 如果你想创建只有一个元素的元组，需要注意在元素后面添加一个逗号，以区分它是一个元组而不是一个普通的值，这是因为在没有逗号的情况下，Python会将括号解释为数学运算中的括号，而不是元组的表示。

    def return_multi_val(a, b):
        """一般来说，函数的返回值一般为一个。
        而函数返回多个值的时候，是以元组的方式返回的。"""
        return a, b # 等效于 return(a,b)
        # return [a, b] # 指定返回列表
    print(type(return_multi_val(1, 2)))

    def var_len_param_test(*args):
        """python中的函数还可以接收可变长参数，
        比如以 "*" 开头的的参数名，会将所有的参数收集到一个元组上。
        :param args <class 'tuple'>
        :return <class 'tuple'>
        """
        print(type(args))
        for i in range(len(args)):
            print("[{}]={}".format(i, args[i]))
        return args
    print("return type:", type(var_len_param_test()))
    var_len_param_test(1)
    var_len_param_test(1, 2)
    var_len_param_test(1, 2.5, [1,2, 3])

    #元组所指向的内存实际上保存的是元组内数据的内存地址集合（即 t[0], t[1]...t[n] 的内存地址），
    # 且元组一旦建立，这个集合就不能增加修改删除，一旦集合内的地址发生改变，
    # 必须重新分配元组空间保存新的地址集
    # （元组类似 C 语言里的指针数组，只不过这个数组不能被修改）。
    c = (1, 2, 3)
    d = (4, 5, 6)
    e = (7,)
    c = c + d + e
    print(c)

def set_base_test():
    """Set（集合）
    Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
    集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
    在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
    另外，也可以使用 set() 函数创建集合。
    可以进行集合运算"""
    a = {1, 2, 3, 3, 3} # 集合是无重复元素的序列，会自动去除重复元素(集合会把相同的合并)
    b = set("134") # 三个元素:'1' '3' '4'
    c = set(["123", "456", 789, 25.6])
    print("{},{},{}".format(type(a), type(b), type(c)))
    print(a - b) # a 和 b 的差集
    print(a | b | c) # a 和 b 的并集
    print((a & b)) # a 和 b 的交集
    print(a ^ b) # a 和 b 中不同时存在的元素

    # print(a[0]) # 集合是无序的，所以不支持索引
    a.add(7) # 添加元素
    print(a)
    a.update([1, 2, 3, 100]) # 增加元素
    print(a)
    a.remove(100) # 删除,将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
    print(a)
    a.discard(7) # 也是移除集合中的元素，且如果元素不存在，不会发生错误
    print(a)
    a.pop() # 随机删除一个（set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。）
    print(a)
    a.clear() # 清空
    print(a)

    if 1 in a:
        print("Exist")
    else:
        print("Not exist")
    e = b.copy()
    print("b:{} id:{}".format(b, id(b)))
    print("e:{} id:{}".format(e, id(e))) # copy() 拷贝一个集合
    print(e.difference(b)) # difference() 返回集合的差集
    # print(e.difference_update(b)) #difference_update()	移除集合中的元素，该元素在指定的集合也存在
    print(e.intersection(b)) # intersection() 返回集合的交集
    print(e.intersection_update(b)) # intersection_update()	返回集合的交集。
    print(e.isdisjoint(b)) # isdisjoint() 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
    print(e)
    print(e.issubset(set("123456789"))) # issubset() 判断指定集合是否为该方法参数集合的子集。
    print(e.issubset(set("1"))) # issuperset()	判断该方法的参数集合是否为指定集合的子集
    print(e.symmetric_difference(b)) # symmetric_difference() 返回两个集合中不重复的元素集合。
    print(b)
    print(e)
    print(e.symmetric_difference_update(b)) # symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
    print(e)
    print(e.union(b)) # union()	返回两个集合的并集


def dict_base_base_test():
    """Dictionary（字典）
    字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
    键(key)必须使用不可变类型。
    在同一个字典中，键(key)必须是唯一的。
    实现:
    python中的字典是使用了一个称为散列表（hashtable）的算法（不具体展开）
    其特点就是：不管字典中有多少项，in操作符花费的时间都差不多。
    """
    a = {1:1, 1:1, "L":[1, 2, 3]} # 字典因为其key唯一性，会自动去除重复元素, 所以也不会出现相同元素,
    b = {"abc":"def", 1:2, "list_item":[1, 2, 3, "One", "Two", "Three"]}
    print("a={}, size:{}".format(a, len(a)))
    print(b)
    print(b[1]) # 输出键为 1 的元素对应的值
    a['one'] = 1 # 字典同样也是无序的，但由于其元素是由键（key）和值（value）两个属性组成的键值对，可以通过键（key）来进行索引
    print(a)
    print("b -> key:{}".format(b.keys())) # 字典类型也有一些内置的函数，例如 clear()、keys()、values() 等
    print("b -> values:{}".format(b.values()))

    for elem in b: # 如果把一个字典对象作为for的迭代对象，那么这个操作将会遍历字典的"键"
        print(elem)
    for k,v in b.items():
        print("k:{} v:{}".format(k, v))

    # 字典键的特性
    # 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，
    # 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，

    # 字典内置函数&方法
    print("len:{}".format(len(a)))
    print("str:{}".format(str(a)))
    print("type:{}".format(type(a)))
    # a.clear() # dict.clear() 删除字典内所有元素
    print("a:{} id:{}".format(a, id(a)))
    c = a.copy() # dict.copy()返回一个字典的浅复制（# 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用）
    d = a # # 浅拷贝: 引用对象
    print("c:{} id:{}".format(c, id(c)))
    c[1] = 'ONE'
    print("a:{} id:{}".format(a, id(a)))
    print("c:{} id:{}".format(c, id(c)))
    c["L"].remove(2)
    print("a:{} id:{}".format(a, id(a)))
    print("c:{} id:{}".format(c, id(c)))

    d = dict.fromkeys([1, 2, 3], [4, 5, 6]) # dict.fromkeys(seq[, value]) 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
    print(d)
    print(d.get(1, None)) # dict.get(key, default=None)返回指定键的值，如果键不在字典中返回 default 设置的默认值
    if 1 in d: # key in dict 如果键在字典dict里返回true，否则返回false
        print("exist")
    else:
        print("does not exist")
    print(d.items()) # dict.items() 以列表返回一个视图对象
    print(d.keys()) # dict.keys() 返回一个视图对象
    print(d.values()) # dict.values() 返回一个视图对象
    print(d.setdefault(4, None)) # 	dict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    print(d)
    e = {}
    e.update(d) # dict.update(dict2) 把字典dict2的键/值对更新到dict里
    print("d:{} id:{}".format(d, id(d)))
    print("e:{} id:{}".format(e, id(e)))
    d.pop(4) # pop(key[,default]) 删除字典 key（键）所对应的值，返回被删除的值。
    print(d)
    print(d.popitem())
    print(d)

    # 字典推导式
    # {key:value for variable in iterable [if expression]}
    # f = {v:k for k,v in e.items()}
    f = {}
    print(f)

    # 字典实现分支需求：
    def status(code):
        stat = {
            400: "print('Bad request')",
            404: "print('Not found')"
        }
        return eval(stat[code])
    print(status(400))

def bytes_base_test():
    """bytes 类型表示的是不可变的二进制序列（byte sequence）。
    与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。
    bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。
    在网络编程中，也经常使用 bytes 类型来传输二进制数据。
    也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。
    bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
    """
    a = bytes("ABCabc", encoding="utf-8") # 指定编码方式
    print(a) # 默认按照编码格式打印
    print("a:{} type:{}".format(a, type(a)))
    for elem in a: # bytes 可迭代类型
        print("0X%X" % elem, sep=",", end=" ")
    print("")
    # 与字符串类型类似，bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等。
    # 同时，由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象。
    # a[0] = b'X' #TypeError: 'bytes' object does not support item assignment
    b = a + b"ZZZ\r\n"
    for elem in b:
        print("0X%X" % elem, sep=",", end=" ")
    print("")
    # ord() 函数用于将字符转换为相应的整数值
    print("%d" % ord("A"))

def var_type_change():
    """Python数据类型转换"""
    # print(int()) # int(x[, base]) # 将x转换为一个整数
    # print(int(3))
    # print(int(3.6))
    # print(int('12', base=16)) # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
    # print(int('0x0A', base=16)) # 如果 base
    # print('10', 8)

    print(float(1)) #float(x) 将x转换到一个浮点数
    print(float(-123))

    print(1 + 2j) # complex(real [,imag]) 创建一个复数
    print(complex("1+2j")) # 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错

    print(str(set([1, 2, 3])))# str(x) 将对象 x 转换为字符串

    z = {"1":"11111111111"}
    print(repr(z)) # TODO:repr(x) 将对象 x 转换为表达式字符串
    print(repr.__doc__)
    # 关于 str() 和 repr() 的区别
    # str()和repr()输出的都是 str 类型
    # 但是 str() 更注重可读性，repr() 更注重数据本身的信息:
    #  str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
    #  repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。
    now = time.time()
    print(str(now))
    print(repr(now))

    x = 5
    print(eval("1 + 3 * x"))# TODO:eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
    # 注意： eval() 函数执行的代码具有潜在的安全风险。
    # 如果使用不受信任的字符串作为表达式，则可能导致代码注入漏洞，因此，应谨慎使用 eval() 函数，并确保仅执行可信任的字符串表达式。

    # tuple() # 起始就是这些数据类型的构造函数
    # list()
    # set()
    # dict()

    h = frozenset([1, 2, 3, 4, 5]) # frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

    print(chr(65)) # chr(x) 将一个整数转换为一个字符
    print(ord('a')) # ord(x) 将一个字符转换为它的整数值
    print(hex(ord('a'))) # ord(x) 将一个字符转换为它的整数值
    print(oct(ord('a'))) # oct(x) 将一个整数转换为一个八进制字符串

def operator_base_test():
    """运算符测试"""
    a = [1, 2, 3]
    if (n := len(a)) > 10: # :=	海象运算符，这个运算符的主要目的是在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增运算符。
        print("large")
    else:
        print(a)
        print(n)

    a = 1 # 00000001 位运算
    b = 2 # 00000010
    print("%d&%d=%d" % (a, b, a & b)) # 按位与运算符
    print("%d|%d=%d" % (a, b, a | b)) # 按位或运算符
    print("%d^%d=%d" % (a, b, a ^ b)) # 按位异或运算符：
    print("~%d=%d" % (a, ~a)) # 按位取反运算符
    print("%d <<= %d" % (a, a << 1)) # 左移动运算符
    print("%d >>= %d" % (b, b >> 1)) # 	右移动运算符

    # Python逻辑运算符 and or not
    # Python成员运算符 in, not in
    # Python身份运算符 is, not is
    a = 20000000 # 果引用的是同一个对象则返回 True，否则返回 False
    b = 20000000
    if a is b: # is 判断两个变量是否是引用同一个内存地址。==判断两个变量是否相等(调用 __eq__()方法判断)。
        print("a 和 b 相等", id(a), id(b), sep=",")
    else:
        print("a 和 b 没相等")

    c = (1, 2, 3)# 其他类型如列表、元祖、字典让a、b分别赋值一样的时：
    d = (1, 2, 3) # 元组相等, list 不相等
    if c is d:
        print("c d Equal")
    else:
        print("c d Not equal {}, {}".format(id(c), id(d)))

    if (id(a) is id(b)): # Return the identity of an object. This is guaranteed to be unique among simultaneously existing objects.
        print("a 和 b 有相同的标识", id(a), id(b), sep=",")
    else:
        print("a 和 b 没有相同的标识")

    print("二进制:", bin(100)) #Return the binary representation of an integer.
    print("数字中1的个数:", bin(7).count('1'), type(bin(7)))

def math_base_test():
    """数学函数"""
    import math
    print("{}".format(abs(-1))) # abs(x) 返回数字的绝对值，如abs(-10) 返回 10
    print("{}".format(math.ceil(4.5))) # ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
    print("{}".format(math.floor(-10))) # floor(x) 返回数字的下舍整数，如math.floor(4.9)返回 4
    print("{}".format(math.exp(1))) #exp(x) 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
    print("{}".format(math.fabs(-10))) #fabs(x) 以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0
    print("{}".format(math.log(math.e))) # log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
    print("{}".format(math.log10(100))) # log10(x) 返回以10为基数的x的对数，如math.log10(100)返回 2.0
    print("{}".format(max(-10, 10)))
    print("{}".format(min(-10, 10)))
    print("{}".format(math.modf(100.598))) # modf(x) 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
    print("{}".format(math.pow(10, 2))) # pow(x, y)	x**y 运算后的值。
    print("{}".format(round(2.1111))) # 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。
    print("{}".format(math.sqrt(16))) # sqrt(x)	返回数字x的平方根。
    def round_fun_test():
        """四舍五入的问题不同 python 版本还不同??
        本地 python2.7 windows 环境测试:都是四舍五入
        使用 env python3.9 环境测试:4舍6入5看齐
        “4舍6入5看齐,奇进偶不进”——我觉得并不是因为浮点数在计算机表示的问题。
        计算机浮点数的表示是 ieee 定义的标准规则，如果 python 中存在，没道理其他语言中不存在。
        事实上是因为该取舍方法比过去的 "四舍五入" 方法在科学计算中更准确。
        而国家标准也已经规定使用 “4舍6入5看齐,奇进偶不进” 取代"四舍五入".
        从统计学的角度上来讲,如果大量数据无脑的采用四舍五入会造成统计结果偏大。
        而"奇进偶舍"可以将舍入误差降到最低。
        奇进偶舍是一种比较精确比较科学的计数保留法，是一种数字修约规则。
        其具体要求如下（以保留两位小数为例）：
         （1）要求保留位数的后一位如果是4或者4以下的数字，则舍去， 例如 5.214保留两位小数为5.21。
         （2）如果保留位数的后一位如果是6或者6以上的数字，则进上去， 例如5.216保留两位小数为5.22。
         （3）如果保留位数是保留整数部分或保留一位小数，则要根据保留位来决定奇进偶舍：
          (4) 如果保留位数的后一位如果是5，且该位数后有数字。则进上去，
          例如5.2152保留两位小数为5.22，5.2252保留两位小数为5.23，5.22500001保留两位小数为5.23
        从统计学的角度，“奇进偶舍”比“四舍五入”要科学，在大量运算时，
        它使舍入后的结果误差的均值趋于零，而不是像四舍五入那样逢五就入，导致结果偏向大数，
        使得误差产生积累进而产生系统误差，“奇进偶舍”使测量结果受到舍入误差的影响降到最低。"""
        print(round(10.4)) # 10
        print(round(10.5)) # 10, 这里不是简单的四舍五入了
        print(round(10.6)) # 11
        print(round(11.4)) # 11
        print(round(11.5))  # 12
        print(round(11.6))  # 12
        print(round(1.5, 0) == round(2.5, 0)) # 如果保留位数是保留整数部分或保留一位小数，则要根据保留位来决定奇进偶舍：
    round_fun_test()

    # 三角函数：acos/asin/atan/atan2/sin/cos/tan/degrees、radians/radians
    # hypot() hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
    # print("{}".format(random.sqrt(16)))

    import random
    # print("choice:{}".format(random.choice(range(100)))) # choice(seq) 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
    # print("{}".format(random.randrange(0, 99, 2))) # randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
    # print("random:{}".format(random.random())) # random() 随机生成下一个实数，它在[0,1)范围内。
    # print("seed:{}".format(random.seed(16))) # seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
    # c = [1, 2, 3]
    # random.shuffle(c)
    # print("shuffle:{}".format(c)) # shuffle(lst) 将序列的所有元素随机排序
    # print("uniform:{}".format(random.uniform(1, 100))) # uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
    # print("randint:{}".format(random.randint(1000, 2000))) # #随机生一个整数int类型，可以指定这个整数的范围
    # print("sample:{}".format(random.sample('abcdefg1234567', 4))) # 可以从指定的序列中，随机的截取指定长度的片断，不修改原序列。

    import operator # Python3中已经不能使用cmp()函数了，被如下五个函数替代:
    print("gt:{}".format(operator.gt(1, 2))) # 意思是greater than（大于）
    print("gt:{}".format(operator.ge(1, 2))) # 意思是greater and equal（大于等于）
    print("gt:{}".format(operator.eq(1, 2))) # 意思是equal（等于）
    print("gt:{}".format(operator.le(1, 2))) # 意思是less and equal（小于等于）
    print("gt:{}".format(operator.lt(1, 2))) # 意思是less than（小于）

    import fractions # fractions 模块提供了分数类型的支持。
    #分子（numerator）和分母（denominator）
    d = fractions.Fraction(1, 3)
    e = fractions.Fraction(4, 6)
    print("d:{} {}".format(d, type(d)))
    print("e:{} {}".format(e, type(e)))
    print(d + e)

    import decimal # decimal 模块提供了一个 Decimal 数据类型用于浮点数计算，拥有更高的精度。
    print(decimal.Decimal.from_float(1.05))

    import numpy as np
    num_array = np.array([1, 2, 3])
    print(num_array)

def condition_control_test():
    """条件控制"""
    import time
    # Python 3.10 增加了 match...case 的条件判断，不需要再使用一连串的 if-else 来判断了。
    # match subject:
    #     case < pattern_1 >:
    #         < action_1 >
    #     case < pattern_2 >:
    #         < action_2 >
    #     case < pattern_3 >:
    #         < action_3 >
    #     case _:
    #         < action_wildcard >

    #e.g. 当前使用 3.9 版本 python, 不支持
    # a = 1
    # match a:
    #     case 1:
    #         print("1")
    #     case 2:
    #         print("2")
    #     case 3:
    #         print("3")
    #     case _:
    #         print("default")

    start = time.time_ns()
    for i in range(10): # 如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列，
        print(i, end=",")
    else:
        print(i*1000)
    end = time.time_ns()
    print("time:{}ns".format(end - start))

    i = 0
    while i in range(0, -10, -1): # 也可以使 range() 以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
        print(i, end=",")
        i -= 1
    else:
        print((i*10000))
        pass # Python pass是空语句，是为了保持程序结构的完整性。

    # 使用内置 enumerate 函数进行遍历:
    a = ['a', 'e', 'i', 'o', 'u']
    for i, j in enumerate(a):
        print("[{}]={}".format(i, j), sep=",", end=",")
    print("")

    # Python 推导式:Python 支持各种数据结构的推导式：
    # 列表(list)推导式
    names = ["ABCD", "E", "Alice", "Bob", "Angel"]
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)
    # 计算 30 以内可以被 3 整除的整数
    b = [i for i in range(30) if i % 3 == 0]
    print(b)
    # 字典(dict)推导式
    c = {key:len(key) for key in names}
    print(c)
    # 平方字典
    d = {i:i**2 for i in range(100) if i % 3 == 0}
    print(d)

    # 集合(set)推导式
    e = {i**2 for i in (1, 2, 3)}
    print(e)
    f = {char for char in 'abcdefghijklmnopq' if char not in 'aeiou'} # 集合无序的
    print(f)

    # 元组(tuple)推导式
    g = (x+1 for x in range(10) if x % 3 == 0) # 返回的是生成器对象
    print(tuple(a)) # 使用 tuple() 函数，可以直接将生成器对象转换成元组


def iterator_base_test():
    """Python3 迭代器与生成器
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
    __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__()
    方法并通过 StopIteration 异常标识迭代的完成。
    __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象
    """
    # 创建迭代器对象:
    a = [1, 2, 3, 4, 5]
    it = iter(a) # 创建迭代器对象
    print(next(it)) # 输出迭代器的下一个元素

    # for x in it: # 通过迭代器进行遍历
    #     print(x, end="  ")
    while True:
        try:
            print(next(it))
        except StopIteration: # StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
            print("iter end")
            # sys.exit()
            break

    class Number(object):
        """实现一个迭代器数字类"""

        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration
    num = Number()
    it2 = iter(num)
    # print("Number:{}".format(next(it2)))
    # print("Number:{}".format(next(it2)))
    # print("Number:{}".format(next(it2)))
    for i in it2:
        print("Number:{}".format(i), end=",")
    print("")

    # 生成器:在 Python 中，使用了 yield 的函数被称为生成器（generator）。
    # yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
    # 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    # 当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
    # 然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
    # 调用一个生成器函数，返回的是一个迭代器对象。

    # 下面是一个简单的示例，展示了生成器函数的使用：
    # 如教程所说，迭代器和生成器算是 Python 一大特色，其核心是基于迭代器协议来的。
    # 而平时我们经常使用的 for in 循环体，本质就是迭代器协议的一大应用。
    # 同时 Python 内置的集合类型（字符、列表、元组、字典）都已经实现了迭代器协议，所以才能使用 for in 语句进行迭代遍历。for in 循环体在遇到 StopIteration 异常时，便终止迭代和遍历。
    # 再说下可迭代、迭代器、生成器三个概念的联系和区别。
    # 1、可迭代概念范围最大，生成器和迭代器肯定都可迭代，但可迭代不一定都是迭代器和生成器，比如上面说到的内置集合类数据类型。可以认为，在 Python 中，只要有集合特性的，都可迭代。
    # 2、迭代器，迭代器特点是，均可以使用 for in 和 next 逐一遍历。
    # 3、生成器，生成器一定是迭代器，也一定可迭代。
    # 至于 Python 中为何要引入迭代器和生成器，除了节省内存空间外，也可以显著提升代码运行速度。

    # yield 是 Python 中一个非常有用的关键字，它用于定义生成器函数并返回生成器对象。
    # 当生成器函数执行到 yield 关键字时，它将将当前函数状态保存为暂停状态，并向调用方返回一个值 a，
    # 之后程序流程将被挂起，直到下次通过 next() 函数调用该生成器对象时再恢复执行状态。
    # 在斐波那契数列生成器函数中，每次执行到 yield a 时，都会生成当前数列的第一个数字 a 并返回给
    # 调用方。
    def countdown(n):
        """countdown 函数是一个生成器函数。它使用 yield 语句逐步产生从 n 到 1 的倒数数字。
        在每次调用 yield 语句时，函数会返回当前的倒数值，并在下一次调用时从上次暂停的地方继续执行。
        通过创建生成器对象并使用 next() 函数或 for 循环迭代生成器，我们可以逐步获取生成器函数产生的值。在这个例子中，我们首先使用 next() 函数获取前三个倒数值，然后通过 for 循环获取剩下的两个倒数值。
        生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。
        此外，生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。
        """
        while n > 0:
            # 打个比方的话，yield有点像断点。
            # 加了yield的函数，每次执行到有yield的时候，会返回yield后面的值 并且函数会暂停，
            # 直到下次调用或迭代终止；
            # yield后面可以加多个数值（可以是任意类型），但返回的值是元组类型的。
            yield n
            n -= 1
    generator = countdown(5) # 创建生成器对象
    print(next(generator)) # 生成器/迭代器
    print(next(generator))
    for value in generator:
        print(value)

a = ["This is a global variable"]

def function_base_test():
    """函数
    参数传递：
    在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：
    """
    a = [1, 2, 3] # [1,2,3] 是 List 类型
    a = "123" # “123” 是 str 类型
    # 而变量 a 是没有类型，它仅仅是一个对象的引用（一个指针），
    # 可以是指向 List 类型对象，也可以是指向 String 类型对象。

    # 可更改(mutable)与不可更改(immutable)对象
    # 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
    # 而 list,dict 等则是可以修改的对象。
    # 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    # 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
    # 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
    # python 函数的参数传递：
    # 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
    # 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
    def immutable_obj_test(a):
        """在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
        可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），
        在函数内部修改形参后，形参指向的是不同的 id。"""
        print("before a:{} id:{}".format(a, id(a)))
        a = 10
        print("after a:{} id:{}".format(a, id(a)))
        return a
    h = 5
    immutable_obj_test(h)
    print("h:%d" % (h))
    def mutable_obj_test(l):
        """而 list,dict 等则是可以修改的对象
        传入函数的和在末尾添加新内容的对象用的是同一个引用。"""
        print("before l:{} id:{}".format(a, id(a)))
        l.append("New Item")
        print("after l:{} id:{}".format(a, id(a)))
        return
    i = [1, 2, 3]
    mutable_obj_test(i) # 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。
    print(i)

    # 以下是调用函数时可使用的正式参数类型：
    # 必需参数
    def fun2(a):
        print(a)
    fun2(1)
    # 关键字参数(使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。)
    def fun3(name, age, grade):
        print("before name:{} age:{} grage:{}".format(name, age, grade))
        name = None
        age = 18
        grade = 100
        print("afger name:{} age:{} grage:{}".format(name, age, grade))
    fun3(grade=200, name="ABC", age=19)

    # 默认参数(调用函数时，如果没有传递参数，则会使用默认参数。)
    def fun4(name="KimJongEn", age="1980", people="30million"):
        print("before name:{} age:{} people:{}".format(name, age, people))
        name += ",South Korean"
        age += str(18)
        people += str(100)
        print("after name:{} age:{} people:{}".format(name, age, people))
    fun4()

    # 不定长参数
    def fun5(name, *args):
        """一个 * 不定长参数默认是元组类型"""
        print(name)
        print("args:{} type:{} id:{}".format(args, type(args), id(args)))
    fun5("Jack Ma", 1, 2, 3, 4, 5)

    def fun6(name, **kwargs):
        """加了两个星号 ** 的参数会以字典的形式导入。"""
        print(name)
        print("kwargs:{} type:{} id:{}".format(kwargs, type(kwargs), id(kwargs)))
    fun6("不知妻美刘强东", param1={1:"JD", 2:"Rape", 3:"江苏徐州", 4:"中国人民大学"}, param2="abc")
    fun6("一般家庭马化腾", paramxyz={1:"copy-super man"})

    def fun7(a, b, *, c):
        """声明函数时，参数中星号 * 可以单独出现，例如:
        如果单独出现星号 *，调用函数时则星号 * 后的参数必须用关键字传入："""
        return a + b + c
    # print(fun7(1, 2, 3)) # ERROR
    print(fun7(1, 2, c=3))

    #匿名函数
    # Python 使用 lambda 来创建匿名函数。
    # 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    # lambda 只是一个表达式，函数体比 def 简单很多。
    # lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
    # lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    # 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。
    # lambda 函数的语法只包含一个语句，如下：
    # lambda [arg1 [,arg2,.....argn]]:expression
    x = lambda a : a + 10
    print(x(5))

    sum = lambda arg1,arg2 : arg1 + arg2
    print(sum(10, 20))

    def fun8(n):
        """我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
        以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：
        :param
        :return 返回一个 lambda 表达式
        """
        return lambda z : z * n
    double = fun8(2)
    triple = fun8(3)
    print("double:", double(2))
    print("triple:", triple(2))

    # Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，
    # 不能使用关键字参数的形式。
    def fun9(a, b, /, c, d, *, e, f):
        """在以下的例子中，形参 a 和 b 必须使用指定位置参数，
        c 或 d 可以是位置形参或关键字形参，
        而 e 和 f 要求为关键字形参:"""
        print(a, b, c, d, e, f)
    fun9(1, 2, c=30, d=40, e=50, f=60)
    print(fun9.__doc__)

    def fun10():
        global a # 全局变量
        # a = 2 # 局部变量
        print(a)
    fun10()

    # lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。
    numbers = [1, 2, 3, 4, 5]
    square = list(map(lambda  x : x**2, numbers))
    print(square)
    even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
    print(even_numbers)

    from functools import reduce
    product = reduce(lambda x, y : x * y, numbers) # 使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：

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
            start = time.time()
            result = origin_fun(*args, **kwargs)
            end = time.time()
            print("time usage:{}".format(end - start))
            return result
        return wrapper

    @time_logger
    def print_hello(n):
        for i in range(n):
            print("hello %d" % i)
    print(print_hello(3))

    def repeat(n):
        """带参数的装饰器 repeat """
        def decrator(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decrator

    @repeat(5)
    def greet(name):
        print(f"Hello {name}")
    greet("Bob")

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
    my_function()

def data_structure_test():
    """Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，
    一句话概括即：列表可以修改，而字符串和元组不能。
    """
    import collections
    class Stack(object):
        """通过列表实现栈的功能"""
        def __init__(self):
            self.stack = []

        def push(self, item):
            self.stack.append(item)

        def pop(self):
            if not self.is_empty():
                return self.stack.pop()
            else:
                raise IndexError("pop from empty stack")

        def peek(self):
            if not self.is_empty():
                return self.stack[-1]
            else:
                raise IndexError("pop from empty stack")

        def is_empty(self):
            return len(self.stack) == 0

        def size(self):
            return len(self.stack)

    class Queue(collections.deque):
        """在 Python 中，列表（list）可以用作队列（queue），但由于列表的特点(TODO:链表???)，
        直接使用列表来实现队列并不是最优的选择。
        队列是一种先进先出（FIFO, First-In-First-Out）的数据结构，意味着最早添加的元素最先被移除。
        使用列表时，如果频繁地在列表的开头插入或删除元素，性能会受到影响，因为这些操作的时间复杂度是 O(n)。
        为了解决这个问题，Python 提供了 collections.deque，它是双端队列，可
        以在两端高效地添加和删除元素
        """
        pass
    # 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
    for i, v in enumerate([1, 2, 3]):
        print("i:{} v:{}".format(i, v))
    # 同时遍历两个或更多的序列，可以使用 zip() 组合：
    for p, q in zip([1, 2, 3], [4, 5, 6]):
        print(p, q)

    # 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
    for i in reversed(range(1, 10, 2)):
        print(i, end=",")
    print("")

def module_base_test():
    """TODO:python 模块"""
    import sys # python 标准库
    print(sys.path)
    # 一个模块被另一个程序第一次引入时，其主程序将运行。
    # 如果我们想在模块被引入时，模块中的某一程序块不执行，
    # 我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
    #  每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
    # 说明：__name__ 与 __main__ 底下是双下划线

    # 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
    print(dir(sys))
    # print(sys.ps1) # 变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:
    # print(sys.ps2)

    # 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，
    # 主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
    # __path__ # 这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦
    # __all__ # 包中的所有的模块名需要写在里面

def package_base_test():
    """TODO:包测试"""
    pass

def file_op_base_test():
    """文件操作"""
    import os
    import os.path
    f = open("foo.txt", "w") # 在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
    f.write("This is a file test")
    f.close() # 使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
    f = open("foo.txt", "r")
    line = f.readline()
    f.seek(0) # offset 表示相对于 whence 参数的偏移量，from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，
    print("lines:{}".format(f.readlines()))
    print("read:", line)
    print("position:", f.tell())
    # 文件系统 API
    f.flush() # file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
    print("fileno:", f.fileno()) # file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
    print("isatty:", f.isatty()) # file.isatty()如果文件连接到一个终端设备返回 True，否则返回 False。
    # f.truncate() # file.truncate([size]) 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。
    f.close() # file.close() 关闭文件。关闭后文件不能再进行读写操作。
    # 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。
    # 而且写起来也比 try - finally 语句块要简短:
    with open("foo.txt", 'r') as f:
        str = f.readline()
        print(str)
    print("closed:", f.closed)

    l = []
    def getPythonFile(path, l):
        """检索指定目录下的 python 文件
        :param path
        :param l
        """
        fileList = os.listdir(path)
        try:
            for file in fileList:
                print("file:", file)
                path_temp = os.path.join(path, file)
                if os.path.isdir(path_temp): # 递归遍历
                    print("directory:", path_temp)
                    getPythonFile(path_temp, l)
                elif path_temp[path_temp.rfind(".")+1:].lower() == 'py':
                    l.append(path_temp)
        except PermissionError:
            pass
    getPythonFile(".", l)
    print("L:", l)

def os_base_test():
    """puthon os 模块
    Python3 OS 文件/目录方法
    """
    import os


if __name__ == '__main__':
    # base_info()
    # str_op()
    # enter_test()
    # var_type_test()
    # list_base_test()
    # tuple_base_test()
    # set_base_test()
    # dict_base_base_test()
    # bytes_base_test()
    # var_type_change()
    # operator_base_test()
    # math_base_test()
    # condition_control_test()
    # iterator_base_test()
    # function_base_test()
    # decorator_base_test()
    # data_structure_test()
    # module_base_test()
    # package_base_test()
    # file_op_base_test()
    os_base_test()




else:
    print("我来自另一模块")