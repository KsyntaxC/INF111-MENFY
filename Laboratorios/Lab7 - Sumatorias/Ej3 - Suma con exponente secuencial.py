#Resolver para n terminos la siguiente sumatoria
n=int(input("Intro n: "))
x=int(input("Intro x: "))
s=0; p=1; t=1
for i in range(1,n+1):
    s=s+x**t
    print(x,"^",t,end=" + ")
    p=p+1
    if p>t:
        t=t+1; p=1
print("=",s)