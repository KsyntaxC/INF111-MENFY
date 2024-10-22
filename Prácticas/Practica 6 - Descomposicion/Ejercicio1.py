#Dado un numero n, eliminar todos los digitos que se encuentren despues de un digito 
#Por ejemplo: n=984257614, el nuevo numero seria 982764
import math
n=int(input("Intro n: "))
cd=int(math.log10(n))+1
nn=0
while n!=0:
    d=n//10**(cd-1)
    n=n%10**(cd-1)
    cd=cd-1
    if d%2==0:
        nn=nn*10+d
        d=n//10**(cd-1)
        n=n%10**(cd-1)
        cd=cd-1
    else:
        nn=nn*10+d
print(nn)