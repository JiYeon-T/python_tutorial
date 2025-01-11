import datetime
import os
import sys

class Codec(object):
    CLASS_TYPE = 'Codec'

    def __init__(self):
        self.name = "codec"
        print("Codec init")

    def decode_stream(self, data=None, format=None):
        print("codec decode_stream data:{} format:{}".format(data, format))

    def encode_stream(self, data=None, format=None):
        print("codec encode_stream data:{} format:{}".format(data, format))

    def __del__(self):
        print("Codec deinit")

    @staticmethod
    def print_time():
        print("time:", datetime.date())

class Util():
    def __init__(self):
        self.name = "codec"
        print("Util init")
    def __del__(self):
        print("Util deinit")

def get_raw_data():
    print("Raw data method")
    return []

if __name__ == '__main__':
    print(sys.argv)
    Codec()
else:
    print('被其他文件导入, Codec 初始化')