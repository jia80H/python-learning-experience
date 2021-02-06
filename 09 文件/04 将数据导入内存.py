# 将数据写入内存涉及到 StringIO 和 BytesIO 两个类
""" StringIO """
from io import BytesIO
from io import StringIO

s_io = StringIO()
s_io.write('hello')  # 将数据写入到内存里，缓存起来
s_io.write('good')
print(s_io.getvalue())  # hellogood

s = ''
s += 'word'
s += 'good'
print(s)

# print参数中file 需要的是一个文件流
# print('hello', file = open('sss.txt', 'w'))

print('good', file=s_o)
print('hello', file=s_o)
print('hi', file=s_o)
print(s_io.getvalue())

s_io.close()  # 记得关闭

""" BytesIO """

b_io = BytesIO()
# b_io.write('你好')  # 报错,只能写二进制
b_io.write('你好'.encode('utf8'))
print(b_io.getvalue().decode('utf8'))

b_io.close()  # 记得关闭
