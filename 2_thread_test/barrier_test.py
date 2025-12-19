import threading
import time

# 通过 barrier 等待固定数量的线程结束

barrier = threading.Barrier(parties=10)

def thread_fun(arg):
    while True:
        print(f"thread:{arg} prepare")
        barrier.wait()
        time.sleep(1)
        print(f"thread:{arg} start running")
        time.sleep(5)

def barrier_test():
    for idx in range(10):
        th = threading.Thread(target=thread_fun, args=(idx, ), name=f"thread-{idx}")
        th.start()


if __name__ == '__main__':
    barrier_test()