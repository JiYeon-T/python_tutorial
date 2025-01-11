import threading
import threading as th
import time
from threading import Condition
from queue import Queue
import serial
import struct

class DongleSerial(th.Thread):
    def __init__(self):
        super(DongleSerial, self).__init__()
        self.ser = serial.Serial()
        self.cond = Condition()
        self.writeFlag = th.Lock()
        self.lost_packet_queue = Queue(maxsize=32)
        self.verify_queue = Queue(maxsize=1)

    def run(self):
        th1 = th.Thread(target=self.write, args=(self.cond, ))
        th2 = th.Thread(target=self.read, args=(self.cond, ))
        th1.start()
        th2.start()
        th1.join()
        th2.join()

    def write(self, cond):
        #with cond:
            #print(str(threading.currentThread().ident) + " running...")
            #print("thread write 写数据...")
            #cond.notify()   # 通知 read 线程可以读了
            #time.sleep(5)
        if not self.lost_packet_queue.empty():
            # 重发丢失的包
            # apollo 使用 seek(或者数组大小索引, 保存到响应的位置)
            l = self.lost_packet_queue.get()    # 读出
            for p_ix in l:
                # write p_ix
                pass

        # if cmdType == data:
        #     pass    # 200 字节1包
        # elif cmdType == Verify:
        #     pass
        # elif cmdType = startUpdate:
        #     pass
        # else:
        #     # ERROR
        #     pass

    def read(self, cond):
        while True:
            #cond.wait() # 等待可以读
            # 读完
            #
            #cond.notify()   # 通知写线程, 继续写
            #print(str(threading.currentThread().ident) + " running...")
            data = self.ser.readall()
            data = data.decode()
            if data == "OK+LOST":
                # 重新发所有数据
                pass
            elif data == "VerifySuccess":
                self.verify_queue.put(1)
            elif data == "VerifyFailed":
                self.verify_queue.put(0)
            elif len == 32 * 4:
                l = struct.unpack(data)
                self.lost_packet_queue.put(l)
            else:
                #othrer sequence
                pass
            time.sleep(5)

d = DongleSerial()
d.start()
d.join()

if __name__ == '__main__':
    pass