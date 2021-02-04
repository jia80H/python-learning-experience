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

""" 特殊字符 """
