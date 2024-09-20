#Resolver las siguientes secuencias para n terminos
# 2 2 3 3 4 4 2 2 3 3 4 4 2 2 3 3 4 4 ...
n=int(input("Intro n: "))
t=2; c=0
for i in range (n):
    print (t)
    c=c+1
    if c==2:
        c=0
        if t<4:
            t=t+1
        else:
            t=2
