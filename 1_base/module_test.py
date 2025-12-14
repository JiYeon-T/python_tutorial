
# https://www.runoob.com/python3/python3-name-main.html
# 在 Python 中，__name__ 和 __main__ 是两个与模块和脚本执行相关的特殊变量。
# __name__ 和 __main__ 通常用于控制代码的执行方式，尤其是在模块既可以作为独立脚本运行，也可以被其他模块导入时。
# 1. __name__ 变量
# __name__ 是一个内置变量，用于表示当前模块的名称。
# __name__ 的值取决于模块是如何被使用的：
# 当模块作为主程序运行时：__name__ 的值被设置为 "__main__"。
# 当模块被导入时：__name__ 的值被设置为模块的文件名（不包括 .py 扩展名）。
# 假设有一个 module.py 文件：

def moudle_import_test():
    print(f"This is a test module:{__name__}")

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print(f'我来自另一模块:{__name__}')