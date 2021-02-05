for i in range(101, 201):

    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        print(i, '是质数')
