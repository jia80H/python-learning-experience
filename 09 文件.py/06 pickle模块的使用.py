# python 里存入数据只支持存入 字符串 和 二进制
# json: 将python里的数据转换成对应的json
# pickle: 将python里*任意*的对象转换成二进制
import pickle

# 序列化:
# 1. dumps: 将python数据转成二进制  
# 2. dump: 将python数据转成二进制,同时保存到指定文件

# 反序列化: 
# 1. loads: 将二进制加载成python数据
# 2. load读取文件,并将读取的内容加载成二进制

# dumps与loads
names = ['zhangsan', 'lisi', 'wangwu']
b_names = pickle.dumps(names)
print(b_names)

file = open('00练习.py', 'wb')
file.write(b_names)  # 写入的是二进制, 不是纯文本
file.close()

file = open('00练习.py', 'rb')
x = file.read()
y = pickle.loads(x)
print(y)
file.close()

# dump与load
names = ['zhangsan', 'lisi', 'wangwu']
file = open('00练习.py', 'wb')
pickle.dump(names, file)
file.close()

file = open('00练习.py', 'rb')
dd = pickle.load(file)
print(dd)
