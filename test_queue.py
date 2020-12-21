import unittest
from queue import Queue

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.test_queue = Queue()
        
    def test_enqueue(self):
        self.assertEqual(self.test_queue.enqueue(1), 1)


    def test_dequeue(self):
        self.assertEqual(self.test_queue.dequeue(), None)

    def test_dequeue2(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.test_queue.enqueue(3)
        self.test_queue.dequeue()
        self.assertEqual(self.test_queue, 23)

    def test_first(self):
        self.test_queue.first()
        self.assertEqual(self.test_queue, None)

    def test_first2(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.test_queue.enqueue(3)
        self.test_queue.first()
        self.assertEqual(self.test_queue, 1)

    def test_size(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.test_queue.enqueue(3)
        self.test_queue.size()
        self.assertEqual(self.test_queue, 3)
        
    def test_size2(self):
        self.test_queue.size()
        self.assertEqual(self.test_queue, 0)

    def test_clear(self):
        self.test_queue.clear()
        self.assertEqual(self.test_queue, None)

    def test_clear2(self):
        self.test_queue.enqueue(1)
        self.test_queue.enqueue(2)
        self.test_queue.enqueue(3)
        self.test_queue.clear
        self.assertEqual(self.test_queue, None)

        
if __name__ == '__main__':
    unittest.main()
