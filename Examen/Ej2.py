#Dado un numero, rotar a la izquierda cada k digitos
#Ejemplo: Si      n= 2451389762 y k=3
#El nuevo numero es: 2145938276
n = int(input("Introduce el número: "))
k = int(input("Introduce el valor de k: "))
def kd(numero, k):
    nstr = str(numero)
    nr = ""
    for i in range(0, len(nstr), k):
        b = nstr[i:i+k]
        br = b[-1] + b[:-1] 
        nr += br
    return int(nr)
NN = kd(n, k)
print(f"El nuevo número es: {NN}")
