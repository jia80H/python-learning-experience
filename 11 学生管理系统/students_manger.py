import file_manager
import model
username = ''


def add_student():
    x = file_manager.read_json('11 学生管理系统/files/'+username+'.json', {})
    if not x:
        students = []
        num = 0
    else:
        students = x['all_students']
        num = int(x['num'])
    while True:
        name = input('输入学生姓名:')
        age = input('请输入年龄')
        gender = input('请输入性别')
        tel = input('请输入电话')
        num += 1
        # 字符串的zfill方法，再字符串前面补零
        id = 'stu_' + str(num).zfill(4)

        # 创建一个student对象
        student = model.Students(id, name, age, gender, tel)
        students.append(student.__dict__)
        data = {'all_students': students, 'num': len(students)}
        file_manager.write_json('11 学生管理系统/files/'+username+'.json', data)
        choice = input('添加成功\n1.继续\n2.返回\n请选择:')
        if choice == '2':
            break


def show_students():
    print('1. 查看所有学生')
    print('2. 根据姓名查找')
    print('3. 根据学号查找')
    print('4. 返回')
    choice = input('请输入（1~4）：')
    students = file_manager.read_json('11 学生管理系统/files/'+username+'.json', {})
    if not students:
        print('没有学生')
        return

    # if not students:
    #     students = []
    # else:
    #     students = students['all_students']
    # 或者
    students = students.get('all_students', [])

    if choice == '1':
        for student in students:
            print('学号:{id},\t 姓名:{name},\t 性别:{gender},\t 年龄:{age},\t 电话:{tel}'.format(
                **student))

    elif choice == '2':
        s_name = input('输入姓名:')

        # same_name = []
        # for student in students:
        #     if student['name'] == s_name:
        #         same_name.append(student)
        same_name = filter(lambda s: s['name'] == s_name, students)

        if not same_name:
            print('不存在')
        for student in same_name:
            print('学号:{id},\t 姓名:{name},\t 性别:{gender},\t 年龄:{age},\t 电话:{tel}'.format(
                **student))
    elif choice == '3':
        s_id = input('输入姓名:')
        same_id = filter(lambda s: s['id'] == s_id, students)
        if not same_id:
            print('不存在')
        for student in same_id:
            print('学号:{id},\t 姓名:{name},\t 性别:{gender},\t 年龄:{age},\t 电话:{tel}'.format(
                **student))
    else:
        pass


def show_students_jianhua():
    key = value = ''
    print('1. 查看所有学生')
    print('2. 根据姓名查找')
    print('3. 根据学号查找')
    print('4. 返回')
    choice = input('请输入（1~4）：')
    students = file_manager.read_json('11 学生管理系统/files/'+username+'.json', {})
    students = students.get('all_students', [])
    if not students:
        print('没有学生')
        return

    if choice == '1':
        pass

    elif choice == '2':
        value = input('输入姓名:')
        key = 'name'
        # 或者
        # s_name = input('输入姓名:')
        # students = filter(lambda s: s['name'] == s_name, students)
        # students只保留指定学生
    elif choice == '3':
        value = input('输入学号:')
        key = 'id'
        # 或者
        # s_id = input('输入姓名:')
        # students = filter(lambda s: s['id'] == s_id, students)
    else:
        return

    students = filter(lambda s: s.get(key, '') == value, students)
    # 或者
    # if choice == '2' or choice == '3':
    #     students = filter(lambda s: s[key] == value, students)

    if not students:
        print('没有学生')
        return

    for student in students:
        print('学号:{id},\t 姓名:{name},\t 性别:{gender},\t 年龄:{age},\t 电话:{tel}'.format(
            **student))


def modify_student():
    pass


def delte_student():
    y = file_manager.read_json(
        '11 学生管理系统/files/'+username+'.json', {})
    students = y.get('all_students', [])
    key = value = ''

    if not students:
        print('没有学生')
        return

    num = input('1. 按照姓名\n2. 按照学号\n 其他:返回')
    if num == '1':
        key = 'name'
        value = input('输入姓名')

    elif num == '2':
        key = 'id'
        value = input('请输入ID')
    else:
        return

    del_students = list(filter(lambda s: s.get(key, '') == value, students))
    if not del_students:
        print('没有学生')
        return
    for i, student in enumerate(del_students):
        print('{x} 学号:{id}, 姓名:{name}, 性别:{gender}, 年龄:{age}, 电话:{tel}'.format(
            x=i, **student))

    n = input('请输入要删除的序号(0~{}), 其他返回/n'.format(i))
    if not n.isdigit() or not 0 <= int(n) <= i:
        print('输入内容不合法')
        return
    students.remove(del_students[int(n)])
    y['all_stdents'] = students
    file_manager.write_json('11 学生管理系统/files/'+username+'.json', y)


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
            show_students_jianhua()
        elif operator == '3':
            print('修改')
        elif operator == '4':
            print('删除')
            delte_student()
        elif operator == '5':
            print('返回')
            break
        else:
            print('输入有误')


if __name__ == '__main__':
    username = 'jia'
    show_manager()
