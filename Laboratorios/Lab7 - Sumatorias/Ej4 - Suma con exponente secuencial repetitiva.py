#Resolver para n terminos la siguiente sumatoria
n=int(input("Intro n: "))
x=int(input("Intro x: "))
s=0; a=-1; b=1; t=a+b; p=1; t2=2
for i in range(1,n+1):
    s=s+x**t/t2
    print(x,"^",t,"/",t2,end="  +  ")
    a=b; b=t; t=a+b
    p=p+1
    if p>t2:
        t2=t2+2; p=1
print("=",s)