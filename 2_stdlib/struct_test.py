import struct
import sys
# https://docs.python.org/3.9/library/struct.html

def print_host_byteorder():
    """Use sys.byteorder to check the endianness of your system."""
    print(f"{sys.byteorder} endian", end="\n\n")

def print_net_byteorder():
    """https://datatracker.ietf.org/doc/html/rfc1700"""
    # !
    return

def struct_example_1():
    fmt = "<hhl"  # 格式串:小端, short, short, long
    print({struct.calcsize(fmt)})  # size:2+2+4
    b = struct.pack(fmt, 1, 2, 3)  #  转换为 bytearray
    print(f" type:{type(b)} {repr(b)}")
    un = struct.unpack(fmt, b)  #
    print(f"type:{type(un)} {un}")

def struct_example2():
    """Unpacked fields can be named by assigning them to variables or by wrapping the result in a named tuple:"""
    from collections import namedtuple
    record = b'raymond   \x32\x12\x08\x01\x08'
    name, serialnum, school, gradelevel = struct.unpack('<10sHHb', record)  # ‘4s’ == 'ssss'
    print(f"{name},{serialnum},{school},{gradelevel}")
    print(f"{type(name)},{type(serialnum)},{type(school)},{type(gradelevel)}")

    Student = namedtuple('Student', 'name serialnum shcool gradelevel')  # namedtuple
    # print(Student._make(struct.unpack('<10sHHb', record)))
    # 等效于:
    res = struct.unpack('<10sHHb', record)  # 返回的是元组
    print(f"type:{type(res)},  {res}")  # 元组类型
    new_stu = Student._make(res)  # 使用 namedtuple 的类方法创建对象
    print(new_stu, end="\n\n")

    # 字节对齐
    # The ordering of format characters may have an impact on size since
    # the padding needed to satisfy alignment requirements is different:
    b = struct.pack("ci", b'*', 0x12131415)  # 8bytes, 4byte 对齐, char, int
    print(f"len:{len(b)}  {b}")
    b = struct.pack("ic", 0x12131415, b'*')  #  5 byte, int, char
    print(f"len:{len(b)}  {b}")
    fmt = "ci"
    print(f"{struct.calcsize(fmt)}")
    fmt = 'ic'
    print(f"{struct.calcsize(fmt)}")

    # The following format 'llh0l' specifies two pad bytes at the end,
    # assuming longs are aligned on 4-byte boundaries:
    ret = struct.pack('llh0l', 1, 2, 3)  # 最后一个 short 字节对齐了???
    print(f"type:{type(ret)} len:{len(ret)} {ret}", end="\n\n")

    # buffer = [] # TypeError: argument must be read-write bytes-like object, not list
    buffer = bytearray(100)  # 必须是 bytes 类型, 因为是二进制
    struct.pack_into("<ll", buffer, 0, 1, 2)
    print(f'len:{len(buffer)} data:{buffer}', end="\n\n")

    ret = struct.unpack_from("<ll", buffer, 0)  # <class 'tuple'>
    print(f"type:{type(ret)} len:{len(ret)} data:{ret}")

def use_struct_class_test():
    """
    直接使用 Struct 类的效率更高一些
    Return a new Struct object which writes and reads binary data according to
    the format string format.
    Creating a Struct object once and calling its methods is more efficient
    than calling the struct functions with the same format since the format
    string only needs to be compiled once.
    """
    # struct.Struct()
    s = struct.Struct("<hh")  # 2 short
    # b = bytearray(100)
    b = s.pack(1, 2)
    print(b)
    s = struct.Struct("<ll")  # 2 long
    b = s.pack(1, 2)
    print(b)
    text = s.unpack(b)
    print(text)

if __name__ == '__main__':
    # print_host_byteorder()
    # struct_example_1()
    # struct_example2()
    use_struct_class_test()