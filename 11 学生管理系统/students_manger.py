import file_manager
import model
username = ''


def add_student():
    x = file_manager.read_json('11 学生管理系统/files/'+username+'.json', {})
    if not x:
        students = []
    else:
        students = x['all_students']
    while True:
        name = input('输入学生姓名:')
        age = input('请输入年龄')
        gender = input('请输入性别')
        tel = input('请输入电话')

        # 创建一个student对象
        student = model.Students(name, age, gender, tel)
        students.append(student.__dict__)
        data = {'all_students': students, 'num': len(students)}
        file_manager.write_json('11 学生管理系统/files/'+username+'.json', data)
        choice = input('添加成功\n1.继续\n2.返回\n请选择:')
        if choice == '2':
            break


def show_students():
    pass


def modify_student():
    pass


def delte_student():
    pass


def show_manager():

    # print('显示管理页面')
    content = file_manager.read_file(
        '11 学生管理系统/files/students_pages.txt') % username
    while True:
        print(content)
        operator = input('请输入(1~5):')
        if operator == '1':
            print('添加')
            add_student()
        elif operator == '2':
            print('查看')
        elif operator == '3':
            print('修改')
        elif operator == '4':
            print('删除')
        elif operator == '5':
            print('返回')
            break
        else:
            print('输入有误')
