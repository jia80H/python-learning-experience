""" 什么是函数 """

# 函数就是一堆封装好的代码，在需要的时候调用
# 在python里用def 来声明一个变量

# def 函数名(参数):
#   函数要执行的操作

def tell_story():
    print('从前有座山，','山里有座庙，','庙里有个老和尚',sep='\n')
    print('老和尚在给小和尚讲故事，','故事的内容是：',sep='\n')

age = int(input('输入孩子年龄'))
if 0 <= age <= 3:
    for i in range(5):
        tell_story()
else:
    tell_story()

""" 函数的参数 """

# 函数声明时，括号里的参数为形式参数，简称形参
# 形参的值是不确定的，只是用来占位
def tell_story(place,person1,person2):
    print('从前有座山','山里有座'+place,'庙里有个'+person1,sep='\n')
    print(person1+'在给'+person2+'讲故事','故事的内容是',sep='\n')

#在调用函数的时候传递参数
# 传入的参数才是真正参与运算的数据，称为实参

#按顺序传递参数
tell_story('道观','老道','小道')
tell_story('尼姑庵','师太','小尼姑')

#按变量传递参数
#可以不按顺序
tell_story(person2='小和尚',person1='小和尚',place='庙')

""" 函数的返回值 """
# 返回值是函数执行的结果，并不是所有函数都必须有返回值
def add(a,b):
    c = a + b #变量c在外部不可见，只能在函数内部使用
    return c # return 表示一个函数的执行结果

result = add(1,2)
print(result ** 4)

# 如果一个函数没有返回值，它的返回值就是None

# print就是一个没有返回值的内置函数
x = print('hello')
print(x) # None
# input是一个有返回值的内置函数
age = input('age')
print(age)
help(print)

# 多个返回值
def shang_yu(m,n):
    x = m // n
    y = m % n
    return x,y # 返回的本质是一个元组
    #也可以这样写 x,y ==> [x,y] or (x,y) or {'x':x,'y':y}
    # 需要用相应的方法取出值

result = shang_yu(13,4)
print('商是{},余数是{}'.format(result[0],result[1]))


""" 函数的注释 """
def add(a,b):
    """
    这个函数是用来将两个数字相加
    a: 第一个数字
    b: 第二个数字
    return：两个数字的和
    """
    c = a + b 
    return c 

result = add(1,2)
print(result)
help(add) #help 可以获得函数的注释

#python可以传入不符合要求的参数
#建议输入的方法（仍可以输入不符合要求的）
def add2(a:int,b:int):
    c = a + b 
    return c 
y = add2('hello','world') #会提示但是无法阻止

""" 函数中调用函数 """
# 求[n,m)之间所有阶乘的和

# 阶乘
def factorial(n):
    y = 1
    for x in range(1,n+1):
        y = y*x
    return y

#阶乘的和
def fac_sum(n,m):
    a = 0
    for t in range(n,m):
        a = a + factorial(t)
    return a

fac_sum(3,5)

""" 全局变量和局部变量 """
a = 100 # 这个变量是全局变量，在整个py文件中都可以访问
word = 'hello'

def test():
    x = 'hello' 
    # 这个变量在函数内部定义的变量，是局部变量，
    # 只能在函数内部使用
    print('x = {}'.format(x))

    #     print('函数内部修改前a = {}'.format(a)) 

    # 如果局部变量的名字和全局变量同名，
    # 会在函数内部重新定义一个新的局部变量
    # 而不是修改全局变量
    a = 10
    print('函数内部修改后a = {}'.format(a))
    #上述修改不能共存
    
    # 在函数内部修改全局变量
    global word
    word = 'ok'

    # 内置函数 globals()可以查看全局变量 
    # locals()可以查看局部变量
    print('locals = {},globals = {}'.format(locals(),globals()))

test()
# print(x) # x 只能在函数内部使用，否则会报错
print('函数外部a = {}'.format(a))
print('函数外部word = {}'.format(word))

# 在python里，只有函数能够分割作用域