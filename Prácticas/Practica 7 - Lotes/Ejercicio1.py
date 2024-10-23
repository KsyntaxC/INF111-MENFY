#Dado un lote de n numeros, sumar en rangos de la secuencia clasica
#Ejemplo si n=23 entonces 2,7,8,3,9,7,10,4,11,21,8,5,3,6,9,10,2,8,6,4,7,9,8
#La salida seria 2,15,12,21,40,14,29,26
n=int(input("Intro n: "))  
c=1; c2=0; s=0; con=1; sw=1
for i in range(1,n+1):
    x=int(input("Intro x: "))
    s=s+x
    c=c+1
    if sw==0:
        sw=1; con=con+1
    else:
        if c>con:
            print(s)
            c=1; c2=c2+1; s=0
    if c2==con:
        sw=0; c2=0