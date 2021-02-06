""" 常见系统内置异常 """
# ZeroDivisionError: 1 / 0
# FileNotFoundError: 文件不存在 open('vdgvrfvsrfv.txt')
# FileExistsError: 多次创建同名文件夹
# ValueError: int('hello')
# KeyError: person = {'name','zhangsan'}  person['age']
# SyntaxError: print（‘hello’）

""" 自定义错误 """
# 用户创建
# 密码长度在6~12位


class LengthError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '长度必须在{}至{}之间'.format(self.x, self.y)


password = input('输入密码')
x = 6
y = 12
if x <= len(password) <= y:
    print('密码格式正确')
else:
    # print('密码格式错误')
    # 使用rise 关键字可以抛出一个异常
    # raise ValueError('密码格式错误')
    raise LengthError(x, y)

# 用户保存到数据库
print('用户创建成功')
