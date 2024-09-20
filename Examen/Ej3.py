#Introducir valores hasta digitar el -1, encontrar en el lote la serie de Finonacci
#Dado n numeros mostrar el 3er numero fibonacci encontrado
#Ejemplo Si n=8
# 4 12 5 2 13 6 7 8 El 3er fibo es 13
a = -1
b = 1
d = a + b
fb = []
x = int(input("Introduce n hasta -1 para terminar: "))
while x != -1:
    if x == d:  
        fb.append(x)
        a = b
        b = d
        d = a + b  
    x = int(input("ntroduce n hasta -1 para terminar): "))
if len(fb) >= 3:
    print(f"El tercer Fibo es: {fb[2]}")
else:
    print("No se encontraron al menos 3 números de Fibonacci.")
