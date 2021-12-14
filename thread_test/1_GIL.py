import threading as th
import dis
# python 执行过程中实际上执行的是字节码
def add(a):
    a = a + 1
    print(a)
    return a
# 将 python 代码反解码为字节码
#print(dis.dis(add))

# 2.python 中存在一个 GIL, 使得 CPU 在每一个时间只有一个线程在运行
# 某一个线程不会一直拿着 GIL, 是通过系统调度的
# 按照执行一定行数的字节码 或者 时间片的时候进行调度
import threading as th
total = 0

def add():
    global  total
    for i in range(1000000):
        total += 1

def sub():
    global  total
    for i in range(1000000):
        total -= 1
th1 = th.Thread(target=add)
th2 = th.Thread(target=sub)
th1.start()
th2.start()
th1.join()
th2.join()
print(total)

if __name__ =='__main__':
    pass