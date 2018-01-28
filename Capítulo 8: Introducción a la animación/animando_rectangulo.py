"""
 Mostramos como usar un sprite respaldado por un gráfico.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Vídeo explicativo: http://youtu.be/vRB_983kUMc
"""

#La animación ocurre al modificar una variable en el bucle

import pygame


# Definimos algunos colores
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Movimiento de rectángulo")

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.

hecho = False

# --- Desplazamiento del rectángulo
rect_x = 50
rect_y = 50

# --- Velocidad y rumbo del rectángulo
rect_cambio_x = 3
rect_cambio_y = 3

# Se usa para establecer cuan rápido se actualiza la pantalla

reloj = pygame.time.Clock()

# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)


    # Dibuja un rectángulo rojo dentro del blanco
    pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(pantalla, ROJO, [rect_x + 10, rect_y + 10 , 30, 30])

    # --- Desplazar el rectángulo en el eje x
    #rect_x += 1

    #.--- Desplazar el rectángulo en el eje y
    #rect_y += 1

    # --- Otra manera de especificar cambio de la posición
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y

    # --- Rebota el rectángulo si es necesario
    if rect_y > 450 or rect_y < 0: #Los otros 50 px son el tamaño del rectángulo
        rect_cambio_y = rect_cambio_y* -1
    if rect_x > 650 or rect_x < 0:
        rect_cambio_x = rect_cambio_x * -1

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()

#