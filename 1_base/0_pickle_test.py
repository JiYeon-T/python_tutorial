# https://www.runoob.com/python3/python3-inputoutput.html
# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

import pickle, pprint

def pickle_test():
    ##寫入，二進制文件
    list1 = [1, 2.34, 'a', [1, 2, 3]]
    pickle_file = open('my_list.pkl', 'wb') #寫二進制方式打開
    pickle.dump(list1, pickle_file) #pickle.dump()
    pickle_file.close()

    ##在讀出來
    pickle_file = open('my_list.pkl', 'rb')
    list2 = pickle.load(pickle_file) #pickle.load()
    pickle_file.close()
    print(f"read:{list2}")

def pickle_test2():
    """从 Pickle 中重构 python 对象"""
    pkl_file = open('my_list.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    pprint.pprint(data1)

    # data2 = pickle.load(pkl_file)
    # pprint.pprint(data2)

    pkl_file.close()

if __name__ == '__main__':
    # pickle_test()
    pickle_test2()