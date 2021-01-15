'''len'''
#使用内置函数len 可以获得字符串的长度
x = 'abcdefgb'
print(len(x))

'''查找'''
#查找内容的方法 find/index/rfind/rindex 可以获得指定字符串的下标
print(x.find('b'))
print(x.index('b'))

print(x.find('h')) #-1 如果字符串里不存在，结果是 -1
#print(x.index('b')) #使用index，如果字符串里不存在会报错

print(x.rfind('b')) #找到最大的下标

'''判断'''
#startswith,endswith,isalpha,isdigit,isalnum,isspace
#以is开头的是判断，结果是一个bool
print('hello'.startswith('he')) #True
print('hello'.endswith('o')) #True
print('he23lo'.isalpha()) #False
print('123'.isdigit()) #True
print('3,14'.isdigit()) #Fals
print('ab123'.isalnum()) #True
print('4-1'.isalnum()) #False
print('   '.isspace()) #True

'''计数'''
#s.count(sub[,start[,end]])
m = 'mlfyiwmdfhhh'
print(m.count('h')) #3

'''替换'''
#replace方法：用来替换字符串
#

word = 'hello lol'
m = word.replace('l', 'x')  #全部替换
print(word) #字符串不可变
print(m) #生成一个新的字符串
print(word.replace('l','x',3)) #hexxo xol

'''内容分隔'''
#内容分割主要涉及到split,splitlines,partition和rpartition四种方法

#split
mystr = '今天天气好晴朗，处处好风光呀好风光'
result = mystr.split() #默认使用空格分隔，所以字符串未被分隔
print(result) #['今天天气好晴朗，处处好风光呀好风光']

result = mystr.split('好') #以好为分隔符
print(result) #['今天天气', '晴朗，处处', '风光呀', '风光']
result = mystr.split('好',2) #以好为分隔符,最多分隔2+1次
print(result) #['今天天气', '晴朗，处处', '风光呀好风光']

#rsplit 和split用法基本一直，只不过从右往左分隔

c = 'xiaoming,xiaohua,xiaofang,xiaowang'
print(c.split(',',2)) #['xiaoming', 'xiaohua', 'xiaofang,xiaowang']
print(c.rsplit(',',2)) #['xiaoming,xiaohua', 'xiaofang', 'xiaowang']

#splitlines 
#按照行分隔，返回一个包含各行作为元素的列表
m = 'hello \nworld'
print(m.splitlines()) #['hello ', 'world']

#partition 
#指定一个字符串作为分隔符，分为三部分（前面，分隔符，后面）
print('abcedefXmpXqrst'.partition('X')) #('abcedef', 'X', 'mpXqrst')
print('abcedefXmpXqrst'.rpartition('X')) #('abcedefXmp', 'X', 'qrst')

file_name = '2020.02.2beautiful.mp4'
print(file_name.rpartition('.')) #('2020.02.2beautiful', '.', 'mp4')

'''修改大小写'''

#capitalize 让第一个单词首字母大写
print('help world.good moring.\nyes'.capitalize()) 
# Help world.good moring.
# yes

#uper 全大写
print('help world.good moring.'.upper()) #HELP WORLD.GOOD MORING. 
#lower 全小写
print('HELP WORLD.GOOD MORING.'.lower()) #help world.good moring. 
#title 每个单词首字母大写
print('help world.good moring.'.title()) #Help World.Good Moring.

'''空格处理'''
#ljust(width,fillchar) 至少占n格,fillchar默认为空格
print('*','monday'.ljust(10),'*',sep='') #*monday    *
print('*','monday'.ljust(10,'^'),'*',sep='') #*monday^^^^*
#rljust变为从左边补不足的

#center 居中 左右补
print('wednesday'.center(20,'~')) #~~~~~wednesday~~~~~~

#lstrip(fillchar) 去除左边fillchar(默认空格)
print('   apple   *'.lstrip()) #apple   *
#rstrip() 去除右边空格
#strip() 去除两边空格

'''字符串拼接join'''
#split可以把字符串转换为列表，join可以将列表转化为字符串
fruit = ['apple','pear','peach','banana']
print('-'.join(fruit)) #apple-pear-peach-banana

print('*'.join('hello')) #h*e*l*l*o

'''查看字符对应编码Unicode'''
#ord查看字符对应编码
print(ord('你')) #20320
#chr查看编码对应字符
print(chr(20320)) #你

#GBK utf-8 Big5
#使用encode转编码
print('你'.encode('gbk')) #b'\xc4\xe3'
print('你'.encode('utf8')) #b'\xe4\xbd\xa0'

#使用decode转字符
print(b'\xe4\xbd\xa0'.decode('utf8')) #你

#乱码出现的原因
y = '你好'.encode('utf8')
print(y.decode('gbk')) #浣犲ソ
