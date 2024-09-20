##Dado un número de 8 dígitos, intercambiar los digitos centrales por los dígitos extremos
import math
n=int(input("introduce un numero de 8 dígitos: "))
c=int(math.log10(n)+1)
if c==8:
    PD=(n//10000000)*10000
    UD=(n%10)*1000
    DC1=((n//10000)%10)*10000000
    DC2=(n//1000)%10
    A1=((n//100000)%100)*100000
    A2=((n//10)%100)*10
    NN=DC1+A1+PD+UD+A2+DC2
    print(NN)
else:
    print("El valor introducido debe de tener 8 digitos") 