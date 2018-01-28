"""
- Utilizar múltiples colores.
Hacer un dibujo coherente. No me interesa el arte abstracto de formas
aleatorias.

- Utilizar múltiples tipos de funciones gráficas (por ejemplo; círculos,
rectángulos, líneas, etc.)

- Utilizar, ya sea un bucle while, o uno for, para crear un patrón repetitivo.
No vayas a dibujar lo mismo, en el mismo sitio, diez veces. Deberías emplear
esa variable índice para que actúe como valor que sirva para desplazar lo que
estés dibujando. Recuerda que puedes poner diversos comandos de dibujo dentro
del bucle, de forma que podrías dibujar, por ejemplo, varios vagones de un tren
"""

#Importar la librería pygame
import pygame

#Inicializar el motor de juegos
pygame.init()

#Definiendo colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

#Definir valor de pi si se va a realizar un círculo
PI = 3.141593

#Establecer el ancho y largo de la pantall
dimensiones = (600, 600)
pantalla = pygame.display.set_mode(dimensiones)

#Título del programa
pygame.display.set_caption("Creando mi primera pantalla de juegos")

#Definiendo valores para el bucle
hecho = False
reloj = pygame.time.Clock()

#Iteramos hasta que hecho == True

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  #Si el usuario presiona salir
            hecho = True
    #Limpiando fondo de pantalla en azul, cielo
    pantalla.fill(AZUL)
    #Tierra
    pygame.draw.rect(pantalla, VERDE, [0, 500, 600,600] )


    #Desde aquí colocar todo los gráficos
    #Triángulo negro, techo
    pygame.draw.polygon(pantalla, NEGRO, [[300, 100], [50, 300],[550, 300]])
    #Rectángulo blanco, pared
    pygame.draw.rect(pantalla, BLANCO, [50, 300, 500, 300])


    #Rectángulo, puerta. El primero es X, el segungo Y, el tercero Ancho, cuarto largo
    pygame.draw.rect(pantalla, ROJO, [250, 400, 100, 200])
    #Manilla
    pygame.draw.rect(pantalla, NEGRO, [330, 490,20, 20])
    #Ventana
    pygame.draw.rect(pantalla, NEGRO, [100, 400, 50, 50], 3)
    #Rejillas de ventanas
    pygame.draw.line(pantalla, NEGRO, [100, 425], [150, 425], 3)
    pygame.draw.line(pantalla, NEGRO, [125, 400], [125, 450], 3)


    #Actualizar pantalla, después de todos los gráficos
    pygame.display.flip()
    #Limitar el bucle while a un máximo de 60 fotogramas por segundo
    reloj.tick(60)

#Obligatorio colocar para un cierre correcto de pygame
pygame.quit()