list = [1,2,3,4,5]
print(sum(list))

print("==================")
list1=[12,5,8,99,23,67,4,78,3]
list2=[]
for i in list1:
    if i>20:
        list2.append(i)
print(list2)
print("===================")
list1=[12,5,8,99,23,67,4,78,3]
list2=[i for i in list1 if i>20]
print(list2)