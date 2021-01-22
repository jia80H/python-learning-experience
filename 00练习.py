""" 装饰器版 """
def cal_time(fn):
    def inner():
        import time
        start = time.time() 
        fn()
        end = time.time() 
        print('耗时',(end - start),'s')

    return inner


@cal_time
def cal():
    x = 0
    for i in range(1,10000000):
        x += i
    print(x)

cal()