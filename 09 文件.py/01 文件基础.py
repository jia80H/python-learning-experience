""" 文件打开方式 """

# open参数介绍
# file: 用来指定打开的文件(不是文件名,而是文件的路径)
# mode: 打开文件的模式, 默认是r 表示只读
# encoding: 打开文件时的编码方式

# open函数会有一个返回值, 即打开的文件对象

# 00练习.py 写入时, 使用的是utf8 编码格式
# 在windows操作系统中,默认使用gbk编码格式打开文件
# 解决方案: 写入和读取时使用相同的编码格式
file = open('00练习.py',encoding='utf8')
print(file.read())

file.close()  # 操作完成以后要关闭文件

""" 路径 """

# 绝对路径: 
# 从电脑盘符开始的路径
import os
print(os.sep) 
# windows系统里,文件之间使用\分隔
# 在python字符串里, \ 表示转义字符

# 路径书写的三种方式
# 方法1 两个\\
# file = open('E:\\git仓库\\python-learning-experience\\00练习.py',encoding='utf8')
# 方法2 前面加上r
# file = open(r'E:\git仓库\python-learning-experience\00练习.py',encoding='utf8')
# 方法3 换成/ (推荐)
file = open(r'E:/git仓库/python-learning-experience/00练习.py',encoding='utf8')
print(file.read())
file.close()

####################

# 相对路径: 
# 当前文件夹开始的路径
# ../ 表示回到上一级
# ./  表示在当前文件夹,可以省略不写
# /   不能随便用
file = open('00练习.py',encoding='utf8')
print(file.read())
file.close()

""" 文件的打开方式 """
# mode 指的是文件的打开方式

# r: 只读模式
# 打开文件以后,只能读取,不能写入. 
# 如果文件不存在会报错
file = open('00练习.py','r',encoding='utf8')
print(file.read())
# file.write('hello') # 不能执行,会报错
# file = open('练习.py') # 文件不存在,会报错
file.close()

# w: 写入模式
# 打开文件以后,只能写入,不能读取
# 如果文件存在,会覆盖文件; 如果文件不存在,会创建
# file = open('00练习.py','w',encoding='utf8')
# print(file.read())  # 报错,不能执行读取
# file.write('hello')
# file.close()

# b: 以二进制形式打开文件(可以用来操作非文本)
# rb: 以二进制形式读取      wb: 以二进制形式写入
# file = open('00练习.py','wb')
# file.write('hhhhhh'.encode('utf8'))
# file.close

# a: 追加模式
# 会在文本最后追加内容


"""
w
一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a
打开一个文件用于追加。如果该文件已存在,文件指针将会放在文件的结尾。
也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
r+
打开一个文件用于读写。文件指针将会放在文件的开头。
W+
打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a+
打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
rb
以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
wb
以二进制格式打开一一个文件只用于写入。如果该文件已存在则将其覆盖。
如果该文件不存在，创建新文件。

ab
以二进制格式打开一-个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就
是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

rb+
以二进制格式打开一 个文件用于读写。 文件指针将会放在文件的开头。
wb+
以二进制格式打开一个文件用于读写。
如果该文件已存在则将其覆盖。如果该文件不存在，创建wb+新文件。
ab+
以二进制格式打开一一个文件用于读写。
如果该文件已存在，文件指针将会放在文件的结尾。
如果该文件不存在，创建新文件用于读写。
"""
# 可读可写用着麻烦基本不用
""" 文件的读取方法 """
# file1 = open('00练习.py',encoding='utf8')
# print(file1.read())  # 读取全部数据
# print(file1.read(n))  # 读取长度为n的数据 1024

# print(file1.readline()) # 读取单行数据
# print(file1.readlines()) # 读取所有行的数据,保存到一个列表里
# file1.close()