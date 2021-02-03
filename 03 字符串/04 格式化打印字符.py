'''%占位符'''
name = 'zhangsan'
age = 18
print('大家好，我的名字是', name, '我今年', age, '岁了', sep='')

# 用占位符表示
print('大家好，我的名字是%s,我今年%d碎了' % (name, age))

# %s ==> 表示字符串占位符

# %d ==> 表示整数占位符
# %nd ==> 至少占n位 前面为空格补齐
# %0nd ==> 至少占n位 前面为0补齐
# %-nd ==> 至少占n位，后面空格补齐

# %f ==> 表示浮点数占位符
# %。nf ==> 小数点后保留n位

# %x或%X 十六进制
a = 255
print(a)  # 255
print('%x' % a)  # ff

x = 18
print('大家好，我的名字是%%s,我今年%d碎了' % x)
