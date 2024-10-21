#Resolver para n terminos
# + 1/x^0 - 3/x^3 + 6/x^1 + 10/x^3 - 15/x^19 - 19/x^22
n=int(input("Intro n: "))
x=int(input("Intro x: "))
sig=1; cs1=0; cs2=0; s=0; ps1=1; ps2=1
a=-1; b=1; e1=a+b
e2= 3; ce2=1; z=3+5
oc=1; sb=2; v=1
for i in range(1,n+1):
    if i%2==0:
        print("",sig,"",oc,"/",x,"^",e2)
        s=s+sig*oc/x**e2
        ce2=ce2+1
        if ce2>e2:
            e2=z-e2; ce2=1
    else:
        print("",sig,"",oc,"/",x,"^",e1)
        s=s+sig*oc/x**e1
        a=b; b=e1; e1=a+b
    if sig>0:
        cs1=cs1+1
        if cs1==ps1:
            ps1=ps1+1; cs1=0; sig=sig*(-1)
    else:
        cs2=cs2+1
        if cs2==ps2:
            ps2=ps2+1; cs2=0; sig=sig*(-1)
    oc=oc+sb; sb=sb+v
    if sb>=5:
        v=v*(-1)
    if sb<=1:
        v=v*(-1)
print(" = ",s)