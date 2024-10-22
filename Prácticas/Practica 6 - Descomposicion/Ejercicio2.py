#Dado un numero, intercambiar los digitos extremos
#Ejemplo: 35794129 pasara a 95794123
import math
n=int(input("intro n: "))
cd=int(math.log10(n))
pd=n//10**(cd)
n=n%10**(cd)
ud=(n%10)*10**(cd)
n=n-(n%10)
NN=ud+n+pd
print(NN)