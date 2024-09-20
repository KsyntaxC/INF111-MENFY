#Resolver la siguiente sumatoria para n terminos
n=int(input("Intro n: "))
x=int(input("Intro x: "))
s=0
for i in range(1,n+1):
    s=s+x**i
    print(x,"^",i,end=" + ")
print("=",s)