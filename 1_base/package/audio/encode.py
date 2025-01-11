import datetime
import os
import sys

class Encoder(object):
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

if __name__ == '__main__':
    print(sys.argv)
    Codec()