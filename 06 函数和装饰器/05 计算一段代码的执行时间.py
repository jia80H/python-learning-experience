""" 普通版 """
import time  # time 模块可以获取当前时间

# 代码运行前获取一下时间
start = time.time()
# time模块里的time方法，可以获取当前时间戳
# 时间戳是从 1970-01-01 00:00:00 UTC ~ 当前UTC时间的秒数
# 我们是UTC时间+8
print('start=', start)

x = 0
for i in range(1, 10000000):
    x += i

print(x)
end = time.time()

print('耗时', (end - start), 's')

""" 优化版 """


def cal_time(fn):
    import time
    start = time.time()
    fn()
    end = time.time()
    print('耗时', (end - start), 's')


def cal():
    x = 0
    for i in range(1, 10000000):
        x += i


cal_time(cal)

""" 装饰器版 """


def cal_time(fn):
    def inner():
        import time
        start = time.time()
        fn()
        end = time.time()
        print('耗时', (end - start), 's')

    return inner


@cal_time
def cal():
    x = 0
    for i in range(1, 10000000):
        x += i
    print(x)


cal()
