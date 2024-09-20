#Dado un numero que represente en dia de la semana, mostrar su correspondiente literal
dia=int(input("Introducir numero de dia de la semana: "))
if dia==1:
    print("LUNES")
elif dia==2:
    print("MARTES")
elif dia==3:
    print("MIERCOLES")
elif dia==4:
    print("JUEVES")
elif dia==5:
    print("VIERNES")
elif dia==6:
    print("SABADO")
elif dia==7:
    print("DOMINGO")
else:
    print("Solo hay 7 dias en una semana")