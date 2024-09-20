#Calcular cuantos ladrillos  entran en una pared rectangular, 
#siendo que cada ladrillo tiene una dimension de base=30 cm y altura=15 cm. 
# Esa pared tiene una puerta rectangular y ventana cuadrada
l=0.30*0.15
b=float(input("Introcuce la base de la pared: "))
h=float(input("Introduce la altura de la pared: "))
bp=float(input("Introduce la base de la puerta: "))
hp=float(input("Introduce la altura de la puerta: "))
lv=float(input("Introduce un lado de la ventana: "))
AP=(b*h)
APt=(bp*hp)
AV=lv*lv
LT=(AP-APt-AV)/l
print("Se necesitaran ",LT," ladrillos para la pared")