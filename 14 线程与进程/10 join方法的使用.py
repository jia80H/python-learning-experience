# join 线程和进程都有join方法
import time
import threading

x = 10


def test(a, b):
    time.sleep(1)
    global x
    x = a + b


# test(1, 1)
# print(x)  # 2

t = threading.Thread(target=test, args=(1, 1))
t.start()

print(x)

t.join()  # 让主线程等待

print(x)  # 10
