#Verificar si un numero es primo o no
n=int(input("Intro n: "))
i=1; c=0
while i<n+1:
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print("Es primo")
else: 
    print("No es primo")