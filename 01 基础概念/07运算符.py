'''*算数运算符*'''
import os


# 数字运算
# + - * /  **幂运算 //整除(向下取整) %取余

print(1+1)  # 2

# py2里，两整数相除，得到的是一个int 9/2=4
# py3里，两整数相除，得到的是一个float
print(6 / 2)  # 3.0

print(81**(1/2))  # 9.0

print(10//3)  # 3 取整

print(10 % 3)  # 1 取余

# 字符串运算

# + 字符串连接
# * 字符串重复
# [] 通过索引获取字符串中字符
# [:] 截取字符串中部分字符
# in 如果字符串中包含给定字符，返回True
# not in 如果字符串中不包含给定字符，返回True

print('hello'+'world')  # helloworld

print('hello' * 2)  # hellohello

s = 'python'
print('thon' in s)  # True
print('thon' not in s)  # False
print(s[0])  # 返回s中索引（序号，从零开始）为0的字符 p
print(s[1:4])  # 返回s中索引（序号，从零开始）从1～3的字符 yth

'''赋值运算符 = '''
# ‘=’将等号右边的值赋给左边
# 等号左边不能是常量或表达式 10=a 3+2=m

x = 1
x = x + 1  # 或者x += 1 （复合运算符）
print(x)

x **= 2

# 等号连接的变量可以传递赋值
a = b = c = d = 'hello'
print(a, b, c, d, sep='+')  # hello+hello+hello+hello

m, n = 3, 6
print(m, n)  # 3 6  拆包

a = (1, 2, 3)
print(a)  # (1, 2, 3)

# ‘*’表示可变长度
o, *p, q = 1, 2, 3, 4, 5, 6
print(o, p, q)  # 1 [2, 3, 4, 5] 6

*o, p, q = 1, 2, 3, 4, 5, 6
print(o, p, q)  # [1, 2, 3, 4] 5 6

m, n, b = (1, 2, 3), (3, 4, 5), 6
print(m, n, b)  # (1, 2, 3) (3, 4, 5) 6

'''比较运算符'''
# 大于> 小于< 大于等于>= 小于等于<= 不等于!= 等等于==
print(2 > 3)  # False
print('hello' == 'HELLO')  # False
print('hello' == 'hello')  # True

# 字符串比较依据ASCII比较
print('a' > 'b')  # False a = 97 b = 98

# 数字和字符串之间 == False， != True, 不支持其他运算符

'''逻辑运算符'''
# and与(并且) or或（或者） not非（取反）

print(2 > 1 and 5 > 3 and 10 > 2)  # True
print(2 > 1 and 5 > 3 and 1 > 2)  # False

print(3 > 9 or 4 < 7 or 10 < 3)  # True
print(3 > 9 or 4 < 2 or 10 < 3)  # False

print(not (5 > 2))  # False

# 逻辑短路

4 > 3 and print('hello world')
4 < 3 and print('你好世界')  # hello world


4 > 3 or print('hahahaha')
4 < 3 or print('heiheihei')  # heiheihei

# and 取第一个为False的值，如何都为真，取最后一个值
print(3 and 5 and 0 and 'hello')  # 0
print(3 and 5 and 1 and 'hello')  # hello

# or 取第一个为True的值；如果全为False，取最后一个值
print(0 or [] or 'list' or 5 or 'ok')  # list
print(o or [] or ())  # ()

'''位运算符'''
# 按位与& 按位或| 按位异或^ 按位左移<< 按位右移>> 按位取反~

# 按位与& 同为1则为1，否则为0
a = 23  # 0001 0111 23
b = 15  # 0000 1111 15
print(a & b)  # 0000 0111 7
# 按位或| 只要有一个为1则为1
print(a | b)  # 0001 1111 31
# 按位异或^ 相同为0，不同为1
print(a ^ b)  # 0001 1000 24
# 按位左移<<
x = 5  # 101 5
print(x << 2)  # 最低位补两个0 10100  20
# 按位右移>>
y = 15  # 1111 15
print(y >> 2)  # 去除最后两位 11 3
# 按位取反~ ~n = -( n + 1 )
m = 12        # 12
print(~m)  # -13
# 练习 获取的16进制颜色0xF0384E的RGB值，并以十进制打印和输出
numColor = 0xF0384E
exB = numColor >> 8
red = exB >> 8
red00 = red << 16
exR = red00 ^ numColor
green = exR >> 8
_0green0 = green << 8
blue = exR ^ _0green0
print(red, green, blue)
print(hex(red), hex(green), hex(blue))

# or简单方法
color = 0xF0384E
red = color >> 16
green = color >> 8 & 0xFF
blue = color & 0xFF
print(red, green, blue)
print(hex(red), hex(green), hex(blue))


'''
运算符的特特殊优先级
'''
# 逻辑运算中not>and>or 而不是从左到右看
print(True or False and True)  # True
print(False or not False)  # True
print(True or True and False)  # True

# 强烈建议用括号来说明优先级
print((True or True) and False)  # False
print(True or (True and False))  # True 用括号提醒自己或他人


os.system('pause')
