# 列表是用来保存多个数据
# 操作列表，一般都包括增加数据、删除数据、修改数据以及查询数据
# 及增删改查

'''增加元素'''
#增加元素的方法 append insert extend

#append 在列表的最后边追加元素
heros = ['ake','yingzheng','hanxin','luna','houyi','yase','liyuanfang']
heros.append('huangzhong')
print(heros)

#insert(index,object)
# index表示下标，在哪个位置插入数据
# object表示对象，具体插入哪个数据
heros = ['ake','yingzheng','hanxin','luna','houyi','yase','liyuanfang']
heros.insert(3,'libai')
print(heros)

#extend(iterable) 
#a.extend(b) ==> 将可迭代对象b添加到a的后面
heros = ['ake','yingzheng','hanxin','luna','houyi','yase','liyuanfang']
x = ['makeboluo','milaidi','direnjie']
heros.extend(x)
print(heros,x,sep="\n")

'''删除元素'''
#删除数据的方法 pop remove clear

#pop 默认删除最后一个，并且返回这个数据
masters = ['wangzhaojun','daji','diaochan','daqiao','xiaoqiao']
x = masters.pop()
print(x)
print(masters)
#pop(n) 删除第n个
masters = ['wangzhaojun','daji','diaochan','daqiao','xiaoqiao']
x = masters.pop(3)
print(x)
print(masters)

#remove 用于删除指定元素
#如果删除的元素不存在会报错
masters = ['wangzhaojun','daji','diaochan','daqiao','xiaoqiao']
masters.remove('xiaoqiao')
print(masters)

#clear 清空列表
masters = ['wangzhaojun','daji','diaochan','daqiao','xiaoqiao']
print(masters.clear()) #None

#del
del masters [2]

a = 100
del a
print(a) #NameError: name 'a' is not defined

'''查询'''
masters = ['wangzhaojun','daji','diaochan','daqiao','xiaoqiao','daji']
#index 查询位置
# 元素不存在会报错
print(masters.index('daji')) # 1
#count 计数
masters.count('daji') #2
#in 运算符
print('daji' in masters) #True

'''修改元素'''
masters = ['wangzhaojun','daji','diaochan','daqiao','xiaoqiao','daji']
masters[2] = '妲己'
print(masters)

'''遍历'''
#便利：将所有数据都访问一边。遍历真的的是可迭代对象
#遍历方式 while循环、for...in 循环
masters = ['wangzhaojun','daji','diaochan','daqiao','xiaoqiao','daji']
for k in masters:
    print(k)

i = 0
while i < len(masters):
    print(masters[i])
    i += 1