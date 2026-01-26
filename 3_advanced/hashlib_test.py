import hashlib

# https://www.runoob.com/python3/python-hashlib.html
# Python hashlib 模块主要用于进行哈希（hash）操作。
# 哈希（Hash）是一种将任意长度的输入数据映射为固定长度输出数据的算法。
# 哈希通常用于验证数据的完整性、安全存储密码等场景。
# 哈希函数的输出通常是一串看似随机的字母和数字。
# hashlib 模块提供了常见的哈希算法的实现，如 MD5、SHA-1、SHA-256 等。


# 在实际应用中，选择合适的哈希算法取决于具体的需求。
# 需要注意的是，MD5 和 SHA-1 已经被认为不安全，特别是在安全领域，推荐使用更强大的算法，如 SHA-256 或 SHA-512。

# Python hashlib 模块中常见的哈希算法及其含义：
# 算法名称	摘要长度（位）	输出长度（字节）	安全性	用途
# md5	128	16	不安全	数据完整性验证、密码存储等
# sha1	160	20	不安全	数据完整性验证、密码存储等
# sha224	224	28	低	数据完整性验证、数字签名等
# sha256	256	32	中等	数据完整性验证、数字签名等
# sha384	384	48	高	数字签名、加密算法等
# sha512	512	64	高	数字签名、加密算法等
# sha3_224	224	28	高	未来标准的 SHA-3 家族成员，适用于数字签名等
# sha3_256	256	32	高	未来标准的 SHA-3 家族成员，适用于数字签名等
# sha3_384	384	48	高	未来标准的 SHA-3 家族成员，适用于数字签名等
# sha3_512	512	64	高	未来标准的 SHA-3 家族成员，适用于数字签名等
# shake_128	可变	可变	高	SHAKE 系列是 SHA-3 家族的可变长度版本，适用于各种应用
# shake_256	可变	可变	高	SHAKE 系列是 SHA-3 家族的可变长度版本，适用于各种应用
# 说明：
# 摘要长度（位）： 表示哈希算法输出的摘要长度，以位为单位。
# 输出长度（字节）： 表示哈希算法输出的摘要长度，以字节为单位。
# 安全性： 表示哈希算法的安全性级别，包括 "不安全"、"低"、"中等"、"高"。这是一个一般性的分类，具体的安全性还要考虑算法的用途和具体的攻击场景。

def __hash_test():
    print(dir(hashlib))

    # hashlib.md5() / hashlib.sha1() / hashlib.sha256() / ...: 直接使用特定的哈希算法创建哈希对象。
    md5_hasher = hashlib.md5()
    sha1_hasher = hashlib.sha1()


def __sha256_test():
    """"""
    # hashlib.new(name, data=None): 创建一个哈希对象。
    sha256_hasher = hashlib.new('sha256')
    sha256_hasher.update(b'TEST')
    # digest(): 获取二进制表示的哈希值。
    print(f"hash val:{sha256_hasher.digest()} len:{len(sha256_hasher.digest())}")
    # hexdigest(): 获取十六进制表示的哈希值。
    print(f"hash val:{sha256_hasher.hexdigest()} len:{len(sha256_hasher.hexdigest())}")


def __md5_test():
    md5_hasher = hashlib.md5()
    md5_hasher.update(b"TEST")
    print(f"MD5:{md5_hasher.digest()} {len(md5_hasher.digest())}")


def __sha1_test():
    sha1_hasher = hashlib.sha1()
    sha1_hasher.update(b"TEST")
    print(f"MD5:{sha1_hasher.digest()} {len(sha1_hasher.digest())}")



if __name__ == '__main__':
    # __hash_test()
    # __sha256_test()
    # __md5_test()
    __sha1_test()
