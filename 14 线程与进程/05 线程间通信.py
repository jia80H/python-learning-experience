import time
import threading
import queue
# queue结构可以在不同线程间传递数据
name = threading.current_thread


def produce():
    for i in range(10):
        time.sleep(1)
        print('生产线{}生产面包b{}'.format(name().name, i))
        q.put('生产线{}b{}'.format(name().name, i))


def consume():
    for i in range(10):
        time.sleep(0.3)
        # q.get() 方法是一个阻塞方法
        print('消费者{}买到了来自{}的面包'.format(name().name, q.get()))


q = queue.Queue()  # 创建一个q

# 生产线
p1 = threading.Thread(target=produce, name='p1')
p2 = threading.Thread(target=produce, name='p2')

# 消费者
c1 = threading.Thread(target=consume, name='c1')
c2 = threading.Thread(target=consume, name='c2')
c3 = threading.Thread(target=consume, name='c3')

p1.start()
p2.start()

c1.start()
c2.start()
c3.start()
