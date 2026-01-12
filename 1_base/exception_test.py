import sys
# import e
# https://www.runoob.com/python3/python3-errors-execptions.html

def exception_base_test():
    """
    Python3 错误和异常
    """
    try:
        a = 10
        assert a > 50
    except (OSError, TypeError, NameError): # 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
        # 发生异常时执行的代码
        print("发生异常时执行的代码块")
        print("Exception")
    except ValueError: # 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
        # 处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
        print(f'value exception')
    except:
        # print("Unexpected error:", sys.exc_info())
        print("Unexpected error:", sys.exc_info()[0])
        # raise # 打印错误，然后再把错误抛出
    else:
        # 没有异常时执行的代码
        # try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后
        # else 子句将在 try 子句没有发生任何异常的时候执行。
        print("没有异常时执行的代码块")
        pass
    finally: # 无论异常是否发生都会执行的代码
        print("无论异常是否发生都会执行的代码块", end="\n\n")

    # raise 唯一的一个参数指定了要被抛出的异常。
    # 它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
    class MyException(Exception):
        """用户自定义异常
        你可以通过创建一个新的异常类来拥有自己的异常。
        异常类继承自 Exception 类，可以直接继承，或者间接继承"""
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)
    try:
        raise MyException("这是我自己创建的异常类")
    except Exception as e:
        print(f"Exception:{e.value}  {repr(e)}")

    def file_op_exception_test():
        """"""
        f = None
        try:
            f = open('a.txt', 'r')
            s = f.readline()
            i = int(s.strip())
        except OSError as e:
            print(f"OS error {e}")
        except ValueError as e:
            print(f"Value error {e}")
        except:
            print(f'unexpected error {sys.exc_info()}') # exception_info 返回一个元组
            raise
        finally:
            if f != None:
                f.close()
            print(f'close file:{repr(f)}')
    file_op_exception_test()


def my_exception_module_test():
    # 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，
    # 然后基于这个基础类为不同的错误情况创建不同的子类:
    class Error(Exception):
        """Base class for exceptions in this module."""
        pass

    class InputError(Error):
        """Exception raised for errors in the input.

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """

        def __init__(self, expression=None, message=None):
            self.expression = expression
            self.message = message

    class TransitionError(Error):
        """Raised when an operation attempts a state transition that's not
        allowed.

        Attributes:
            previous -- state at beginning of transition
            next -- attempted new state
            message -- explanation of why the specific transition is not allowed
        """

        def __init__(self, previous=None, next=None, message=None):
            self.previous = previous
            self.next = next
            self.message = message

    input = "Abc"
    try:
        # b = 1 / 0
        if not input:
            raise InputError()
        else:
            raise TransitionError()
    except InputError as e:
        print(repr(e))
    except TransitionError as e:
        print(repr(e))
    except (TypeError,ZeroDivisionError,NameError): # 同时捕获多个异常
        print(f'{sys.exc_info()}')
    except:
        print(f"{sys.exc_info()}")
    finally:
        print("无论如何都会执行的代码")


def capture_all():
    try:
        a = 1/ 0
    except Exception as e:  # 捕获所有异常
        print(repr(e))


if __name__ == '__main__':
    # exception_base_test()
    # my_exception_module_test()
    capture_all()