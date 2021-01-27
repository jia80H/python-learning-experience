class Dog(object):
    def work(self):
        print('狗正在工作')
class pDog(Dog):
    def attack_enemy(self):
        print('警犬正在攻击坏人')


class Bdog(Dog):
    def zhilu(self):
        print('导盲犬正在指路')


class Ddog(Dog):
    def jidu(self):
        print('缉毒犬正在搜毒')


class Person(object):
    def __init__(self,name):
        self.name = name

    def work_with_dog(self):
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
