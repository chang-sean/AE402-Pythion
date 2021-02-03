n=int(input('多少'))
score=[]
name=[]
hs=0
ls=100
hn=""
ln=""
summath=0
for i in range(n):
    mn=input("name")
    ms=int(input("score?"))
    name.append(mn)
    score.append(ms)
    if hs<ms:
        hs=ms
        hn=mn
    if ls>ms:
        ls=ms
        ln=mn
    summath=summath+ms
print (score)
print("班上最高",hs,"分","是",hn)
print("班上最低",ls,"分","是",ln)
print("班平",summath/n) 



