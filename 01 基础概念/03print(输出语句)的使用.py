import os
#print输出语句
print('hello world!')

''' print的使用
def print(
         *values: object, 
         sep: Optional[Text] = ..., #默认空格为分隔符
         end: Optional[Text] = ...,
             #输出完print语句后，默认输出的字符为'/n'（换行）
         file: Optional[_Writer] = ...,
             #改变存的位置
         flush: bool = ...
    )
 -> None: ...
'''

print('hello','good','yes')

'''
>>> print('hello','good','yes')
hello good yes
>>>
'''


print('hello','good','yes','hi',sep = '+')

'''
>>> print('hello','good','yes','hi',sep = '+')
hello+good+yes+hi
>>>
'''
print('hello','good','yes')
print('hello','good','yes')
'''
hello good yes
hello good yes
'''
print('hello','good','yes','hi',sep = '+',end = "\t")
print('hello','good','yes','hi',sep = '+',end = "&&*&*%^&$%^")

'''
hello+good+yes+hi       hello+good+yes+hi&&*&*%^&$%^
'''
os.system('pause')