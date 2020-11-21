x = int(input())
a = int(input())
b = int(input())
c = int(input())
class N:
    def __init__(self, x):
        self.x = x

    def check(self, a, b, c):
        if (a+b+c) == x:
            print("Сумма чисел равна %d" % self.x)

n = N(x)
n.check(a, b, c)

x = 180
a = int(input())
b = int(input())
c = int(input())
class N:
    def __init__(self, x):
        self.x = x

    def check(self, a, b, c):
        if (a+b+c) == x:
            print("Введённые числа являются углами треугольника")

n = N(x)
n.check(a, b, c)
