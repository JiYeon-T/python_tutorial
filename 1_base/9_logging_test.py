import logging
# 几乎所有开发语言都会内置日志相关功能，或者会有比较优秀的第三方库来提供日志操作功能，比如：log4j，log4php等。
# 它们功能强大、使用简单。Python自身也提供了一个用于记录日志的标准库模块--logging。
# 当为某个应用程序指定一个日志级别后，应用程序会记录所有日志级别大于或等于指定日志级别的日志信息，
# 而不是仅仅记录指定级别的日志信息，nginx、php等应用程序以及这里要提高的python的logging模块都是这样的。
# logging.basicConfig(level=logging.DEBUG)
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
LOG_FILENAME = "log_test.log"
# 函数是一个一次性的简单配置工具使，
# 也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作。
logging.basicConfig(filename='abc.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def log_test():
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")


    #
    logging.log(logging.DEBUG, "debug")
    logging.log(logging.INFO, "info")
    logging.log(logging.WARNING, "warning")
    logging.log(logging.ERROR, "ERROR")
    logging.log(logging.CRITICAL, "critical")





if __name__ == '__main__':
    log_test()
    pass