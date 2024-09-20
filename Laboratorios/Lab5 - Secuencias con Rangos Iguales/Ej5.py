#Resolver para n terminos
# 2 2 5 5 5 5 5 2 2 5 5 5 5 5 2 2 .....
n=int(input("Intro n terminos: "))
t=2; c=1; z=2+5
for i in range (1,n+1):
    print(t, end=", ")
    c=c+1
    if c>t:
        t=z-t
        c=1