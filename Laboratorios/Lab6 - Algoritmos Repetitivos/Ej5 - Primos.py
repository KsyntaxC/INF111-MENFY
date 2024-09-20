#Primos
n=int(input("Intro n: "))
c=0; k=2; p=2
while c<=n:
    if p%k!=0 and k<=p//2:
        k=k+1
    else:
        if k>p//2:
            print(p,end=(", "))
            c=c+1
        p=p+1
        k=2