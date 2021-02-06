import threading
import time

ticket = 10

# 创建一把锁
lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:
        lock.acquire()  # 加同步锁
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            lock.release()
            print('{}卖出一张票,还剩{}张'.format(
                threading.current_thread().name, ticket))
        else:
            print('票售罄')
            lock.release()
            break


t1 = threading.Thread(target=sell_ticket, name='线程1')  # 创建线程1
t2 = threading.Thread(target=sell_ticket, name='线程2')  # 创建线程2

t1.start()
t2.start()
