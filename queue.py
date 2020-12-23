class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

# Добавление данных элемента в очередь
    def enqueue(self, data):
        element = Element(data)
        self.size += 1
        if self.back is None:
            self.front = element
            self.back = self.front
        else:
            self.back.next = element
            self.back = self.back.next
        return self.front.data


# Удаление первого элемента из очереди
    def dequeue(self):
        if self.front is None:
            self.back = None
            return None
        else:
            temp = self.front.data
            self.size -= 1
            self.front = self.front.next
            return temp


# Возврат верхнего элемента в очередь
    def first(self):
        if self.size == 0:
            return None
        else:
            return self.front.data

# Размер очереди
    def size_function(self):
        return self.size

# Очистить очередь
    def clear(self):
        self.front = None
        self.back = None
        self.size = 0
