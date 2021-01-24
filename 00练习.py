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
s1 = Student('小明',18,175) # Student() ==> 会自动调用__init__方法
s2 = Student('小美',17,165)

# 根据业务逻辑，让不同对象执行不同的行为
s1.run
s1.eat

s2.eat