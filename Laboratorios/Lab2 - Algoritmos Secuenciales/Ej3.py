#Dado un número de 6 dígitos, eliminar el dígito que representa el dígito de la decena, osea el penultimo dígito
n=int(input("Introducir un número de 6 dígitos: "))
b=n%10
a=(n//100)*10
c=a+b
print(c)