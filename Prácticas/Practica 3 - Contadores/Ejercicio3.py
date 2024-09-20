#Resolver la siguiente secuencia para n terminos
# 2 2 3 3 3 4 4 4 4 2 2 3 3 4 4 4 4 2 2 3 3 ....
n=int(input("Intro n: "))
c=0; a=2; b=4; t=a
for i in range (1,n+1):
    print(t, end=", ")
    c=c+1
    if c==t:
        t=t+1; c=0
        if t>b:
            t=a