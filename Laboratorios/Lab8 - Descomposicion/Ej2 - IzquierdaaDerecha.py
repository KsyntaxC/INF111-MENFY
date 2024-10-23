#Descomposicion de Izquierda a Derecha
import math
n=int(input("Intro n: "))
cd=int(math.log10(n)+1)
print("cd=",cd)
while n!=0:
    d=n//10**(cd-1)
    n=n%10**(cd-1)
    cd=cd-1
    print("d=",d)