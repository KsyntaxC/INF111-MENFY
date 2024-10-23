#Descomposicion de derecha a izquierda
n=int(input("Intro n:"))
while n!=0:
    d=n%10
    n=n//10
    print(d)