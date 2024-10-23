#Dado un numero, encontar el digito mayor u el digito menor
n=int(input("Intro n: "))
may=0; men=9
while n!=0:
    d=n%10; n=n//10
    if d>may:
        may=d
    if d<men:
        men=d
print("El mayor es: ",may)
print("El menor es: ",men)