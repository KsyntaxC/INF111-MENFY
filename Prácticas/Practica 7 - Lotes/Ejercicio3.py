#Introducir numeros hasta digitar el -5, contar cuantos valores impares se encuentran despues de dos valores pares
x=int(input("Intro x: "))
cp=0; ci=0
while x!=-5:
    if x%2==0:
        cp=cp+1
    else:
        if cp>=2:
            if x%2!=0:
                ci=ci+1
                print(ci)
        cp=0
    x=int(input("Intro x: "))
