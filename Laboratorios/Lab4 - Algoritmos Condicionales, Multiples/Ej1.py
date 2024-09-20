#Ordenar 3 numeros ascendentemente
a=int(input("Intro a: "))
b=int(input("Intro b: "))
c=int(input("Intro c: "))
if a<b:
    m1=a; m2=b
else:
    m1=b; m2=a
if c<m1:
    m3=m2; m2=m1; m1=c
else:
    if c<m2:
        m3=m2; m2=c
    else:
        m3=c
print(m1, m2, m3)