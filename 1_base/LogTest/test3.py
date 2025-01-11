import logging
import test1

logger = logging.getLogger('test_logger_1')

if __name__ == '__main__':
    logger.debug("test3 debug log")
    logger.info("test3 info log")
    logger.warning("test3 warning log")
    logger.error("test3 error log")
    logger.critical("test3 critical log")