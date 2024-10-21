n=int(input("Intro n: "))
s=0
for i in range(1,n+1):
    print("(",1,"/",2,") *",i,"* (",i,"+",1,")")
    s=s+(1/2)*i*(i+1)
print(" = ",s)