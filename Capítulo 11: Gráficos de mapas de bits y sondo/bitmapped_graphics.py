"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/4YqIKncMJNs
 Explanation video: http://youtu.be/ONAK8VZIcI4
 Explanation video: http://youtu.be/_6c4o41BIms
"""

import pygame

# Definimos algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Inicializamos
pygame.init()

# Creamos una pantalla de 800x600.
pantalla = pygame.display.set_mode([800, 600])

# Establecemos el nombre de la ventana.
pygame.display.set_caption('CMSC 150 es divertido')

reloj = pygame.time.Clock()

# Antes del bucle cargamos el sonido del disparo
sonido_click = pygame.mixer.Sound("click.wav")

# Establecemos la posición de los gráficos
posicion_base = [0, 0]

# Fondo
imagen_de_fondo = pygame.image.load("saturn_family1.jpg").convert()

# Nave
imagen_personaje = pygame.image.load("player.png").convert()

# Quitar fondo negro de la nave
imagen_personaje.set_colorkey(NEGRO)

# Ocultar el cursor del ratón
pygame.mouse.set_visible(False)

hecho = False

while not hecho:
    reloj.tick(10)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        # Sonido del disparo al presionar clic
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            sonido_click.play()

    # Fondo de pantalla
    pantalla.blit(imagen_de_fondo, posicion_base)

    # Obtiene la posición actual del ratón. Devuelve ésta como
    # una lista de dos números.
    posicion_del_personaje = pygame.mouse.get_pos()
    x = posicion_del_personaje[0]
    y = posicion_del_personaje[1]

    # Imagen de la nave
    pantalla.blit(imagen_personaje, [x, y])


    pygame.display.flip()

pygame.quit()