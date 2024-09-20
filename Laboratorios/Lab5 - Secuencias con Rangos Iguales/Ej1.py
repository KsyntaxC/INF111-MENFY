#Resolver la siguiente secuencia para n terminos
# 0 0 1 1 0 0 1 1 0 0 1 1 0 ......
n=int(input("Introducir n terminos: "))
t=0
for i in range (1,n+1):
    print(t, end=", ")
    if i%2==0:
        t=1-t