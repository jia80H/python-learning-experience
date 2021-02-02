# 生成器的本质就是迭代器。
# 生成器包括两种:生成器函数和生成器表达式
# 生成器可以实现多任务(协程-->模拟并发)。

""" 生成器函数 """
# 一个包含yield关键字的函数就是一个生成器函数。
# 并且yield不能和return共用，并且yield只能用在函数内。
# (1).生成器函数执行之后会得到一个生成器作为返回值，并不会执行函数体。
# (2).执行了__next__()方法之后才会执行函数体，并且获得返回值。
# (3).next()内置方法，内部调用生成器函数的__next__()方法。
# (3).yield和return相同的是可以返回值，但是不同的是yield 不会结束函数

# 练习1:创建一个生成器，并且调用
# 创建生成器
def generator():
    print('xxx')
    yield
    print('zzz')

# 接收返回值
ret = generator()
print(ret)  # 返回一个生成器对象 <generator object generator at 0x0000000002165888>
# 调用__next__()方法执行生成器
ret.__next__()  # xxx 执行函数体，遇到yield结束
# ret.__next__()  # StopIteration 报错
# next()方法相当于调用__next__方法
# next(ret)
# next(ret)


# 练习2：创建一个生成器，并且设置返回值
def generator():
    print('xxx')
    yield 1  # 返回值

g = generator()
ret = next(g)  # xxx
print(ret)  # 1


# 练习3：创建生成器，定义多个yield 值
def generator():
    print('xxx')
    yield 1
    print('zzz')
    yield 2

g = generator()
ret1 = next(g)  # xxx
ret2 = next(g)  # zzz
print(ret1, ret2)  # 1,2
# 练习4：创建生成器，生成200万桶康师傅方便面。
# 一秒一桶
def ksf():

    for i in range(1, 2*10**6):
        yield '正在生产第{}桶'.format(i)

g = ksf()
print(next(g))

import time

for i in g:
    print(i)
    time.sleep(1)

""" send """
# send 获取下一个值的效果和next()基本一致,
# 只是在获取下一个值的时候，给上一yield的位置传递一个数据

# 使用send的注意事项
# (1).第一次使用生成器的时候 是用next获取下一个值
# (2).最后一个yield不能接受外部的值

# 练习1：使用send()方法给yield传递参数
def generator():
    print('=====')
    content = yield 1
    print(content)
    print('xxxx')
    yield 2


g = generator()
c = next(g)
print(c)
s = g.send(88)  # 传给上一个yield,yield再传给content
print(s)

# 练习2：计算移动平均值
def avg():
    sum = 1  # 数字个数
    avg = 0  # 平均数
    total = 0  # 和
    while True:
        ret = yield avg
        total += ret
        avg = total/sum
        sum += 1

g = avg()
next(g)
print(g.send(10))  # 10.0
print(g.send(20))  # 15.0
print(g.send(30))  # 20.0

""" yield form """
# yield from 循环遍历容器类型

# 练习1：使用for循环取出g1生成器中所有的值。
def g1():
    for i in range(3):
        yield i
    for j in 'abc':
        yield j

g = g1()
for gg in g:
    print(gg)

# 练习2：使用 yield from 遍历出可变数据类型中的数据。
def g1():
    yield from range(3)

    yield from 'abc'


g = g1()
for gg in g:
    print(gg)

""" 生成器表达式 """
# 格式：将列表解析式[] 改成 () 即可。

# 列表表达式
lst = [i for i in range(4)]
print(lst)  # [0, 1, 2, 3]

# 练习1：使用生成器表达式，进行数数.
g = (i for i in range(4))
for i in g:
    print(i)

# 练习2：利用list转换数数
def demo():
    for i in range(4):
        yield i

g = demo()
print(list(g))  # 列表转换自动调用__next__方法 [0, 1, 2, 3]