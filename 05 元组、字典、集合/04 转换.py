""" 内置类转换 """
#list tuple set
#字典转成其他三个只能转出key
nums = [1,2,3,4,5]
x = tuple(nums)
y = set(nums)
z = list(x)
print(nums)
print(x)
print(y)
print(z)

""" 内置函数eval """
# 函数eval() 用来执行一个字符串表达式，并返回表达式的值
#eval(expression, globals[ ], locals[ ])
a = 'input("输入姓名")'
print(eval(a))

""" json """
#Json本质是字符串
#Json的使用，把列表、元组、字典等转换为jason字符串
# 字典如果想把它传给前端页面或者把字典写到一个文件里 需要变成字符串

#用json转字符串
import json
person = {'name':'zhangsan','age':'18'}
m = json.dumps(person)
print(m)       # {"name": "zhangsan", "age": "18"}
print(type(m)) # <class 'str'>

#字符串转代码
n = '{"name": "zhangsan", "age": "18"}'
#json法(best)
s = json.loads(n)
print(s)
print(type(s)) #<class 'dict'>
#eval法
p = eval(n)
print(p)       #{'name': 'zhangsan', 'age': '18'}
print(type(p)) #<class 'dict'>

# py中数据转换成json的对应关系
# python            json
# 字符串             字符串
# 字典               对象
# 列表 元组          数组
# True False        true false
#json中数组转到python中转成列表