import sys
# https://docs.python.org/3.9/library/stdtypes.html#bytes


def bytes_example1():
    """
    class bytes([source[, encoding[, errors]]])
    """
    b1 = b'abc' # bytes 类型的对象
    print(f'type:{type(b1)} data:{b1} len:{len(b1)}')

    b2 = bytes(10)  # 初始化一个空的 bytes 对象, init with zero
    print(f'type:{type(b2)} data:{b2} len:{len(b2)}')

    b3 = bytes.fromhex('B9 01EF AA BB 30')  # 使用 16 进制构造 bytes 对象
    print(f'type:{type(b3)} data:{b3} len:{len(b3)}')

    b4 = bytes([1, 2, 3, 4, 5, 6, 198])  # 使用 int 元素的可迭代对象初始化
    # integer 超过 256 会触发 ValueError,
    # ValueError: bytes must be in range(0, 256)
    print(f'type:{type(b4)} data:{b4} len:{len(b4)}')

    b5 = bytes(b4)  # Copying existing binary data via the buffer protocol:
    print(f'type:{type(b5)} data:{b5} len:{len(b5)}')

    # bytes() 类型的二进制数据转换为字符串表示
    # A reverse conversion function exists to transform a
    # bytes object into its hexadecimal representation.
    # s3 = b3.hex()
    # s3 = b3.hex(' ', bytes_per_sep=1)  # <class 'str'>, 也可以控制输出格式
    s3 = b3.hex('-', bytes_per_sep=1)
    print(f'type:{type(s3)} data:{s3} len:{len(s3)}')

    # You can always convert a bytes object into a list of integers using list(b).
    l3 = list(b3)  # ASCII 码的十进制表示, 相当于用一个可迭代对象初始化一个 list
    print(f'type:{type(l3)} data:{l3} len:{len(l3)}')

    # element
    # This contrasts with text strings, where both indexing and slicing will produce a string of length 1
    # range from 0 - 256
    print(f"elem type:{type(b3[0])}, ")  # <class 'int'>, ASCII 码的十进制表示


def bytes_str_example():
    # b1 = bytes(b'123456')
    # 如果直接用字符串初始化需要加上编码格式
    # TypeError: string argument without an encoding
    b1 = bytes('123456', encoding='utf-8')
    print(f'type:{type(b1)} data:{b1} hex:{b1.hex()} len:{len(b1)}')

def bytes_parameter_test():
    """
    bytes: 不可变类型
    bytearray: 可变类型
    """
    byte = bytes(b'112233')
    byte_array = bytearray(b'112233')
    print(f'type:{type(byte)} data:{byte} hex:{byte.hex()} len:{len(byte)}')
    print(f'type:{type(byte_array)} data:{byte_array} hex:{byte_array.hex()} len:{len(byte_array)}')
    def fun(a, b):
        a = None  # 不可变类型, 函数传参:值拷贝
        b[0] = 125  # 可变类型, 函数传参:传递的引用
    fun(byte, byte_array)
    print(f'type:{type(byte)} data:{byte} hex:{byte.hex()} len:{len(byte)}')
    print(f'type:{type(byte_array)} data:{byte_array} hex:{byte_array.hex()} len:{len(byte_array)}')


def bytearray_example1():
    """
    bytearray
    bytearray objects are a mutable counterpart to bytes objects.
    class bytearray([source[, encoding[, errors]]])
    """
    b1 = bytearray()  # Creating an empty instance:
    b2 = bytearray(b'Hello, world')  # Copying existing binary data via the buffer protoco
    b3 = bytearray(10)  # Creating a zero-filled instance with a given length
    print(f'type:{type(b2)} data:{b2} len:{len(b2)}')
    b4 = bytearray.fromhex('FF BB AADD EE AB')
    print(f'b4 type:{type(b4)} data:{b4} len:{len(b4)}')
    b5 = bytearray(b4)
    print(f'b5 type:{type(b5)} data:{b5} len:{len(b5)}')

    # A reverse conversion function exists to transform a bytearray object into its hexadecimal representation.
    h4 = b4.hex('-')
    print(f'b4 type:{type(h4)} data:{h4} len:{len(h4)}')

    elem = b4[0]  # 支持索引, bytes 类型不支持
    print(f'elem type:{type(elem)} data:{elem} len:{sys.getsizeof(elem)}')  # <class 'int'>
    slice = b4[0:1]
    print(f'slice type:{type(slice)} data:{slice} len:{len(slice)}', end="\n\n")  # <class 'bytearray'>

def bytearray_api_example():
    """api"""
    # b4 = b'0A BB AADD EE AB BB'  # class bytes
    b4 = bytearray(b'AA BB AADD EE AB BB\n dd ee ff')
    # b4 = bytearray.fromhex('0A BB AADD EE AB')  # class bytearray,使用字符串从16进制创建时会自动省略空格
    print(f'b4 type:{type(b4)} data:{b4} len:{len(b4)}')
    #  The methods on bytes and bytearray objects don’t accept strings as their
    #  arguments, just as the methods on strings don’t accept bytes as their arguments.
    b5 = b4.replace(b'A', b'B')  # 替换的是十六进制对应的 ASCII 码
    # b5 = b4.replace(b'AB', b'BB')  # 替换的是十六进制对应的 ASCII 码
    print(f'b5 type:{type(b5)} data:{b5} len:{len(b5)}', end="\n\n")

    print(f"'BB' cnt:{b4.count(b'BB')}")
    print(f"remove prefix:{b4.removeprefix(b'BB')}")
    print(f"remove suffix:{b4.removesuffix(b'BB')}")
    # print(f"decode:{b4.decode(encoding='utf-8')}")
    print(f"end with:{b4.endswith(b'BB')} {b4.endswith(b'AA')}")
    print(f"startswith:{b4.startswith(b'AA')}  {b4.startswith(b'FF')}")
    print(f"find :{b4.find(b'BB')}")
    print(f"rfind :{b4.rfind(b'BB')}")  # 从右边(末尾)开始查,
    # Like find(), but raise ValueError when the subsequence is not found
    # print(f"index:{b4.index(b'BB')}")  # 与 find() 相比会抛出异常
    # print(f"rindex:{b4.rindex(b'BB')}")
    print(f"partition:{b4.partition(b'AA')}")
    table = bytearray.maketrans(b'ABCDEF', b'abcdef')
    print(f"table:{repr(table)}")
    print(f"translate:{b4.translate(table)}")
    # print(f"translate delete f:{b4.translate(None, delete=b'F')}")  # set table = None when only delete
    # TypeError: sequence item 0: expected a bytes-like object, int found
    # print(f"join:{b4.join(bytearray(b'AA BB CC DD EE'))}")
    insert_byte_array = [b'ABCD', b'DDDDDDD0', b'JJJJ']
    print(f"join:{b4.join(insert_byte_array)}")  # 需要是一个可迭代的对象
    print(f"cap:{b4.capitalize()} len:{len(b4)}")  # 首字母大写
    print(f"expand_tab_size:{b4.expandtabs(tabsize=8)}")
    print(f"isalnum:{b4.isalnum()}")
    print(f"isalpha:{b4.isalpha()}")
    # Return True if the sequence is empty or all bytes in the sequence are ASCII, False otherwise.
    # ASCII bytes are in the range 0-0x7F
    print(f"isascii:{b4.isascii()}")
    print(f"isdigit:{b4.isdigit()}")  # byte values in the sequence b'0123456789'
    print(f"islower:{b4.islower()}")
    print(f"isupper:{b4.isupper()}")
    print(f"upper:{b4.upper()}  lower:{b4.lower()}")
    print(f"splitlines:{b4.splitlines(keepends=True)}")  # 按照:\r\n 拆分, keepends 保留结尾
    print(f"swap case:{b4.swapcase()}")
    print(f"istitle:{b4.istitle()}")
    print(f"extend:{b4.extend(b'EE EEE EEEE')} after:{b4}")  # 添加到末尾

if __name__ == '__main__':
    # bytes_example1()
    # bytes_str_example()
    # bytes_parameter_test()
    # bytearray_example1()
    bytearray_api_example()
