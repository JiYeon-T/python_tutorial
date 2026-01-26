import os

test_list = [100, 100, 100, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8]
# 去除列表中的重复元素的方法:
# (1) 新添加一个列表, 储存第一次出现的所有元素
def fun1(test_list):
    res = []
    for elem in test_list: # 遍历
        if elem not in res:
            res.append(elem)
    return res

# (2) 列表解析式（第一一种方法的简化版本）
def fun2(test_list):
    res = []
    [res.append(x) for x in test_list if x not in res]
    return res

# (3) set()
# 这种方式是最流行的方法来去除列表中的重复元素。但该方法的最大的一个缺点就是使用过后列表中元素的顺序不再继续保持与原来一致了。
def fun3(test_list):
    test_list = list(set(test_list))
    return test_list

# (4) 列表解析式 + enumerate()
def fun4(test_list):
    res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
    return res


#(5)完成特殊任务中最快的方法。它先是将列表中的重复项移除并返回一个字典，最后转换成列表。这种方法对于字符串也可以进行处理。
def fun5(test_list):
    import collections
    res = list(collections.OrderedDict.fromkeys(test_list))
    return res

# （6）多维列表
# 对于多维列表（列表嵌套）中的重复元素去除。
# 这里假设列表中元素（也是列表）它们具有相同的元素（但不一定顺序相同）都被当做重复元素。那么下面使用 set() + sorted() 方法来完成任务。
# # initializing list
# test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],
#              [1, 2, 3], [3, 4, 1]]
# # printing original list
# print("The original list : " + str(test_list))
# # using set() + sorted()
# # removing duplicate sublist
# res = list(set(tuple(sorted(sub)) for sub in test_list))
# # print result
# print("The list after duplicate removal : " + str(res))

# (7) set() + map() + sorted()
# test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],
#              [1, 2, 3], [3, 4, 1]]
# # printing original list
# print("The original list : " + str(test_list))
# # using set() + map() + sorted()
# # removing duplicate sublist
# res = list(set(map(lambda i: tuple(sorted(i)), test_list)))
# # print result
# print("The list after duplicate removal : " + str(res))

if __name__ == '__main__':
    #global test_list
    print(f"before:{str(test_list)}")
    print(f"after:{str(fun1(test_list))}")
    print(f"after:{str(fun2(test_list))}")
    print(f"after:{str(fun3(test_list))}")
    print(f"after:{str(fun4(test_list))}")
    print(f"after:{str(fun5(test_list))}")

    print(f"before:{str(test_list)}")