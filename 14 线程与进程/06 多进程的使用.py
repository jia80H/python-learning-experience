import os
import multiprocessing
import time
# 同一进程的不同线程可以共享全局变量
# 不同进程不能共享全局变量
# 至少有一个主进程,主进程中至少有一个主线程


def dance(n):
    for i in range(n):
        time.sleep(1)
        print('正在跳舞{}'.format(i))
        print('dance的pid={}'.format(os.getpid()))


def sing(m):
    for i in range(m):
        time.sleep(1)
        print('正在唱歌{}'.format(i))
        print('sing的pid={}'.format(os.getpid()))


# windows 中需要下边这一行代码， 其他不需要
if __name__ == '__main__':
    print('主进程的pid={}'.format(os.getpid()))
    # 可以在任务管理器中终止进程

    # 创建两个进程
    # target 用来表示执行的任务
    # args 用来传参， 类型是一个元组(线程也可传参)
    p1 = multiprocessing.Process(target=dance, args=(20,))
    p2 = multiprocessing.Process(target=sing, args=(20,))

    p1.start()
    p2.start()
