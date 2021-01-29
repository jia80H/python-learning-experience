# 序列化: 将数据从内存持久化保存的过程
# 反序列化: 将数据从硬盘加载到内存的过程

# write时, 只能写入字符串或二进制
# 字典,列表,数字等都不能直接写入到文件里

# 将字典等写入文件的方法
# 1. 将数据转成字符串: repr/str/使用jison模块(最好)
#    jison 本质是字符串, 区别在于json里要用""表示字符串
# 2. 将数据转成二进制: 使用pickle模块
import json
file = open('00练习.py', 'w', encoding='utf8')
names = ['a', 'b', 'c', 'd']
name = 1234
# json: '["a", "b", "c", "d"]'

# file.write(names)  # 报错 write时, 只能写入字符串或二进制

x = json.dumps(names)  # dumps 的作用是将数据转换为字符串
print(x, type(x))
file.write(x)

# json里将数据持久化有两个方法:
# 1. dumps: 将数据转换为json字符串, 不会将数据保存到文件里
# 2. dump: 将数据转成json字符串的同时写入到指定文件

json.dump(name, file)
json.dump(names, file)

file.close()

# json里两个反序列化方法:
# 1. loads: 将json里的字符串加载成python里的数据
# 2. load: 读取文件, 将读取的内容加载成python里的数据
y = '{"name":"zhangsan", "age":18}'
p = json.loads(y)
print(p, type(p))

file1 = open('00练习.py', 'r', encoding='utf8')
m = json.load(file1) # 需要注释掉上边三个写入中两个或者文件中换行
print(y)
file1.close()

# python 和 json 字符串对应关系

# python   ==>    json
# dict            object
# list,tuple      array
# str             string
# int,float       number
# True            true
# False           false
# None            null
