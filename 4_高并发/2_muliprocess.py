import multiprocessing as mp

# 在使用pyqt5的过程中，会存在界面卡死的现象，
# 原因:只能在 UI 线程中操作控件, 其他线程不可以, 即使是定时器也不可以

# 为了优化改善，可以利用多线程来解决此类问题。
# 可以实现信号与槽在多个线程中的相互传递数据。
# 用法很简单，创建一个进程类，不同触发时刻分别调用即可。

# TODO: python 多进程实现以及应用
# python multiprocessing:
# https://docs.python.org/zh-cn/3/library/multiprocessing.html

