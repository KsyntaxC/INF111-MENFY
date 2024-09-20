#Seguir esta estructura repetitiva
# 2 2 5 5 5 5 5 2 2 5 5 5 5 5 2 2 5 5.....
n=int(input("Intro n: "))
t=2; p=1; z=2+5
for i in range (1,n):
    print (t)
    p=p+1
    if p>t:
        t=z-t
        p=1
