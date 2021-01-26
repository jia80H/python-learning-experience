class Singleton(object):
    __instance = None 
    __is_first = True

    @classmethod
    def __new__(cls, *rgs, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,a,b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False

s1 = Singleton('aaaa', 'bbbbb')
s2 = Singleton('hhhh', 'lllll') 

print(s2.a) # aaaa
