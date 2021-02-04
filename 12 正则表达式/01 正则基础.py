""" 正则表达式介绍 """
# 正则表达式用来处理字符串
# 对字符串进行检索和替换
# 1. 检索 2. 替换
import re

x = 'hello\\world'
# 在正则表达式里,如果像要匹配一个\ 需要\\\\

# 第一个参数就是正则表达式匹配规则
# 第二个参数表示要匹配的字符串
m = re.search('\\\\', x)  # match和search

# 还可以在字符串前面加r , \\ 就表示 \
m = re.search(r'\\', x)

# search和match方法执行结果是一个Match类型的对象
print(m)  # <re.Match object; span=(5, 6), match='\\'>

""" 正则查找 """
# 查找相关的方法
# match search finditer findall fullmatch

####################
# match 和 search
# 共同点:
# 1. 只对字符串查找一次     2. 返回值类型都是 re.Match类型的对象
# 不同点:
# match: 是从头开始匹配, 一旦匹配失败, 就会返回None;
# search: 是在整个字符串里匹配
a = 'hello good morning'
a1 = re.match(r'hello', a)
print(a1)  # <re.Match object; span=(0, 5), match='hello'>
a1 = re.match(r'good', a)
print(a1)  # None
a2 = re.search(r'good', a)
print(a2)  # <re.Match object; span=(6, 10), match='good'>
####################
# finditer
# 返回结果是一个可迭代对象
# 可迭代对象里的数据是匹配到的所有结果, 结果是re.Match类型的对象
a3 = re.finditer(r'x', 'bcdxdxxxscsxsdxfs')
for i in a3:
    print(i)
####################
# findall: 把查找到的所有字符串结果放到一个列表里
a4 = re.findall(r'x\d+', 'bcdxdxx832xscsxsdx12fs')
print(a4)  # ['x832', 'x12']

####################
# fullmatch
# 完整匹配, 字符串需要完全满足正则规则才会有结果, 否则就是None
a5 = re.fullmatch(r'hello world', 'hello world')
print(a5)

""" re.Match类的使用 """
m = re.search(r'm', 'afwmefwa')
# print(dir(a2))

# pos: 从什么地方开始匹配
# endpos: 到哪里结束匹配
print(m.pos, m.endpos)  # 0 8

# span: 匹配到的结果字符串的开始和结束的下标
# 传递参数n获取第n组的下标, 默认第0组
m = re.search(r'm.*a', 'afsefmffae')  # . 任意字符 * 出现任意次数
print(m.span())  # (5, 9)

# group 方法:获取匹配的字符串结果
# group可以传参, 表示第n个分组,默认拿第0组
print(m.group())  # mffa

# group方法表示正则表达式的分组
# 1. 在正则表达式里使用()表示一个分组
# 2. 如果没有分组, 默认只有一组
# 3. 分组的下标从0开始

m1 = re.search(r'(9.*)(0.*)(5.*7)', 'aw9ef0waef5sdvs7ecddse')
# 有四个分组
# 第0组是全部
print(m1.group(0))  # 9ef0waef5sdvs7
print(m1.group(1))  # 9ef
print(m1.group(2))  # 0waef
print(m1.group(3))  # 5sdvs7

# groups: 0以外的分组(元组形式)
print(m1.groups())  # ('9ef', '0waef', '5sdvs7')

# (?P<name>表达式)  可以给分组起一个名字
m2 = re.search(r'(9.*)(?P<第二组>0.*)(5.*7)', 'aw9ef0waef5sdvs7ecddse')
# groupdict方法 可以获取这种形式
print(m2.groupdict())  # {'第二组': '0waef'}
# 用group可以通过分组名或分组的下标获取到匹配 字符串
print(m2.group('第二组'))
print(m2.group(2))

""" re.compile方法的使用 """
# 在re模块里,可以使用re方法调用函数,
# 还可以调用re.compile得到一个对象

# 直接调用re.search方法
m = re.search(r'm.*a', 'afsefmffae')
print(m.span())  # (5, 9)

# 创建方法,多次使用
r = re.compile(r'm.*a')
x = r.search('afsefmffae')
y = r.search('afsefmffsaae')
print(x, y)

""" 正则修饰符 """
# 正则修饰符是对正则表达式进行修缮

# . 表示除了换行以外的任意字符
# re.S: 让. 匹配换行
x = re.search(r'm.*a', 'afsefmf\nfae')
y = re.search(r'm.*a', 'afsefmf\nfae', re.S)
print(x)  # >None
print(y)  # <re.Match object; span=(5, 10), match='mf\nfa'>

# re.I: 忽略大小写
# re.M: 让$ 匹配到换行
z = re.findall(r'\w+$', 'i am boy\nyou are girl', re.M)
k = re.findall(r'\w+$', 'i am boy\nyou are girl')
# \w: 表示字母和_    +: 出现异常以上     $: 以指定的内容结尾
print(z)  # ['boy', 'girl']
print(k)  # ['girl']
