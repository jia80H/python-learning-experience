#使用[]来表示一个列表，列表里的每一个数据称为元素
#元素之间使用都好进行分隔
#列表可以存储任意数据类型，但是一般情况下我们都存储单一数据类型

names = ['张三','李四','王五','joy','linda','sazi']

names = list(('张三','李四','王五','joy','linda','sazi'))
print(names)

# 列表和字符串一样，都可以用下标来获取元素和对象
#同时，我们可以使用下标来修改列表里的元素

names = list(('张三','李四','王五','joy','linda','sazi'))
print(names[3]) #joy
names[3] = '花木兰'
print(names) # ['张三', '李四', '王五', '花木兰', 'linda', 'sazi']
print(names[3:5])