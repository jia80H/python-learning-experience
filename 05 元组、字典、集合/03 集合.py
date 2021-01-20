""" set的基本使用 """
# set 是一个无序且无重复元素的序列，
# 可以用{}或set() 来表示
# 空集合是set(), 空字典是{}
# {}里放键值对是键值对是字典，是单个的值就是一个集合
# set会自动去除重复数据
names = {'a','b','c','d','e','f','a'}
print(names) # {'b', 'a', 'e', 'c', 'd', 'f'}

nums = [1,3,2,12,4,3,5,7,9,3,8,2]
x = set(nums) #去重
y = list(x) 
y.sort(reverse=True) #排序
print(y)

# 增加元素
names.add('阿珂')
names.update('g','h') # 括号内为可迭代对象
print(names)
c = {'ee','aa','cc'}
d = names.union(c)
print(d)
# update是拼接，union生成一个新集合

# 删除元素
# 随机删除
names.pop()
# 删除指定元素
names.remove('a') # 如果删除的不存在会报错

# 清空
names.clear()

""" set的高级使用 """
x = {'a','b','c','d','e','f','g'}
y = {'g','f','s','d','a','r','c'}

# 不支持加法
# 减法
print(x - y) #sing减去共有的

#求交集 &
print(x & y)

#求并集 |
print(x | y)

#求并集减去交集
print(x ^ y) 