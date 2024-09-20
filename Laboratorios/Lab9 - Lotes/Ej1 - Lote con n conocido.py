#Dado un n, introducir valores numericos, sumar en rangos com indica el primer elemento de cada rango
n=int(input("Intro n: "))
p=1; sw=0; s=0
for i in range(1,n+1):
    x=int(input("Intro x: "))
    if sw==0:
        k=x; p=1
        s=0; sw=1
    else:
        s=s+x;p=p+1
        if p>k:
            print(s)
            sw=0