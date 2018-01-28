# Importamos El Motor de Juegos Blender
import bge

# Obtenemos una referencia para el objeto azul
cont = bge.logic.getCurrentController()
blue_object = cont.owner

# Imprimimos las coordenadas x,y donde se encuentra el objeto azul
print(blue_object.position[0], blue_object.position[1] )

# Cambiamos las coordenadas x,y en función de x_change e
# y_change. x_change e y_change son propiedades del juego
# asociadas al objeto azul.
blue_object.position[0] += blue_object["x_change"]
blue_object.position[1] += blue_object["y_change"]

# Comprobar si el objeto ha alcanzado un lado.
# Si es así, revertir su rumbo. Hacerlo para los cuatro lados.
if blue_object.position[0] > 6 and blue_object["x_change"] > 0:
    blue_object["x_change"] *= -1

if blue_object.position[0] < -6 and blue_object["x_change"] < 0:
    blue_object["x_change"] *= -1

if blue_object.position[1] > 6 and blue_object["y_change"] > 0:
    blue_object["y_change"] *= -1

if blue_object.position[1] < -6 and blue_object["y_change"] < 0:
    blue_object["y_change"] *= -1