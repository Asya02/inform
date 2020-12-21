class Element:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

# Добавление данных элемента в очередь
    def enqueue(self, data):
        if self.back is None:
            self.front = Element(data)
            self.back = self.front
        else:
            self.back.next = Element(data)
            self.back.next.prev = self.back
            self.back = self.back.next

# Удаление первого элемента из очереди
    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front.data
            self.front = self.front.next
            self.front.prev = None
            return temp

# Возврат верхнего элемента в очередь
    def first(self):
        return self.front.data

# Размер очереди
    def size(self):
        temp = self.front
        count = 0
        while temp is not None:
            count = count+1
            temp = temp.next
        return count

# Очистить очередь
    def clear(self):
        self.front = None
        self.back = None
        self.size = None
