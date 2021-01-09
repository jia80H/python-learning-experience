import os
#内置函数转换类型
age = input('年龄：')
new_age = int(age)
print(type(new_age))
print(new_age+1)
'''
年龄：12
<class 'int'>
13
'''
#字符串转整数
a = '123cd'
b = int(a,16)
print(int(a,16)) #识别含字母的数字 int() base must be >= 2 and <= 36, or 0
print(bin(b))
#字符串转浮点
c = '12.31'
C = float(c)

#浮点转字符串
r = 13.232
r = str(r)
print(r)

#转布尔函数   
# 数字只有0转布尔函数为False 
print(bool(100)) #True
print(bool(0))  #False
# 字符串只有空(''/"")才能转False
print(bool(''))  #False
#其他False
print(bool(None))  #False 空数据
print(())  #False 空元组
print({})  #False 空字典

s = set()
print(bool(s))  #False  空集合

#隐式转换
if 3: #if后面自动转换为bool
    print('good')
#good
if 0:
    print('false')
# 什么也没有
os.system('pause')