import base64
from Crypto.Cipher import DES
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
# RSA 非堆成加密
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
# AES-GCM 加密/解密
import base64
import random
import string
from Crypto.Cipher import AES
# TODO:
# 《密码学》

class MyDESCrypto:
    """对 Crypto DES 算法进行封装"""
    def __init__(self, key = ''):
        if key is not '':
            # key 长度必须为16(DES-128), 24(DES-192) 或者 32(DES-256)
            self.key = key.encode('utf-8')
        else:
            self.key = '12345678'.encode('utf-8')
        self.mode = DES.MODE_CBC

    def encrypt(self, text):
        try:
            text = text.encode('utf-8')
            cryptor = DES.new(self.key, self.mode, self.key)
            length = 16 # length 可以设置为 8 的倍数
            count = len(text)
            if count < length:
                add = (length - count)
                text = text + ('\0' * add).encode('utf-8')
            elif count > length:
                add = (length - (count % length))
                text = text + ('\0' * add).encode('utf-8')
            self.ciphertext = cryptor.encrypt(text)
            # DES 加密后得到的字符串不一定是 ASCII 字符集的, 输出到终端无法识别
            # 所以这里同意转化成 16 进制字符串
            return b2a_hex(self.ciphertext)
        except:
            return ""

    def decrypt(self, text):
        """解密后去掉补的空格"""
        try:
            cryptor = DES.new(self.key, self.mode, self.key)
            plain_text = cryptor.decrypt(a2b_hex(text))
            return bytes.decode(plain_text).rstrip('\0')
        except:
            return ""

def my_des_test():
    des = MyDESCrypto()
    raw_data = "hello, world"
    encrypt_data = des.encrypt(raw_data)
    decrypt_data = des.decrypt(encrypt_data)
    print(f"raw_data:{raw_data}")
    print(f"encrypt_data:{encrypt_data}")
    print(f"decrypt_data:{decrypt_data}")


def aes_encrypt(key, data):
    """
    AES-ECB 加密/解密
    encrypt data with AES algorithm
    :param key
    :param data
    """

    data = bytes(data, encoding="utf-8")
    # 填充数据采用 pkcs7
    data = pad(data, block_size=16, style="pkcs7")
    cipher = AES.new(key=key.encode('utf-8'), mode=AES.MODE_ECB)
    encrypted_data = cipher.encrypt(data)
    # 对数据进行 base64 编码,为了二进制数据的可读性
    encrypted_data = base64.b64encode(encrypted_data)
    return encrypted_data.decode()

def aes_decrypt(key, data):
    """
    decrypt data
    """
    data = base64.b64decode(data)
    cipher = AES.new(key=key.encode('utf-8'), mode=AES.MODE_ECB)
    decrypt_data = cipher.decrypt(data)
    decrypt_data = unpad(decrypt_data, block_size=16, style="pkcs7")
    return decrypt_data.decode("utf-8")

def my_aes_ecb_test():
    print("AES-ECB test")
    raw_data = "hello, world"
    key = "112233445566778899AABBCCDDEEFF00"
    encrypt_data = aes_encrypt(key, raw_data)
    decrypt_data = aes_decrypt(key, encrypt_data)
    print(f"raw_data:{raw_data}")
    print(f"encrypt_data:{encrypt_data}")
    print(f"decrypt_data:{decrypt_data}")


def aes_gcm_encrypt(key, data, associated_data=None, nonce=None):
    """
    AES-GCM 加密
    :param key 16/24/32位
    :param data
    :param associated_data 附加数据, 一般为 None
    :param nonce 随机值,和 MD5 中的"加盐"有些类似,目的是防止同样的明文块,始终加密成同样的加密数据
    :return
    """
    key = key.encode('utf-8')
    data = data.encode('utf-8')
    nonce = nonce or "1234567812346578"
    nonce = nonce.encode('utf-8')
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    if associated_data is not None:
        cipher.update(associated_data.encode())
    encrypted_data, auth_tag = cipher.encrypt_and_digest(data)
    # 拼接数据:前 16 位 nonce; 后 16 位 auth_tag; 中间为加密数据
    join_data = nonce + encrypted_data + auth_tag
    # base64.b64encode() 生成的数据为 bytes() 类型, 需要自己转成 str 类型
    return base64.b64encode(join_data).decode('utf-8')

def aes_gcm_decrypt(key, data, associated_data=None):
    """
    AES-GCM 解密
    :param key
    :param data
    :param associated_data
    """
    key = key.encode('utf-8')
    data = base64.b64decode(data)
    # 分割数据
    nonce = data[:16]
    encrypted_data = data[16:-16]
    auth_tag = data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    if associated_data is not None:
        cipher.update(associated_data.encode())
    plaintext = cipher.decrypt_and_verify(encrypted_data, auth_tag)
    return plaintext.decode()

def my_aes_gcm_test():
    print("AES-GCM test")
    raw_data = "hello, world"
    key = "112233445566778899AABBCCDDEEFF00"
    associate_data = "1234567812345678"
    nonce = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    encrypt_data = aes_gcm_encrypt(key, raw_data, associated_data=associate_data, nonce=nonce)
    decrypt_data = aes_gcm_decrypt(key, encrypt_data, associated_data=associate_data)
    print(f"raw_data:{raw_data}")
    print(f"encrypt_data:{encrypt_data}")
    print(f"decrypt_data:{decrypt_data}")


def get_key():
    """生成公钥&私钥"""
    rsa = RSA.generate(1024, Random.new().read)
    private_key = rsa.exportKey()
    public_key = rsa.public_key().exportKey()
    return {"public_key" : public_key.decode(),
            "private_key" : private_key.decode()
    }

def rsa_encrypt(data, public_key):
    """
    使用公钥加密数据
    :param data
    :param public_key
    """
    # 加载公钥
    rsakey = RSA.importKey(public_key)
    cipher = PKCS1_v1_5.new(rsakey)
    # 加密数据。注意:在 python3 中加密的数据必须是 bytes 类型, 不能是 str 类型
    data = data.encode(encoding='utf-8')
    encrypt_data = cipher.encrypt(data)
    encrypt_data = base64.b64encode(encrypt_data)
    # 公钥每次加密的结果不一样, 原因是每次 padding 的数据不一样
    return encrypt_data.decode()

def rsa_decrypt(data, private_key):
    """
    使用私钥进行解密
    :param data
    :param private_key
    """
    # 加载私钥
    rsakey = RSA.importKey(private_key)
    cipher = PKCS1_v1_5.new(rsakey)
    data = base64.b64decode(data)
    decrypted_data = cipher.decrypt(data, "解密失败")
    # 解密后的数据是 bytes 类型, 需要自己转成 str
    return decrypted_data.decode()

def my_rsa_test():
    print("RSA test")
    key = get_key()
    public_key = key.get('public_key')
    private_key = key.get('private_key')
    print(f"public_key:{public_key}")
    print(f"private_key:{private_key}")
    raw_data = "hello, world"
    encrypt_data = rsa_encrypt(raw_data, public_key)
    decrypt_data = rsa_decrypt(encrypt_data, private_key)
    print(f"raw_data:{raw_data}")
    print(f"encrypt_data:{encrypt_data}")
    print(f"decrypt_data:{decrypt_data}")

if __name__ == '__main__':
    print("crypto test")
    # my_des_test()
    # my_aes_ecb_test()
    # my_aes_gcm_test()
    my_rsa_test()
