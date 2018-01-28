#Ejercicio de Sección 1
print ("Sección 1")
'''
Haz un código que imprima lo siguiente
10
11 12
13 14 15
16 17 18 19
20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36 37
38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54
'''

variable = 9
for fila in range (9):
    for columna in range (fila+1):
        print (variable +1, end=" ")
        variable += 1
    print()

#Ejercicio de la sección 2
print ()
print ()
print ("Ejercicio de sección 2")

'''
Crea un código que solicite un número y de allí que imprima
Por ejemplo, para n = 3
oooooo
o    o
oooooo

Por ejemplo, para, n = 8
oooooooooooooooo
o              o
o              o
o              o
o              o
o              o
o              o
oooooooooooooooo
'''
'''
valor = int (input("Ingresa un número "))  #Con float no funciona
print ()
for fila in range (valor):
    for columna in range (valor*2):
        if columna >= 1 and columna < valor*2-1 and fila <= valor-2 and fila > 0:
            print (" ", end=" ")
        else:
            print ("0", end=" ")
    print ()
'''
#Ejercición Sección 3
print ()
print ()
print ("Ejercicio sección 3")
'''
Haz un códio que imprima
Por ejemplo, para = 3

1 3 5 5 3 1
3 5     5 3
5         5
5         5
3 5     5 3
1 3 5 5 3 1

Por ejemplo, para = 5

1 3 5 7 9 9 7 5 3 1
3 5 7 9     9 7 5 3
5 7 9         9 7 5
7 9             9 7
9                 9
9                 9
7 9             9 7
5 7 9         9 7 5
3 5 7 9     9 7 5 3
1 3 5 7 9 9 7 5 3 1
'''

'''
#Solicitud de número
valor = int(input ("Ingrese un número "))


#========================Lado superior=========================================

for fila in range (1,valor*2,2):  #Desde 1 hasta el valor*2 sumándose de dos en dos

#-----------------------Lado superior izquierdo--------------------------------

    for columna in range (1,valor*2,2): #Desde 1 hasta el valor*2 sumándose de dos en dos
        if columna+fila-1 > valor*2-1 : #Agregar el espacio en blanco para un número mayor que la suma de columna y fila menos 1
            print (" ", end=" ")
        elif fila == valor*2-1 and columna == valor:
            print ("Z", end=" ")
        else:
            print (columna+fila-1, end=" ")  #Al sumarse fila y columna éstas se combinan

#------------------------Lado superior derecho---------------------------------

    for columna in range (valor*2-1,0,-2): #Desde valor*2 hasta cero (Para imprimir 1) restándose de dos en dos
        if columna+fila-1 > valor*2-1 :
            print (" ", end=" ")
        else:
            print (columna+fila-1, end=" ")
    print ()

#==========================Lado inferior=======================================

for fila in range (valor*2-1,0,-2): #Desde valor*2 hasta cero (Para imprimir 1) restándose de dos en dos

#-------------------------Lado inderior izquierdo------------------------------
    for columna in range (1,valor*2,2):
        if columna+fila-1 > valor*2-1:
            print (" ", end=" ")
        else:
            print (columna+fila-1, end=" ")

#-------------------------Lado inferior derecho--------------------------------
    for columna in range (valor*2-1,0,-2):
        if columna+fila-1 > valor*2-1:
            print (" ", end=" ")
        else:
            print (columna+fila-1, end=" ")

#Fin del bucle for
    print()

'''




print()
print ()
print ("Ejercicio sección 5")
'''
Imprime una retícula dibujando cuadros verdes en un fondo negro
'''
#Nunca llamar un programa como pygame..py
#Importar la librería
import pygame

#Inicializa el motor de juegos
pygame.init()

#Las constantes se escriben en mayúsuculas
# Definir algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)

#Están escritas en mayúsculas porque son constantes, no cambian
#Si fuera un cielo que cambia por el Sol, sería en minúsuculas porque cambian

#Abrir y establecer las dimensiones de una ventana
dimensiones = (700, 500)
pantalla = pygame.display.set_mode(dimensiones)

#Establecer el título de la ventana
pygame.display.set_caption("Después de haber resuelto la sección anterior, esto es divertido")

#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Esto que indica que hemos acabado y sale de este bucle

    # Limpia la ventana y establece el color del fondo
    pantalla.fill(NEGRO)



    #Rectángulo, puerta. El primero es X, el segungo Y, el tercero Ancho, cuarto largo
    for rectangulos in range (0,700,10):
        for todo in range (0,700,10):
            pygame.draw.rect(pantalla, VERDE, [0+rectangulos,0+todo, 5, 5])




    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)



# Avanza y actualiza la pantalla con lo que hemos dibujado.
    pygame.display.flip()

pygame.quit()






