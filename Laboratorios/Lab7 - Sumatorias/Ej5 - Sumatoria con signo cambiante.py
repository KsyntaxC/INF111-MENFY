#Resolver para n terminos
n=int(input("Intro n: "))
x=int(input("Intro x: "))
s=0; a=-1; b=1; t=a+b; sig=1
for i in range(1,n+1):
    s=s+sig*(x**t/(i*2))
    print(sig,"*",x,"^",t,"/",i*2,end=" + ")
    a=b; b=t; t=a+b
    if i%2==0:
        sig=sig*(-1)
print("=",s)
