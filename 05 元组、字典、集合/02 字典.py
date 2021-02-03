# 列表只能存储值，但是无法对值进行描述
# 字典不仅可以表示值，还可以对值进行描述
# 使用大括号来表示一个字典，值value，描述key
# 字典里的数据都是以键值对key:value的形式保留
person = {
    'name': 'zhangsna',
    'age': '18',
    'score': '98',
    'weight': '150',
    'hobbies': ['唱', '跳', 'rap']
}

'''字典使用的注意事项'''
# 1 字典里的key不允许重复。
# 如果重复，后一个key会覆盖前一个
# 2 字典里的value可以是任意数据类型，但是key只能是不可变数据类型，一般用字符串
# 不可变数据类型有字符串 元组 数字

""" 查找数据 """
# 字典里的数据在保存时是无序的，不能用下标来获取
person = {
    'name': 'zhangsna',
    'age': '18',
    'score': '98',
    'weight': '150',
    'hobbies': ['唱', '跳', 'rap']
}
print(person['name'])
# 只能根据key找value
# 如果要查找的key不存在，会报错
# print(person['height'])
# 使用字典的get方法，如果key不存在，会默认返回None，而不报错
print(person.get('height'))
# 更改默认值
print(person.get('height', '185'))

""" 修改和增加数据 """

# 直接使用key可以修改对应的value
person['name'] = 'lisi'

# 如果key存在就修改，如果不存在就添加
person['gender'] = 'female'
print(person)

""" 删除数据 """
# 把name对应的键值对删除
x = person.pop('name')
print(x)  # 只返回value
print(person)

result = person.popitem()
print(result)  # ('gender', 'female')
# {'age': '18', 'score': '98', 'weight': '150', 'hobbies': ['唱', '跳', 'rap']}
print(person)

# 也能这样删除
del person['weight']
print(person)

# 清空
person.clear()

""" update方法的使用 """

# 列表可以使用extend方法将两个列表合并为一个列表
# 字典中可以使用update方法合并
person1 = {'name': 'zhangsan', 'age': '18'}
person2 = {'addr': 'henan', 'height': '180'}
person1.update(person2)
print(person1)

""" 字典的遍历 """
# 列表和元组是一个单一的数据，但是字典是键值对

# 第一种遍历方法：直接for……in循环字典
person = {'name': 'zhangsan', 'age': '18'}
for x in person:
    print(x)  # 获取的是key
    print(x, '=', person[x])  # 获取key和value

# 第二种遍历方法：
# 获取到所以的key，然后再遍历key，根据key获取value
person = {'name': 'zhangsan', 'age': '18'}
print(person.keys())  # dict_keys(['name', 'age'])
for k in person.keys():
    print(x, '=', person[x])  # 获取key和value

# 第三种方式：
# 获取到所以的value
# 只能拿到值，不能拿到value
person = {'name': 'zhangsan', 'age': '18'}
for v in person.values():
    print(v)

# 第四种遍历方式
person = {'name': 'zhangsan', 'age': '18'}
print(person.items())
#dict_items([('name', 'zhangsan'), ('age', '18')])
for item in person.items():
    print(item)
    # ('name', 'zhangsan')
    # ('age', '18')
    print(item[0], '=', item[1])

# 拆包
for k, v in person.items():
    print(k, '=', v)

""" 练习1 """
chars = ['w', 'b', 'c', 'a', 's', 'a', 'w', 'd', 'w', 'a', 'x', 'v', 'x']
# 拿出各自次数
char_count = {}

for char in chars:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# 更优
chars = ['w', 'b', 'c', 'a', 's', 'a', 'w', 'd', 'w', 'a', 'x', 'v', 'x']
char_count = {}
for char in chars:
    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)

# 找到最多的
vs = char_count.values()
# 可以使用内置函数max取最大数
max_count = max(vs)

for k, v in char_count.items():
    if v == max_count:
        print(k)

""" 练习2 """
persons = [
    {'name': 'zhhangsan', 'age': 18},
    {'name': 'lisi', 'age': 20},
    {'name': 'wangwu', 'age': 19},
    {'name': 'jerry', 'age': 21},
]
# 让用户输入姓名，如果姓名存在，提醒用户；
# 如果姓名不存在，继续输入年龄，存入列表
x = input('输入名字')
if x in person:  # 错误
    # in运算符，如果用在字典上，是用来判断key是否存在
    print('姓名存在')

# 正确
persons = [
    {'name': 'zhhangsan', 'age': 18},
    {'name': 'lisi', 'age': 20},
    {'name': 'wangwu', 'age': 19},
    {'name': 'jerry', 'age': 21},
]
x = input('输入名字')
for person in persons:
    if person['name'] == x:
        print('用户存在')
        break
else:
    print('用户不存在')
    newbie = {'name': 'x'}
    y = int(input('输入年龄'))
    newbie['age'] = y
    persons.append(newbie)
    print('用户已添加成功')
print(persons)

""" 练习3 """
dict1 = {'a': 100, 'b': 200, 'c': 300}
# 将key和value换位

# 方法1
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k
print(dict2)

# 方法2
# 字典推导式
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict1 = {v: k for k, v in dict1.items()}
print(dict1)

""" 练习4 """
students = [
    {'name': '张三', 'age': 18, 'score': 98, 'tel': '17335463210', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 95, 'tel': '12734632108', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 98,
        'tel': '16835463210', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 58,
        'tel': '17835486108', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52,
        'tel': '1883546808', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 89,
        'tel': '17835463210', 'gender': 'unknown'}
]
# (1) 统计不及格学生个数
count = 0
for student in students:
    if student['score'] < 60:
        count += 1
print('不及格人数为%d' % count)
# (2) 打印不及格学生名字和对应成绩
for student in students:
    if student['score'] < 60:
        print('%s不及格，分数是%d' % (student['name'], student['score']))
# (3) 统计未成年学生个数
teen = 0
for student in students:
    if student['age'] < 18:
        teen += 1
print('未成年学生有%d人' % teen)
# (4) 打印手机尾号是8的学生的名字
for student in students:
    if student['tel'].endswith('8'):  # 或者这样  if student['tel'][-1] == '8':
        print('%s的手机尾号是8' % student['name'])
# (5) 打印最高分和对应学生的名字
max_score = 0
for student in students:
    if student['score'] > max_score:
        max_score = student['score']
for student in students:
    if student['score'] == max_score:
        print('%s分数最高，最高分为%d' % (student['name'], max_score))
# (6) 删除性别不明的所有学生

# 方法1 将保留的数据添加到空表中
new_students = [
    student for student in students if student['gender'] != 'unknown']
print(new_students)
# 方法2 使用for循环倒着删除数据
i = 0
for i in range(len(students)-1, -1, -1):
    if students[i]['gender'] == 'unknown':
        students.remove(students[i])
print(students)
# 方法3 使用while循环删除数据，并及时补齐因删除数据而导致列表索引的变化
i = 0
while i < len(students):
    if students[i]['gender'] == 'unknown':
        students.remove(students[i])
        i -= 1
    i += 1
print(students)
# 方法4 遍历在新的列表中操作，删除在原来列表中操作
i = 0
for student in students[:]:
    if student['gender'] == 'unknown':
        students.remove(student)
print(students)
# 方法5 使用内置函数filter()和匿名函数
new_students = filter(lambda x: x['gender'] != 'unknow', students)

# (7) 将列表中学生成绩按降序排列
for j in range(0, len(students)-1):
    for i in range(0, len(students)-1):
        if students[i]['score'] < students[i + 1]['score']:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)

""" 练习4 """
# 选课的情况如下
sing = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
dance = ('g', 'f', 's', 'd', 'a', 'r', 'c')
rap = ('g', 'e', 'y', 'i', 't', 'h', 'r', 'a')
# (1) 求选课的总人数
allPerson = sing + dance + rap
print(len(set(allPerson)))  # set 可以去除重复
# (2) 求只选第一门课的人数和姓名
sing_only = []
for p in sing:
    if p not in dance and p not in rap:
        sing_only.append(p)
print(sing_only)

p_dict = {}
allPerson = sing + dance + rap
for name in allPerson:
    if name not in p_dict:
        p_dict[name] = allPerson.count(name)
print(p_dict)
# (3) 求只选一门的学生姓名和数目
print('报了1门的有', end='')
for k, v in p_dict.items():
    if v == 1:
        print(k, end=' ')
print()
# (4) 求选两门的学生姓名和数目
print('报了2门的有', end='')
for k, v in p_dict.items():
    if v == 2:
        print(k, end=' ')
print()
# (5) 求选了三门的学生姓名和数目
print('报了3门的有', end='')
for k, v in p_dict.items():
    if v == 3:
        print(k, end=' ')
print()
