n=int(input("Intro n: "))
nn = 0
ad=None 
while n>0:
    d=n%10  
    n=n//10     
    if d!=ad:
        nn=nn*10+d
        ad=d
NN=0
while nn>0:
    NN=NN*10+nn%10
    nn=nn//10
print(NN)