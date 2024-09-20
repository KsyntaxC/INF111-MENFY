#Encontrar el menor de 3 numeros
a=int(input("Intro a: "))
b=int(input("Intro b: "))
c=int(input("Intro c: "))
if a<b:
    men=a
else: 
    men=b
if c<men:
    men=c
print("El menor es ",men)