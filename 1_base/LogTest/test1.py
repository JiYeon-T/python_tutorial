import logging

# create Logger
logger_name = "test_logger_1"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# create Handler
log_path = "./log_test.log"
# fh = logging.FileHandler(log_path)
fh = logging.StreamHandler()
fh.setLevel(logging.DEBUG) # 低于 INFO 的 log 不处理

# create Formatter
# fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
fmt = "%(asctime)-15s %(levelname)s [%(thread)d|%(threadName)s] %(message)s"
# datefmt = "%a %d %b %Y %H:%M:%S"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add Handler and Formatter to Logger
fh.setFormatter(formatter)
logger.addHandler(fh)


# import 一个模块的时候, 模块外面的这些代码是会被执行的.
# logger.debug("test1 debug log")
# logger.info("test1 info log")
# logger.warning("test1 warning log")
# logger.error("test1 error log")
# logger.critical("test1 critical log")

if __name__ == '__main__':
    logger.debug("test1 debug log")
    logger.info("test1 info log")
    logger.warning("test1 warning log")
    logger.error("test1 error log")
    logger.critical("test1 critical log")