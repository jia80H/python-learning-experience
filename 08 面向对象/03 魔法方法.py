""" 魔法方法 """
# 魔法方法也称魔术方法，是类里的一些特殊方法
# 特点
# 1. 不需要手动调用，会在合适的时机自动调用
# 2. 这些方法，都是以__开始，以__结束
# 3. 方法名都是系统规定好的，在合适的时机自己调用


class Student(object):
    def __init__(self, x, y):
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


p = Student('张三', 18)

# 如果不做任何修改，直接打印一个对象，
# 结果是对象的模块名、类型和内存地址
# print(p) # <__main__.Student object at 0x0000017C1335B700>


# 当打印一个对象,会调用这个对象的__str__或者__repr__方法
# 如果两个方法都写了，选择__str__
print(p)  # good

print(repr(p))  # 调用内置函数repr 会触发对象的__repr__方法
print(p.__repr__())  # 手动调用，但是魔法方法一般不手动调用

p()  # 对象名() ==> 调用这个对象的 p.__call__() 方法
# 可以把对象当成一个函数

""" 运算符相关的魔法方法 """


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
        # 条件成立返回True 否则返回False


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
# p1 p2 不是同一个对象
# 比较内存地址判断是否是同一个对象

num1 = [1, 2, 3]
num2 = [1, 2, 3]
print(num1 is num2)  # False
print(num1 == num2)  # True
# is 比较两个对象的内存地址
# == 会调用对象的__eq__方法，获取这个方法的比较结果

# is 身份运算符
# 可以判断两个对象是否是同一个对象
print(p1 is p2)  # False
print(p1 == p2)
# __eq__如果不重写，默认比较仍然是内存地址 结果是 # False
# 改写后为 # True

print(p1 != p2)
# != 本质上调用__ne__方法 或者 __eq__方法取反（没有重写ne 调用eq取反）

# > 本质上自动调用 __gt__(self,other)    即greater than
# >= 本质上自动调用 __ge__(self,other)   即greater equal
# <  ........__lt__
# <= ........__le__
# +         __add__
# -         __sub__
# *         __mul__
# /         __trudiv__
# %         __mod__
# **        __pow__

""" 转换相关 """

# str()将对象转换成字符串，会自动调用 __str__ 方法
# 打印*对象*也会调用

# int() ==> 调用对象 __int__方法
# float() ==> __float__

""" 实例 """
# 房子有 户型、总面积、剩余面积 和家具名称列表 __slots__属性的使用
# 新房子没有任何家具
# 将 家具名称 追加到 家具列表 中
# 判断 家具面积 是否 超过 剩余面积 ，如果超过，提示不能添加这件家具

# 家具 有 名称 和占地面积属性，其中
# 席梦思 占地 4 平米
# 衣柜 占地 2 平米
# 餐桌 占地 1.5 平米
# 将上面三件 家具 添加到 房子 中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表


class House(object):
    def __init__(self, house_type, total_area, fur_list=None):
        if fur_list is None:
            fur_list = []  # 将fur_list设置为空列表

            self.house_type = house_type
            self.total_area = total_area
            self.free_area = total_area * 0.6
            self.fur_list = fur_list

    def add_fur(self, fru):
        # 将任务交给房子做，把家具添加到房子里
        # （面向对象关注点：让谁做）
        if self.free_area < fru.area:
            print('剩余面积不足')
        else:
            self.fur_list.append(fru.name)
            self.free_area -= fru.area

    def __str__(self):  # 必须返回字符串
        return '户型为{}，总面积为{}，剩余面积为{}，家具列表为{}'.format(self.house_type, self.total_area, self.free_area, self.fur_list)


class Furiture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房子时传入户型和总面积
house1 = House('两室一厅', 56)

# 创建家具
bed = Furiture('席梦思', 4)
chest = Furiture('衣柜', 2)
table = Furiture('餐桌', 1.5)

house1.add_fur(bed)
house1.add_fur(chest)
house1.add_fur(table)

print(house1)
