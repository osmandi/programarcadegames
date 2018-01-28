'''
 Animating multiple objects using a list.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Vídeo explicativo: http://youtu.be/Gkhz3FuhGoI
'''
# Importamos las bibliotecas llamadas 'pygame' y 'random'.
import pygame
import random

# Inicializamos el motor de juegos.
pygame.init()

NEGRO = (0, 0, 0)
BLANCO = [255, 255, 255]

# Establecemos el largo y ancho de la pantalla.
dimensiones = [400, 400]

pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Está Nevando")

reloj = pygame.time.Clock()

# Iteramos hasta que el usuario haga click sobre le botón de salida.
hecho = False
while not hecho:

    for evento in pygame.event.get():  # El usuario realizó alguna acción.
        if evento.type == pygame.QUIT: # Si el usuario hizo click sobre salir.
            hecho = True # Marcamos que hemos acabado y abandonamos este bucle.

    # Establecemos el color de fondo.
    # ------------------- alfo ----------------------------
    pantalla.fill(NEGRO)

    # Avanzamos y actualizamos con lo que hemos dibujado.
    pygame.display.flip()
    reloj.tick(60)

# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
pygame.quit ()