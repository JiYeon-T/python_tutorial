import time

# 将时间戳转换为标准时间格式
def timestamp_to_fomat(timestamp=None,format='%Y%m%d_%H%M%S'):
    # 默认返回当前格式化好的时间
    # 传入时间戳的话，把时间戳转换成格式化好的时间，返回
    if timestamp:
        time_tuple = time.localtime(timestamp)
        res = time.strftime(format,time_tuple)
    else:
        res = time.strftime(format)  # 默认读取当前时间
    return res


# 将标准时间转换为时间戳
def str_to_timestamp(str=None, format='%Y-%m-%d %H:%M:%S'):
    if str:
        tp = time.strptime(str,format)  # 转成时间元组
        res = time.mktime(tp)  # 再转成时间戳
    else:
        res = time.time()  # 默认获取当前时间戳
    return int(res)


def test():
    DATE_FORMAT = "%Y%m%d_%H%M%S"
    print(time.time())
    print(time.asctime(DATE_FORMAT))
    print(time.gmtime())
    print(time.localtime())


if __name__ == '__main__':
    print(timestamp_to_fomat(time.time()))