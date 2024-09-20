#Una secuencia oculta
# 1 3 5 8 11 14 18 22 26 30 35 ....
n=int(input("Intro n: "))
t=1; p=1; k=0
for i in range (1,n+1):
    k=k+t
    print(k,end=", ")
    p=p+1
    if p>t:
        t=t+1
        p=1