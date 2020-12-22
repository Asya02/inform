class Element:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


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
            self.back.next.prev = self.back
            self.back = self.back.next

        return self.front.data


# Удаление первого элемента из очереди
    def dequeue(self):
        if self.size == 1:
            self.size = 0
            return None
        elif self.size == 0:
            return None
        else:
            self.size -= 1
            self.front = self.front.next
            self.front.prev = None
            return self.front.data


# Возврат верхнего элемента в очередь
    def first(self):
        if self.size == 0:
            return None
        else:
            return self.front.data


# Очистить очередь
    def clear(self):
        self.front = None
        self.back = None
        self.size = 0
