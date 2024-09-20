#Resolver las siguientes secuencias para n terminos
# 2 2 3 3 4 4 2 2 3 3 4 4 2 2 3 3 4 4 ...
n=int(input("Intro n: "))
a=int(input("Intro a: "))
b=int(input("Intro b: "))
t=a; c=0
for i in range (1,n+1):
    print (t, end=", ")
    c=c+1
    if c==2:
        c=0
        if t<b:
            t=t+1
        else:
            t=a