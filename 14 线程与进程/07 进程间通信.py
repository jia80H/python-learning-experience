import os
import multiprocessing
import time


def produce(x):
    for i in range(10):
        time.sleep(1)
        print('生产了面包pid={},第{}个'.format(os.getpid(), i))
        x.put('pid{}{}'.format(os.getpid(), i))


def consume(x):
    for i in range(10):
        time.sleep(1)
        print('购买了面包{}'.format(x.get()))
        print('pid={}'.format(os.getpid()))


if __name__ == '__main__':
    print('主进程的pid={}'.format(os.getpid()))
    q = multiprocessing.Queue()  # 进程和线程中队列导入模块不同

    p1 = multiprocessing.Process(target=produce, args=(q,))
    p2 = multiprocessing.Process(target=produce, args=(q,))
    p3 = multiprocessing.Process(target=produce, args=(q,))
    p1.start()
    p2.start()
    p3.start()

    c1 = multiprocessing.Process(target=consume, args=(q,))
    c2 = multiprocessing.Process(target=consume, args=(q,))
    c1.start()
    c2.start()
