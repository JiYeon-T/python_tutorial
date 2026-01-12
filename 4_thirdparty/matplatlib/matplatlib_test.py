# import matplotlib as plt
from matplotlib import pyplot as plt
import numpy
import numpy as np


# https://matplotlib.org/
# https://github.com/matplotlib/matplotlib

# TODO:


# Matplotlib produces publication-quality figures in a variety of hardcopy
# formats and interactive environments across platforms. Matplotlib can be
# used in Python scripts, Python/IPython shells, web application servers,
# and various graphical user interface toolkits.


def show_quadratic(a, b, c):
    """
    求解二次方程 ax^2 + bx + c = 0
    :param a: 二次项系数
    :param b: 一次项系数
    :param c: 常数项
    :return: 方程的解（可能为实数或复数）
    """
    # 创建 x 的数组,
    x = numpy.linspace(-3, 3, 40000)  # 从-10到10生成400个点

    # 计算 y 的值:
    y = a * x ** 2 + b * x + c

    # 绘图
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a}x^2+{b}x+{c}=0')
    plt.title("Quadratic Equation")
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.legend()  # TODO:
    plt.show()




if __name__ == '__main__':
    show_quadratic(1, 2, 1)
