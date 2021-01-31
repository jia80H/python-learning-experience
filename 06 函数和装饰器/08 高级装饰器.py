""" 装饰器传递参数 """
def can_play(clock):
    print('最外层函数被调用了, clock = {}'.format(clock))


    def handle_action(fn):  # 
        def do_action(name, game):
            if clock < 21:
                fn(name, game)
            else:
                print('太晚了,不能玩游戏')

        return do_action
    
    return handle_action


@can_play(22)
def play_game(name, game):
    print(name + '正在玩儿' + game)


play_game('张三', '王者荣耀')
# 第一步: 调用canplay函数,并将参数22传递给clock
# 第二步: 调用handle_action()方法, 把plaay_game('张三', '王者荣耀')传递给fn
# 第三步: 调用play_game,其实就是调用do_action

""" 高级装饰器的使用 """
# 用户权限
user_permission = 6     # 2+4 0110 读写

# 权限因子
del_permission = 8      # 1000
read_permission = 4     # 0100
write_permission = 2    # 0010
exe_permission = 1      # 0001
# 二进制位中, 哪一位有值就有哪一位的权限
# 用户权限 & 权限因子 != 0 ==> 有权限


def check_permisson(x, y):
    def handle_action(fn):
        def do_action():
            if x & y != 0:
                fn()
            else:
                print('没有权限')

        return do_action
    return handle_action


@check_permisson(user_permission, read_permission)
def read():
    print('我正在读取内容')



@check_permisson(user_permission, write_permission)
def write():
    print('我正在写入内容')


@check_permisson(user_permission, exe_permission)
def excute():
    print('我正在执行内容')


@check_permisson(user_permission, del_permission)
def delete():
    print('我正在删除内容')


read()
write()
excute()
delete()