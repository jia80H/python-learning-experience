""" 正则匹配规则 """
# 1. 数字和字母都表示它本身
# 2. 很多字母前面添加\ 会有特殊含义(重点)
# 3. 绝大数标点符号都有特殊含义(重点)
# 4. 如果想要查找标点符号, 需要前加\
import re

# 数字和字母表示它本身
re.search(r'x', 'hex light')
re.search(r'6', 'hex6light')

print(re.search(r'd', 'good'))  # 字母d是普通字符
print(re.search(r'\d', 'good'))  # \d 有特殊含义不在表示字母d
print(re.search(r'\d', 'gdsv4o5od'))  # \d 表示数字

# re.search('+', '1+2')  # 不能直接使用, + 有特殊含义
re.search(r'\+', '1+2')

""" 正则匹配模式 """

# \s 表示任意空白字符
print(re.search(r'\s', 'hello world'))  # 空格
print(re.search(r'\n', 'hello\nworld'))  # 换行
print(re.search(r'\t', 'hello\tworld'))  # tab

# \S 表示非空白字符
print(re.search(r'\S', ' \t\n  x'))

""" 标点符号的特殊含义 """

# () 用来表示分组
# . 表示匹配除了换行以外的任意字符

# [] 用来表示可选项范围(一次) [x-y]从x到y区间,保护x,y
m = re.search(r'f[1-6]m', 'sff3mse')
print(m)  # <re.Match object; span=(2, 5), match='f3m'>
m = re.search(r'f[u-w]m', 'sffvmse')
print(m)  # 字母也可
# [0-5a-dx]  0到5 或者 a到d 或者 x

# | 用来表示 或者
# | 可以出现多个值 [] 只能单个值
re.search(r'f(x|p)m', 'axfpms')

# {n} 用来限定{n}前面元素出现n次数
# {n,} 表示前面元素出现n次及以上
# {,n} 表示出现n次及以下
# {m,n} m到n次
print(re.search(r'go{2}d', 'good'))

# * 表示前面元素出现任意次数(0次及以上) 等价于 {0,}

# + 前面元素出现一次及以上 {1,}

# ? 两种用法
# 1. 规定前面元素最多出现一次 {,1}
# 2. 将贪婪模式转换我非贪婪模式
print(re.search(r'go?d', 'gd'))

# ^ 以指定内容开头
# $ 以指定内容结尾
print(re.search(r'^a.*i$', 'asdfghi'))
print(re.search(r'^a.*i$', 'daxcv\nasdfghi\n', re.M))

# ^ 在[]里面 还表示取反
""" <字母>的特殊含义 """
# \n 换行    \t tab    \s 空白字符    \S 非空白字符
# \d 表示数字 及[0-9]
# \D 表示非数字 及[^0-9]
# \w 数字 字母 下划线 汉字等(非标点)
# \W \w取反 (标点)

""" 练习 """
# 匹配数字
num = input('数字')
if re.fullmatch(r'\d+(\.?\d+)?', num):
    print('是数字')
else:
    print('不是数字')

""" 贪婪与非贪婪模式 """

# 在python的正则表达式里, 默认是贪婪模式
# 即尽可能多的匹配
m = re.search(r'm.*a', 'sdmrsdfsadssa')
print(m)  # <re.Match object; span=(2, 13), match='mrsdfsadssa'>

# 在贪婪模式后边加? 可以转换位非贪婪模式
# 即尽可能少的匹配
n = re.search(r'm.*?a', 'sdmrsdfsadssa')
print(n)  # <re.Match object; span=(2, 9), match='mrsdfsa'>
