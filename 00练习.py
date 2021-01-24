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
s1 = Student('张三', 18)
s1.say_hello()

# 申请一块新的内存空间
s2 = Student('jack',18)
s2.say_hello()