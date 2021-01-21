# 多个返回值
def shang_yu(m,n):
    x = m // n
    y = m % n
    return x,y # 返回的本质是一个元组
    #也可以这样写 x,y ==> [x,y] or (x,y) or {'x':x,'y':y}
    # 需要用相应的方法取出值

result = shang_yu(13,4)
print('商是{},余数是{}'.format(result[0],result[1]))