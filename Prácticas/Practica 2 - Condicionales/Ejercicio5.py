##Resolver la ecuacion cuadratica completa
a=int(input("Introducir A: "))
b=int(input("Introducir B: "))
c=int(input("Introducir C: "))
z=b*b-4*a*c
if z>0:
    x1=(-b+(z**(1/2)))/(2*a)
    x2=(-b-(z**(1/2)))/(2*a)
    print("Las respuestas son: ",x1," y ",x2)
else:
    print("No hay raices")