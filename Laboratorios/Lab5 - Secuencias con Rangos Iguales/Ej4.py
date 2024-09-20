#Resolver para n terminos
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 ......
n=int(input("Intro n terminos: "))
t=1; c=1
for i in range (1,n+1):
    print(t, end=", ")
    c=c+1
    if c>t:
        t=t+1
        c=1