# 多态基于继承, 通过子类重写父类的方法
# 达到不同子类调用相同父类方法,得到不同结果
# 提高代码的灵活度
""" 不使用多态 """
class pDog(object):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class Bdog(object):
    def zhilu(self):
        print('导盲犬正在指路')


class Ddog(object):
    def jidu(self):
        print('缉毒犬正在搜毒')


class Person(object):
    def __init__(self,name):
        self.name = name

    def work_with_pd(self):
        self.dog.attack_enemy()

    def work_with_bd(self):
        self.dog.zhilu()

    def work_with_dd(self):
        self.dog.jidu()


p = Person('张警官')

pd = pDog()
p.dog = pd
p.work_with_pd()

bd = Bdog()
p.dog = bd
p.work_with_bd()

dd = Ddog()
p.dog = dd
p.work_with_dd()

""" 使用多态 """


class Dog(object):
    def work(self):
        print('狗正在工作')


class pDog(Dog):
    def work(self):
        print('警犬正在攻击坏人')


class Bdog(Dog):
    def work(self):
        print('导盲犬正在指路')


class Ddog(Dog):
    def work(self):
        print('缉毒犬正在搜毒')


class Person(object):
    def __init__(self,name):
        self.name = name
        self.dog = None

    def work_with_dog(self):
        if self.dog is not None and isinstance(self.dog,Dog):
            self.dog.work()

p = Person('张三')

pd = pDog()
p.dog = pd
p.work_with_dog()

bd = Bdog()
p.dog = bd
p.work_with_dog()

dd = Ddog()
p.dog = dd
p.work_with_dog()
