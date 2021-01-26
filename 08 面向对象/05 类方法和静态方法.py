class Person(object):

    type = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self, food): 
        print(self.name + '正在吃' + food)
    
    # 如果一个方法没有用到实例对象的任何属性,可以将这个方法定义为static
    @staticmethod
    def demo():
        print('我是静态方法demo')

    @classmethod
    def test(cls): 
        # 如果这个函数只用到了类属性,我们可以把它定义为一个类方法
        # 类方法有一个参数cls, 也不需要手动传参,会自动传参
        # cls 指的是类对象 cls is Person ==> True
        print('我是类方法test')

p = Person('张三', 18)
# 实例对象在调用方法时,不需要给形参self传参,
# self会自动接收实例对象为实参
p.eat('红烧牛肉泡面') # 直接使用实例对象调用参数

# eat对象方法, 可以直接使用 实例对象.方法名(参数) 调用
# 使用上面的方法不需要给self传参

# 对象方法也能使用 类名.方法名() 来调用
# 这种方法不会自动给self传参,需要手动指定self
Person.eat(p, '西红柿鸡蛋面')

# 静态方法调用
Person.demo()
p.demo()

# 类方法
# 可以使用实例对象和类对象来调用
p.test()
Person.test()