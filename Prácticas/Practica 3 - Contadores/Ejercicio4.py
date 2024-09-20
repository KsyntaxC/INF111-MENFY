#Generalizar ejercicio 3
n=int(input("Intro n: "))
a=int(input("Intro a: "))
b=int(input("Intro b: "))
c=0; t=a
for i in range (1,n+1):
    print(t, end=", ")
    c=c+1
    if c==t:
        t=t+1; c=0
        if t>b:
            t=a