import threading as th
import time


def fun():
    for ix in range(10):
        print(th.current_thread().getName(), "running...")
        time.sleep(1)
    print(th.current_thread().getName(), "结束.")

if __name__ == '__main__':
    # 创建新线程， 不设置守护线程, 子线程不受控制， 主线程结束, 子线程还在自己跑
    # (1)Daemon 设置子线程为守护线程, 听主线程的话
    # (2)join() 让主线程阻塞等待子线程结束, 然后自己再结束
    th1 = th.Thread(target=fun, name="thread1")
    th1.setDaemon(True)
    th1.start()
    th1.join() # 阻塞等待, 知道子线程执行结束, 按钮开启新的线程后, 可以开启 join() 这样就没有问题了
    time.sleep(1)
    print("主线程结束")