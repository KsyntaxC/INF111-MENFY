#Generaliza la secuencia anterior
n=int(input("Intro n terminos: "))
a=int(input("Intro a terminos: "))
b=int(input("Intro b terminos: "))
t=a; c=1; z=a+b
for i in range (1,n+1):
    print(t, end=", ")
    c=c+1
    if c>t:
        t=z-t
        c=1