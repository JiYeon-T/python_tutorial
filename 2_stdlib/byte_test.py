

# https://docs.python.org/3.9/library/stdtypes.html#bytes
import sys


def bytes_example1():
    b1 = b'abc' # bytes 类型的对象
    print(f'type:{type(b1)} data:{b1} len:{len(b1)}')

    b2 = bytes(10)  # 初始化一个空的对象
    print(f'type:{type(b2)} data:{b2} len:{len(b2)}')

    b3 = bytes.fromhex('B9 01EF AA BB 30')  # 使用 16 进制构造 bytes 对象
    print(f'type:{type(b3)} data:{b3} len:{len(b3)}')

    # bytes() 类型的二进制数据转换为字符串表示
    # A reverse conversion function exists to transform a
    # bytes object into its hexadecimal representation.
    # s3 = b3.hex()
    # s3 = b3.hex(' ', bytes_per_sep=1)  # <class 'str'>, 也可以控制输出格式
    s3 = b3.hex('-', bytes_per_sep=1)
    print(f'type:{type(s3)} data:{s3} len:{len(s3)}')

    # You can always convert a bytes object into a list of integers using list(b).
    l3 = list(b3)  # ASCII 码的十进制表示
    print(f'type:{type(l3)} data:{l3} len:{len(l3)}')

def bytearray_example1():
    """
    bytearray
    """
    b1 = bytearray()  # Creating an empty instance:
    b2 = bytearray(b'Hello, world')  # Copying existing binary data via the buffer protoco
    b3 = bytearray(10)  # Creating a zero-filled instance with a given length
    print(f'type:{type(b2)} data:{b2} len:{len(b2)}')

    b4 = bytearray.fromhex('FF BB AADD EE AB')
    print(f'b4 type:{type(b4)} data:{b4} len:{len(b4)}')
    # A reverse conversion function exists to transform a bytearray object into its hexadecimal representation.
    h4 = b4.hex('-')
    print(f'b4 type:{type(h4)} data:{h4} len:{len(h4)}')

    elem = b4[0]
    print(f'elem type:{type(elem)} data:{elem} len:{sys.getsizeof(elem)}')  # <class 'int'>
    slice = b4[0:1]
    print(f'slice type:{type(slice)} data:{slice} len:{len(slice)}', end="\n\n")  # <class 'bytearray'>

def bytearray_api_example():
    """api"""
    b4 = b'FF BB AADD EE AB'
    # b4 = bytearray.fromhex('FF BB AADD EE AB')  # 使用字符串从16进制创建时会自动省略空格
    print(f'b4 type:{type(b4)} data:{b4} len:{len(b4)}')
    b5 = b4.replace(b'A', b'B')  # 替换的是十六进制对应的 ASCII 码
    print(f'b5 type:{type(b5)} data:{b5} len:{len(b5)}', end="\n\n")

    idx = b4.rfind(b'BB')
    print(f"find :{b4.rfind(b'BB')}")
    print(f"find index:{b4.rindex(b'BB')}")
    print(f"partition:{b4.partition(b'AA')}")
    print(f"startswith:{b4.startswith(b'AA')}  {b4.startswith(b'FF')}")
    table = bytearray.maketrans(b'ABCDEF', b'abcdef')
    print(f"table:{repr(table)}")
    print(f"translate:{b4.translate(table)}")
    # print(f"translate delete f:{b4.translate(None, delete=b'F')}")  # set table = None when only delete
    #TODO:

if __name__ == '__main__':
    # bytes_example1()
    # bytearray_example1()
    bytearray_api_example()
