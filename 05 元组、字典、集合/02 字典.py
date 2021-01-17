#列表只能存储值，但是无法对值进行描述
#字典不仅可以表示值，还可以对值进行描述
#使用大括号来表示一个字典，值value，描述key
#字典里的数据都是以键值对key:value的形式保留
person = {
    'name':'zhangsna',
    'age':'18',
    'score':'98',
    'weight':'150',
    'hobbies':['唱','跳','rap']
    }

'''字典使用的注意事项'''
# 1、字典里的key不允许重复。
    # 如果重复，后一个key会覆盖前一个
# 2、字典里的value可以是任意数据类型，但是key只能是不可变数据类型，一般用字符串
    #不可变数据类型有字符串、元组、数字

""" 查找数据 """
#字典里的数据在保存时是无序的，不能用下标来获取
person = {
    'name':'zhangsna',
    'age':'18',
    'score':'98',
    'weight':'150',
    'hobbies':['唱','跳','rap']
    }
print(person['name'])
#只能根据key找value
#如果要查找的key不存在，会报错
#print(person['height'])
#使用字典的get方法，如果key不存在，会默认返回None，而不报错
print(person.get('height'))
#更改默认值
print(person.get('height','185'))

""" 修改和增加数据 """

# 直接使用key可以修改对应的value
person['name'] = 'lisi'

# 如果key存在就修改，如果不存在就添加
person['gender'] = 'female'
print(person)

""" 删除数据 """
# 把name对应的键值对删除
x = person.pop('name')
print(x) #只返回value
print(person)

result = person.popitem()
print(result) # ('gender', 'female')
print(person) # {'age': '18', 'score': '98', 'weight': '150', 'hobbies': ['唱', '跳', 'rap']}

# 也能这样删除
del person['weight']
print(person)

#清空
person.clear()

""" update方法的使用 """

#列表可以使用extend方法将两个列表合并为一个列表
#字典中可以使用update方法合并
person1 = {'name':'zhangsan','age':'18'}
person2 = {'addr':'henan','height':'180'}
person1.update(person2)
print(person1)

""" 字典的遍历 """
# 列表和元组是一个单一的数据，但是字典是键值对

#第一种遍历方法：直接for……in循环字典
person = {'name':'zhangsan','age':'18'}
for x in person:
    print(x) #获取的是key
    print(x,'=',person[x]) # 获取key和value

# 第二种遍历方法：
# 获取到所以的key，然后再遍历key，根据key获取value
person = {'name':'zhangsan','age':'18'}
print(person.keys()) #dict_keys(['name', 'age'])
for k in person.keys():
    print(x,'=',person[x]) # 获取key和value

#第三种方式：
# 获取到所以的value
# 只能拿到值，不能拿到value
person = {'name':'zhangsan','age':'18'}
for v in person.values():
    print(v)

# 第四种遍历方式
person = {'name':'zhangsan','age':'18'}
print(person.items()) 
#dict_items([('name', 'zhangsan'), ('age', '18')])
for item in person.items():
    print(item)
    # ('name', 'zhangsan')
    # ('age', '18')
    print(item[0],'=',item[1])

# 拆包
for k,v in person.items():
    print(k,'=',v)

""" 练习 """
chars = ['w','b','c','a','s','a','w','d','w','a','x','v','x']
# 拿出各自次数
char_count = {}

for char in chars:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# 更优
chars = ['a','b','c','a','s','a','w','d','w','a','x','v','x']
char_count = {}
for char in chars:
    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)

# 找到最多的
vs = char_count.value()
# 可以使用内置函数max取最大数
max_count = max(vs)

for k,v in char_count.items():
    if v == max_count:
        print(k)
