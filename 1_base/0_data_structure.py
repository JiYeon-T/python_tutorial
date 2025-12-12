# https://www.runoob.com/python3/python3-data-structure.html
import collections


def data_structure_test():
    """
    Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，
    一句话概括即：列表可以修改，而字符串和元组不能。
    """
    def list_op_api():
        l = [1, 2, 3, 4, 5]
        print(f"before:{l}")
        l.extend([4, 5, 6, 7]) # 扩充 list
        print(f"after:{l}")
    # list_op_api()

    class Stack(object):
        """通过列表实现栈的功能"""
        def __init__(self):
            self.stack = []

        def push(self, item):
            self.stack.append(item)

        def pop(self):
            if not self.is_empty():
                return self.stack.pop()
            else:
                raise IndexError("pop from empty stack")

        def peek(self):
            if not self.is_empty():
                return self.stack[-1]
            else:
                raise IndexError("pop from empty stack")

        def is_empty(self):
            return len(self.stack) == 0

        def size(self):
            return len(self.stack)

    def stack_test():
        s = Stack()
        s.push(1)
        s.push("ABC")
        print(f"size:{s.size()}")
        s.pop()
        print(f"size:{s.size()}")
    # stack_test()

    class Queue(collections.deque):
        """在 Python 中，列表（list）可以用作队列（queue），但由于列表的特点(TODO:链表???)，
        直接使用列表来实现队列并不是最优的选择。
        队列是一种先进先出（FIFO, First-In-First-Out）的数据结构，意味着最早添加的元素最先被移除。
        使用列表时，如果频繁地在列表的开头插入或删除元素，性能会受到影响，因为这些操作的时间复杂度是 O(n)。
        为了解决这个问题，Python 提供了 collections.deque，它是双端队列，可以在两端高效地添加和删除元素
        """
        def __init__(self):
            self.queue = []

        def enqueue(self, item):
            self.queue.append(item)

        def dequeue(self):
            if not self.is_empty():
                return self.queue.pop(0)
            else:
                raise IndexError("dequeue from a empty queue")

        def peek(self):
            if not self.is_empty():
                return self.queue[0]
            else:
                raise IndexError("peek from a empty queue")

        def is_empty(self):
            return len(self.queue) == 0

        def size(self):
            return len(self.queue)

    def queue_test():
        q = Queue()
        q.enqueue(123)
        q.enqueue("ABC")
        print(f"size:{q.size()}")
        print(f"dequeu:{q.dequeue()}")
        print(f"size:{q.size()}")
    queue_test()



if __name__ == '__main__':
    data_structure_test()