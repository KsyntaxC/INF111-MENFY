#Vamos con un Sube y baja
n=int(input("intro n terminos: "))
a=int(input("intro a numero mas bajo: "))
b=int(input("intro b numero mas alto: "))
c=0; t=a; v=1
for i in range (1,n+1):
    print(t, end=", ")
    t=t+v; c=c+1
    if c==b-a:
        v=v*(-1); c=0