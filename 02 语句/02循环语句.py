'''循环语句基本使用'''
print('hello world')

#py中循环有while和for循环
#py不支持do...while循环

'''while'''#可以无限循环
#while 判断条件：
#   条件成立时执行的代码

x = 0
while x<10:
    print(x)
    x=x+1
    #x++ py中不支持自增自减运算符

'''for...in'''
#for ele in itrable
#in 的后边必须是一个可迭代对象（字符串、列表、字典。元组、集合。range）
for i in range(0,10):
    print(i)

for j in 'hello':
    print(j)


'''break和continue'''

#break用于结束整个循环
#continue用于结束本轮循环，并开启下一轮循环

i = 0
while i < 5 :
    if i == 3:
        i += 1
        continue #回到while
    print(i)
    i += 1

i = 0
while i < 5 :
    if i == 3:
        i += 1
        break #结束循环
    print(i)
    i += 1

'''应用'''
#直到你爱我
answer = input('你喜欢我吗？')
while answer != '爱' :
    answer = input('你喜欢我吗？')
print('我也爱你')

#不太好的用户名与密码询问代码
userName = input('输入用户名')
password = input('输入密码')
while not(userName == 'zhangsan' and password == '1234'):
    userName = input('输入用户名')
    password = input('输入密码')
print('nihao zhangsan')
#简洁版
while True :
    userName = input('输入用户名')
    password = input('输入密码')
    if userName == 'zhangsan' and password == '1234':
        break
print('nihao zhangsan')

'''嵌套循环'''

#while 条件1：
#   外循环代码块
#   while 条件2：
#       内循环代码块

#内循环一旦开始，则要执行到条件2不满足，才会继续执行外循环
#外循环可以控制内循环执行次数

n = 0
while n<5 :
    n = n + 1
    print('*'*n)

#*
#**
#***
#****
#*****

j = 0
while j<5 :
     j += 1
     n = 0
     while n<5 :
         n = n + 1
         print('*'*n)
#重复打印5组

'''打印九九乘法表'''

 #三角形结构框架
j = 0
while j < 9:
    j += 1
    i = 0
    while i < j:
        i += 1
        print('*', end=" ")
    print() #换行
    
#乘法表
j = 0
while j < 9:
    j += 1
    i = 0
    while i < j:
        i += 1
        print(i,'*',j,'=',i*j,sep="", end="\t")
    print()

'''
1*1=1
1*2=2   2*2=4
1*3=3   2*3=6   3*3=9
1*4=4   2*4=8   3*4=12  4*4=16
1*5=5   2*5=10  3*5=15  4*5=20  5*5=25
1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81
'''

'''for....else'''
#打印（100，201）内的质数

for i in range(101,201):

    for j in range (2,int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        print(i,'是质数')

# for 循环也有一个大多数人都不熟悉 else 子句，
# 该 else 子句在循环正常完成时执行，
# 这意味着循环没有遇到任何 break 语句。
# 如果有break，就会结束执行else



