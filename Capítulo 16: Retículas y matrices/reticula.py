import pygame, sys, time
from pygame.locals import *



# Definimos algunos colores
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [255,255]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Primer juego en Informática")




# Se usa para establecer cuan rápido se actualiza la pantalla

reloj = pygame.time.Clock()

# Variabes
largo = 20
alto = 20
margen = 5

# --- Creamos una retícula numérica

# Creamos una lista vacía
grid = []
# Iteramos para cada fila
for fila in range(10):
    # Para cada fila, creamos una lista que
    # representará una fila completa
    grid.append([])
    # Iteramos para cada columna
    for columna in range(10):
        # Añade el número cero a la fila actual
        grid[fila].append(0)




# -------- Bucle principal del Programa -----------
while True:
    # --- Bucle principal de eventos



    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == KEYUP:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit




        if evento.type == MOUSEBUTTONDOWN:
            # Posición del ratón al hacer click
            pos = pygame.mouse.get_pos()
            columna = pos[0] // (largo+margen)
            fila = pos[1] // (alto+margen)
            grid[fila][columna] = 1
            print ("Columna: %s Fila: %s" %(fila, columna))


    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ



    for fila in range(10):
        for columna in range(10):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = VERDE
            pygame.draw.rect (pantalla, color, [(margen+largo)*columna + margen, (margen+alto)*fila + margen,largo,alto])



    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()