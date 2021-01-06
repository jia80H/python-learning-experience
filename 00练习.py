#if elif elif else
score = float(input('请输入你的成绩：'))
if 0<=score<60:
    print('不及格，重修')
elif 60<=score<80:
    print('及格了，但是一般般')
elif 80<=score<90:
    print('贡献良好，但是你还能更优秀')
else :
    print('优秀！满绩点！恭喜')
         
