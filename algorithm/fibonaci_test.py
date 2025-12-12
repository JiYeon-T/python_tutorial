#斐波那契额数列:两个元素的总和确定了下一个数
# 0 1 1 2 3 5 8 13 21 34 55 ...


def fibonaci_print():
    """Just display result"""
    # 复合赋值：变量 a 和 b 同时得到新值 0 和 1
    # 右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。
    a, b = 0, 1
    # while b < 100:
    for i in range(40):
        print(f"b={b}", sep=",", end="  ")
        a, b = b, a + b

def fibonaci_recursion():
    def fib(n):
        if (n < 1):
            print("ERROR")
            return -1
        if n == 1 or n == 2:
            return 1
        else:
            print(f"{fib(n-1) + fib(n-2)}", end="  ")
            return fib(n-1) + fib(n-2)
    print(f"\nresult:{fib(10)}")

if __name__ == '__main__':
    fibonaci_print()
    # fibonaci_recursion()
