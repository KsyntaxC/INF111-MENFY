##Dado un numero de 5 digitos intercambiar los digitos extremos
n=int(input("Introduce un numero de 5 cifras: "))
d1=n//10000                                ##Deja el primer digito suelto
d5=(n%10)*10000                            ##Deja el quinto digito suelto
dc=((n%10000)//10)*10                      ##Deja los cuatro ultimos numeros con un cero al final         
nf=d5+dc+d1                                ##Suma el quinto digito como una unidad de mil, los digitos centrales y el ultimo
print ("Al intercambiar los extremos nos da: ", nf)
#En aca hise muchos apuntes porque literal me pase un dia entero tratando de decifrarlo xddddd