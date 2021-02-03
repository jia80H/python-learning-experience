""" 写入 """
import csv
file = open('demo.csv', 'w', encoding='utf8', newline='')
w = csv.writer(file)

# 写入单行
w.writerow(['name', 'age', 'score'])
csv.writer(file).writerow(['jack', '18', '98'])
# 写入多行
w.writerows(
    [
        ['lisi', '19', '88'],
        ['wangwu', '20', '91']
    ]
)
file.close

""" 读取 """
file = open('demo.csv', 'r', encoding='utf8', newline='')
r = csv.reader(file)
for date in r:
    print(date)

file.close
