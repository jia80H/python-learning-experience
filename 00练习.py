money = input('输入指定格式转换')
if 'RMB' in money:
    num = float(money[3:])
    usd = round(num / 6.78,2)
    print('{}与USD{}等值'.format(money,usd))
elif 'USD' in money:
    num = float(money[3:])
    rmb = round(num * 6.78,2)
    print('{}与RMB{}等值'.format(money,rmb))
else:
    print('错误格式输入')