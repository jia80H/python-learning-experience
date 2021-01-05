import os 
#暂停防止闪退
''' 
变量
    数字类：有有符号整数（int)，浮点数（fload)，复数（complex)
    布尔函数 True False   字符串 String   
    列表 List             元组 Tuple
    字典 Dictionary       集合 set
'''
a = 12 #int
print(a)
print(type(a))

'''
>>> a = 12 #int
>>> print(a)
12
>>> print(type(a))
<class 'int'>
'''

a = 1.32222 #fload
print(a)
print(type(a))

'''
>>> a = 1.32222 #fload
>>> print(a)
1.32222
>>> print(type(a))
<class 'float'>
>>>
'''

a = (-4)**0.5 #complex
print(a)
print(type(a))

'''>>> print(a)
(1.2246467991473532e-16+2j)
>>> print(type(a))
<class 'complex'>
'''

a = ('hello world!') #string
print(a)
print(type(a))

'''
>>> print(a)
hello world!
>>> print(type(a))
<class 'str'>
>>>
'''

a = True #bool
print(a)
print(type(a))

a = False #bool
print(a)
print(type(a))

print(3>4) #bool

'''
>>> a = True #bool
>>> print(a)
True
>>> print(type(a))
<class 'bool'>
>>>
>>> a = False #bool
>>> print(a)
False
>>> print(type(a))
<class 'bool'>
>>>
>>> print(3>4) #bool
False
'''

names = ['jjh','cyx','yyl','ztt'] #list
print(names)
print(type(names))

'''
>>> print(names)
['jjh', 'cyx', 'yyl', 'ztt']
>>> print(type(names))
<class 'list'>
'''

person = {'name':'jjh','afe':'18','gender':'men'} #字典
print(person)
print(type(person))

'''
>>> person = {'name':'jjh','afe':'18','gender':'men'} #字典
>>> print(person)
{'name': 'jjh', 'afe': '18', 'gender': 'men'}
>>> print(type(person))
<class 'dict'>
>>>
'''

nums = (1,2,3,4) #元组
print(nums)
print(type(nums))

'''
>>> print(nums)
(1, 2, 3, 4)
>>> print(type(nums))
<class 'tuple'>
>>>
'''

jihe = {1,2,1.2,'strdfvds','你好',True}
print(jihe)
print(type(jihe))

'''
>>> print(jihe)
{1, 2, 1.2, '你好', 'strdfvds'}
>>> print(type(jihe))
<class 'set'>
>>>
'''
os.system('pause') #暂停程序