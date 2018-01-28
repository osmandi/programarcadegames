# Importar la biblioteca math
# Esta linea se usa una sola vez y al principio del
# del programa.
from math import *

y_string = input ("Ingrese el valor del seno")  #Solicita el ingreso de un número
y = float(y_string)  #Para decirle a python que es un número, otra opción es int()

#Una simplificación es y=(float(input("Ingrese valor del seno")))

z_string = input ("Ingrese el valor del coseno")
z = float (z_string)

# Calcular x usando seno y coseno
x = sin(y) + cos(z)

print (x)
