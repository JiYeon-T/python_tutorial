import threading as th
import logging
import time
# Condition 使用场景
# Condition 对象就是条件变量，它总是与某种锁相关联，可以是外部传入的锁或是系统默认创建的锁。
# 当几个条件变量共享一个锁时，你就应该自己传入一个锁。这个锁不需要你操心，Condition 类会管理它。
# acquire() 和 release() 可以操控这个相关联的锁。其他的方法都必须在这个锁被锁上的情况下使用。
# wait() 会释放这个锁，阻塞本线程直到其他线程通过 notify() 或 notify_all() 来唤醒它。一旦被唤醒，这个锁又被 wait() 锁上。
# 示例:consumer() and Producer()

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) - %(message)s')
def consumer(cv):
    """ 消费者 """
    logging.debug('consumer thread started')
    with cv: # cv.acquire1
        logging.debug('consumer wating')
        cv.acquire() # acquire 2
        cv.wait() # 阻塞等生产者发送通知
        logging.debug('consumer consumed the resource')
        cv.release() # release2
        # cv.release1
    logging.debug('consumer thread end')

def producer(cv):
    """ 生产者 """
    logging.debug('producer thread started')
    with cv: # cv.acquire1
        cv.acquire() # cv.acquire2
        logging.debug('Making resource available')
        logging.debug('Notify to all consumer')
        #cv.notify() # 通知某一个线程
        cv.notify_all()
        cv.release() # cv.release2
        # cv.release1
    logging.debug('producer thread end')

def test():
    condition = th.Condition()
    cs1 = th.Thread(target=consumer, name="consumer1", args=(condition, ))
    cs2 = th.Thread(target=consumer, name="consumer2", args=(condition, ))
    pd = th.Thread(target=producer, name="producer", args=(condition, ))
    cs1.start()
    cs2.start()
    time.sleep(2)
    pd.start()

if __name__ == '__main__':
    test()

