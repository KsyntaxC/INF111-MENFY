#Resolver para n terminos la siguiente secuencia
# 2 2 2 5 5 5 2 2 2 5 5 5 2 2 2
n=int(input("Introducir n terminos: "))
k=int(input("Introducir k: "))
a=int(input("Introducir numero uno: "))
b=int(input("Introducir numero dos: "))
t=a; c=a+b
for i in range (1,n+1):
    print(t, end=", ")
    if i%k==0:
        t=c-t