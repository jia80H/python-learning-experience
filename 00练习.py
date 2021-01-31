def demo(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        return '除数不能为零'
    else:
        return x
    finally:
        return 'good'

print(demo(1,0)) # g	``
print(demo(1,2)) 