import threading
import time

# 多线程可以共享同一个全局变量
# 但是会有线程安全问题(如下)
ticket = 20


def sell_ticket():
    global ticket
    while True:
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            print('{}卖出一张票,还剩{}张'.format(
                threading.current_thread().name, ticket))
        else:
            print('票售罄')
            break


t1 = threading.Thread(target=sell_ticket, name='线程1')  # 创建线程1
t2 = threading.Thread(target=sell_ticket, name='线程2')  # 创建线程2

t1.start()
t2.start()
