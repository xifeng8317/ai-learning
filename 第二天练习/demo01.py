sum1=0
sum2=0
j=0
for i in range(1,101):
    if i%2==0:
        sum1+=i
print(sum1)

while j<100:
    j+=1
    if j%2!=0:
        sum2+=j
print(sum2)

print("====================")
# for 循环：1-100 偶数和，步长2，从2开始
sum1 = sum(range(2, 101, 2))
print("偶数和", sum1)

# for 循环：1-100 奇数和，步长2，从1开始
sum2 = sum(range(1, 100, 2))
print("奇数和", sum2)
