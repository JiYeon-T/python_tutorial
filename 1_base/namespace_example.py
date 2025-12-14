# https://www.runoob.com/python3/python3-namespace-scope.html

# 一般有三种命名空间：
# 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# 假设我们要使用变量 runoob，则 Python 的查找顺序为：局部的命名空间 -> 全局命名空间 -> 内置命名空间。

# 有四种作用域：
#
# L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
# E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
# G（Global）：当前脚本的最外层，比如当前模块的全局变量。
# B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
# LEGB 规则（Local, Enclosing, Global, Built-in）：Python 查找变量时的顺序是： L –> E –> G –> B。
#
# Local：当前函数的局部作用域。
# Enclosing：包含当前函数的外部函数的作用域（如果有嵌套函数）。
# Global：当前模块的全局作用域。
# Built-in：Python 内置的作用域。



def namespace_test1():
    """"""
    g_count = 0  # 全局作用域

    def outer():
        o_count = 1  # 闭包函数外的函数中

        def inner():
            i_count = 2  # 局部作用域

    # 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，
    # 所以必须导入这个文件才能够使用它。
    import builtins
    print(f"builtins:{dir(builtins)}")

    # Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
    # 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
    # 也就是说这些语句内定义的变量，外部也可以访问，
    if 1:
        msg = "abc"
    print(f"msg={msg}")  # 同一个作用域中, 因此可以正常访问变量 msg


num = 10

def global_test():
    """
    global 和 nonlocal关键字
    当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了

    总结:
    全局变量在函数外部定义，可以在整个文件中访问。
    局部变量在函数内部定义，只能在函数内访问。
    使用 global 可以在函数中修改全局变量。
    使用 nonlocal 可以在嵌套函数中修改外部函数的变量。
    """
    # global num  # 这里注释掉, num 变成了 global 中的局部变量
    num = 20
    print(f"num = {num}")

    # 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，
    def enclosing_test():
        nonlocal num  # 上一级函数中的局部变量 Num
        num = 30

    enclosing_test()
    print(f"num = {num}")


if __name__ == '__main__':
    # namespace_test1()
    global_test()
    print(f"global scope num = {num}")

