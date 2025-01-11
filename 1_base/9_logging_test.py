import logging

# logging.basicConfig(level=logging.DEBUG)
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
LOG_FILENAME = "log_test.log"
# 函数是一个一次性的简单配置工具使，
# 也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作。
# logging.basicConfig(filename='abc.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def log_test():
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")

    logging.log(logging.DEBUG, "debug")
    logging.log(logging.INFO, "info")
    logging.log(logging.WARNING, "warning")
    logging.log(logging.ERROR, "ERROR")
    logging.log(logging.CRITICAL, "critical")





if __name__ == '__main__':
    log_test()
    pass