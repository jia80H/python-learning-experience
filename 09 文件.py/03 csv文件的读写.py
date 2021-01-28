import csv

file = open('demo.csv', 'w', encoding='utf8', newline='')
w = csv.writer(file)

w.writerow(['name', 'age', 'score'])
csv.writer(file).writerow(['jack', '18', '98'])

w.writerows(
    [
        ['lisi', '19', '88'],
        ['wangwu', '20', '91']
    ]
)