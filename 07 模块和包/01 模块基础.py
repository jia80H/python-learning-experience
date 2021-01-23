""" 模块的介绍 """
# 模块：在python里的一个py文件，就可以理解为模块
# 不是所有的py文件都能作为一个模块导入
# 如果想让一个py文件能被导入，模块名必须遵守命名规则（规则见基础概念）
# python为了方便开放，提供了很多内置模块

""" 导入模块的方法 """
# 方法一：
# import 模块名 ==> 直接导入一个模块
import time
# 导入模块后，就可以使用这个模块里的方法和变量
print(time.time()) # 前一个time是模块，后一个是方法

# 方法二：from 模块名 import 函数名 ==> 导入模块里的方法或变量
from random import randint
randint(0,2) # random.randint(0,2) 会报错 这个使用于方法一

# 方法三 from 模块名 import * ==> 导入模块里的"所有"方法和变量
from math import *
print(e) # 2.718281828459045
# 这个方法本质上市读取模块里的__all__属性，
# 看这个属性里定义里哪些变量和函数
# 如果模块里没有定义__all__才会导入所有不以_开头的变量和函数

# _开头的变量和函数，是建议只在本模块使用的

# 方法四 import 模块名 as 别名 ==> 导入一个模块，并给它起个别名
import datetime as dt 
# print(datetime.MAXYEAR) 不能使用原名
print(dt.MAXYEAR)

# 方法五 from 模块名 import 函数名 as 别名 
from copy import deepcopy as dc 

""" pip管理第三方模块 """

# 下载包
# pip install <package_name>

# 使用第三方包
# from <package_name> import <package_name>

# 卸载
# pip uninstall <package_name>

# 总览 
# 列出当前环境安装的第三方模块和版本号
# pip list
# pip freeze

# pip freeze > requirement.txt 模块名和版本号重新定向到指定文件
# pip install -r requirement.txt 读文件里的模块名和版本号并下载

# 临时更改下载地址
# pip install <package_name> -i <url> 

""" 自定义模块 """

# _开头的变量和函数，是建议只在本模块使用的
###################
# 不允许别人使用的实例
# 定义
_x = 100

# 最后删除
del _x
# 当别人导入后使用这个变量会报错
###################

# 测试模块只在本文件能执行，导入后不执行
# 使用 __name__ 
# 当直接执行本文件时 __name__ 值是 __name__
# 当这个文件作为模块导入时，值是 文件名
if __name__ == '__name__':
    print('这是测试')

###################

""" 包 """
# 可以将多个具有相似或者有关联的多个模块放到一个文件夹里便于统一管理
# 这个文件夹，我们称之为包
# python包里，会有一个 __init__.py 文件
