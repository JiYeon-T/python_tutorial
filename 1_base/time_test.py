import time
import calendar

# https://www.runoob.com/python3/python3-date-time.html
# Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
# https://docs.python.org/3/library/datetime.html


# 将时间戳(从 1970/1/1 开始的秒数)转换为标准时间格式
def timestamp_to_fomat_str(timestamp=None,format='%Y%m%d_%H%M%S'):
    # 默认返回当前格式化好的时间
    # 传入时间戳的话，把时间戳转换成格式化好的时间，返回
    if timestamp:
        time_tuple = time.localtime(timestamp)
        print(f"time:{time_tuple}")
        # 我们可以使用 time 模块的 strftime 方法来格式化日期：
        res = time.strftime(format, time.localtime())
    else:
        res = time.strftime(format)  # 默认读取当前时间
    return res


# 将标准时间转换为时间戳
def format_str_to_timestamp(str=None, format='%Y-%m-%d %H:%M:%S'):
    if str:
        # time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
        # 根据fmt的格式把一个时间字符串解析为时间元组。
        timestr = time.strptime(str, format)  # 转成时间元组
        # # 将格式字符串转换为时间戳
        # 	time.mktime(tupletime)
        # 接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
        res = time.mktime(timestr)  # 再转成时间戳
        print(f"timestamp:{res}")
    else:
        res = time.time()  # 默认获取当前时间戳
    return int(res)


def __time_test():
    """time 模块的其他 api"""
    DATE_FORMAT = "%Y%m%d_%H%M%S"
    print("timestamp:", time.time())
    # 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
    print("asctime:", time.asctime(time.localtime()))
    # time.gmtime([secs])
    # 接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
    print('gmtime:', time.gmtime())
    # time.localtime([secs]
    # 接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）
    print('localtime:', time.localtime())
    # 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
    print('altzone:', time.altzone)
    # asctime: 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
    print('asctime:', time.asctime(time.localtime()))
    # time.clock()
    # 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
    # 由于该方法依赖操作系统，在 Python 3.3 以后不被推荐，而在 3.8 版本中被移除，需使用下列两个函数替代。

    # time.perf_counter()
    # 返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间。由于返回值的基准点是未定义的，
    # 所以，只有连续调用的结果之间的差才是有效的。
    print('系统运行时间:', time.perf_counter(), time.perf_counter_ns())  # 返回系统运行时间
    # time.process_time()
    # 返回当前进程执行 CPU 的时间总和，不包含睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。
    print('进程运行时间:', time.process_time(), time.perf_counter_ns())  # 返回进程运行时间
    # time.ctime([secs])
    # 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
    print(f"ctime:{time.ctime()}")
    # 	time.sleep(secs)
    # 推迟调用线程的运行，secs指秒数。
    time.sleep(1)
    # 	time.strftime(fmt[,tupletime])
    # 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
    print(time.strftime("%H/%m/%d %H:%M:%S", time.localtime()))
    # 属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
    print(f"时区:{time.timezone}")
    # 属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。
    print(f"名称:{time.tzname}")


def __calendar_test():
    """
    # Constants for weekdays
    (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
    """

    # calendar.calendar(year,w=2,l=1,c=6)
    # 返回一个多行字符串格式的 year 年年历，3 个月一行，间隔距离为 c。
    # 每日宽度间隔为w字符。每行长度为 21* W+18+2* C。l 是每星期行数。
    cal = calendar.calendar(2026)
    print(cal, end="\n\n")

    # calendar.firstweekday( )
    # 返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一
    first_day = calendar.firstweekday()
    print(first_day)

    # calendar.isleap(year)
    # 是闰年返回 True，否则为 False。
    print(f"isleap:", calendar.isleap(2026))

    # calendar.leapdays(y1,y2)
    # 返回在Y1，Y2两年之间的闰年总数。
    print(f"leap year totoal num:", calendar.leapdays(2020, 2030))

    # calendar.month(year,month,w=2,l=1)
    # 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
    # cal = calendar.month(2026, 1)
    # print(cal, end="\n\n")

    # calendar.monthcalendar(year,month)
    # 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。
    # Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
    print(calendar.monthcalendar(2026, 1))

    # calendar.monthrange(year,month)
    # 返回两个整数。第一个是该月的星期几，第二个是该月有几天。星期几是从0（星期一）到 6（星期日）。
    # 注意:星期从 0 开始
    # (5, 30)解释：5 表示 2014 年 11 月份的第一天是周六，30 表示 2014 年 11 月份总共有 30 天。
    print(calendar.monthrange(2026, 1))

    # calendar.prcal(year, w=0, l=0, c=6, m=3)
    # 相当于 print (calendar.calendar(year, w=0, l=0, c=6, m=3))。
    # print(calendar.prcal(2026))

    # calendar.prmonth(theyear, themonth, w=0, l=0)
    # 相当于 print(calendar.month(theyear, themonth, w=0, l=0))。
    print(calendar.prmonth(2026, 1), end="\n\n")

    # calendar.setfirstweekday(weekday)
    # 设置每周的起始日期码。0（星期一）到6（星期日）。
    # calendar.setfirstweekday()

    # calendar.timegm(tupletime)
    # 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
    print(f'timestamp:', time.time())
    print(calendar.timegm(time.localtime()))

    # calendar.weekday(year,month,day)
    # 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
    print("星期:", calendar.weekday(2026, 1, 11) + 1)  # 实际星期需要 + 1


def __datetime_test():
    """
    https://docs.python.org/3/library/datetime.html
    """
    import datetime
    # TODO
    pass


def __perf_counter_test():
    scale = 50

    print("执行开始".center(scale // 2, "-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -

    start = time.perf_counter()  # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。两个函数取差，即实现从时间点B1到B2的计时功能。
    for i in range(scale + 1):
        a = '*' * i  # i 个长度的 * 符号
        b = '.' * (scale - i)  # scale-i） 个长度的 . 符号。符号 * 和 . 总长度为50
        c = (i / scale) * 100  # 显示当前进度，百分之多少
        dur = time.perf_counter() - start  # 计时，计算进度条走到某一百分比的用时
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur),
              end='')
        # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，
        # 输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；
        # {}，对应输出的数为a；{}，对应输出的数为b；
        # {:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
        time.sleep(0.1)  # 在输出下一个百分之几的进度前，停止0.1秒
    print("\n" + "执行结果".center(scale // 2, '-'))


if __name__ == '__main__':
    # print(timestamp_to_fomat(time.time()))
    # __time_test()
    # str_to_timestamp()
    # __calendar_test()
    __perf_counter_test()