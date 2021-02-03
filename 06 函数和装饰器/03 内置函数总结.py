""" 数学相关的内置函数 """
# abs 是取绝对值的
print(abs(-1))  # 1
# divmod 求两个数的商和余数
# pow 求幂运算 和** 一样
# max 求最大数
# min 求最小数
# round 四舍五入保留到指定位
round(3.1415926, 3)  # 3.142
# sum 用来求和

""" 可迭代对象相关的方法 """
# all是将可迭代对象里的元素转为bool值，
# 一旦有一个bool值为False则为False
print(all([1, 2, 3, '0', 'hello']))  # True
print(all([1, 2, 3, 0, 'hello']))  # False

# any 是将可迭代对象里的元素转为bool值，
# 一旦有一个bool值为True则为True
print(any([1, 2, 3, 0, 'hello']))  # True
print(any([0, False, None, '']))  # False

# len 获取长度
# iter 获取到可迭代对象的迭代器
# next for……in循环本质就是调用迭代器的next方法
# sorted 用来排序

""" 转换相关 """
# bin 将数字转为二进制
bin(2796202)  # '0b1010101010101010101010'
# oct 将数字转为八进制
# hex 将数字转为十六进制

# chr 将字符编码转换为对应的字符
chr(97)  # 'a'
# ord 将字符转化为对应的编码
ord('a')  # 97
# eval 执行字符串里的python代码

""" 输入输出相关 """
# print
# input

""" 变量相关 """
# globals 查看所有全局变量
# locals 查看所有局部变量

""" 判断对象相关的方法 """
# isinstance 判断一个对象是否是由一个类创建出来的
# issubclass 判断一个类是否是另一个类的子类

""" help """
# help 用来查看帮助文档
help(print)
# Help on built-in function print in module builtins:

# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

""" id """
# 获取内存地址

""" dir """
# dir 列出对象所有属性和方法
dir([12, 3])
# ['__add__', '__class__', '__class_getitem__',
# '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__',
# '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__',
# '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'clear', 'copy',
# 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

""" exit """
# exit 以指定的退出码结束程序

""" open """
# open 用来打开一个文件
