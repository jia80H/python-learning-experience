class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    pass
p1 = Person('张三', 18)
p2 = Person('张三', 18)

s = Student('jack',18)
print(id(p1))

# 身份运算符is: 
# 比较是否是同一个对象(比较内存地址)
print(p1 is p2)
print(id(p2),id(p2))

# type() : 获取的是类对象
print(type(p1) is Person) # True

print(type(s) == Student)
print(type(s) == Person) # False

# isinstance : 
# 用来判断一个对象是否是由指定的类或父类创建的
print(isinstance(s, Student))
print(isinstance(s, Person)) # True

# issbuclass:
# 用来判断一个类是否是另一个类的子类
print(issubclass(Student, Person)) # True


