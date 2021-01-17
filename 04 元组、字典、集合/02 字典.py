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
print(result)
print(person)