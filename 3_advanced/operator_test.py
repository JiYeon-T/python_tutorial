import operator
# Python2.x 版本中，使用 cmp() 函数来比较两个列表、数字或字符串等的大小关系。
# Python 3.X 的版本中已经没有 cmp() 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象


def __base_test1():
    """
    对象比较函数适用于所有的对象，函数名根据它们对应的比较运算符命名。
    许多函数名与特殊方法名相同，只是没有双下划线。为了向后兼容性，也保留了许多包含双下划线的函数，
    为了表述清楚，建议使用没有双下划线的函数。
    """
    # a = "Hello"
    # b = "World"
    a = [1, 2, 3]  # 比较 列表
    b = [123, ]
    print(operator.lt(a, b))  # less than
    print(operator.le(a, b))  # less equal
    print(operator.eq(a, b))  # equal
    print(operator.ne(a, b))  # not equal
    print(operator.ge(a, b))  # greater equal
    print(operator.gt(a, b))  # greater than
    print(operator.__lt__(a, b))
    print(operator.__le__(a, b))
    print(operator.__eq__(a, b))
    print(operator.__ne__(a, b))
    print(operator.__ge__(a, b))
    print(operator.__gt__(a, b), end="\n\n")

    list_a = [1, 2, 3]  # 比较 列表
    list_b = [123, ]
    # print(f"sub:{operator.sub(a, b)}")  # ERROR
    # print(f"mul:{operator.mul(a, b)}")  # ERROR
    # print(f"mul:{operator.mul(a, 3)}")  # TypeError: can't multiply sequence by non-int of type 'list'

    str_a = "Hello"
    str_b = "World"
    # 运算  语法  函数
    print(f"add:{operator.add(list_a, list_b)}") # 加法 a + b    add(a, b)
    print(f"concate:{operator.concat(str_a, str_b)}")  # 字符串拼接 seq1 + seq2 concat(seq1, seq2)
    print(f"contains:{operator.contains(list_a, list_b)}") # 包含测试 obj in seq contains(seq, obj)
    print(f"truediv:{operator.truediv(1, 2)}")  # 除法 a / b truediv(a, b), 可以返回小数，而不是当做整型和整型相除
    print(f"floordiv:{operator.floordiv(1, 2)}")  # 除法 a // b floordiv(a, b), 地板除

    print(f"and_:{operator.and_(0x08, 0x04)}")  # 按位与 a & b and_(a, b)
    print(f"xor:{operator.xor(0x01, 0x02)}")  # 按位异或 a ^ b xor(a, b)
    print(f"invert:{operator.invert(0x01)}")  # 按位取反 ~ a invert(a)
    print(f"or_:{operator.or_(0x01, 0x02)}")  # 按位或 a | b or_(a, b)
    print(f"pow:{operator.pow(2, 3)}")  # 取幂 a ** b pow(a, b)
    print(f"is:{operator.is_(1, 1)}")  # 标识 a is b is_(a, b)
    print(f"is_not:{operator.is_not(1, 1)}")  # 标识 a is not b is_not(a, b)

    operator.setitem(list_a, 1, 1000)# 索引赋值 obj[k] = v setitem(obj, k, v)
    print(f"list_a:{list_a}")
    operator.delitem(list_a, 1)# 索引删除 del obj[k] delitem(obj, k)
    print(f"list_a:{list_a}")
    print(f"getitem:{operator.getitem(list_a, 1)}")  # 索引取值 obj[k] getitem(obj, k)

    # 左移 a << b lshift(a, b)
    # 取模 a % b mod(a, b)
    # 乘法 a * b mul(a, b)
    # 矩阵乘法 a @ b matmul(a, b)
    # 取反（算术）- a neg(a)
    # 取反（逻辑） not a not_(a)
    # 正数 + a pos(a)
    # 右移 a >> b rshift(a, b)
    # 切片赋值 seq[i:j] = values  setitem(seq, slice(i, j), values)
    # 切片删除 del seq[i:j] delitem(seq, slice(i, j))
    # 切片取值 seq[i:j] getitem(seq, slice(i, j))
    # 字符串格式化 s % obj mod(s, obj)
    # 减法 a - b sub(a, b)
    print(f"trueth:{operator.truth(1)}")# 真值测试 obj truth(obj)
    # 比较 a < b lt(a, b)
    # 比较 a <= b le(a, b)
    # 相等 a == b eq(a, b)
    # 不等 a != b ne(a, b)
    # 比较 a >= b ge(a, b)
    # 比较 a > b gt(a, b)


if __name__ == '__main__':
    __base_test1()