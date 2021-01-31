""" with关键字的使用 """
try:
    file = open('xxx.text', 'r')
except FileNotFoundError:
    print('文件不存在')
else:
    try:
        file.read()
    finally:
        file.close()

# 使用with
try :
    with open('xxxx.txt', 'r') as file:
        file.read()  # 不需要手动的关闭文件
        # with关键字会帮助我们关闭文件
except FileNotFoundError:
    print('文件未找到')

# with我们称之为上下文管理器, 很多需要手动关闭的连接
# 如 文件连接, socket连接, 数据库的连接
# 都能使用with关键字自动关闭

# with 关键字后面需要实现__enter__和__exit__魔法方法

""" 上下文管理器 """
# with 语句后面的结果对象需要重写__enter__和__exit__方法
# 当进入到with代码块时,会自动调用__enter__方法里的代码
# 当with代码执行完成以后, 会自动调用__exit__方法


class Demo():
    def __enter__(self):
        print('method "__enter__" has been excuted ')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('method "__exit__" has been excuted ')
        


def creat_obj():
    x = Demo()
    return x


with creat_obj() as d:  # as 变量名
    # 变量d 不是 create_obj的返回结果
    # 而是创建的对象x调用__enter__之后的返回结果
    # d = creat_obj().__enter__()
    print(d)

