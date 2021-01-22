""" 装饰器的基本使用 """
def cal_time(fn):

    print('我是外部函数，我被调用了')
    print('fn={}'.format(fn))

    def inner():
        import time
        start = time.time() 
        fn()
        end = time.time() 
        print('耗时',(end - start),'s')

    return inner


@cal_time
# 上行代码的第一件事是调用cal_time；
# 第二件事是把被装饰的函数传给fn
def cal():
    x = 0
    for i in range(1,10000000):
        x += i
    print(x)

# 第三件事：当再次调用cal函数时，这是的cal函数已经不是上面的cal
print('装饰后的cal={}'.format(cal)) 
#装饰后的cal=<function cal_time.<locals>.inner at 0x00000223FD0369D0>
cal()

""" 装饰器详解 """
