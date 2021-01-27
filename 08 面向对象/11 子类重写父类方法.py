# 继承的特点:
# 子类能直接使用父类里定义的方法

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print(self.name + '正在睡觉')

class Student(Person):
    # 子类在父类的基础上又添加了自己的新的功能
    def __init__(self,name,age,school):
        # 可以再写一个自己的
        # self.name = name
        # self.age = age
        # 调用父类的
        # 1. 父类名.方法名(self,参数列表)
        # Person.__init__(self, name, age)
        # 2. 使用super直接调用父类方法(推荐使用)
        super(Student, self).__init__(name,age)
        self.school = school

    # 子类的实现和父类实现完全不一样, 子类可以选择重写父类方法
    def sleep(self):
        print(self.name + '正在课件睡觉')
    def study(self):
        print(self.name + '正在学习')

s = Student('jack',18,'JLU') # 调用父类__init__方法
s.sleep()
