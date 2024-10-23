#Introducir numero hasta digitar el -7, encontrar secuenciad de numeros impares ascendentes consecutivos y mostrarlos
# 4,6,5,7,9,12,3,7,8,11,13,15,17,32,5,3,6,9,8,1,3,4,5,9,11,15,-7
# 5,7,9,11,13,15,17,1,3,9,11
x=int(input("Intro x: "))
sw=0; im=x; s=x+2
while x!=-7:
    if x%2==0:
        sw=1
    else:
        if x==s:
            sw=0
        im=x
        s=x+2
    if sw==0:
        if x==im-2:
            print(im)
        else:
            print(x)
            sw=1
    x=int(input("Intro x: "))
    im=x