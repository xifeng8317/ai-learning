import random
num = random.randint(1,100)
count=0
while True:
    a = int(input("请猜一个数："))
    count+=1
    if(a>num):
        print("猜大了")
    elif(a<num):
        print("猜小了")
    else:
        print(f"恭喜猜对了！一共猜了{count}次结束")
        break