# 更优
chars = ['a','b','c','w','s','a','w','d','w','a','x','v','x']
char_count = {}
for char in chars:
    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)

# 找到最多的
vs = char_count.values()
# 可以使用内置函数max取最大数
max_count = max(vs)

for k,v in char_count.items():
    if v == max_count:
        print(k)