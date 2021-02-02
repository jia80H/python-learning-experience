def g1():
    for i in range(3):
        yield i
    for j in 'abc':
        yield j

g = g1()
for gg in g:
    print(gg)