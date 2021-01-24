""" 面向对象的基本语法 """
##############
# 类名
# class 类名：类名一般需要遵循大驼峰命名法，第一个单词首字母大写
# 1. class <类名>:
# 2. class <类名>(object):

class Student(object): # 关注这个类有哪些特征和行为
    # 在__init__方法里以参数的形式定义特征，我们称之为属性
    def __init__(self,name,age,height): 
        self.name = name
        self.age = age
        self.height = height

    # 行为定义为函数
    def run(self):
        print('正在跑步')
    
    def eat(self):
        print('正在吃饭')



# s使用Student 类创建两个实例对象 s1 s2
# s1 s2 都会有name，age，height属性，同时都有run和eat方法
s1 = Student('小明',18,1.75) # Student() ==> 会自动调用__init__方法
s2 = Student('小美',17,1.65)

# 根据业务逻辑，让不同对象执行不同的行为
s1.run
s1.eat

s2.eat

""" self语句的使用 """
class Student(object):
    def __init__(self,x,y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是',self.name)

# Student('张三'，18) 这段代码做了什么？
# 1.调用__new__方法，用来申请内存空间
# 2.调用__init__方法传入参数，将self指向创建好的内存空间，填充数据
# 3.变量s1 也指向创建好的内存空间
s1 = Student('张三', 18)
print('s1的名字是%s，年龄是%d'%(s1.name,s1.age))
s1.say_hello() # 大家好，我是 张三

# 申请一块新的内存空间
s2 = Student('jack',18)
s2.say_hello() # 大家好，我是 jack

# 没有属性，会报错
# print(s.height)

# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 如果这个属性以前存在，会修改这个属性对应的值
# 动态属性
s1.city = 'beijaing' # 给对象添加一个city属性
print(s1.city)

""" __slots__属性的使用 """

class Student(object):
    __slots__ = ('name','age') 
    # 这个属性直接定义在类里，是一个元组，
    # 用来规定队形可以存在的属性
    # 上边的动态属性city不写进了无法使用

    def __init__(self,x,y):
        self.name = x
        self.age = y

    def say_hello(self):
        print('大家好，我是',self.name)