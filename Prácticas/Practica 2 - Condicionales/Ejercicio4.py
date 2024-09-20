#Encontrar el tercer mayor de 6 numeros
a=int(input("Intro a: "))
b=int(input("Intro b: "))
c=int(input("Intro c: "))
d=int(input("Intro d: "))
e=int(input("Intro e: "))
f=int(input("Intro f: "))
if a>b:
    m1=a; m2=b
else:
    m1=b; m2=a
if c>m2:
    if c>m1:
        m3=m2; m2=m1; m1=c
    else:
        m3=m2; m2=c
else:
    m3=c
if d>m3:
    if d>m2:
        if d>m1:
            m3=m2; m2=m1; m1=d
        else:
            m3=m2; m2=d
    else:
        m3=d
if e>m3:
    if e>m2:
        if e>m1:
            m3=m2; m2=m1; m1=e
        else:
            m3=m2; m2=e
    else:
        m3=e
if f>m3:
    if f>m2:
        if f>m1:
            m3=m2; m2=m1; m1=f
        else:
            m3=m2; m2=f
    else:
        m3=f
print ("El tercer mayor es ",m3)