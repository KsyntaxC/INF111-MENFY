#Dado un numero, eliminar digitos repetidos
#Ejemplo: 988744465551 -> 9874651
n=int(input("Intro n: "))
nn = 0
ad=None 
NN=0
while n>0:
    d=n%10  
    n=n//10     
    if d!=ad:
        nn=nn*10+d
        ad=d
while nn>0:
    NN=NN*10+nn%10
    nn=nn//10
print(NN)