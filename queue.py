class Element:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        


class Queue:
    def __init__(self, size):
        self.front = None
        self.back = None
        self.size = 0

# Добавление данных элемента в очередь
    def enqueue(self, data, size):
        element = Element(data)
        size += 1
        if self.back is None:
            self.front = element
            self.back = self.front
        else:
            self.back.next = element
            self.back.next.prev = self.back
            self.back = self.back.next

# Удаление первого элемента из очереди
    def dequeue(self, size):
        if self.front is None:
            return None
        else:
            size -= 1
            temp = self.front.data
            self.front = self.front.next
            self.front.prev = None
            return temp

# Возврат верхнего элемента в очередь
    def first(self, size):
        if size == 0:
            return None
        else:
            return self.front.data

# Размер очереди
    def size(self, size):
        return size

# Очистить очередь
    def clear(self):
        self.front = None
        self.back = None
        size = 0
