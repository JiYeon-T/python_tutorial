import logging
import test1

# logging.basicConfig(filename="def.log", level=logging.DEBUG) # 如果再使用一次 root logger 会触发两次 log 保存， test1 & test2
logger = logging.getLogger('test_logger_1')



if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    logger.debug("test2 debug log")
    logger.info("test2 info log")
    logger.warning("test2 warning log")
    logger.error("test2 error log")
    logger.critical("test2 critical log")
