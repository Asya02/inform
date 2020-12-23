import unittest
from queue import Queue


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.test_queue = Queue()

    def test_enqueue(self):
        self.assertEqual(self.test_queue.enqueue(1), 1)
        self.assertEqual(self.test_queue.size_function(), 1)

    def test_dequeue(self):
        self.assertEqual(self.test_queue.dequeue(), None)
        self.assertEqual(self.test_queue.size_function(), 0)

    def test_dequeue2(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.test_queue.enqueue(3)
        self.test_queue.dequeue()
        self.test_queue.dequeue()
        self.assertEqual(self.test_queue.dequeue(), 3)
        self.assertEqual(self.test_queue.size_function(), 0)

    def test_get_front(self):
        self.assertEqual(self.test_queue.get_front(), None)
        self.assertEqual(self.test_queue.size_function(), 0)

    def test_get_front2(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.test_queue.enqueue(3)
        self.assertEqual(self.test_queue.get_front(), 1)

    def test_get_back(self):
        self.assertEqual(self.test_queue.get_back(), None)
        self.assertEqual(self.test_queue.size_function(), 0)

    def test_get_back2(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.test_queue.enqueue(3)
        self.assertEqual(self.test_queue.get_back(), 3)

    def test_clear(self):
        self.assertEqual(self.test_queue.clear(), None)
        self.assertEqual(self.test_queue.size_function(), 0)

    def test_clear2(self):
        self.test_queue.enqueue(1)
        self.assertEqual(self.test_queue.clear(), None)
        self.assertEqual(self.test_queue.size_function(), 0)


if __name__ == '__main__':
    unittest.main()
