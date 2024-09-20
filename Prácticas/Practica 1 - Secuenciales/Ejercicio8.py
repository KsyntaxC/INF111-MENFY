##Dado un numero de 7 digitos eliminar el digito central y reemplazar en los extremos
n=int(input("Introduce un numero de 7 dígitos: "))
dc=(n//1000)%10
de1=((n//10000)%100)*1000
de2=((n//10)%100)*10
NN=dc*100000+de1+de2+dc
print(NN)