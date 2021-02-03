""" 内置属性介绍 """


class Student(object):
    """ 学生 """

    # __slots__ = ('name','age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


p = Student('张三', 18)

print(dir(p))  # dir 列出对象所有属性和方法
""" 
['__class__', '__delattr__', '__dict__', 
'__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', 
'__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 
'age', 'eat', 'name'] 
"""

print(p.__class__)
# <class '__main__.Student'> 告诉是什么类

print(p.__dict__)  # 把对象的属性和值转换成字典
print(p.__dir__())  # 等价于dir(p)
print(p.__doc__)  # 查看对类的说明 写类名也可 即 Student.__doc__
print(p.__module__)  # __main__
# print(p.__slots__)  # 需要自己定义

""" 把对象当作字典使用 """


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        # print('setitem方法被调用了, key={}, value={}'.format(key,value))
        # self.key = value # 打印p.name时仍为张三 p多了一个属性key
        # self[] = value 会无限递归
        p.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person('张三', 18)
print(p.__dict__)  # 将对象转成字典

# 不能直接把一个对象当字典来使用
# [] 语法会调用对象的__setitem__方法,改写即可
p['name'] = 'jack'
print(p.name)

# 不能直接使用,
# 下面的会调用__getitem__
print(p['name'])  # 修改__getitem__方法 就可以使用


""" 类属性和对象属性 """


class Person(object):
    type = '人类'  # 类属性: 这个属性定义在类里, 函数之外

    def __init__(self, name, age):
        # name和age时对象属性, 在__init__方法里以参数的形式定义
        self.name = name
        self.age = age
    # Person 我们称之为*类对象*


# 对象p是通过Person类创建出来的*实例对象*
# 只要创建了一个实例对象,这个实例对象就有自己的name和age属性
# 对象属性(name 和 age): 每个实例对象都单独保存的属性
# 每个实例对象之间的属性没有关联, 互不影响
p1 = Person('张三', 18)
p2 = Person('李四', 19)

# 类属性可以通过类对象和实例对象来获取
print(Person.type)  # 通过类对象获取类属性
print(p1.type)  # 通过实例对象来获取类属性
# p1 和p2 实例对象没有保存类属性

# 类属性只能通过类对象来修改
p1.type = 'human'  # 没有修改类属性,而是在p1里添加了一个对象属性
print(p1.type)  # human
print(p2.type)  # 人类

# 类属性的修改
Person.type = '人類'
print(p1.type)
print(p2.type)

""" 私有属性的使用 """


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.__money = 1000  # 以两个下划线开始的变量是私有变量

    def test(self):
        self.__money += 10  # 在这里可以访问私有变量

    def get_money(self):
        # 可以用来记录
        # print('某时间查询了余额')
        return self.__money

    def set_money(self, qian):
        print('修改余额了')
        self.__money = qian

    def __demo(self):
        # 以两个下划线开始的函数,是私有函数,在外部无法调用
        print('我是demo函数')
        # 硬要调用
        # p._Person__demo()


p = Person('张三', 18)
print(p.name, p.age)  # 可以直接获取到
# print(p.__money) # 不能直接获取到私有变量

p.test()  # 内部函数可以访问私有变量

# 获取私有变量的方法:
# 1. 使用 对象._类名__私有变量名 获取
print(p._Person__money)
# 2. 定义get和set方法
print(p.get_money())
# 3. 使用property来获取
p.set_money(100)
print(p.get_money())
