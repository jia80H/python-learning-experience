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

# 方法四 import 模块名 as 别名 ==> 导入一个模块，并给它起个别名
import datetime as dt 
# print(datetime.MAXYEAR) 不能使用原名
print(dt.MAXYEAR)

# 方法五 from 模块名 import 函数名 as 别名 
from copy import deepcopy as dc 
