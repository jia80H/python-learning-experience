import file_manager
import model
import Tools
import students_manger

def register():
    # 读取文件, 查看文件是否有数据. 如果文件不存在默认是一个字典
    teachers = file_manager.read_json('11 学生管理系统/files/users.json', {})

    while True:
        username = input('请输入账号(3~6位)')
        if not 3 <= len(username) <= 6:
            print('账号不符合要求,请重新输入')
        else:
            break

    if username in teachers:
        print('用户已存在')
        return

    while True:
        password = input('请输入密码(6~12位)')
        if not 6 <= len(password) <= 12:
            print('密码不符合要求,请重新输入')
        else:
            break
    # 使用对象
    teacher = model.Teachers(username, password)
    teachers[teacher.username] = teacher.password
    # 不用对象
    # teachers[username] = password
    file_manager.write_json('11 学生管理系统/files/users.json', teachers)


def login():
    # 读取文件，查看文件是否有数据。如果文件不存在默认是一个字典
    teachers = file_manager.read_json('11 学生管理系统/files/users.json', {})
    username = input('输入用户名：')
    if username not in teachers:
        print('用户不存在')
        return
    password = input('请输入密码：')
    if teachers[username] == Tools.encrypt_password(password):
        students_manger.username = username
        students_manger.show_manager()
    else:
        print('密码错误')


def start():
    content = file_manager.read_file('11 学生管理系统/files/welcome.txt')
    while True:
        operator = input(content + '\n')
        if operator == '1':
            print('登录')
        elif operator == '2':
            print('注册')
            register()
        elif operator == '3':
            print('退出')
            break  # 把死循环停止
            # exit(0)  # 退出整个程序
            # sys.exit(0)
        else:
            print('无效操作')


if __name__ == '__main__':
    start()