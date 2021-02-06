import threading
import time


def dance():
    for i in range(50):
        time.sleep(0.1)
        print('dance')


def sing():
    for i in range(50):
        time.sleep(0.1)
        print('sing')


# 多任务同时执行
# python里执行多任务的方法:
# 多线程 多进程 多线程+多进程

# 不能同时进行
# dance()
# sing()

# target 需要的是一个函数, 用来指定线程需要执行的任务
t1 = threading.Thread(target=dance)  # 创建线程1
t2 = threading.Thread(target=sing)  # 创建线程2

# 启动线程
t1.start()
t2.start()
