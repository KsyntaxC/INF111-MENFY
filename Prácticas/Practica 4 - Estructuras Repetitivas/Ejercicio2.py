#Resolver las siguientes secuencias para n terminos
#Una doble: 2 2 2 3 3 5 3 7 3 11 2 13 2 17 3 9 3 23 3
n=int(input("Intro n:"))
c=1; sc=2; z=2+3; p=2
for i in range(1,n+1):
    if i%2==0:
        print(p,end=", ")
        p=p+1; sw=0
        while sw==0:
            s=1; c2=0
            while s<=p:
                if p%s==0:
                    c2=c2+1
                s=s+1
            if c2==2:
                sw=1; c2=0
            else:
                p=p+1
    else:
        print(sc,end=", ")
        c=c+1
        if c>sc:
            sc=z-sc; c=1