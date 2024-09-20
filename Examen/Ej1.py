n=int(input("Intro n: "))
a=1; b=2; t=1; c1=1; c2=0; sig=1
for i in range(1,n+1):
    print(t,end=", ")
    z=a+b; t=t+sig; c1=c1+1
    if c1>z:
        t=1; c1=1; a=a+1; b=b+1
    else:
        c2=c2+1
        if c2==a:
            sig=sig*(-1); c2=0