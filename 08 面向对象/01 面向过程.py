""" 面向过程的名片管理系统 """
user_list=[]

def add_info():
    # print('添加名片')

    # 1.使用input接收用户输入
    name = input('请输入姓名：')
    
    # 4.用户输入完成以后查看用户是否存在
    for user in user_list:
        if user['name'] == name:
            print('此用户名已被占用')
            return # 直接使用return结束整个函数
            # break # 不需要再使用break
    tel = input('请输入手机号：')
    qq = input('请输入qq号：')

    # 2.使用字典格式保存数据
    person = {}
    person['name']=name
    person['tel']=tel
    person['qq']=qq
    # 3.添加到用户列表
    user_list.append(person)

    print(user_list)

def is_available(num):
    if not num.isdigit(): # 如果序号不是数字
        return False
    num = int(num)
    if num < 0 or num > len(user_list) - 1:
        return False
    return True

def del_user():
    # print('删除名片')
    num = input('请输入需要删除的序号：')
    if not is_available(num):
        print('序号有误，请重新输入')
        return
    
    # 如果是数字，同时也在范围内，提示用户删除
    num = int(num)
    answer = input('确定删除吗？yes or no')
    if answer.lower() == 'yes':
        user_list.pop(num)
        # user_list.remove(user_list[num])
        # del user_list[num]

def modify_info():
    # print('修改名片')
    num = input('输入要修改的序号：')
    if not is_available(num):
        print('序号有误，请重新输入')
        return
    
    user = user_list[int(num)] # 根据用户输入的下标获得数据
    print('你要修改的信息是：\n',user)
    user['name'] = input('请输入新的姓名：')
    user['tel'] = input('请输入新的手机号：')
    user['qq'] = input('请输入新的qq号：')

def quer_info():
    # 查询名片
    search_name = input('请输入要查询的姓名：')
    
    for user in user_list:
        if user['name'] == search_name:
            print('查询到的信息如下：')
            print(user)
            break
    else:
        print('查无此人')

def show_all():
    # 显示所有名片
    print('序号\t\t姓名\t\t手机号\t\t\tqq')
    for i,user in enumerate(user_list):
        print(i,user['name'].center(15),user['tel'].center(10),user['qq'].center(10))
    
def quit_system():
    answer = input('是否要退出？yes or no')
    return answer.lower() == 'yes'

def start():
    while True:
        print('---------------------------')
        print('      名片管理系统 V1.0')
        print('1：添加名片')
        print('2：删除名片')
        print('3：修改名片')
        print('4：查询名片')
        print('5：显示所有名片')
        print('6：退出系统')
        print('---------------------------')
        operator = int(input('输入要进行的操作（数字）'))
        if operator == 1:
            add_info()
        elif operator == 2:
            del_user()
        elif operator == 3:
            modify_info()
        elif operator == 4:
            quer_info()
        elif operator == 5:
            show_all()
        elif operator == 6:
            if quit_system():
                break
        else:
            print('输入有误，请重新输入')

start()

