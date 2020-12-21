import unittest
from queue import Queue, Element


class TestStringMethods(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

    def test_dequeue(self):
        queue = Queue()
        queue.dequeue()

    def test_dequeue2(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()

    def test_first(self):
        queue = Queue()
        queue.first()

    def test_first2(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.first()

    def test_size(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.size()

    def test_size2(self):
        queue = Queue()
        queue.size()

    def test_clear(self):
        queue = Queue()
        queue.clear()

    def test_clear2(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.clear


if __name__ == '__main__':
    unittest.main()
