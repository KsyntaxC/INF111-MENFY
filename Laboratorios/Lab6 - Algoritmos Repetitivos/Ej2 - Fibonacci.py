#Una version de Fibonacci
# 0 1 1 2 3 5 8 13 .....
n=int(input("intro n terminos: "))
a=1; b=0; t=a+b
for i in range (1,n+1):
    print (t, end=(", "))
    a=b; b=t
    t= a+b