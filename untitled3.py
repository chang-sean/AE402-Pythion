import random 
condition=True
num=random.randint(1,10)
while condition:
    guess=int(input("猜數字"))
    num=int(num)
    if(num>10) or (num<1):
        print("重輸")
    elif num==guess:
        print("對")
        condition=False
    else:
        print("錯")
        print("答案是",num)

