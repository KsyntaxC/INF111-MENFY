#Generalizar la anterior secuencia para rangos de k, ejemplo si n=10, k=3
# 0 0 0 1 1 1 0 0 0 1
n=int(input("Introducir n terminos: "))
k=int(input("Introducir k: "))
t=0
for i in range (1,n+1):
    print(t, end=", ")
    if i%k==0:
        t=1-t