import threading
import threading as th
import time
from queue import  Queue

# 线程间通信
# (1)全局变量， 全局变量的使用方法比较简单
# (2)队列，队列是线程安全的，不用关心共享数据的问题
# queue.task_done() 和 queue.join()，阻塞主线程，只有其它线程执行了 queue.task_done() 之后，主线程才会停止
# 否则，一直阻塞在 queue.join()
# 问题: 如果多线程使用同一个线程入口函数, 如何使用队列呢 ？
def get_detail_html(queue):
    print("get_detail_html started.")
    while True:
        # put_nowait() 和 get_nowait() 是不阻塞的
        html = queue.get()  # 阻塞等待

        print(html)
        time.sleep(2)

        #queue.task_down()
    print("get_detail_html ended.")

def get_detail_list(queue):

    print("get_detail_list started.")
    time.sleep(2)
    for ix in range(10):
        queue.put("第{}条数据".format(ix))      # 如果队列满，也阻塞等待
        # time.sleep(1)
    print("get_detail_list ended.")




if __name__ == '__main__':
    detail_url__queue = Queue(maxsize=1000)
    # queue 作为参数传入线程，
    # queue 是线程安全的
    # th1 = th.Thread(target=get_detail_html, args=(detail_url__queue, ))
    # th2 = th.Thread(target=get_detail_list, args=(detail_url__queue, ))
    # th1.start()
    # th2.start()
    # th1.join()
    # th2.join()
    #queue.join()

    # get_detail_list 线程一次可以获取到很多 HTML 列表, get_detail_html 一次只能处理一个 url, 速度慢
    # 也不可以打开很多的线程
    # 开辟很多的线程 CPU 切换也需要时间
    th1 = th.Thread(target=get_detail_list, args=(detail_url__queue, ))
    th1.start()

    # 创建线程
    for ix in range(10):
        thx = th.Thread(target=get_detail_list, args=(detail_url__queue))
        thx.start()

    # 所有主线程等待所有线程执行结束
    thread_list = threading.enumerate() # 获取正在运行的所有线程的列表
    print(thread_list)
    for thread_ix in thread_list:
        thread_ix.join()