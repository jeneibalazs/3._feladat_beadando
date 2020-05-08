db=int(input("Adja meg a tesztesetek számát: "))
precedencia={"+":1,"-":1,"*":2,"/":2,"^":2}
while db!=0:
    muvelet=input("Adjon meg egy kifejezést: ")
    ujstring=""
    lista=[]
    db-=1
    for i in muvelet:
        if i.isalpha():
            ujstring+=i
        else:
            if i=="(":
                lista.append(i)
            elif i==")":
                operator=lista.pop()
                while operator!="(":
                    ujstring+=operator
                    operator=lista.pop()
            else:
                while len(lista)!=0 and lista[-1]!="(" and precedencia.get(i)<=precedencia.get(lista[-1]):
                    ujstring+=lista.pop()
                lista.append(i)
    print(ujstring)
