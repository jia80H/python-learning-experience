""" 介绍 """
# 在程序运行过程中, 由于编码不规范等造成程序无法正常执行,此时程序就会报错
# 健壮性: 很多编程语言都有异常处理机制


def div(a, b):
    return a / b


try:
    x = div(5, 0)
    print('hhh')
except Exception as e:
    # 如果程序出错了, 会立刻跳转到except 语句
    # 不会打印hhh
    print('程序出错了')
    print(e)
else:
    # 如果程序没有出错, 会执行else里的代码
    print('计算的结果是', x)

""" try...except """
# try...except 语句用来处理程序运行过程中的异常

try:
    file = open('ddd.txt')
    print(file.read)
    file.close()
except Exception as e:  # 给异常起了一个变量名 e
    print(e)
# 可以直接这样写
# except:
    # print('出错了')
# 也可以处理指定错误
# 多个用元组储存
# except FileNotFoundError as e:
    # print(e)

""" 应用 """
# 原版 V1.0
age = input('输入你的年龄')
if age.isdigit():
    age = float(age)

    if age > 18:
        print('欢迎')
    else:
        print('未满18')

else:
    print('输入的不是数字')
# 21.5 提示输入的不是数字

# 优化 V2.0
age = input('输入你的年龄')
try:
    age = float(age)
except ValueError:
    print('输入的不是数字')
else:
    if age > 18:
        print('欢迎')
    else:
        print('未满18')

""" finally关键字的使用 """
# try ....:
# somerthing
# finnally:
# another things
# finally最终一定会执行的代码

try:
    print(1/0)
finally:
    print('nihao')


def demo(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        return '除数不能为零
    else:
        return x
    finally:
        return 'good'


print(demo(1, 0))  # good
print(demo(1, 2))  # good
# 如果函数里有finally,
# finally里的返回值会覆盖前面的返回值
