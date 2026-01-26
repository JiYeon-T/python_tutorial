import keyword
import math
import os
import time
import datetime

# 导入模块
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *


# https://www.runoob.com/python3/python3-basic-syntax.html
import random
import sys
import time
import timeit


def base_info():
    """python 关键字"""
    # print(keyword.kwlist)

    # 内容太多, 一行写不下时使用 \ 进行换行
    item1 = 1
    item2 = 2
    item3 = 3
    sum = item1 + 2 + 3 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + \
          item2 + 2 + 3 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + \
          item3
    print(f"sum = {sum}")

    # Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    name = "Lebron James"
    print("first:{} last:{}".format(name[0], name[-1]))

    # if else 可以写在同一行
    print(f"sum={sum} 是 {'偶数' if sum % 2 == 0 else '奇数'}")


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

    print("\110") #特殊字符:\yyy 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
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


def str_test2():
    str1 = "1B7E8251-2877-41C3-B46E-CF057C562023"
    str2 = "bafdfkdljf     1B7E8251-2877-41C3-B46E-CF057C562023; selected, bacdafa"
    print(f"str1:{str1} str2:{str2}")
    print(f"UPPER:{str1.upper()}")
    if str1 in str2:
        print("Yes")
    else:
        print("No")


def terminal_input_test():
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
    def list_tuidao():
        print(["ELEM:" + str(x) for x in e])
        print(["result:"+str(i) for i in range(100) if i % 3 == 0 and i % 10 == 0], end="\n\n")
    list_tuidao()

    def index_val_test():
        # 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
        for i, v in enumerate([1, 2, 3]):
            print("i:{} v:{}".format(i, v))
    # index_val_test()

    # 同时遍历两个或更多的序列，可以使用 zip() 组合：
    def traverse_more_seq():
        for p, q in zip([1, 2, 3], [4, 5, 6, 7, 8, 9]):
            print(p, q)
        print("\n\n")
    # traverse_more_seq() # 也仅遍历前 3 个元素, 因为 seq1 只有三个元素

    # 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
    def reverse_transverse():
        for i in reversed(range(1, 10, 2)):
            print(i, end=",")
        print("\n\n")
    # reverse_transverse()

    # 按顺序遍历可以使用 sorted(), 返回一个已排序的序列，并不修改原值
    def sorted_traverse():
        print(f"before:{a}")
        a[0] = 100
        for i in sorted(a):
            print(i, end=",")
        print("\n\n")
    sorted_traverse()

    def list_op_test1():
        l = [1, 2, 3, 4, 5]  # pyhton 中列表默认传递的就是引用, 如果想使用值传递, 则要切分

        def modify_list_elem(l):
            l[0] = 10
            print(l)

        # modify_list_elem(l[:])
        # print(l)
    # list_op_test1()

    def list_op_test2():
        l = [1, 2, 3, 4, 5]
        print(l)
        l.remove(1)
        print(l)
        l.append(1)
        print(l)
        # l.insert(0, 1)  # 列表的插入
        l.insert(0, 1)  # 列表的插入
        l.insert(0, 1)  # 列表的插入
        l.insert(0, 1)  # 列表的插入
        l.insert(-1, 100)
        print(l)
        for ix in l:
            if ix == 2:
                l.remove(2)
        # l.remove(5)
        print(l)

        del l[0]  # 删除
        print(l)
        s = list(set(l))  # set, unique
        print(s)

        print(type(s))
        item = 999
        s.append(item)  # 插入元素
        print(s)
        item = s.pop()  # 从列表中弹出一个元素
        print(s)
        print(item)
    # list_op_test2()


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
    def var_test():
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
    # var_test()

    def repr_test():
        """"""
        from datetime import datetime
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
        present = datetime.now()
        print(f"str:{str(present)}")
        print(f"repr:{repr(present)}", end="\n\n")
    repr_test()

    def eval_test():
        # 注意： eval() 函数执行的代码具有潜在的安全风险。
        # 如果使用不受信任的字符串作为表达式，则可能导致代码注入漏洞，
        # 因此，应谨慎使用 eval() 函数，并确保仅执行可信任的字符串表达式。
        x = 5
        print(eval("1 + 3 * x"))# TODO:eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
    # eval_test()

    # tuple() # 起始就是这些数据类型的构造函数
    # list()
    # set()
    # dict()

    # frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
    h = frozenset([1, 2, 3, 4, 5])

    def character_display_test():
        print(f"char:{chr(32)}") # chr(x) 将一个整数转换为一个字符
        print(f"ord:{ord('a')}") # ord(x) 将一个字符转换为它的整数值
        print(f"""hex:{hex(ord('a'))}""") # ord(x) 将一个字符转换为它的整数值
        print(f"""oct:{(ord('a'))}""", end="\n\n") # oct(x) 将一个整数转换为一个八进制字符串
    character_display_test()

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


def python_comprehension():
    """"""
    # Python 推导式:Python 支持各种数据结构的推导式：
    # 列表(list)推导式
    # [表达式 for 变量 in 列表]
    # [out_exp_res for out_exp in input_list] 或者 :
    # [表达式 for 变量 in 列表 if 条件]
    # [out_exp_res for out_exp in input_list if condition]
    names = ["ABCD", "E", "Alice", "Bob", "Angel"]
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names, sep=",", end="\n\n")

    # 计算 30 以内可以被 3 整除的整数
    b = [i for i in range(30) if i % 3 == 0]
    print(b, end="\n\n")

    # 字典(dict)推导式
    # { key_expr: value_expr for value in collection } 或:
    # { key_expr: value_expr for value in collection if condition }
    c = {key:len(key) for key in names if len(key) >= 3}
    print(f"{type(c)}") # <class 'dict'>
    print(c, end="\n\n")
    # 平方字典
    d = {i:i**2 for i in range(5) if i % 3 == 0}
    print(d, end="\n\n")

    # 集合(set)推导式
    # { expression for item in Sequence } 或:
    # { expression for item in Sequence if conditional }
    e = {i**2 for i in (1, 2, 3)}
    print(f"type:{type(e)}")  # type:<class 'set'>
    print(e, end="\n\n")
    # if
    f = {char for char in 'abcdefghijklmnopq' if char not in 'aeiou'}  # 集合无序的
    print(f, end="\n\n")

    # 元组(tuple)推导式
    # (expression for item in Sequence ) 或：
    # (expression for item in Sequence if conditional )
    g = (x**2 for x in range(10) if x % 3 == 0)  # 元组推导式返回的是生成器对象
    print(type(g), g, sep=", ") # <generator object python_comprehension.<locals>.<genexpr> at 0x000001E79FC98120>
    print(tuple(g), end="\n\n") # 使用 tuple() 函数，可以直接将生成器对象转换成元组


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

    # for x in it: # 迭代器可以通过 for 进行遍历
    #     print(x, end="  ")
    while True:
        try:
            print(next(it), end=",")
        except StopIteration: # StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
            print("iter end", end="\n\n")
            # sys.exit()
            break

    class Number(object):
        """实现一个迭代器数字类，实现 __iter__ 和 __next__ 方法即可"""
        def __init__(self, max=10):
            self.max = max
            print("iter init")

        def __iter__(self):
            """
            当显示调用 iter() 方法或者使用 for 循环遍历的时候会调用 __iter__ 方法
            :return 返回迭代器对象
            """
            self.a = 1
            print("iter started")
            return self

        def __next__(self):
            if self.a <= self.max:
                print("iter iterated")
                x = self.a
                self.a += 1
                return x
            else: # 通过触发该异常来表示迭代结束
                print("iter stopped")
                raise StopIteration

    def self_iter_test():
        """自己写的迭代器测试"""
        num = Number(max=10)
        # it2 = iter(num)
        # for i in it2:
        for i in num:
            print("{}".format(i), end=",")

    self_iter_test()

    # 生成器:在 Python 中，使用了 yield 的函数被称为生成器（generator）。
    # yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，
    # 而不是一次性返回所有结果。
    # 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    # 当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
    # 然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
    # 调用一个生成器函数，返回的是一个迭代器对象。

    # 下面是一个简单的示例，展示了生成器函数的使用：
    # 如教程所说，迭代器和生成器算是 Python 一大特色，其核心是基于迭代器协议来的。
    # 而平时我们经常使用的 for in 循环体，本质就是迭代器协议的一大应用。
    # 同时 Python 内置的集合类型（字符、列表、元组、字典）都已经实现了迭代器协议，
    # 所以才能使用 for in 语句进行迭代遍历。for in 循环体在遇到 StopIteration 异常时，便终止迭代和遍历。
    # 再说下可迭代、迭代器、生成器三个概念的联系和区别。
    # 1、可迭代概念范围最大，生成器和迭代器肯定都可迭代，但可迭代不一定都是迭代器和生成器，
    # 比如上面说到的内置集合类数据类型。可以认为，在 Python 中，只要有集合特性的，都可迭代。
    # 2、迭代器，迭代器特点是，均可以使用 for in 和 next 逐一遍历。
    # 3、生成器，生成器一定是迭代器，也一定可迭代。
    # 至于 Python 中为何要引入迭代器和生成器，除了节省内存空间外，也可以显著提升代码运行速度。

    # yield 是 Python 中一个非常有用的关键字，它用于定义生成器函数并返回生成器对象。
    # 当生成器函数执行到 yield 关键字时，它将将当前函数状态保存为暂停状态，并向调用方返回一个值 a，
    # 之后程序流程将被挂起，直到下次通过 next() 函数调用该生成器对象时再恢复执行状态。
    # 在斐波那契数列生成器函数中，每次执行到 yield a 时，都会生成当前数列的第一个数字 a 并返回给
    # 调用方。
    def countdown(n):
        """countdown 函数是一个生成器函数。
        它使用 yield 语句逐步产生从 n 到 1 的倒数数字。
        在每次调用 yield 语句时，函数会返回当前的倒数值，并在下一次调用时从上次暂停的地方继续执行。
        通过创建生成器对象并使用 next() 函数或 for 循环迭代生成器，我们可以逐步获取生成器函数产生的值。
        在这个例子中，我们首先使用 next() 函数获取前三个倒数值，然后通过 for 循环获取剩下的两个倒数值。
        生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。
        此外，生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。
        """
        while n > 0:
            # yield有点像断点。加了yield的函数，每次执行到有yield的时候，会返回yield后面的值 并且函数会暂停，
            # 直到下次调用或迭代终止, yield后面可以加多个数值（可以是任意类型），但返回的值是元组类型的。
            yield n # 函数直行到这里返回 n
            n -= 1

    generator = countdown(5) # 创建生成器对象
    # print(next(generator)) # 使用 next() 方法迭代 生成器/迭代器
    # print(next(generator), end="'\n'and more:'\n'")
    # for value in generator: # 继续迭代剩余元素
    #     print(value)

    def fibonacci(n):
        """
        通过生成器函数实现计算斐波那契数列
        本质上还是迭代的方式计算，效率比递归高很多, 算法时间复杂度:O(n)
        """
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return
            print(f"[{counter}] = {a}", end=",")
            yield a
            a, b = b, a + b
            counter += 1

    def calculate_fibnonacci(num):
        f = fibonacci(num)  # 生成器函数
        while True:
            try:
                print(f"{next(f)}")
            except StopIteration:
                sys.exit()

    # calculate_fibnonacci(2)

    # 迭代器和生成器具体应用场景，就凡是需要提升运行效率或节约内存资源，且遍历的数据是集合形式的，都可以考虑。
    # 另外一个小众的使用场景，是变相实现协程的效果，即在同一个线程内，实现不同任务交替执行
    def task1():
        print('task1 开始执行')
        #other code
        yield # 直行到这里后暂停并返回，等待下次执行

    def task2():
        print('task2 开始执行')
        #other code
        yield

    def coroutine_test(n):
        """简单的协程测试"""
        g1 = task1()
        g2 = task2()
        for i in range(n):
            next(g1)
            next(g2)

    # coroutine_test(3)

def with_test():
    """
    https://www.runoob.com/python3/python3-with-keyword.html
    在 Python 编程中，资源管理是一个重要但容易被忽视的环节。
    with 关键字为我们提供了一种优雅的方式来处理文件操作、数据库连接等需要明确释放资源的场景。
    with 是 Python 中的一个关键字，用于上下文管理协议（Context Management Protocol）。
    它简化了资源管理代码，特别是那些需要明确释放或清理的资源（如文件、网络连接、数据库连接等）。
    """
    def file_open_test():
        """最基基础的文件打开操作，有代码冗长,容易造成资源泄露等问题"""
        file = open('examble.txt', 'r')
        try:
            content = file.read()
        finally:
            file.close()

    def file_open_with():
        """with 语句通过上下文管理协议（Context Management Protocol）解决了这些问题：
        """
        with open('example.txt', 'r') as file:
            content = file.read()

    # with 语句的工作原理 ———— 上下文管理协议
    # with 语句背后是 Python 的上下文管理协议，该协议要求对象实现两个方法：
    # __enter__()：进入上下文时调用，返回值赋给 as 后的变量
    # __exit__()：退出上下文时调用，处理清理工作
    # __exit__() 方法接收三个参数：
    # exc_type：异常类型
    # exc_val：异常值
    # exc_tb：异常追踪信息
    # 如果 __exit__() 返回 True，则表示异常已被处理，不会继续传播；返回 False 或 None，异常会继续向外传播。

    def file_open_with_test2():
        """可以同时打开多个文件
        文件操作结束后自动关闭"""
        with open('in.txt', 'r') as in_file, open('out.txt', 'w+') as out_file:
            content = in_file.read()
            out_file.write(content.upper())

    def db_open_test():
        """可是使用 with 实现数据库的连接操作, 结束后连接自动关闭"""
        import sqlite3
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * from users')
            result = cursor.fetchall()

    def lock_with_test():
        import threading
        lock = threading.Lock()
        with lock:
            # 临界区代码
            print('Thread safety execute')

    class TimerUsage():
        """
        可以通过实现 __enter__ 和 __exit__ 方法创建自定义的上下文管理器
        """
        import time

        def __enter__(self):
            self.start = time.time()

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.end = time.time()
            print(f'use:{self.end - self.start} sec')
            return False # 异常向外传播

    def timer_test():
        counter = TimerUsage()
        with counter:
            time.sleep(2)
    # timer_test()

    # 使用 contextlib 模块
    # Python 的 contextlib 模块提供了更简单的方式来创建上下文管理器：
    from contextlib import contextmanager
    @contextmanager # 装饰器
    def tag(text):
        print(f'{text} start')
        yield
        print(f'{text} end')

    def contextmanager_test():
        with tag("context"):
            print("测试")

    contextmanager_test()

a = ["This is a global variable"]

def function_base_test():
    """函数
    参数传递：
    在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：
    函数传参:
    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
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
        """在 python 中，strings, tuples, 和 numbers 是不可更改的对象（不可变对象），
        可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），
        在函数内部修改形参后，形参指向的是不同的 id。"""
        print("before a:{} id:{}".format(a, id(a)))  # 指向的是同一个对象
        a = 10  # # 一个新对象
        print("after a:{} id:{}".format(a, id(a)))
        return a
    # h = 5
    # immutable_obj_test(h)
    # print("h:%d" % (h))

    def mutable_obj_test(l):
        """而 list,dict 等则是可以修改的对象(可变对象)
        传入函数的和在末尾添加新内容的对象用的是同一个引用。"""
        print("before l:{} id:{}".format(a, id(a)))
        l.append("New Item")  # 修改原对象中的成员后, 仍然指向原对象
        print("after l:{} id:{}".format(a, id(a)), end="\n\n")
        return
    # i = [1, 2, 3]
    # mutable_obj_test(i) # 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。
    # print(i)

    # 以下是调用函数时可使用的正式参数类型：
    # 1.必需参数
    def fun2(a):
        print(a)
    # fun2(1)

    # 2.关键字参数(使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。)
    def fun3(name, age, grade):
        print("before name:{} age:{} grage:{}".format(name, age, grade), end="\n\n")
        name = None
        age = 18
        grade = 100
        print("afger name:{} age:{} grage:{}".format(name, age, grade), end="\n\n")
    # fun3(grade=200, name="ABC", age=19)

    # 3.默认参数(调用函数时，如果没有传递参数，则会使用默认参数。)
    def fun4(name="KimJongEn", age="1980", people="30million"):
        print("before name:{} age:{} people:{}".format(name, age, people))
        name += ",South Korean"
        age += str(18)
        people += str(100)
        print("after name:{} age:{} people:{}".format(name, age, people), end="\n\n")
    # fun4()

    # 4.不定长参数
    def fun5(name, *args):
        """一个 * 不定长参数默认是元组类型"""
        print(name)
        print("args:{} type:{} id:{}".format(args, type(args), id(args)), end="\n\n")
    # fun5("Jack Ma", 1, 2, 3, 4, 5)

    def fun6(name, **kwargs):
        """加了两个星号 ** 的参数会以字典的形式导入。"""
        print("name:", name)
        print("kwargs:{} type:{} id:{}".format(kwargs, type(kwargs), id(kwargs)), end="\n\n")
    # fun6("不知妻美刘强东", param1={1:"JD", 2:"Rape", 3:"江苏徐州", 4:"中国人民大学"}, param2="abc")
    # fun6("一般家庭马化腾", paramxyz={1:"copy-super man"})

    def fun7(a, b, *, c):
        """声明函数时，参数中星号 * 可以单独出现，例如:
        如果单独出现星号 *，调用函数时则星号 * 后的参数必须用关键字传入："""
        return a + b + c
    # print(fun7(1, 2, 3)) # ERROR
    # print(fun7(1, 2, c=3))

    #匿名函数
    # Python 使用 lambda 来创建匿名函数。
    # 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    # lambda 只是一个表达式，函数体比 def 简单很多。
    # lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
    # lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    # 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。
    # lambda 函数的语法只包含一个语句，如下：
    # lambda [arg1 [,arg2,.....argn]]:expression
    def lambda_test():
        x = lambda a : a + 10
        print(x(5))

        sum = lambda arg1,arg2 : arg1 + arg2
        print(sum(10, 20))

        # lambda 也可以使用默认参数以及关键字参数
        square = lambda x=1, y=2 : x**2 + y** 3
        print(square(x=3, y=4) , end="\n\n")
    # lambda_test()

    def fun8(n):
        """可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
        以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：
        :param
        :return 返回一个 lambda 表达式
        """
        return lambda z : z * n
    # double = fun8(2)
    # triple = fun8(3)
    # print("double:", double(2))
    # print("triple:", triple(2))

    # Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，
    # 不能使用关键字参数的形式。
    def fun9(a, b, /, c, d, *, e, f):
        """在以下的例子中，形参 a 和 b 必须使用指定位置参数，
        c 或 d 可以是位置形参或关键字形参，
        而 e 和 f 要求为关键字形参:"""
        print(a, b, c, d, e, f)
    fun9(1, 2, c=30, d=40, e=50, f=60)

    def fun10():
        """这是一个全局变量测试函数"""
        global a # 全局变量
        # a = 2 # 局部变量
        print(a)
    # fun10()

    # lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。
    def lambda_test2():
        numbers = [1, 2, 3, 4, 5]
        square = list(map(lambda  x : x**2, numbers))
        print(f"square:{square} type:{type(square)}")

        even_numbers = list(filter(lambda x : x % 2 == 0, numbers)) # 找到 list 的偶数, filter(fun, array)
        print(f"even:{even_numbers}")

        from functools import reduce
        # 使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：
        # python 内置函数:reduce 函数查看函数定义,
        # reduce 函数累加 计算 numbers 的和
        product = reduce(lambda x, y : x * y, numbers)
        print(f"product:{product}")

    # lambda_test2()

    def fun_doc_test():
        # __doc__ 打印函数的说明文档
        print(fun10.__doc__, end="\n\n")
    # fun_doc_test()

def kwargs_example():
    # kwargs 是 python 函数中关键字参数的缩写，它是一个字典，
    # 用于存储在函数调用时传递的额外关键字参数。
    # 在函数定义中，使用 *kwargs 来表示 kwargs 参数。
    # 在调用函数时，使用格式 func_name(**kwargs) 来传递额外关键字参数。

    def fun(name, **kwargs):
        """字典类型形参测试"""
        print(name)
        # 访问字典
        for k, v in kwargs.items():
            print(f"k:{k, type(k)} v:{v, type(v)}")

    def fun2(shape, **kwargs):
        """访问字典"""
        area = 0
        if shape == "square":
            area = kwargs["width"] ** 2
        elif shape == 'rectangle':
            area = kwargs['width'] * kwargs['height']
        print(f"area:{area}")
        return area

    fun('Lee', score=110)  # k:('score', <class 'str'>) v:(456, <class 'int'>)
    fun2('square', width=4)  # area:16
    fun2('rectangle', width=3, height=30)  # area:90

def standard_input_and_output_test():
    """
    https://www.runoob.com/python3/python3-inputoutput.html
    str()： 函数返回一个用户易读的表达形式。
    repr()： 产生一个解释器易读的表达形式。
    """
    l = [1, 2.0, 1/3, 4, 5]
    # print(f"{str(l).rjust(10)}")
    # print(f"{repr(l)}")

    # 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
    # 类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
    s = "1"
    print(s.rjust(10))
    print(s.rjust(10, '-'))
    print(s.center(10, '-'))
    print(s.ljust(10, '-'))
    # 另一个方法 zfill(), 它会在数字的左边填充 0
    print(s.zfill(10))

    # format() 方法格式化输出字符串
    # 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。
    print("{0:10} => {1:10d}".format("Hello", 125))
    # 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
    # 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
    table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
    print('Runoob:{0[Runoob]:d} Google:{0[Google]:d} Taobao:{0[Taobao]:d}'.format(table))
    # 也可以这样写: 通过在 table 变量前使用 ** 来实现相同的功能
    print('Runoob:{Runoob:d}'.format(**table))

    import math
    # 旧式字符串格式化
    # % 操作符也可以实现字符串格式化。
    # 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
    #  大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().
    print("PI = %5.3f" % math.pi)  # 小数点后 3 位

    def key_input_test():
        str = input("请输入:")
        print(str)
    key_input_test()

def file_op_base_test():
    """文件操作
    https://www.runoob.com/python3/python3-file-methods.html
    """
    import os
    import os.path
    def write_test():
        f = open("foo.txt", "w") # 在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
        f.write("This is a file test")
        f.close() # 使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
    write_test()

    # 其他文件操作 api 测试:
    f = open("foo.txt", "r")
    line = f.readline()
    # offset 表示相对于 whence 参数的偏移量，from_what 的值,
    # 如果是 0 表示开头,
    # 如果是 1 表示当前位置, 2 表示文件的结尾，
    f.seek(0)
    print("lines:{}".format(f.readlines()))
    print("read:", line)
    # f.tell() 用于返回文件当前的读/写位置（即文件指针的位置）。
    # 文件指针表示从文件开头开始的字节数偏移量。f.tell() 返回一个整数，表示文件指针的当前位置。
    print("position:", f.tell())
    # 文件系统 API
    f.flush() # file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
    # file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型),
    # 可以用在如os模块的read方法等一些底层操作上。
    print("fileno:", f.fileno())
    print("isatty:", f.isatty()) # file.isatty()如果文件连接到一个终端设备返回 True，否则返回 False。
    # f.truncate()
    # file.truncate([size]) 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；
    # 截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。
    f.close() # file.close() 关闭文件。关闭后文件不能再进行读写操作。

    def with_file_test():
        # 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。
        # 而且写起来也比 try - finally 语句块要简短:
        with open("foo.txt", 'r') as f:
            str = f.readline()
            print(f"read:{str}")
    with_file_test()

    print(f"closed:{f.closed}\n\n")

    l = []
    def getPythonFile(path, l):
        """
        遍历目录
        检索指定目录下的 python 文件
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
        except PermissionError as e:
            print(repr(e))
    getPythonFile("../2_advanced/process", l)
    print("L:", l)

def os_base_test():
    """puthon os 模块
    os 模块是跨平台的
    Python3 OS 文件/目录操作方法
    https://www.runoob.com/python3/python3-os-file-methods.html
    """
    import os, sys, stat
    path = "./foo.txt"
    print("access:", os.access(path, os.F_OK)) # os.access(path, mode) 检验权限模式
    print("access:", os.access(path, os.R_OK))
    print("access:", os.access(path, os.W_OK))
    print("access:", os.access(path, os.X_OK))
    fd = open(path, 'r')
    # os.chdir(path) # os.chdir(path) 改变当前工作目录
    flags = stat.SF_NOUNLINK # 为文件设置标记，使得它不能被重命名和删除
    # os.chflags(path, flags) # os.chflags(path, flags) 设置路径的标记为数字标记。
    stat = stat.S_IXGRP # 设置文件可以通过用户组执行
    # os.chmod(path, stat) # os.chmod(path, mode) 更改权限
    # os.chown(path, uid, gid) # os.chown(path, uid, gid) 更改文件所有者
    # os.chroot(path) # os.chroot(path) 改变当前进程的根目录
    # os.close(fd) # os.close(fd) 关闭文件描述符 fd
    # os.closerange() # os.closerange(fd_low, fd_high) 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
    # os.dup(fd) # os.dup(fd) 复制文件描述符 fd
    # os.dup2(fd, sys.stdout) # os.dup2(fd, fd2) 将一个文件描述符 fd 复制到另一个 fd2
    # os.fchdir(fd) # os.fchdir(fd) 通过文件描述符改变当前工作目录
    # os.fchmod(fd, mode) # os.fchmod(fd, mode) 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
    # os.fchown(fd, uid, gid) # so.fchown(fd, uid, gid) 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
    # os.fdatasync(fd) # os.fdatasync(fd) 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
    # os.fdopen(fd) # os.fdopen(fd[, mode[, bufsize]]) 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
    # os.fpathconf(fd, name) # os.fpathconf(fd, name)返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
    # os.fstat(fd) # os.fstat(fd) 返回文件描述符fd的状态，像stat()。
    # print(f"fstat:{repr(os.fstat(fd.fileno()))}")
    # os.fstatvfs(fd) # os.fstatvfs(fd) 返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。
    # os.fsync(fd) # os.fsync(fd) 强制将文件描述符为fd的文件写入硬盘。
    # os.ftruncate(fd, 1024) # os.ftruncate(fd, length) 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
    print("cwd:", os.getcwd()) # os.getcwd() 返回当前工作目录
    print("cwdb:", os.getcwdb()) # os.getcwdb() 返回一个当前工作目录的Unicode对象
    # os.isatty(fd) # os.isatty(fd) 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
    # os.lchflags() # os.lchflags(path, flags) 设置路径的标记为数字标记，类似 chflags()，但是没有软链接
    # os.lchmod(path, mode) # os.lchmod(path, mode) 修改连接文件权限
    # os.lchown(path, uid, gid) # os.lchown(path, uid, gid) 更改文件所有者，类似 chown，但是不追踪链接。
    # os.link(src, dst) # os.link(src, dst) 创建硬链接，名为参数 dst，指向参数 src
    print("listdir:", os.listdir("../2_advanced/process/")) # os.listdir(path) 返回path指定的文件夹包含的文件或文件夹的名字的列表
    # os.lseek(fd, pos, how) # os.lseek(fd, pos, how) 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
    # os.lstat(path) # os.lstat(path) 像stat(),但是没有软链接
    # info = os.lstat(path)
    # print("major:", os.major(info.st_dev)) # os.major(device) 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
    # print("minor:", os.minor(info.st_dev)) # os.minor(device) 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
    # os.makedev(major, minor) # os.major(device) 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
    # os.mkdir(path) # os.mkdir(path[, mode]) 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
    # os.makedirs(path) # os.makedirs(path[, mode]) 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
    # os.mkfifo(path) # os.mkfifo(path[, mode]) 创建命名管道，mode 为数字，默认为 0666 (八进制)
    # os.mknod(path) # os.mknod(filename[, mode=0600, device]) 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
    # os.open(path) # os.open(file, flags[, mode]) 打开一个文件，并且设置需要的打开选项，mode参数是可选的
    # os.openpty() # os.openpty() 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
    # os.pathconf(path) # os.pathconf(path, name) 返回相关文件的系统配置信息。
    # os.pipe() # os.pipe() 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
    # os.popen() # os.popen(command[, mode[, bufsize]]) 从一个 command 打开一个管道
    # os.read() # os.read(fd, n)从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
    # os.readlink(path) # os.readlink(path) 返回软链接所指向的文件
    # os.remove(path) # os.remove(path) 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
    # os.removedirs(name) # os.removedirs(path) 递归删除目录。
    # os.rename(src, dst) # os.rename(src, dst) 重命名文件或目录，从 src 到 dst
    # os.renames(old, new) # os.renames(old, new) 递归地对目录进行更名，也可以对文件进行更名。
    # os.rmdir(path) # os.rmdir(path) 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
    # os.stat(path) # os.stat(path) 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
    # os.stat_float_times() # os.stat_float_times([newvalue]) 决定stat_result是否以float对象显示时间戳
    # os.statvfs(path) # os.statvfs(path) 获取指定路径的文件系统统计信息
    # os.symlink() # os.symlink(src, dst) 创建一个软链接
    # os.tcgetpgrp(fd) # os.tcgetpgrp(fd) 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
    # os.ttyname(fd) # os.ttyname(fd) 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
    # os.unlink(path) # os.unlink(path) 删除文件路径
    # os.utime(path) # os.utime(path, times) 返回指定的path文件的访问和修改的时间。
    # os.walk() # os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) 输出在文件夹中的文件名通过在树中游走，向上或者向下。
    # os.write() # os.write(fd, str) 写入字符串到文件描述符 fd中.返回实际写入的字符串长度
    # print("path:", os.path)
    # print("parent:", os.pardir) # os.pardir() 获取当前目录的父目录，以字符串形式显示目录名。
    # os.replace(src_name, dest_name) # os.replace() 重命名文件或目录。
    # os.startfile() # os.startfile() 用于在 Windows 上打开一个文件或文件夹。
    print(f"PATH:{os.getenv('PATH')}", sep=", ") # 获取环境变量
    print(f"LS:{os.system('ls -l')}") # 执行 shell 命令

    def os_path_test():
        """os.path 模块:
        os.path 模块是 Python 标准库中 os 模块的一部分，专门用于操作和处理文件路径。
        os.path 提供了一组强大的工具来对文件和目录路径进行各种操作，例如获取文件名、
        判断路径是否存在、路径拼接、路径规范化等。
        os.path 模块在跨平台操作系统中表现良好，使得同一段代码能够在不同操作系统
        （如 Windows、Linux、macOS）上运行时处理路径相关问题。
        https://www.runoob.com/python3/python3-os-path.html
        """
        print("\n\n\n")
        print(__file__) # 绝对路径
        # 路径操作
        print(os.path.abspath("."))# os.path.abspath(path)	将相对路径转换为绝对路径。
        print(os.path.basename(__file__)) # os.path.basename(path)	获取路径的最后一部分，即文件名。
        print(os.path.dirname(__file__)) # os.path.dirname(path)	获取路径中的目录部分。
        print(os.path.split(__file__)) # os.path.split(path)	将路径分割为目录和文件名的元组。
        print(os.path.splitext(__file__)) # os.path.splitext(path)	将路径分割为文件名和扩展名的元组。
        # 路径信息获取
        print(os.path.exists(__file__)) # os.path.exists(path)	判断路径是否存在。
        print(os.path.isfile(__file__)) # os.path.isfile(path)	判断路径是否为文件。
        print(os.path.isdir(__file__)) # os.path.isdir(path)	判断路径是否为目录。
        print(os.path.getsize(__file__)) # os.path.getsize(path)	获取文件的大小，以字节为单位。
        print(os.path.getatime(__file__)) # os.path.getatime(path)	获取文件的最后访问时间。
        print(os.path.getmtime(__file__)) # os.path.getmtime(path)	获取文件的最后修改时间。
        print(os.path.getctime(__file__)) # os.path.getctime(path)	获取文件的创建时间（在某些操作系统上表示最后状态更改时间）。
        # 路径规范化
        print(os.path.normpath(__file__)) # os.path.normpath(path)	规范化路径，消除冗余的分隔符和相对路径标记。
        print(os.path.realpath(__file__)) # os.path.realpath(path)	获取文件的真实路径，解析符号链接。
        print(os.path.relpath(__file__, start="../../")) # os.path.relpath(path, start=os.curdir)	计算相对路径，从 start 到 path。
        print(os.path.relpath(__file__, start=os.path.curdir))
        # 路径比较
        print(os.path.commonpath([__file__, "D:\Files\GitFile\python_tutorial\\1_base"])) # os.path.commonpath(paths)	返回路径序列中的共同路径。
        print(os.path.commonprefix([__file__, "D:\Files\GitFile\python_tutorial\\1_base"])) # os.path.commonprefix(list)	返回路径序列中的最长公共前缀。
        print(os.path.samefile("0_base_test.py", "0_base_test.py")) # os.path.samefile(path1, path2)	判断两个路径是否指向同一个文件。
        # print(os.path.sameopenfile(fp1, fp2)) # os.path.sameopenfile(fp1, fp2)	判断两个打开的文件对象是否指向同一个文件。
        # os.path.samestat(stat1, stat2)	判断两个文件是否拥有相同的 stat 状态。
        # 平台依赖功能
        print(os.path.splitdrive(__file__)) # os.path.splitdrive(path)	在 Windows 上，返回路径的驱动器/设备部分和路径部分的元组。
        # print(os.path.splitunc(__file__)) # os.path.splitunc(path)	分割路径中的共享设备和路径部分（Windows 特有）。

        print(__file__) # 当前文件名
        print(os.path.abspath(__file__)) # 当前文件名的绝对路径
        print(os.path.dirname(os.path.abspath(__file__))) # 返回当前文件所在文件夹的路径
        new_path = os.path.join('D:', "root", "test", "timer_test.py")
        print(os.path.normpath(new_path))
    os_path_test()

if True: # 判断语句不会创建新的作用域, 因此 msg 成为全局变量
    msg = "abc" # 全局变量
    # int = 1 # 全局变量


def namespace_test():
    import builtins # 导入 python3 内置作用域的功能
    print(dir(builtins)) #内置作用域中的变量

    # 若没有使用 global 或 nonlocal 关键字对局部变量进行声明，
    # 在局部作用域中，可以访问全局命名空间中的变量，不可对其进行赋值。例如：
    global msg
    print(f"msg = {msg}")
    msg = "def" # 不声明 global msg 编译:UnboundLocalError: local variable 'msg' referenced before assignment

    msg2 = "xyz" # 非局部变量, 对于下面的函数体来说
    # 变量的搜索顺序：
    # 局部 -> 非局部 -> 全局 -> 内建作用域(builtin)
    # int = 2
    def var_search_seq():
        print("int:", int) # 内建作用域中搜索到 `int`
    var_search_seq()

    def var_scope_test1():
        """局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
        调用函数时，所有在函数内声明的变量名称都将被加入到局部作用域中。"""
        msg = "def" # 局部变量
        print("local:", msg)
    var_scope_test1()
    print("global:", msg) # 全局变量

    def var_scope_test2():
        global msg # # 需要使用 global 关键字声明
        msg = "ghi"
    var_scope_test2()
    print("global:", msg) # 全局变量

    def var_scope_test3():
        nonlocal msg2  # nonlocal关键字声明
        # 关于多层嵌套函数中，用 nonlocal 关键字声明的变量只影响上一层的变量，再外一层的不受影响，
        print("nonlocal:", msg2)
    var_scope_test3()

def virtual_enviroment_example():
    """
    https://www.runoob.com/python3/python-venv.html
    不同的项目可能需要不同的 python 环境, 第三方库等等
    TODO: 不同的环境进行测试
    """
    pass

def type_hints_test():
    """
    https://www.runoob.com/python3/python-type-hints.html
    类型注解就是在代码中注明数据类型的语法，它的核心目的是：
    提高代码可读性：让他人（以及未来的你）一眼就能看懂代码的意图
    便于静态检查：在运行代码前，通过工具发现潜在的类型错误
    增强IDE支持：让代码编辑器提供更准确的自动补全和提示

    最佳实践指南
    1. 渐进式采用
    从新代码开始使用类型注解
    逐步为重要的旧代码添加注解
    不需要一次性为所有代码添加类型
    2. 保持一致性
    在项目中保持统一的注解风格
    团队协商决定注解的详细程度
    3. 避免过度注解

    Q&A:
    Q:类型注解会影响性能吗？
    A:不会。类型注解在运行时会被忽略，只用于静态分析和开发工具。
    Q:必须使用类型注解吗？
    A:不强制。Python 仍然是动态类型语言，类型注解是可选的。但强烈推荐使用，特别是大型项目。
    Q:如果注解错了会怎么样？
    A:类型检查器会报错，但程序仍然可以运行。注解只是"提示"而不是"强制"。
    """

    def greet(name: str) -> str:
        """有类型注解(这里是函数注解)
        在函数参数后加 : 类型"""
        return f"Hello,{name}"

    def var_type_hints_example1():
        # 有类型注解的代码
        name: str = "Alice"  # 注解为字符串 (str)
        age: int = 30  # 注解为整数 (int)
        is_student: bool = False  # 注解为布尔值 (bool)
        scores: list = [95, 88, 91]  # 注解为列表 (list)
        print(f"type:{type(name)} {name}")
    # var_type_hints_example1()

    def say_hello(name: str, times: int = 1) -> str:
        """默认实参
        向某人问好指定次数"""
        ret_str =  "".join([f"Hello, {name}!\r\n"] * times)
        print(ret_str)
        return ret_str
    # say_hello("Libai", times=3)

    def complex_type_hints_example():
        """
        复杂类型注解
        基本的 str, int, list 很好用，但如果我们想表达"一个由整数组成的列表"该怎么办？
        这时就需要 Python 的 typing 模块提供更强大的工具。
        列表、字典等容器类型
        """
        from typing import List, Dict, Tuple, Set

        # List[int] 表示这是一个只包含整数的列表
        numbers: List[int] = [1, 2, 3, 4, 5]
        # Dict[str, int] 表示这是一个键为字符串、值为整数的字典
        student_scores: Dict[str, int] = {"Alice": 95, "Bob": 88}
        # Tuple[int, str, bool] 表示这是一个包含整数、字符串、布尔值的元组
        person_info: Tuple[int, str, bool] = (25, "Alice", True)
        # Set[str] 表示这是一个只包含字符串的集合
        unique_names: Set[str] = {"Alice", "Bob", "Charlie"}

    def optional_type_hints():
        """
        当值可能是某种类型或者是 None 时使用：
        """
        from typing import Optional

        def find_student(name: str) -> Optional[str]:
            """根据名字查找学生，可能找到也可能返回None"""
            students = {"Alice": "A001", "Bob": "B002"}
            return students.get(name)  # 可能返回字符串或None,  等价于 Union[str, None]

    def union_type_hints():
        """
        当值可能是多种类型之一时使用：
        """
        from typing import Union
        from typing import List, Dict, Tuple, Set

        def process_input(data: Union[str, int, List[int]]):
            if isinstance(data, int):
                print(f"整数:{data}")
            elif isinstance(data, str):
                print(f"字符串:{data}")
            elif isinstance(data, list):
                print(f"列表:{data}")
            else:
                raise TypeError(f"unknown type:{type(data)}")

        process_input(1)
        process_input("1")
        process_input([1,])
        process_input((1, ))
    # union_type_hints()

    def type_check():
        """对输入的变量进行类型检查的工具 mypy
        Mypy 是最流行的 Python 类型检查器。首先安装它：
        pip install mypy
        """

        def add_numbers(a: int, b: int) -> int:
            return a + b

        add_numbers("1", "2")  # 这里类型错误, 使用 MyPy 进行检查， 运行: MyPy 0_base_test.py

    def type_hints_example2():
        """使用类型注解的程序"""

        from typing import List, Dict, Union, Optional

        def process_students(students: List[Dict[str, Union[str, int]]]) -> Optional[float]:
            """
            处理学生数据，计算平均分数

            参数:
                students: 学生列表，每个学生是包含'name'和'score'的字典

            返回:
                平均分数（浮点数），如果没有学生则返回None
            """
            if not students:
                return None

            total = 0
            for student in students:
                total += student['score']

            return total / len(students)

        # 测试数据
        students_data = [
            {"name": "Alice", "score": 95},
            {"name": "Bob", "score": 88},
            {"name": "Charlie", "score": 92}
        ]

        average = process_students(students_data)
        print(f"平均分: {average}")

    type_hints_example2()


def assert_test():
    """断言"""
    def foo(param):
        """assert 的使用"""
        assert param, "Should not be None"
    # foo(None)  # AssertionError: Should not be None
    foo(1)


def exchange_var_test():

    def exchange1():
        a = 1
        b = 2
        a, b = b, a
        print(f"a={a} b={b}")

    def exchange2():
        """不使用中间变量交换变量"""
        a = 1
        b = 2
        a = a + b
        b = a - b
        a = a - b
        print(f"a={a} b={b}")

    # exchange1()
    exchange2()


def leap_year_test():
    """
    平年和闰年的设置主要用于调整公历日历年与地球公转周期之间的差异，确保日历与季节变化保持同步。‌
    地球公转周期约为365.2422天‌，但公历规定平年为365天，每年会多出约0.2422天（约5小时48分46秒）。
    如果长期不修正，累积误差会导致季节逐渐偏移，例如每100年可能偏移约24天。通过设置闰年（366天），
    并在每四年增加一天（2月29日），可以补偿这部分误差，维持日历的准确性。‌
    https://www.runoob.com/python3/python3-leap-year.html
    """
    def is_leap_year():
        year = int(input("输入一个年份: "))
        if (year % 4) == 0:
            if (year % 100) == 0:  # 是整百年, 还需要可以被 400 整除才是润年
                if (year % 400) == 0:
                    print("{0} 是闰年".format(year))  # 1.整百年能被400整除的是闰年
                else:
                    print("{0} 不是闰年".format(year))
            else:
                print("{0} 是闰年".format(year))  # 2.非整百年只需要能被4整除——即为闰年
        else:
            print("{0} 不是闰年".format(year))

    def is_leap_year2():
        """python 标准库"""
        import calendar
        year = int(input("输入一个年份: "))
        leap = calendar.isleap(year)
        print(f"{year} 是 {'闰年' if leap else '平年'}")

    # is_leap_year()
    is_leap_year2()


def max_num_test():
    """max()"""
    print(f"{max([1, 2, 3])}")
    print(f"{max(1, 2, 3)}")


def sys_test():
    """
    https://www.runoob.com/python3/python-sys.html
    sys 是 Python 标准库中的一个模块，提供了与 Python 解释器及其环境交互的功能。
    通过 sys 库，你可以访问与 Python 解释器相关的变量和函数，例如命令行参数、标准输入输出、程序退出等。
    """
    import sys
    print(dir(sys))
    # sys.path 是一个列表，包含了 Python 解释器在导入模块时搜索的路径。
    # 你可以修改这个列表来添加自定义的模块搜索路径。
    print("模块搜索路径:", sys.path)
    sys.path.append('/custom/path')
    print("更新后的模块搜索路径:", sys.path)
    print("argv:", sys.argv)
    # sys.exit() 用于退出程序。你可以传递一个整数作为退出状态码，通常 0 表示成功，非零值表示错误。
    # sys.exit(-1)

    def stdout_test():
        """
        sys.stdin、sys.stdout 和 sys.stderr 分别代表标准输入、标准输出和标准错误流。
        你可以重定向这些流以实现自定义的输入输出行为。
        """
        # 重定向标准输出到文件
        with open('output.txt', 'w', encoding='utf-8') as f:
            sys.stdout = f
            print("这行内容将写入 output.txt")

        # 恢复标准输出
        sys.stdout = sys.__stdout__
        print("这行内容将显示在控制台")

    # stdout_test()

    # sys.version 和 sys.version_info 提供了当前 Python 解释器的版本信息。
    print(f"version:{sys.version}\n{sys.version_info}")

    # sys 模块常用属性
    # sys.argv	命令行参数列表，sys.argv[0] 是脚本名称
    # sys.path	Python 模块搜索路径（PYTHONPATH）
    # sys.modules	已加载模块的字典
    print("platform:", sys.platform)  # sys.platform	操作系统平台标识（如 'win32', 'linux', 'darwin'）
    # sys.version	Python 解释器版本信息
    print(f"python:", sys.executable)  # sys.executable	Python 解释器的绝对路径
    # sys.stdin	标准输入流（文件对象）
    # sys.stdout	标准输出流（文件对象）
    # sys.stderr	标准错误流（文件对象）
    print(f"byteorder:{sys.byteorder}")  # sys.byteorder	字节序（'little' 或 'big'）
    print(f"max:{sys.maxsize}")# sys.maxsize	最大整数值（2**31-1 或 2**63-1）

    # sys 模块常用方法
    # sys.exit([status])	退出程序，status=0 表示正常退出
    print("sizeof:", sys.getsizeof("abc"))  # sys.getsizeof(obj)	返回对象占用的内存字节数
    print(f"encoding:{sys.getdefaultencoding()}")  # sys.getdefaultencoding()	获取默认字符串编码（通常 'utf-8'）
    # sys.setrecursionlimit(limit)	设置递归深度限制（默认 1000）
    print(f"recursion:{sys.getrecursionlimit()}")# sys.getrecursionlimit()	获取当前递归深度限制
    # sys.getrefcount(obj)	返回对象的引用计数
    try:
        1/0
    except:
        print(f"exe_info:{sys.exc_info()}")  # sys.exc_info()	获取当前异常信息（(type, value, traceback)）
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])

    # sys.settrace(tracefunc)	设置调试跟踪函数
    # sys.setprofile(profilefunc)	设置性能分析函数


def builtin_fun_test():
    """
    https://www.runoob.com/python3/python3-built-in-functions.html
    """
    class C:
        name = "class C"

    print(f"abs:{abs(-100)}")  # abs() 函数返回数字的绝对值。
    print(f"dict{dict([(1, 'a'), (2, 'b'), (3, 'c')])}")  # dict() 函数用于创建一个字典。
    print(f"dict:{dict(a='a', b='b', c=b'c')}")

    # print(f"help:{help(help)}")  # help function

    print(f"min:{min(-100, 0, 100)}")

    c = C()
    print(f"setattr:{setattr(c, 'age', 18)}")  # 如果属性不存在会创建一个新的对象属性，并对属性赋值：
    print(f"getattr:{getattr(c, 'age')}")

    # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
    # 元素除了是 0、空、None、False 外都算 True。
    print(f"all:{all([1, 2, 3, 0])}")
    # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，
    # 如果有一个为 True，则返回 True。
    # 元素除了是 0、空、FALSE 外都算 TRUE。
    print(f"any:{any([1, 2, 3, 0])}")

    # dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
    # 带参数时，返回参数的属性、方法列表。
    # 如果参数包含方法__dir__()，该方法将被调用。
    # 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
    # print(f"dir:{dir([])}")  # 返回列表的所有方法

    # hex() 函数用于将一个指定数字转换为 16 进制数。
    # print(f"hex:{hex(13)} type:{type(hex(13))}")
    # oct() 函数将一个整数转换成 8 进制字符串，8 进制以 0o 作为前缀表示。
    # print(f"oct:{oct(13)} type:{type(oct(13))}")
    # bin() 返回一个整数 int 或者长整数 long int 的二进制表示。 前缀为: "ob"
    # print(f"bin:{bin(13)} type:{type(bin(13))}")
    # int() 函数用于将一个字符串或数字转换为整型。十进制, 没有前缀
    # print(f"int:{int('13')} type:{type(int('13'))}")
    # ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，
    # 它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
    # print(f"ord:{ord('a')} type:{type(ord('a'))}")

    # next() 返回迭代器的下一个项目。
    # next() 函数要和生成迭代器的 iter() 函数一起使用。
    def iter_test():
        # 首先获得Iterator对象:
        it = iter([1, 3, 5, 7, 9])
        while True:
            try:
                # 获得下一个值:
                x = next(it)
                print(x, end=", ")
            except StopIteration:
                # 遇到StopIteration就退出循环
                break
    # iter_test()

    # slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
    # class slice(stop)
    # class slice(start, stop[, step])
    # my_slice = slice(5)
    # print(f"slice:{my_slice} type:{type(my_slice)}")
    # arr = [x for x in range(10)]
    # print(f"subarr:{arr[my_slice]}")

    # Python divmod() 函数接收两个数字类型（非复数）参数，返回一个包含商和余数的元组(a // b, a % b)。
    # 在 python 3.x 版本该函数不支持复数。
    # 函数语法
    # divmod() 函数接受两个参数，通常是两个数字，并返回一个包含两个值的元组。
    # 第一个值是第一个参数除以第二个参数的商（即整数部分），第二个值是余数。
    # divmod(a, b)
    # 参数说明：
    # a: 数字，非复数。
    # b: 数字，非复数。
    # 如果参数 a 与 参数 b 都是整数，函数返回的结果相当于 (a // b, a % b)。
    secs = 3986
    hours, sec = divmod(secs, 3600)
    mins, sec = divmod(sec, 60)
    print(f"divmod {secs}sec = {hours}h {mins}m {sec}s")  # 返回3986秒对应的小时数以及剩余的秒数

    # id() 函数返回对象的唯一标识符，标识符是一个整数。
    # CPython 中 id() 函数用于获取对象的内存地址。
    # print(f"id:{id(secs)}")

    # object() 函数返回一个空对象，我们不能向该对象添加新的属性或方法。
    # object() 函数返回的对象是所有类的基类，它没有任何属性和方法，只有 Python 内置对象所共有的一些特殊属性和方法，
    # 例如 __doc__ 、__class__、__delattr__、__getattribute__ 等。
    # object() 是 Python 中最基本的对象，其他所有对象都是由它派生出来的。
    # 因此，object() 对象是所有 Python 类的最顶层的超类（或者称为基类或父类），所有的内置类型、用户定义的类以及任何
    # 其他类型都直接或间接地继承自它。
    # print(f"object:{id(object())}")

    def sorted_test():
        """
        sorted() 函数对所有可迭代的对象进行排序操作。
        sort 与 sorted 区别：
        sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
        list 的 sort 方法返回的是对已经存在的列表进行操作，
        而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

        语法
        sorted 语法：
        sorted(iterable, key=None, reverse=False)
        参数说明：
        iterable -- 可迭代对象。
        key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
        reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
        """
        print(sorted([1, 3, 2, 5, 4]))  # 默认为升序

        # 另一个区别在于list.sort() 方法只为 list 定义。
        # 而 sorted() 函数可以接收任何的 iterable。
        print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

        # 利用key进行倒序排序
        example_list = [5, 0, 6, 1, 2, 7, 3, 4]
        # 利用key进行倒序排序
        print(sorted(example_list, key=lambda x: x * -1))
    # sorted_test()

    # ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr()
    # 函数使用 \x, \u 或 \U 编码的字符。 生成字符串类似 Python2 版本中 repr() 函数的返回值。
    # print(ascii("12345abcde--..##我"))

    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    # 同时列出数据和数据下标，一般用在 for 循环当中。
    # example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    # print(f"enumerate:{enumerate(example_list)} type:{type(enumerate(example_list))}")
    # for i, elem in enumerate(example_list):
    #     print(i, elem, end=", ")

    # Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
    # 注意：在 Python3.x 中 raw_input() 和 input() 进行了整合，去除了 raw_input( )，仅保留了input( )函数，
    # 其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
    # print(f"input:{input('输入:')}")

    # python staticmethod 返回函数的静态方法。
    # 该方法不强制要求传递参数，如下声明一个静态方法
    # class C(object):
    #     @staticmethod
    #     def f(arg1, arg2, ...):
    #         ...
    # 以上实例声明了静态方法 f，从而可以实现实例化使用 C().f()，当然也可以不实例化调用该方法 C.f()。

    # 注意： eval() 函数执行的代码具有潜在的安全风险。
    # 如果使用不受信任的字符串作为表达式，则可能导致代码注入漏洞，因此，
    # 应谨慎使用 eval() 函数，并确保仅执行可信任的字符串表达式。
    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    # 字符串表达式可以包含变量、函数调用、运算符和其他 Python 语法元素。
    # 语法
    # 以下是 eval() 方法的语法:
    # eval(expression[, globals[, locals]])
    # 参数
    # expression -- 表达式。
    # globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
    # locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
    # eval() 函数将字符串 expression 解析为 Python 表达式，并在指定的命名空间中执行它。
    # print(f"eval:{eval('pow(2, 2)')}")
    # x = 2
    # print(f"eval:{eval('x*2')}")
    # exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec 可以执行更复杂的 Python 代码。
    # 语法
    # 以下是 exec 的语法:
    # exec(object[, globals[, locals]])
    # 参数
    # object：必选参数，表示需要被指定的 Python 代码。它必须是字符串或 code 对象。
    # 如果 object 是一个字符串，该字符串会先被解析为一组 Python 语句，然后再执行（除非发生语法错误）。
    # 如果 object 是一个 code 对象，那么它只是被简单的执行。
    # globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
    # locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与 globals 相同的值。
    # 返回值
    # exec 返回值永远为 None。
    # exec('print("Hello, world")')
    def exec_test():
        x = 10
        expr = """
z = 30
sum = x + y + z
print(f"sum={sum}")
        """

        def func():
            y = 20
            # exec(expr)  # x 未定义
            exec(expr, {'x': 1, 'y': 2})  # 全局变量
            exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})  # 传入全局变量以及局部变量

        func()
    exec_test()

    # str() 函数将对象转化为适于人阅读的形式。
    # print(str(123))
    # bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
    # bool 是 int 的子类。
    # print(f"bool:{bool(123)}")

    # isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
    # isinstance() 与 type() 区别：
    # type() 不会认为子类是一种父类类型，不考虑继承关系。
    # isinstance() 会认为子类是一种父类类型，考虑继承关系。
    # 如果要判断两个类型是否相同推荐使用 isinstance()。
    # print(f"isinstance:{isinstance(secs, list)}")

    # sum() 方法对序列进行求和计算。
    # 语法
    # 以下是 sum() 方法的语法:
    # sum(iterable[, start])
    # 参数
    # iterable -- 可迭代对象，如：列表、元组、集合。
    # start -- 指定相加的参数，如果没有设置这个值，默认为0。
    # print(f"sum:{sum([1, 2, 3])}")


if __name__ == '__main__':
    # base_info()
    # str_op()
    # str_test2()
    # terminal_input_test()
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
    # python_comprehension()
    # iterator_base_test()
    # with_test()
    # function_base_test()
    # data_structure_test()
    # standard_input_and_output_test()
    # kwargs_example()
    # file_op_base_test()
    # os_base_test()
    # oob_base_test()
    # namespace_test()
    # type_hints_test()
    # assert_test()
    # exchange_var_test()
    # is_number_test()
    # even_num_test()
    # leap_year_test()
    # max_num_test()
    # sys_test()
    builtin_fun_test()
else:
    print("我来自另一模块")