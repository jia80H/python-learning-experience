""" 可迭代对象 """
# list/tuple/dict/set/str/range/filter/map 是可迭代对象
# for...in <可迭代对象>
from collections.abc import Iterable


class demo(object):
    def __init__(self, x):
        self.x = x


class test(object):
    def __init__(self, x):
        self.x = x

    def __iter__(self):  # 只要重写了__iter__方法就是一个可迭代对象
        return test2(self.x)


class test2():
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return 1
        else:
            raise StopIteration  # 让迭代器停止


class Foo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return 1
        else:
            raise StopIteration  # 让迭代器停止


f = Foo(3)
# isinstance: 用来判断一个对象是否是由指定的类创建出来的
d = demo(100)
print(isinstance(d, Iterable))  # False
m = []
print(isinstance(m, Iterable))  # True
i = test(100)
print(isinstance(i, Iterable))  # True

# for...in 的本质
# for...in 本质就是调用对象__iter__方法,获取到这个方法的返回值
# 这个返回值是一个迭代器对象,然后再调用这个对象的__next__方法
for x in i:
    print(x)

for x in f:
    print(x)

#####################


class Foo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return self.count
        else:
            raise StopIteration


f = Foo(31)
# print(f.__iter__().__next__())  # 手动调用

# i = f.__iter__()
# i.__next__()

i = iter(f)  # 内置函数iter 可以获取到一个可迭代对象的迭代器
print(next(i))

""" 迭代器的使用 """
# 求斐波那契数列


class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


# f = Fibonacci(3000)  # 占时间, 不占空间
# x = [1, 1, 2, '......', 'Fibonacci(3000)']   # 占用大量空间
