d={}
print('歡迎來到sean的英辭')
while True:
    print('1.建辭')
    print('2.搜辭')
    print('3.英=>中')
    print('4.中=>英')
    print('5.測驗')
    print('6.Bye')
    sel=input('輸入數字')
    if sel=="1":
        while True:
            voc=input('英')
            if voc=='0':
                break
            if voc not in d:
                m=input('中')
                d[voc]=m
            else:
                print('單字已存在')
    elif sel =='2':
        lk=sorted(d)
        for item in lk:
                print(item,'是',d[item])
    elif sel=='3':
        voc=input('英查(0)')
        if voc=='0':
           break
        if voc in d:
           print(d[voc])
        else:
           print('無此字')
    elif sel=='4':
        got=False
        ch=input('中查(0)')
        if ch=='0':
            break
        for k,v in d.items():
            if ch==v:
                print(ch,"=>",k)
                got=True
        if not got:
            print('無此字')
    elif sel=='5':
        score=0
        print('最高',len(d),'分')
        for k,v in d.items():
            print(v,":")
            ans=input()
            if ans==k:
                score+=1
                print('讚',score,"分")
            else:
                print('爛',score,'分')
    elif sel=='6':
        break
    else:
        print("傻子")