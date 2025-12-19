import threading
import time
import serial
import queue


def serial_recv_test():
    q = queue.Queue(maxsize=1000)
    child_thread_alive_flag = True
    main_thread_alive_flag = True
    # send_thread_alive_flag = True, 发送暂时不使用队列, 这个可以主动控制的
    # 还是要使用发送队列，防止 UI 线程被阻塞 -> 优化

    def recv_entry(ser):
        print("recv thread running...")
        while child_thread_alive_flag:
            # IO 阻塞
            data = ser.read(ser.in_waiting or 1)
            q.put(data, block=True, timeout=5)
            print(f"->put:{data} len:{len(data)}")
        print("recv thread exit")

    def recv_thread_exit():
        child_thread_alive_flag = False

    def main_thread_exit():
        main_thread_alive_flag = False

    ser = serial.Serial(port="COM22", baudrate=230400)
    recv_thread = threading.Thread(target=recv_entry, name="recv_thread", args=(ser,))
    recv_thread.start()
    print("main thread running...")
    time.sleep(0.5)
    cmd = "AT+SCAN?"
    print(f"send cmd:{cmd}")
    ser.write(data=bytearray(str(cmd), 'utf-8'))

    while main_thread_alive_flag:
        data = q.get(block=True, timeout=1000)  # 队列阻塞
        print(f"<-get:{data} len:{len(data)} qsize:{q.qsize()}")
        # time.sleep(0.1)  # qsize increment test
    print("main thread exit")


def serial_exception_test():
    """ serial.Serial 正常使用中出现异常后, 线程正常退出"""
    ser = None
    try:
        ser = serial.Serial(port="COM22", baudrate=230400)
        ret = ser.read(size=1000) # 串口拔出后不会抛出异常, read 会返回
        print("read:{}".format(ret))
    except Exception as e:
        print(e)
        print("Excepiton")
    finally:
        if ser:
            ser.close()
        print("删除与串口上下文/环境")
    print("Normal exit")

if __name__ == '__main__':
    serial_recv_test()
    # serial_exception_test()
