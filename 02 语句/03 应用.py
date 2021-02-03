'''求质数'''
# 打印（100，201）内的质数 方法1 if...else

for i in range(101, 201):

    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        print(i, '是质数')


# 打印（100，201）内的质数 方法2 假设成立

for i in range(101, 201):
    flag = True
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, '是质数')

# 打印（100，201）内的质数 方法3 计数法

for i in range(101, 201):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1  # 求有几个因子
            break
    if count == 0:
        print(i, '是质数')

'''求斐波那契数列的第n个值'''
m = int(input('第几个数？'))

num1 = 1
num2 = 2

for i in range(0, m - 2):
    a = num1
    num1 = num2
    num2 = a + num2
print(num2)

'''九九乘法表'''
# while循环
j = 0
while j < 9:
    j += 1
    i = 0
    while i < j:
        i += 1
        print(i, '*', j, '=', i*j, sep="", end="\t")
    print()

# for循环
