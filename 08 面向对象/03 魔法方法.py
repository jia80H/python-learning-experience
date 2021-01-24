""" __init__魔法方法 """
# 魔法方法也称魔术方法，是类里的一些特殊方法
# 特点
# 1. 不需要手动调用，会在合适的时机自动调用
# 2. 这些方法，都是以__开始，以__结束
# 3. 方法名都是系统规定好的，在合适的时机自己调用

class Student(object):
    def __init__(self,x,y):
        # 在创建对象时，自动调用这个方法
        print('__init__方法被调用了')
        self.name = x
        self.age = y

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__方法被调用了')
    
    def __repr__(self):
        return 'hello'
    
    def __str__(self):
        return 'good'

    def __call__(self, *args, **kwargs):
        print('__call__方法被调用了')

p = Student('张三',18)

# 如果不做任何修改，直接打印一个对象，
# 结果是对象的模块名、类型和内存地址
# print(p) # <__main__.Student object at 0x0000017C1335B700>


# 当打印一个对象,会调用这个对象的__str__或者__repr__方法
# 如果两个方法都写了，选择__str__
print(p) # good

print(repr(p)) # 调用内置函数repr 会触发对象的__repr__方法
print(p.__repr__()) # 手动调用，但是魔法方法一般不手动调用

p()