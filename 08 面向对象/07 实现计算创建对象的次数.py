class Person(object):
    __count = 0 # 类属性

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        x = object.__new__(cls)
        # 申请内存, 创建一个对象, 并设置类型是Person
        return x
    
    def __init__(self,name,age):
        # Person.__count += 1 # 直接这样写可以计数
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        return cls.__count

# 每次创建对象,都会调用__new__和__init__方法
# __new__方法用来申请内存
# 如果不重写__new__方法,它会自动找0bject的__new__
# object的__new__方法,默认实现是申请一段内存,创建一个对象

p1 = Person('张三', 18)
p2 =Person('jack',20)

print(Person.get_count())

p3 = object.__new__(Person)
p3.__init__('tony',23) # 手动调用创建对象

print(Person.get_count())
