'''{}占位符'''
x = '大家好，我的名字是{}，我今年{}岁了'.format('张三', 18)
print(x)

m = '大家好，我的名字是{1}，我今年{0}岁了'.format('18', '张三')
print(m)
# {n}内的数字n表示顺序（从0开始）

m = '大家好，我的名字是{name}，我今年{age}岁了'.format(age=18, name='张三')
print(m)
# {变量名}里边也可以是变量

# list
d = ['zhangsan', '18', 'henan']
m = '大家好，我的名字是{}，我今年{}岁，来自{}'.format(d[0], d[1], d[2])
print(m)

d = ['zhangsan', '18', 'henan']
m = '大家好，我的名字是{}，我今年{}岁，来自{}'.format(*d)  # *d拆包
print(m)

# dict
info = {'name': 'zhangsan', 'age': '18', 'addr': 'henan'}
m = '大家好，我的名字是{name}，我今年{age}岁，来自{addr}'.format(**info)
print(m)
