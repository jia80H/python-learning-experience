# 字符串、列表、元组、字典和集合，它们有很多相同点
# 都是由多个元素组成的可迭代对象，它们都有一些可以共同使用的方法

""" 算法运算符 """
# +：可以用来拼接，用于 字符串、元组、列表
print('hl'+'m')
print(('google', 'yes')+('hi', 'm'))
print([1, 2, 3]+[45, 1])

# -: 只能用于集合 求差集
print({1, 2, 3}-{2, 3, 4})

# *: 用于字符串、列表、元组，表示重复多次。不能用于字典和集合
print('hello'*2)  # hellohello
print([1, 2]*2)   # [1, 2, 1, 2]
print((1, 2, 3)*2)  # (1, 2, 3, 1, 2, 3)

""" 成员运算符in和not in """
# in 可以用于字符串、列表、元组、集合、字典
print('a' in 'abc')
print(1 in [1, 2, 3])
print(4 in (4, 5, 6))
print(7 in {7, 8, 9})

# in 用于字典是用来判断key是否存在
person = {'name': 'zhangsan', 'age': '18'}
print('name' in person)

""" 遍历 """

# for……in……可以遍历字符串、列表、元组、字典、集合等可迭代对象
# 字符串遍历
chars = 'hello word'
for char in chars:
    print(char, end='    ')
# 列表的遍历
list1 = [1, 2, 3, 4, 5]
for num in list1:
    print(num, end=' ')

# 带下标的遍历
# enumerate一般用于列表、元组等有序数据
list1 = [1, 2, 3, 4, 5]
for e in enumerate(list1):
    print(e)
for i, e in enumerate(list1):  # 拆包
    print(i, e)
