
""" 匿名函数 """

# 除了使用def 关键字定义一个函数外，
# 我们还能使用lambda 表达式定义一个函数
# 匿名函数用来表达一个简单的函数，函数调用的次数很少，基本只用1次

# 调用匿名函数的 方法
# 方法一：给它定义一个名字（很少用）

# 给函数起名
from functools import reduce


def add(a, b):
    return a + b


print('0x%X' % id(add))  # 0x2AD5AD26820
print(add(3, 4))  # 7

fn = add  # 相对于给函数fn起了一个笔名
print(fn(3, 7))  # 10
print('0x%X' % id(add))  # 0x2AD5AD26820


def m(a, b): return a * b

# 方法二：把这个函数当作参数传给另一个函数使用（使用场景较多）

# 普通版本


def calc(a, b, fn):
    c = fn(a, b)
    return c


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


print(calc(12, 3, add))
print(calc(3, 2, minus))

# 上述缩减版


def calc(a, b, fn):
    c = fn(a, b)
    return c


print(calc(12, 3, lambda x, y: x + y))
print(calc(3, 2, lambda x, y: x - y))


""" sort进阶 """
# 回顾

# 有几个内置函数和内置类用到了匿名函数

nums = [2, 8, 32, 1, 5, 7, 83, 66, 4]
# 列表的sort方法，会直接对列表进行排序
nums.sort()
print(nums)

ints = (1, 5, 3, 7, 38, 9, 56)
# sort内置函数，不会改变原有数据，而是生成一个新的有序列表
x = sorted(ints)
print(x)

# 进阶
students = [
    {'name': 'zhangsan', 'age': '18', 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': '21', 'score': 97, 'height': 185},
    {'name': 'jack', 'age': '22', 'score': 100, 'height': 175},
    {'name': 'tony', 'age': '23', 'score': 90, 'height': 176},
    {'name': 'henry', 'age': '20', 'score': 95, 'height': 172},
]

# 字典和字典之间不能使用比较运算符
# students.sort()

# 需要传递参数key 指定比较规则
# key需要的是一个函数
# 在sort内部实现的时候，调用key中方法，并且传入了一个参数，参数就是列表里的元素
students.sort(key=lambda ele:  ele['name'])
print(students)

""" filter的使用 """
# filter 对可迭代对象进行过滤，得到的是一个filter对象
# python2中是内置函数，python3中是内置类

ages = [18, 23, 12, 33, 17, 19]
# filter可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象
# fillter结果是一个filter类型的对象 # 可迭代可以使用for……in……遍历
x = filter(lambda ele: ele > 18, ages)
print(x)  # <filter object at 0x0000027DB621FBE0>

adults = list(x)
print(adults)

""" map的使用 """
# map是让可迭代对象里的每一个元素都执行一下函数操作
ages = [18, 23, 12, 33, 17, 19]
m = map(lambda ele: ele + 2, ages)
print(list(m))

""" reduce的使用 """

# reduce 以前是一个内置函数
scores = [100, 89, 90, 67]
print(reduce(lambda x, y: x+y, scores))  # 346 = 100 + 89 +……
print(reduce(lambda x, y: x*y, scores))
#   reduce
# Apply a function of two arguments cumulatively to the items of a
# sequence, from left to right, so as to reduce the sequence to a single
# value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#  calculates ((((1+2)+3)+4)+5). If initial is present, it is placed
# before the items of the sequence in the calculation, and serves as a
# default when the sequence is empty.
students = [
    {'name': 'zhangsan', 'age': '18', 'score': 98, 'height': 180},
    {'name': 'lisi', 'age': '21', 'score': 97, 'height': 185},
    {'name': 'jack', 'age': '22', 'score': 100, 'height': 175},
    {'name': 'tony', 'age': '23', 'score': 90, 'height': 176},
    {'name': 'henry', 'age': '20', 'score': 95, 'height': 172},
]
# 求学生总年龄
print(reduce(lambda x, y: x+int(y['age']), students, 0))  # 104
# 最后边的0是初始值
