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
    while n < len(numbs) - 1 - i: #-i 为优化次数
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
