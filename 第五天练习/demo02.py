count=0
t=(5,2,9,2,7)
print(t[2])
for i in t:
    if i==2:
        count=count+1
print(f"数字2出现的次数为{count}")
list1=list(t)
list1.append(6)
print(list1)