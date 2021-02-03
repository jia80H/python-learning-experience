import os
'''
int 整数 默认十进制
'''
a = 98  # 默认十进制
print(a)

b = 0b11001010100  # 0b表示二进制
print(b)  # 输出为十进制

c = 0o2132342467  # 0o表示八进制
print(c)  # 默认输出十进制

d = 0x12a3b1f324  # 0x表示十六进制
print(d)  # 默认输出十进制

print(bin(c))  # 转二进制
print(oct(a))  # 转八进制
print(hex(a))  # 转十六进制
os.system('pause')
