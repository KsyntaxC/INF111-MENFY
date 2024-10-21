#Resolver las siguientes secuencias para n terminos
# 1 2 3 2 1 1 2 3 2 1 1 2 3 2 1 1 ....
n=int(input("Introducir n: "))
t=1; c=0; c2=1; v=1
for i in range (1,n+1):
    print(t,end=" ")
    t=t+v; c=c+1
    if c==5:
        t=1; c=0; v=1; c2=1
    else:
        c2=c2+1
        if c2>2:
            c2=1; v=v*(-1)