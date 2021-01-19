students=[
    {'name':'张三','age':18,'score':98,'tel':'17335463210','gender':'female'},
    {'name':'李四','age':28,'score':95,'tel':'12734632108','gender':'male'},
    {'name':'王五','age':21,'score':98,'tel':'16835463210','gender':'unknown'},
    {'name':'chris','age':17,'score':58,'tel':'17835486108','gender':'male'},
    {'name':'jack','age':23,'score':52,'tel':'1883546808','gender':'female'},
    {'name':'tony','age':15,'score':89,'tel':'17835463210','gender':'unknown'}
]



i = 0
while i < len(students):
    if students[i]['gender'] == 'unknown':
        students.remove(students[i])
        i -= 1
    i += 1
print(students)