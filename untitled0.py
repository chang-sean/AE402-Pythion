n=int(input('多少人'))
score=[]
name=[]
hs=0
ls=100
hn=""
ln=""
summath=0
for i in range(2*n):
    mn=input("名字?")
    score.append(ms)
    print(score)
    if i%2==1:
        score[i]=int(score[i])
        summath=summath+score[i]
        if hs<score[i]:
            hs=score[i]
            hn=mn
        if ls>score[i]:
            ls=score[i]
            ln=mn
            
print (score)
print("班上最高",hs,"分","是",hn)
print("班上最低",ls,"分","是",ln)
print("班平",summath/n) 

