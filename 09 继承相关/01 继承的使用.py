""" 面向对象的三大特征 """
# 面向对象编程有三大特性: 封装 继承 多态
# 封装:
# 函数是对语句的封装
# 类是对函数和变量的封装
# 继承:
# 类和类之间可以手动建立父子关系, 
# 父类的属性和方法, 子类可以使用
# 多态:
# 是一种技巧,提高代码的灵活度

""" 继承的基本使用 """
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(self.name+'正在吃')
    
    def sleep(self):
        print(self.name + '正在睡')

class Dog(Animal):  # 继承Animal 不用写重复的代码
    def bark(self):
        print(self.name + '正在叫')

# Dog() 调用__new__方法,再调用__init__方法

# Dog 里没有__new__,会查看父类是否重写__new__方法
# 父类里也没有重写__new__方法, 再查找父类的父类,找到 object

# 调用__init__ 方法,Dog类没有实现,会自动找Animal父类
d1 = Dog('大黄', 2)
print(d1.name) # 父类里定义的属性, 子类可以直接调用
d1.sleep() # 父类的方法子类可以直接调用
""" 继承的注意事项 """
class A(object):
    def demo_a(self):
        print('我是A类里的demo_a')
class B(object):
    def demo_b(self):
        print('我是B类里的demo_b')

# python里允许多继承
# 继承也可以传递
class C(A, B):  # 可以有多个父类  
    pass

c = C()
c.demo_a()
c.demo_b()

# 如果两个不同父类里有同名方法
# 会调用靠前的那个父类

# __mro__类属性可以查看方法的调用顺序
print(C.__mro__)