'''交换两个变量的值'''
a = 13
b = 20

#方法一 引入第三个变量
c = a
a = b
b = c
#方法二 运算符 只能是数字
a = a + b
b = a - b
a = a - b
#方法三 使用异或运算符
a = a ^ b
b = a ^ b
a = a ^ b
#方法四 python独有的
a, b = b , a

'''冒泡排序'''
numbs = [6,5,3,1,8,7,2,4]
i = 0
while i < len(numbs)-1:
    i += 1
    n = 0
    while n < len(numbs) - 1: #-i 为优化次数
        #print(numbs[n],numbs[n+1])
        if numbs[n]>numbs[n+1]:
            numbs[n],numbs[n+1]=numbs[n+1],numbs[n]
        n += 1

    print(numbs)
#可以优化的地方：
#每一次比较次数的优化 
#总共比较的趟数

'''调用函数直接排序'''
#sort 直接对原有列表排序
#升序
numbs = [6,5,3,1,8,7,2,4]
numbs.sort()
print(numbs)
#降序
numbs = [6,5,3,1,8,7,2,4]
numbs.sort(reverse=True)
print(numbs)

#sorted(nums) 内置函数sorted
#不会改变原有数列数据，会生成一个新的有序数列
numbs = [6,5,3,1,8,7,2,4]
a = sorted(numbs)
print(numbs)
print(a)

'''反转'''
numbs = [6,5,3,1,8,7,2,4]
numbs.reverse()
print(numbs)  #或者使用切片 print(numbs[::-1])

'''复制'''
a = 12
b = a
a = 10
print(b) #12 b不随着a改变而改变

num1 = [100,200,300]
num2 = num1
num1[0] = 1
print(num2) # [1, 200, 300] num2随着num1改变而改变

'''
python里的数据都是保存在内存里的
python里的数据分为可变类型和不可变类型

不可变类型：字符串、数字、元组
可变类型：列表、字典、集合

不可变数据类型，如果修改值，内存地址会发生改变
可变数据类型，如果修改值，内存地址不会发生改变

使用内置函数id可以获得一个变量的内存地址
'''

'''列表的潜复制'''
x = [100,200,300]
y = x #x y 指向同一个内存空间，会相互影响

#调用copy方法，可以复制一个列表
#这个列表和原有发列表内容一样，但是指向不同的内存空间
z = x.copy()
print('%X,%X,%X'%(id(x),id(y),id(x))) 
# 26BE9DF4AC0,26BE9DF4AC0,26BE9DF4AC0

#除了使用列表自带的copy方法以外，还可以使用copy模块实现浅拷贝
import copy
x = [100,200,300]
b = copy.copy(x)
print(b)

#切片就是一个浅拷贝
x = [100,200,300]
y = x[::]
x[1] = 2
print('%X,%X,%X'%(id(x),id(y),id(x))) 
# 26BE9DFC400,26BE9DFC340,26BE9DFC400

'''深复制与浅复制'''

nums = [1, 2, 3, 4]
nums1 = nums 
#这不是拷贝，是赋值，是一个指向
nums2 =nums.copy()
#浅拷贝，两个内容一样，但是不是同一个对象

#深拷贝。只能使用copy模块实现
#在浅拷贝中，如果列表内还要列表，内部的列表
#被不会拷贝，两个内部的列表指向同一块内存
import copy
words = ['hello','good',[100,200,300],'yes']
words1 = words.copy()
words2 = copy.deepcopy(words)
words[2][0] = 1
print(words1) #改变
print(words2) #不改变

'''求列表里的最大数和下标'''
#方法一
numbs = [6,5,3,1,8,7,2,4]
a = sorted(numbs)
print(a)
print(a[-1]) # 获得最大值 降序也可以
print(numbs.index(a[-1])) #获得下标


#方法二
num = [1,5,2,6,23,7,4,9,4]
x = num[0] # 假设第0个数是最大数
n = 0
i = 0
while n<len(num):
    n += 1
    if x < num[n-1]:
        x = num[n-1]
        i = n-1

print(x,i)


num = [1,5,2,6,23,7,4,9,4]
x = num[0]
for n in num:
    if n > x:
        x = n

print(x,num.index(x))

'''删除列表里的空字符串'''

x = ['hello','','good','fine','','yes','']
for word in x: 
    if word == '':
        x.remove(word)
print(x) # 此方法有bug 最好不要用
#在使用for……in循环遍历列表时，最好不要对元素进行增加删除操作

x = ['hello','','good','fine','','','yes','']
i = 0
while i < len(x):
    if x[i] == '':
        x.remove(x[i])
        i -= 1 # 将光标移回去
    i += 1
print(x)

#最佳
x = ['hello','','good','fine','','','yes','']
x2 =[]
for word in x:
    if word !='':
        x2.append(word)

x = x2
print(x)

'''列表的嵌套'''
num = [12,3,[100,23,34],45,33]

#一个学校有3个办公室，有10为老师等待工作分配，用编程完成随机分配
import random
teachers = ['a','b','c','d','e','f','g','h','i','j']
rooms = [[],[],[]]
for teacher in teachers:
    room = random.choice(rooms) #从列表中随机选择一个数据
    room.append(teacher)
print(rooms)
#带下表一般使用while循环
#for循环也可以带下标
for i,room in enumerate(rooms):
    print('房间%d里一共有%d个老师,分别是'%(i,len(room)),end='')
    for teacher in room:
        print(teacher,sep='',end='')
    print()

'''列表推导式'''
#列表推导式是使用简单的语法创建一个列表
num = [i for i in range(20)]
print(num)
#类似于
num = []
for i in range(20):
    num.append(i)

x = [i for i in range(10) if i % 2 == 0] 
print(x) #打印偶数，如果是i%2则打印奇数

#双循环 (x,y)是元组
points = [(x, y) for x in range(5,9)for y in range(2,6)]
print(points)

m = [i for i in range(1,101)]
print(m)
n = [m[j:j+3]for j in range(0,100,3)]
print(n)