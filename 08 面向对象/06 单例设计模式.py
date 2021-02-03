# 需要全局唯一的变量
""" 后边的覆盖前边 """


class Singleton(object):
    __instance = None  # 私有

    @classmethod
    def __new__(cls, *rgs, **kwargs):
        if cls.__instance is None:
            # 申请内存,创建一个对象,并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        self.a = a
        self.b = b


# 调用__new__方法申请内存
# 如果不重写__new__方法,会调用object的__new__方法
# object的__new__会申请内存
# 如果重写了__new__方法,需要手动申请内存
s1 = Singleton('aaaa', 'bbbbb')
s2 = Singleton('hhhh', 'lllll')
# print(s1 is s2) # 结果变为True

print(s1.a)  # hhhh

""" 只有第一次保存 """


class Singleton(object):
    __instance = None
    __is_first = True

    @classmethod
    def __new__(cls, *rgs, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False


s1 = Singleton('aaaa', 'bbbbb')
s2 = Singleton('hhhh', 'lllll')
# 给自己添加了一个属性
# __is_first = False
# 没有更改类属性,类属性只能通过类对象来修改

print(s1.a)  # hhhh
