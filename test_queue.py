import unittest
from queue import Queue


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.test_queue = Queue()

    def test_enqueue(self):
        self.assertEqual(self.test_queue.enqueue(1), 1)
        self.assertEqual(self.test_queue.size, 1)

    def test_dequeue(self):
        self.assertEqual(self.test_queue.dequeue(), None)
        self.assertEqual(self.test_queue.size, 0)

    def test_dequeue2(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.assertEqual(self.test_queue.dequeue(), 2)
        self.assertEqual(self.test_queue.size, 1)

    def test_first(self):
        self.assertEqual(self.test_queue.first(), None)
        self.assertEqual(self.test_queue.size, 0)

    def test_first2(self):
        self.test_queue.enqueue(1)
        self.assertEqual(self.test_queue.first(), 1)
        self.assertEqual(self.test_queue.size, 1)

    def test_clear(self):
        self.assertEqual(self.test_queue.clear(), None)
        self.assertEqual(self.test_queue.size, 0)

    def test_clear2(self):
        self.test_queue.enqueue(1)
        self.assertEqual(self.test_queue.clear(), None)
        self.assertEqual(self.test_queue.size, 0)

if __name__ == '__main__':
    unittest.main()
