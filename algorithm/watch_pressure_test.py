import time
import re
from serial import Serial
import sys

# NOTE: 手表 AT 命令压测：


class TestItem(object):
    def __init__(self, at_cmd=None, get_recv_delay=1, except_rsp=None):
        self._op = "send_at_cmd" # 该测试项要进行的操作
        self._at_cmd = at_cmd # 要发送的 AT 命令
        self._get_recv_delay = get_recv_delay # 发送命令后获取结果的超时时间
        self._except_rsp = except_rsp # 期望获取到的结果

    def start_test(self, ser):
        """
        开始测试
        @param ser: serial.Serial 对象
        """
        print(f"send:{self._at_cmd}")
        if self._op == "send_at_cmd":
            ser.write(bytearray(f"{self._at_cmd}\r\n", 'utf-8'))
            time.sleep(self._get_recv_delay)
            if self._except_rsp == None: # 不需要回复的情况
                return True
            else: # 需要回复
                try:
                    recv = ser.read(ser.in_waiting).decode('utf-8')
                except:  # 开机后会打印异常字符
                    print(f"Except")
                    # if len(recv) == 0:
                    #     return False
                    # else:
                    return True
                print(f"recv:{recv}")
                if recv == None or len(recv) == 0:
                    return False
                if self._except_rsp in recv:
                    return True
                else:
                    return False
        else:
            print("other test method")
        return False

    def __del__(self):
        pass


if __name__ == '__main__':
    print("test start")
    testList = []
    ser = Serial(port="COM54", baudrate=921600, timeout=1000) # AT 命令串口

    start_item = TestItem(at_cmd="AT^START", except_rsp="OK")
    testList.append(start_item)

    not_rsp_list = ["AT^BTMAC?", "AT^BSN?", "AT^DID?", "AT^KEY?", "AT^GETVBAT", "AT^GETVBAT", "AT^GPSENABLE", "AT^GPSGETFREQDIFT=1", "AT^GPSDISABLE"]
    for test_cmd in not_rsp_list:
        item = TestItem(at_cmd=test_cmd)
        testList.append(item)

    item1 = TestItem(at_cmd="AT^TBT_ENTER_HCI_MODE", except_rsp="OK", get_recv_delay=3)
    testList.append(item1)

    item2 = TestItem(at_cmd="AT^BNSG=m1b4c0p0y1d0", except_rsp="OK", get_recv_delay=3)
    item3 = TestItem(at_cmd="AT^BNSG=m3b4", except_rsp="OK", get_recv_delay=1)
    repeatList = []
    for cnt in range(3): # repeat 3 times
        repeatList.append(item2)
        repeatList.append(item3)
    for item in repeatList:
        testList.append(item)

    reboot_item =  TestItem(at_cmd="AT^REBOOT", get_recv_delay=30)
    testList.append(reboot_item)

    idx = 0
    while True:
        for item in testList:
            if not item.start_test(ser):
                print("test failed")
                # 退出 shipmode, 避免重启
                exitShipMode = TestItem(at_cmd="AT^SHIPMODE_CTRL=0", except_rsp="OK")
                if not exitShipMode.start_test(ser):
                    print("Exit shipmode failed")
                while True: # dead loop
                    time.sleep(10000)
            time.sleep(0.2)

        if idx % 100 == 0:
            print(f"idx:{idx}")
        idx += 1
