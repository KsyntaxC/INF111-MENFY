#Introducir valores hasta digitar el -1, encontrar en el lote la serie de Finonacci
a=-1; b=1; d=a+b
x=int(input("Intro x: "))
while x!=-1:
    if x==d:
        print(x)
        a=b;b=d;d=a+b
    x=int(input("Intro x: "))
    