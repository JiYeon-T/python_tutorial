import dis
import threading
# python 代码字节码

def add(a):
    """字节码: a 加载到内存 -> 常量1加载到内存 -> add -> 结果赋值给 a"""
    for ix in range(10000):
        a[0] += 1
        print("a = " + str(a[0]))

def sub(a):
    """字节码: a 加载到内存 -> 常量1加载到内存 -> sub -> 结果赋值给 a"""
    for ix in range(10000):
        a[0]-= 1
        print("a = " + str(a[0]))
# print(dis.dis(add))
# print(dis.dis(sub))

a = [0, ]
print("main a = " + str(a[0]))
th2 = threading.Thread(target=sub, args=(a, ))  # 这里tuple, 传递的是拷贝 ??????a
th2.start()
th1 = threading.Thread(target=add, args=(a, ))
th1.start()
th1.join()
th2.join()
print("main a = " + str(a[0]))

# 使用场景eg:
# web, 电商网站的开发中，检查库存，多个用户同时购买某一个商品时, 使用的是同一个变量:总库存
