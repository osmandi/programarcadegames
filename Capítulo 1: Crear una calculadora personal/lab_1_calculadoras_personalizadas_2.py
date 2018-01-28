'''
Crear un programa que le pregunte al usuario por la información
necesaria para encontrar el área de un trapezoide y que luego
la imprima
'''

print ("Cálculo del área de un trapezoide")
print ("Todas las varianles debe estar en metros (m)")
altura_trapezoide = float(input("Ingrese la altura del trapezoide "))
longitud_base_inferior = float(input("Ingrese longitud de la base inferior "))
longitud_base_superior = float (input("Ingrese la longitud de la base superior "))
area = (1/2)*(longitud_base_inferior + longitud_base_superior)*altura_trapezoide
print ("El área es: ", area, "m")