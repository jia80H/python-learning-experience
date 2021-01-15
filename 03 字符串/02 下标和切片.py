'''下标'''
#下表我们又称之为索引，表示第几个数据
#m[index]==>获得指定下标下的数据

#可迭代对象：str list tuple dick set range
#str list tuple 可以通过下标来获取或者操作数据

#在计算机中，下标都是从o开始的
word = 'i love you'
print(word[2])

#字符串是不可变数据类型

'''切片'''
#切片就是从字符串中复制一段指定的内容，生成一个新的字符串
#m[start:end:step] step指步长，默认为1
m = 'i love you'
print(m[2:6])
print(m[:6])

print(m[2:6:2])
print(m[5:1:-1]) #倒着打印
print(m[::]) #从头到尾复制
print(m[::-1]) #倒序

print(m[-5:-1]) #倒数第五到倒数第一