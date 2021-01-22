""" 高阶函数类型 """
# 1、一个函数作为另一个函数的参数 
# 如lambda函数
# 2、一个函数作为另一个函数的返回值

def foo():
    print('我是foo，我被调用了')
    return 'foo' # 返回字符串foo

def bar():
    print('我是bar，我被调用了')
    return foo   # 返回函数名

def test():
    print('我是test，我被调用了')
    return foo()  # 返回字符串foo

x = test()
print('x是{}'.format(x))
# 我是test，我被调用了
# 我是foo，我被调用了
# x是foo
print('------------')
y = bar()
print(y)
y()
# 我是bar，我被调用了
# <function foo at 0x0000026C126C6820>
# 我是foo，我被调用了
print('------------')



# 3、函数内部再定义一个函数（函数的嵌套）

def outer():
    m = 100

    def inneer():
        n = 90
        print('我是inner函数')
    
    print('我是outer函数')
    return inneer

outer()()

""" 闭包的格式 """
def outer():
    x = 100 # 在外部函数里定义一个变量x，是一个局部变量

    def inneer():
        # 在内部函数如何修改外部函数的局部变量
        nonlocal x
        y = x + 1
        x = 20

        print('inner 里的y = ',y)

    return inneer


outer()() # inner 里的y =  101
