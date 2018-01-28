#No se debe guardar el archivo .py con el nombre de la librería
print ("\n")
import random

#Número aleatorio entre 0 y 49
mi_numero = random.randrange(50)
print (mi_numero)

print("")

#Número aleatorio entre 100 y 200
numero = random.randrange(100,201) #El límite no se imprime
print (numero)

print ("")

#Elegir al azar un objeto de una lista
mi_lista = ["piedra","papel", "tijera"]
random_index = random.randrange(3)
print (mi_lista [random_index])

#Número aleatorio real entre 0 y 1
mi_numero = random.random()
print(mi_numero)

#Número aleatorio real entre 10 y 15
mi_numero = random.random()*5+10
print(mi_numero)

