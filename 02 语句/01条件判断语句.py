'''if'''
# if 和if else 以及if elif elif else

# if 条件判断 ：
#   条件成立时，执行的代码
age = int(input('请输入你的年龄：'))
if age < 18:
    print('未满十八禁止入内')

# if...else
# if 条件判断 ：
#   条件成立时，执行的代码
# else:
#   条件不成立时，执行的代码
age = int(input('请输入你的年龄：'))
if age < 18:
    print('未满十八禁止入内')
else:
    print('欢迎光临')


# if elif elif else
score = float(input('请输入你的成绩：'))
if 0 <= score < 60:  # 有的语言不能连续比较大小，必须用逻辑连接符 0<=score and score<60
    print('不及格，重修')
elif 60 <= score < 80:
    print('及格了，但是一般般')
elif 80 <= score < 90:
    print('贡献良好，但是你还能更优秀')
else:
    print('优秀！满绩点！恭喜')

'''if的镶嵌'''
tick = input('买票了吗？Y/N\n')
if tick == 'Y':
    safe = input('安检通过了吗？Y/N\n')
    if safe == 'Y':
        print('欢迎进站\n')
    else:
        print('再次安检\n')
else:
    print('买票去\n')
    pass

# pass没有意义，用来占位

'''三元表达式'''
num1 = int(input('数字1'))
num2 = int(input('数字2'))
x = num1 if num1 > num2 else num2
print(x)
