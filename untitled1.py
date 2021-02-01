score=input("成績?")
score=int(score)
if(not(score>0 and score<100)):
    print('請輸入1-100')
elif(score>=90 and score<=99):
    print("A")
elif(score>=80 and score<=89):
    print("B")
elif(score>=70 and score<=79):
    print("C")
elif(score>=60 and score<=69):
    print("D")
else:
    print("E")
