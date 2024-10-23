#Dado un numero eliminar el digito que ocupa la unidad de mil
n=int(input("Intro n: "))
c=0; y=0; po=1
while n!=0:
    d=n%10
    n=n//10
    c=c+1
    if c!=4:
        y=d*po+y
        po=po*10
print("y=",y)