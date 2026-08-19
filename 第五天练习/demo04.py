stu = {"name":"小王","age":20,"city":"武汉"}
print(stu["name"])
stu["age"]=21
print(stu)
stu["score"]=85
print(stu)

keys=stu.items()
for key in keys:
    print(key)