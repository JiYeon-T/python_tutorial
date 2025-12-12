import datetime
import os
import random
import sys

class Decoder(object):
    CLASS_TYPE = 'Decoder'

    def __init__(self):
        self.name = "Decoder"
        print("Decoder init id:", id(self))

    def decode_stream(self, data=None, format=None):
        print("Decoder decode_stream data:{} format:{}".format(data, format))

    def encode_stream(self, data=None, format=None):
        print("Decoder encode_stream data:{} format:{}".format(data, format))

    def __del__(self):
        print("Decoder deinit id:", id(self))

    @staticmethod
    def print_time():
        print("Decoder time:", random.randint(1, 1000))

def decorder_test_fun():
    decoder = Decoder()
    decoder.print_time()

if __name__ == '__main__':
    print(sys.argv)
    Decoder()
    decorder_test_fun()