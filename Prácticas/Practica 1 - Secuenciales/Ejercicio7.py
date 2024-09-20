##Dado un numero de 8 digitos sumar de 2 en 2 digitos
n=int(input("Introduce un numero de 8 cifras: "))
a=n//10000000
b=(n//1000000)%10
c=(n//100000)%10
d=(n//10000)%10
e=(n//1000)%10
f=(n//100)%10
g=(n//10)%10
h=n%10
SUMd= a+b, c+d, e+f, g+h
print( a,  b,  c,  d,  e,  f,  g,  h)
print("La suma de los digitos es: ", SUMd)