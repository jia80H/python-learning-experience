import file_manager
username = ''

def show_manager():

    # print('显示管理页面')
    content = file_manager.read_file('11 学生管理系统/files/students_pages.txt')%username
    while True:
        print(content)
        input('请输入(1~5):')