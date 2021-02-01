math=input("數學成績?")
eng=input("英文成績?")
math=int(math)
eng=int(eng)
if(math>=60 and eng>=60):
    print("有獎")
elif(math<60 and eng<=60):
    print("有獎_罰站1小時")
else:
    print("87878787")