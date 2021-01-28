""" 基础版 V1.0 """
file_name = input('请输入一个文件路径: ')
# 打开旧文件
old_file = open(file_name, encoding='utf8')

new_file_name = 'test.txt'
new_file = open(new_file_name, 'w', encoding='utf8')

# 把就文件的数据读取出来写入到新文件
new_file.write(old_file.read())

new_file.close()
old_file.close()

""" 优化版 V2.0 """
# 优化文件不存在会报错
# 根据被复制的文件名生成备份
# 兼容复制非文本

import os
file_name = input('请输入一个文件路径: ')

if os.path.isfile(file_name): # 判断文件是否存在
    # 打开旧文件
    old_file = open(file_name, 'rb')  # 以二进制打开
    
    names = file_name.rpartition('.')
    new_file_name = names[0] + '.bak.' +names[2]
    # 或者使用os.splitext() 
    # names = os.path.splitext(file_name)
    # new_file_name = names[0] + '.bak' +names[2]

    new_file = open(new_file_name, 'wb')

    # 把就文件的数据读取出来写入到新文件
    content = old_file.read()  # 读取出来的是二进制
    new_file.write(content)

    new_file.close()
    old_file.close()
else:
    print('文件不存在')

""" 优化版 V3.0 """
# 优化大文件复制
import os
file_name = input('请输入一个文件路径: ')

if os.path.isfile(file_name): # 判断文件是否存在
    # 打开旧文件
    old_file = open(file_name, 'rb')  # 以二进制打开
    
    names = file_name.rpartition('.')
    new_file_name = names[0] + '.bak.' +names[2]
    # 或者使用os.splitext() 
    # names = os.path.splitext(file_name)
    # new_file_name = names[0] + '.bak' +names[2]

    new_file = open(new_file_name, 'wb')

    while True:
        # 把就文件的数据读取出来写入到新文件
        content = old_file.read(1024)  # 读取出来的是二进制
        new_file.write(content)
        if not content:
            break

    new_file.close()
    old_file.close()
else:
    print('文件不存在')