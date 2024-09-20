#Debe calcular la nota de un alumno de inf111, dado que el primer parcial se saco 80/100, el segundo 51/100 y el tercer 65/100. 
#Cada parcial se debe ponderar de la siguiente forma: 
#Primer parcial sobre 25, segundo sobre 30, y el tercer sobre 35, 10 practicas. Mostrar nota final:
p1=int(input("Introducir resultado del primer parcial: "))
p2=int(input("Introcucir resultado del segundo parcial: "))
p3=int(input("Introcucir resultado del tercer parcial: "))
n1=p1*0.25
n2=p2*0.30
n3=p3*0.35
nf=10+n1+n2+n3
print("Su nota total es de" ,nf)