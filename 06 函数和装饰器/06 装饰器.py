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
# 看懂这个
def cal_time(fn):

    print('我是外部函数，我被调用了')
    print('fn={}'.format(fn))

    def inner(s):
        import time
        start = time.time() 
        k= fn(s)
        end = time.time() 
        print('耗时',(end - start),'s')
        return k


    return inner


@cal_time
def cal(n):
    x = 0
    for i in range(1,n):
        x += i
    return x # 和之前不一样
print(cal(1000000))

""" 装饰器的使用 """
# 更改需求 但不改变源代码
# 开放封闭原则 ：
# 软件实体应该是可扩展，而不可修改的。
# 也就是说，对扩展是开放的，而对修改是封闭的。

# 新需求，需要防沉迷

# 先把装饰器结构搭建出来
def can_play(fn):
    def inner():
        pass

    return inner

# 原来的需求
def play_game(name,game):
    print('{}正在玩儿{}'.format(name,game))

# 成品
def can_play(fn):
    def inner(x,y,*args,**kwargs):
        print(args)
        if args[0] >= 18:
            fn(x,y)
        else:
           print('未成年')

    return inner


@can_play
def play_game(name,game):
    print('{}正在玩儿{}'.format(name, game))


play_game('Mlfoy','TFT',22)
