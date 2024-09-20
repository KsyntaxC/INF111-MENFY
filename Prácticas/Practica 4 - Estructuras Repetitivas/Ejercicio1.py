#Resolver las siguientes secuencias para n terminos
# 1 2 3 2 1 1 2 3 2 1 1 2 3 2 1 1 ....
n=int(input("Introducir n: "))
a=int(input("Introducir a: "))
b=int(input("Introducir b: "))
c1=0; c2=0; t=a; v=1
for i in range (1,n+1):
    print (t, end=", ")
    t=t+v; c1=c1+1
    if c1>a+b:
        t=a; c1=0
    else:
        c2=c2+1
        if c2==b-a:
            v=v*(-1); c2=0
#Solo funciona para el ejemplo xd, n=10, a=1, b=3
#Para los demas se buguea y ya me estrese para generalizarlo mas xdxd