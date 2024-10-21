#Resolver para n terminos
# + 1/x^2 + 2/x^2 - 3/x^5 - 2/x^5 + 1/x^5 + 1/x^5 - 2/x^5 - 3/x^2 + 2/x^2 + 1/x^5 - 1/x^5 - 2/x^5
n=int(input("Intro n: "))
x=int(input("Intro x: "))
s=0; sig=+1; sb=1; v=1; c=0; c2=1; e=2; ce=1; z=2+5
for i in range(1,n+1):
    print(" ",sig,"",sb,"/",x,"^",e,end="")
    s=s+sig*sb/x**e
    if i%2==0:
        sig=sig*(-1)
    sb=sb+v; c=c+1
    if c==5:
        sb=1; c=0; c2=1; v=1
    else:
        c2=c2+1
        if c2>2:
            c2=1; v=v*(-1)
    ce=ce+1
    if ce>e:
        e=z-e; ce=1
print (" = ",s)