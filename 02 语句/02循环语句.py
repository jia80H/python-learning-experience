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