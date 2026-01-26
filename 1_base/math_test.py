import math
import cmath


def math_constant_test():
    print(f"e=", math.e)  # math.e	返回欧拉数 (2.7182...)
    print("inf=", math.inf)  # math.inf	返回正无穷大浮点数
    print("nan=", math.nan)  # math.nan	返回一个浮点值 NaN (not a number)
    print("pi=", math.pi)  # math.pi	π 一般指圆周率。 圆周率 PI (3.1415...)
    print("tau=", math.tau)  # math.tau	数学常数 τ = 6.283185...，精确到可用精度。 Tau 是一个圆周常数，等于 2π，圆的周长与半径之比。


def math_base_test():
    """数学函数
    Python math 模块提供了许多对浮点数的数学运算函数。
    math 模块下的函数，返回值均为浮点数，除非另有明确说明。
    “如果你需要计算复数，请使用 cmath 模块中的同名函数。”
    https://www.runoob.com/python3/python-math.html

    math.acos(x)	返回 x 的反余弦，结果范围在 0 到 pi 之间。
    math.acosh(x)	返回 x 的反双曲余弦值。
    math.asin(x)	返回 x 的反正弦值，结果范围在 -pi/2 到 pi/2 之间。
    math.asinh(x)	返回 x 的反双曲正弦值。
    math.atan(x)	返回 x 的反正切值，结果范围在 -pi/2 到 pi/2 之间。
    math.atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值，结果是在 -pi 和 pi 之间。
    math.atanh(x)	返回 x 的反双曲正切值。
    math.ceil(x)	将 x 向上舍入到最接近的整数
    math.comb(n, k)	返回不重复且无顺序地从 n 项中选择 k 项的方式总数。
    math.copysign(x, y)	返回一个基于 x 的绝对值和 y 的符号的浮点数。
    math.cos()	返回 x 弧度的余弦值。
    math.cosh(x)	返回 x 的双曲余弦值。
    math.degrees(x)	将角度 x 从弧度转换为度数。
    math.dist(p, q)	返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。
    math.erf(x)	返回一个数的误差函数
    math.erfc(x)	返回 x 处的互补误差函数
    math.exp(x)	返回 e 的 x 次幂，Ex， 其中 e = 2.718281... 是自然对数的基数。
    math.expm1()	返回 Ex - 1， e 的 x 次幂，Ex，其中 e = 2.718281... 是自然对数的基数。这通常比 math.e ** x 或 pow(math.e, x) 更精确。
    math.fabs(x)	返回 x 的绝对值。
    math.factorial(x)	返回 x 的阶乘。 如果 x 不是整数或为负数时则将引发 ValueError。
    math.floor()	将数字向下舍入到最接近的整数
    math.fmod(x, y)	返回 x/y 的余数
    math.frexp(x)	以 (m, e) 对的形式返回 x 的尾数和指数。 m 是一个浮点数， e 是一个整数，正好是 x == m * 2**e 。 如果 x 为零，则返回 (0.0, 0) ，否则返回 0.5 <= abs(m) < 1 。
    math.fsum(iterable)	返回可迭代对象 (元组, 数组, 列表, 等)中的元素总和，是浮点值。
    math.gamma(x)	返回 x 处的伽马函数值。
    math.gcd()	返回给定的整数参数的最大公约数。
    math.hypot()	返回欧几里得范数，sqrt(sum(x**2 for x in coordinates))。 这是从原点到坐标给定点的向量长度。
    math.isclose(a,b)	检查两个值是否彼此接近，若 a 和 b 的值比较接近则返回 True，否则返回 False。。
    math.isfinite(x)	判断 x 是否有限，如果 x 既不是无穷大也不是 NaN，则返回 True ，否则返回 False 。
    math.isinf(x)	判断 x 是否是无穷大，如果 x 是正或负无穷大，则返回 True ，否则返回 False 。
    math.isnan()	判断数字是否为 NaN，如果 x 是 NaN（不是数字），则返回 True ，否则返回 False 。
    math.isqrt()	将平方根数向下舍入到最接近的整数
    math.ldexp(x, i)	返回 x * (2**i) 。 这基本上是函数 math.frexp() 的反函数。
    math.lgamma()	返回伽玛函数在 x 绝对值的自然对数。
    math.log(x[, base])	使用一个参数，返回 x 的自然对数（底为 e ）。
    math.log10(x)	返回 x 底为 10 的对数。
    math.log1p(x)	返回 1+x 的自然对数（以 e 为底）。
    math.log2(x)	返回 x 以 2 为底的对数
    math.perm(n, k=None)	返回不重复且有顺序地从 n 项中选择 k 项的方式总数。
    math.pow(x, y)	将返回 x 的 y 次幂。
    math.prod(iterable)	计算可迭代对象中所有元素的积。
    math.radians(x)	将角度 x 从度数转换为弧度。
    math.remainder(x, y)	返回 IEEE 754 风格的 x 除于 y 的余数。
    math.sin(x)	返回 x 弧度的正弦值。
    math.sinh(x)	返回 x 的双曲正弦值。
    math.sqrt(x)	返回 x 的平方根。
    math.tan(x)	返回 x 弧度的正切值。
    math.tanh(x)	返回 x 的双曲正切值。
    math.trunc(x)	返回 x 截断整数的部分，即返回整数部分，删除小数部分

    """
    print(dir(math))
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


def sqrt_test():
    """计算平方根
    https://www.runoob.com/python3/python3-square-root.html"""
    def sqrt1(num):
        """x的 1/2 次方, 只能计算正数"""
        # return math.sqrt()
        return num ** 0.5

    def sqrt2(num):
        """使用 c 标准库, 可以用于计算负数以及复数"""
        import cmath
        return cmath.sqrt(num)

    print("%0.3f" % sqrt1(16))
    num = -8
    square_root = sqrt2(num)
    print(f"{num}  {square_root.real}+{square_root.imag}")
    print("{0} 的平方根 {1:0.3f}+{2:0.3f}j".format(num, square_root.real, square_root.imag))
    complex_num = complex(11, 12)
    print("{0} 的平方根 {1}".format(complex_num, sqrt2(complex_num)))


def solve_quadratic(a, b, c):
    """
    求解二次方程 ax^2 + bx + c = 0
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: 方程的解（可能为实数或复数）
    """
    if a == 0:
        if b == 0:
            return "无解" if c != 0 else "无穷多解"
        else:
            return f"一元一次方程:x={-1 * b / c}"

    # 计算判别式:
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"两个实数根:{root1} {root2}"
    elif delta == 0:
        return f"一个实数根:{-b / (2 * a)}"
    else:
        # cmath.sqrt() 可以计算复数
        root1 = (-b + cmath.sqrt(delta)) / (2 * a)
        root2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return f"两个复数根:{root1} {root2}"


def __quadratic_test():
    a = -1
    b = 2
    c = 1
    print(f"{a}x^2+{b}x+{c}=0, 解:{solve_quadratic(a, b, c)}")


def triangle_area_test():
    """三角形面积计算
    https://www.runoob.com/python3/python3-area-triangle.html
    海伦公式
    """
    def triangle_area(a, b, c):
        if a+b <= c or a+c <= b or b+c <= a:  # 判断是否是三角形
            print("Not a valid triangle")
            return
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    print(triangle_area(3, 4, 5))




def is_number_test():
    """判断输入是否为数字
    https://www.runoob.com/python3/python3-check-is-number.html
    Python isdigit() 方法检测字符串是否只由数字组成。
    Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
    """
    def is_number(s):
        try:
            val = float(s)
            print(val)
            return True
        except Exception as e:
            pass

        try:
            import unicodedata
            # 只能分辨普通数字, 分数, 复数等都无法识别
            val = unicodedata.numeric(s)
            print(val)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def isnumeric(text):
        """
        核心区别在于判断范围：‌ isdigit() 只接受‌Unicode数字字符、单字节数字（如b'1'）和全角数字‌，并‌包括罗马数字‌（如 "IV"），
        但‌不接受汉字数字‌（如 "四"）；而 isnumeric() 范围更广，接受‌Unicode数字、全角数字、罗马数字和汉字数字‌，例如 "四" 或
         "五万" 会返回 True。‌
        """
        # isdigit() 和 isnumeric() 连小数都无法识别
        print(text.isdigit())
        print(text.isnumeric())  # 甚至连负数都无法识别

    while True:
        text = input("输入:")
        print(is_number(text))
        print(isnumeric(text))


def even_num_test():
    """
    判断是否是偶数
    https://www.runoob.com/python3/python3-odd-even.html
    """
    def is_even1(num):
        return num % 2 == 0

    def is_even2(num):
        """使用按位与操作优化性能"""
        return (num & 1) == 0


def prime_number_test():
    """
    质数判断:
    一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
    换句话说就是该数除了1和它本身以外不再有其他的因数。
    1 - 既不是质数，也不是合数
    https://www.runoob.com/python3/python3-prime-number.html
    """
    def is_prime(val):
        """遍历,
        时间复杂度O(n)"""
        for i in range(2, val):
            if val % i == 0:
                return False
        return True

    def is_prime2(val):
        """降低时间复杂度
        在判断一个大数是质数还是合数的情况下，应该在查看因子那里的循环中使用到平方根。"""
        if val > 1:
            # 找到其平方根（ √ ），减少算法时间
            square_num = math.floor(math.sqrt(val))
            for i in range(2, square_num):
                if val % i == 0:
                    return True
            return False
        else:
            return False

    for i in range(2, 1000):
        if is_prime2(i):
            print(f"{i}", end=",")




if __name__ == '__main__':
    # math_constant_test()
    math_base_test()
    # sqrt_test()
    # __quadratic_test()
    # triangle_area_test()
    # random_test()
    # prime_number_test()

