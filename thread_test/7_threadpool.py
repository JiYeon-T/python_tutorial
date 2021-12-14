from concurrent.futures import ThreadPoolExecutor, as_completed, wait # 用于编写多线程 以及 多进程的代码, 线程与进程的状态
from concurrent import  futures
from threading import Semaphore, Thread, Condition
from queue import Queue
import time
# 线程池
# (1)控制开启的线程数目 -> semaphore
# (2)主线程获取某一个线程的状态 或者 某一个线程的状态以及返回值
# 当一个线程结束的时候主线程可以立即知道
# (3)futures 可以让多线程与多进程的接口一致，可以实现平滑的切换工作方式(当多线程性能不够时, 可以转换为进程)
# eg: java 中的 concurrent 包

def get_html(times):
    time.sleep(times)
    print("Get a page from thread time->{}".format(times))
    return  "thread " + str(times) + " complete."

executor = ThreadPoolExecutor(max_workers = 3)
# task1 = executor.submit(get_html, (3))  # 其中 3 是参数
# task2 = executor.submit(get_html, (2))
#
# print(task1.done())
# print(task2.done())
#
# time.sleep(3)
#
# print(task1.done())
# print(task2.done())
# print(task1.result())

# 要获取已经完成的任务的返回
urls = [1, 2, 3, 4, 5 ,6]
# all_task = [executor.submit(get_html, (url)) for url in urls]
# for future in as_completed( ):    #从所有的任务中找到已经完成的任务
#     data = future.result()  # 获取任务的返回值， 阻塞等待任务的执行结果
#     print("thread finish->" + data)

# 同构 executor 的 map 获取已经完成的 task 的值
# for data in executor.map(get_html, urls):
#     print("get thread {} page".format(data))    # 返回已经执行完成的线程的结果

all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=futures.FIRST_COMPLETED) # 主线程阻塞等待, ALL_COMPLETED

print("main thread end.")


if __name__ == '__main__':
    pass