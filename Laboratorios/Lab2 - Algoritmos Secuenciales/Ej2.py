#Dado un número de 5 dígitos, eliminar el dígito central 
n=int(input("Introducir un número de 5 dígitos: "))
de1=(n//1000)*100
de2=n%100
dsc=de1+de2
print("El nuevo número sin el centro es", dsc)