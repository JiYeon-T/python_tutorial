import os

l = [1, 2, 3, 4, 5] # pyhton 中列表默认传递的就是引用, 如果想使用值传递, 则要切分
def fun(l):
    l[0] = 10
    print(l)

# fun(l[:])
# print(l)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    for ix in l:
        print(ix)
    # print(l)
    # l.remove(1)
    # print(l)
    # l.append(1)
    # print(l)
    # # l.insert(0, 1)  # 列表的插入
    # l.insert(0, 1)  # 列表的插入
    # l.insert(0, 1)  # 列表的插入
    # l.insert(0, 1)  # 列表的插入
    # l.insert(-1, 100)
    # print(l)
    # for ix in l:
    #     if ix == 2:
    #         l.remove(2)
    # # l.remove(5)
    # print(l)

    # del l[0]    # 删除
    # print(l)
    # s = list(set(l)) # set, unique
    # print(s)

    # print(type(s))
    # item = 999
    # s.append(item) # 插入元素
    # print(s)
    # item = s.pop() # 从列表中弹出一个元素
    # print(s)
    # print(item)

    pass