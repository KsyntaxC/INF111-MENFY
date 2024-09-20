#Por medio de una secuencia repetitiva, determinar si el numero es primo o no es primo
p=int(input("Introduce el valor numerico: "))
c=0
for i in range (1,p+1):
    if p%i==0:
        c=c+1
if c==2:
    print ("Es primo")
else:
    print ("No es primo")