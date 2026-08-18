n=int(input("请输入成绩:"))
if 100>=n>=90:
    print("优秀")
elif 90>n>=80:
    print("良好")
elif 80>n>=60:
    print("及格")
elif 60>n>=0:
    print("不及格")
else:
    print("输入无效")