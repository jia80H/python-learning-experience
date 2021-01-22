""" 名片管理系统 V1.0 """
persons=[]

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

    step = input('请输入要进行的操作（数字）')
    step = int(step)


    # 第一步添加
    if step ==1:
        name = input('输入名字\n')
        for person in persons:
            if name == person['name']:
                print('用户已存在')
                break
                
        else:
            age = input('输入年龄\n')
            tel = input('输入手机号\n')
            qq = input('输入qq号\n')
            person = {}
            person['name']=name
            person['age']=age
            person['tel']=tel
            person['qq']=qq
            persons.append(person)
            print('添加完成')
        input('请按任意键，并回车以继续')
    # 第二步删除       
    elif step == 2:
        name = input('输入删除的人的名字')
        for person in persons:
            if name == person['name']:
                persons.remove(person)
                print('删除成功')
                input('请按任意键，并回车以继续')
                break
        else:
            print('用户不存在')
            input('请按任意键，并回车以继续')
    #第三步修改
    elif step == 3:
        name = input('输入修改的人的名字')
        for person in persons:
            if name == person['name']:
                persons.remove(person)
                name = input('输入名字\n')
                age = input('输入年龄\n')
                tel = input('输入手机号\n')
                qq = input('输入qq号\n')
                person = {}
                person['name']=name
                person['age']=age
                person['tel']=tel
                person['qq']=qq
                persons.append(person)
                
                break
        else:
            print('用户不存在')
            input('请按任意键，并回车以继续')


    # 第四步查询
    elif step == 4:
        chaxun = input('本系统仅支持姓名查询\n请输入想要查询的姓名')

        for person in persons:
            if chaxun == person['name']:
                print('姓名\t\t年龄\t\t手机\t\t\tqq')
                for v in person.values():
                    print(v,end='\t\t')
                print()
                input('请按任意键，并回车以继续')
                break
        else:
            print('用户不存在')
            input('请按任意键，并回车以继续')


    # 第五步遍历
    elif step == 5:
        print('姓名\t\t年龄\t\t手机\t\t\tqq')
        for person in persons:
            for v in person.values():
                print(v,end='\t\t')
            print()            
        input('请按任意键，回车结束')
    # 第六步退出
    elif step == 6:
        tuichu = input('亲，真的要退出吗？yes/no \n')
        tuichu = tuichu.lower()
        print(tuichu)
        if tuichu == 'yes':
            break
        else:
            continue

