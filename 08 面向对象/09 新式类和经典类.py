# 手动指定Anim的父类为object
class Animal(object):
    pass

# 没有指定Dog的父类,python3默认继承自object
class Dog:  
    pass

# 新式类和经典类的概念
# 1. 新式类: 继承自object 的类
# 2. 经典类: 不继承自object的类

# 在python2里,如果不手动指定一个类的父类是object,这个类就是一个经典类
