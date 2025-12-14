
# https://tool.oschina.net/regex/
import os
import sys

# This module provides access to mathematical functions for complex numbers.
import cmath  # 复数数学模块, 计算实数和复数平方根

def compute_sum():
    """Python 数字求和"""
    num1 = input("请输入")
    num2 = input("请输入")
    sum = 0
    try:
        sum = float(num1) + float(num2)
    except Exception as e:
        print("输入无效:")
        print(e)
    else:
        print(f"{num1}+{num2}={sum}")

def sqrt_test():
    """Python 平方根"""
    num = input("请输入:")
    # result = float(num) ** 0.5 # x^0.5
    result = cmath.sqrt(float(num))
    print(f"{num}^0.5={result.real:.3f}+{result.imag:.3f}j") # 复数

def quadratic_test():
    # 程序功能: 求解二次方程 ax**2 + bx + c = 0
    # 注意: a ≠ 0，a、b、c 为用户输入的实数

    import cmath  # 导入 cmath 模块，支持复数运算

    def get_float_input(prompt):
        """
        获取用户输入的浮点数，并处理非法输入。
        :param prompt: 提示信息
        :return: 用户输入的浮点数
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("请输入有效的数字！")

    def solve_quadratic(a, b, c):
        """
        计算二次方程的解。
        :param a: 二次项系数
        :param b: 一次项系数
        :param c: 常数项
        :return: 二次方程的两个解
        """
        discriminant = b ** 2 - 4 * a * c  # 计算判别式
        root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2

    a = get_float_input("请输入二次项系数 a（a ≠ 0）：")
    while a == 0:
        print("二次方程的二次项系数 a 不能为 0！")
        a = get_float_input("输入a")
    b = get_float_input("请输入一次项系数 b：")
    c = get_float_input("请输入常数项 c：")

    root1, root2 = solve_quadratic(a, b, c)
    print(f"方程的解为：{root1} 和 {root2}")

def triangle_test():
    """Python 计算三角形的面积"""
    sides_str = input('输入三角形三条边长(如:3,4,5):')
    sides = [int(side) for side in sides_str.split(',')]
    if len(sides) != 3:
        return
    a, b, c = sides
    if a+b<c or a+c<b or b+c<a:
        return
    s = (a + b + c) / 2 # 半周长
    area = cmath.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"{a},{b},{c}, area:{area}")

if __name__ == '__main__':
    # compute_sum()
    # sqrt_test()
    # quadratic_test()
    triangle_test()