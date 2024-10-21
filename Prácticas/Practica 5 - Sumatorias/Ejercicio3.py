#Resolver para n terminos
# + 1/2 - 2/2 - 4/3 + 4/6 + 4/11 - 4/20 -6/37
n=int(input("Intro n: "))
num=2; con=1; a=0; a=0; b=1; c=0; den=a+b+c; sig=1; c1=0; con1=1; c2=0; con2=2; s=0
for i in range(1,n+1):
    print(" ",sig,"(",num,"/",den,")")
    s=s+sig*(num/den)
    if sig>0:
        c1=c1+1
        if c1==con1:
            con1=con1+1; c1=0; sig=sig*(-1)
    else:
        c2=c2+1
        if c2==con2:
            con2=con2+1; c2=0; sig=sig*(-1)
    con=con+1
    if con==num:
        num=num+2; con=1
    a=b; b=c; c=den; den=a+b+c
print(" = ",s)
            