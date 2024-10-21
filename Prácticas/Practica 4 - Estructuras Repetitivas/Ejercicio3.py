#Resolver las siguientes secuencias para n terminos
#Una oculta: 2, 5, 10, 17, 28, 41, 58
n=int(input("Intro n:"))
t=2; p=3
for i in range(1,n+1):
    print(t,end=", ")
    t=t+p
    p=p+1; sw=0
    while sw==0:
        s=1; c=0
        while s<=p:
            if p%s==0:
                c=c+1
            s=s+1
        if c==2:
            sw=1; c=0
        else:
            p=p+1