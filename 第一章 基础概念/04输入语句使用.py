# input 接收用户输入
# input() ==> 括号里写提示信息
# 输入的结果都被保存为字符串!!!

name = input('小哥哥，告诉妹妹你的名字好不好嘛:')
'''
>>> input("小哥哥，告诉妹妹你的名字好不好嘛:")
小哥哥，告诉妹妹你的名字好不好嘛:
'''
print(name,'哥哥你好呀')
'''
小哥哥，告诉妹妹你的名字好不好嘛:name
name 哥哥你好呀
'''
print(name*2) #输出为namename

#如何转换为其他类型
    #指定类型转换
'''
1.指定类型转换

 >>> y = int(input())
 10
 >>> type(y)
 <class 'int'>

y = int(input("名字"))
print(type(y))

名字123
<class 'int'>

2.自动转换

函数eval() 用来执行一个字符串表达式，并返回表达式的值

eval(expression, globals[ ], locals[ ])

global 和 locals 分别相当于全局和局部变量，eval函数会优先在局部变量存储空间中检索

  >>> y = eval(input())
  4.5
  >>> type(y)
 <class 'float'>
y = eval(input("随意"))
print(type(y))

3.切割转换

利用函数split()通过指定分隔符对字符串进行切片。

str.split(str="", num=string.count(str))

str为分割符，包括空格、\n，\t 等 ，num是分割次数。
'''
