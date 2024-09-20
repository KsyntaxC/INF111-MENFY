#Una doble
# 0 1 1 2 1 2 2 3 3 3 5 .....
n=int(input("intro n: "))
a=-1; b=1; t=a+b; t2=1; p2=1
for i in range (1,n+1):
    if i%2==0:
        print(t2,end=(", "))
        p2=p2+1
        if p2>t2:
            t2=t2+1; p2=1
    else:
        print(t,end=", ")
        a=b; b=t
        t=a+b