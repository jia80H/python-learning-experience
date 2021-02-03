""" os模块 """
# os 模块里提供的方法就是用来调用操作系统里的方法
import uuid
import hashlib
import hmac
import calendar
import time
import datetime
import random
import math
import sys
import os


################################
# os 模块里的path 经常会使用
# abspath ==> 获取文件的绝对路径
print(os.path.abspath('02 常见系统模块.py'))
# E:\git仓库\python-learning-experience\02 常见系统模块.py

# isdir 判断是否是文件夹
print(os.path.isdir('02 常见系统模块.py'))  # False
print(os.path.isdir('07 模块和包'))  # Ture

# isfile 判断是否是文件
print(os.path.isfile('02 常见系统模块.py'))  # True
print(os.path.isfile('07 模块和包'))  # Falsse

# os.path.exists 是否存在

# os.path.splittext
file_name = '2021.1.23.demo.py'
print(file_name.rpartition('.'))  # ('2021.1.23.demo', '.', 'py')
print(os.path.splitext(file_name))  # ('2021.1.23.demo', '.py')
#####################################

# os里的其他方法

os.getcwd()  # 获取当前的工作目录，即当前python脚本工作的目录
# os.chdir('test') # 改变当前脚本工作目录，相当于shell下的cd命令
os.rename('毕业论文.txt', '毕业论文-最终版.txt')  # 文件重命名
os.remove('毕业论文.txt')  # 删除文件
os.rmdir('demo')  # 删除空文件夹
os.removedirs('demo')  # 删除空文件夹
os.mkdir('demo')  # 创建-一个文件夹
os.chdir('C:\\')  # 切换工作目录
os.listdir('C:\\')  # 列出指定目录里的所有文件和文件夹
os.name  # nt- >widonws posix->Linux/Unix或 者MacoS
os.environ  # 获取到环境配置
os.environ.get('PATH')  # 获取指定的环境配置

""" sys模块 """
# 系统相关的方法

# sys.exit() # 退出程序，（并给出退出码）
# 和内置函数exit功能一直

print(sys.path)  # 结果是一个列表，表示查找模块的路径
# ['e:\\git仓库\\python-learning-experience',
# 'E:\\python\\python39.zip', 'E:\\python\\DLLs',
# 'E:\\python\\lib', 'E:\\python',
# 'C:\\Users\\HP\\AppData\\Roaming\\Python\\Python39\\site-packages',
# 'E:\\python\\lib\\site-packages']

# sys.stdin # 可以像unput一样，接收用户的输入。
# input 就是读取sys.stdin 里的数据
s_in = sys.stdin
while Ture:
    content = s_in.readline().rstrip('\n')
    if content == '':
        break
    print(content)

# sys.stdout # 修改这个可以改变默认输出位置 默认在控制台
sys.stdout = open('00练习.py', 'w', encoding='utf8')
print('hello')
print('good')

# sys.stdrr # 修改这个 可以改变错误输出的默认位置 默认在控制台
sys.stdrr = open('00练习.py', 'w', encoding='utf8')
print(1 / 0)
""" math模块 """
# 数学相关的模块
print(math.factorial(6))  # 720 求阶乘
print(math.pow(2, 10))  # 1024 幂运算

print(math.floor(12.98))  # 12 向下取整
print(math.ceil(15.00001))  # 16 向上取整

# round() 内置函数，实现四舍五入
print(math.sin(math.pi / 6))
print(math.cos(math.pi / 6))

""" random模块 """
# 用来生成一个随机数

# randint(a,b) 用来生成[a，b]的随机整数
print(random.randint(1, 10))

# random() 用来生成[0，1)的随机浮点数
print(random.random())

# randrange(a,b) 用来生成[a，b)的随机整数
print(random.randrange(1, 10))

# choice 用来在可迭代对象里随机抽取一个数据
print(random.choice(['a', 'b', 'c', 'd']))

# sample 用于在可迭代对象里随机抽取n个数据
print(random.sample(['a', 'b', 'c', 'd'], 2))

""" datetime模块 """

# 涉及到的类 datetime/date/time/timedelta
print(datetime.datetime.now())  # 获取当前的日期时间
print(datetime.date(2020, 1, 1))  # 创建一个日期
print(datetime.time(18, 23, 45))  # 创建一个时间
print(datetime.datetime.now()+datetime.timedelta(3))
# 计算三天后的日期时间

""" time模块 """

print(time.time())
# 获取到时间戳 UTC 1970.1.1 00：00：00 至今的秒数

print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 按照指定格式输出时间

print(time.asctime())
print(time.ctime())  # 给时间戳可以生成时间

time.sleep(10)  # 让程序休息10s

""" calendar模块 """

calendar.setfirstweekday(calendar.SUNDAY)
# 设置每周起始日期码 周一到周日对应的是0~6
print(calendar.firstweekday())

# 打印日历,以周日为其日期吗
c = calendar.calendar(2021)
print(c)

# 判断闰年
print(calendar.isleap(2000))

# 判断有几个闰年
count = calendar.leapdays(1996, 2010)
print(count)

# 打印某月的日历
print(calendar.month(2020, 3))

""" hashlib 和 hmac """

# 这两个模块都是用来数据加密的

# hahlib模块主要支持两个算法 md5 和 sha 加密
# 加密方式：
# 单向加密：只有加密过程，不能解密 md5、sha
# 对称加密   ，非对称加密 rsa

# 需要将加密的内容转换成二进制
x = hashlib.md5()
x.update('Jia..+1-1'.encode('utf8'))
# 上边两行可以化为 x = hashlib.md5('12345678'.encode('utf8'))
print(x.hexdigest())

# sha 加密
# 密文的长度不一样
h1 = hashlib.sha1('12345678'.encode())
print(h1.hexdigest())
h2 = hashlib.sha224('12345678'.encode())
print(h2.hexdigest())
h3 = hashlib.sha256('12345678'.encode())
print(h3.hexdigest())
h4 = hashlib.sha384('12345678'.encode())
print(h4.hexdigest())

# hmac 加密
# h = hmac.new('h'.encode('utf8'),'你好'.encode('utf8'),'') # 待解决报错
# result = h.hexdigest()
# print(h)

""" uuid模块 """
# uuid用来生成一个全局唯一的模块

# uuid1
print(uuid.uuid1())  # 随机生成唯一32位16进制数

# uuid2 不可用
# uuid3 和uuid 5 是使用传入的字符串根据固定的算法算出来的，固定
print(uuid.uu3(uuid.NAMESPACE_DNS, 'mlfy'))
print(uuid.uu5(uuid.NAMESPACE_DNS, 'mlfy'))

# uuid 4  随机
print(uuid.uuid4())  # 使用最多
