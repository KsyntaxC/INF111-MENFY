#Composicion a la Izquierda
n=int(input("Intro n: "))
y=0; po=1
for i in range(n):
    d=int(input("Intro d (DIGITO) "))
    y=d*po+y
    pro=po*10
print("y=",y)