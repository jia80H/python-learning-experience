
""" 运算符相关的魔法方法 """
class Person(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

p1 = Person('zhangsan',18)
p2 = Person('zhangsan',18)
# p1 p2 不是同一个对象
# 比较内存地址判断是否是同一个对象

# is 身份运算符 
# 可以判断两个对象是否是同一个对象
print(p1 is p2) # False

