# Importamos la librería de pygame
import pygame

# Iniciamos pygame
pygame.init()

# Definimos algunos colores
NEGRO = [0, 0, 0]
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VIOLETA = (98,0,255)



# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [400, 500]
pantalla = pygame.display.set_mode(dimensiones)

# Título del programa
pygame.display.set_caption("Mandos de juegos y gráficos")


# Establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# Condición del bucle
hecho = False

def dibuja_hombrepalitos(pantalla, x, y):
    # Cabeza
    pygame.draw.ellipse(pantalla, NEGRO, [96 - 95 + x, 83 - 83 + y, 10, 10], 0)

    # Piernas
    pygame.draw.line(pantalla, NEGRO, [100 - 95 + x, 100 - 83 + y], [105 - 95 + x, 110 - 83 + y], 2)
    pygame.draw.line(pantalla, NEGRO, [100 - 95 + x, 100 - 83 + y], [95 - 95 + x, 110 - 83 + y], 2)

    # Cuerpo
    pygame.draw.line(pantalla, ROJO, [100 - 95 + x, 100 - 83 + y], [100 - 95 + x, 90 - 83 + y], 2)

    # Brazos
    pygame.draw.line(pantalla, ROJO, [100 - 95 + x, 90 - 83 + y], [104 - 95 + x, 100 - 83 + y], 2)
    pygame.draw.line(pantalla, ROJO, [100 - 95 + x, 90 - 83 + y], [96 - 95 + x, 100 - 83 + y], 2)

# Función para dibujar hombre de nieve
def dibujar_hombredenieve(pantalla, x, y):
    # Dibuja un círculo para la cabeza
    pygame.draw.ellipse(pantalla,BLANCO, [35 + x, 0 + y, 25, 25])
    # Dibuja un círculo para la parte central del hombre
    pygame.draw.ellipse( pantalla,BLANCO, [23 + x, 20 + y, 50, 50])
    # Dibuja un círculo para la parte baja del hombre
    pygame.draw.ellipse( pantalla,BLANCO, [0 + x, 65 + y, 100, 100])


# Ocultar el cursor del ratón
pygame.mouse.set_visible(False)


# ----------------------- Bucle principal del programa-------
while not hecho:
    # -------- Bucle principal de eventos ---------------
    # Cerrar la pantalla de pygame al presionar en la x
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
    # ------------ Lógica del juego -------------------------
    # Controlar un objeto vía ratón
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    #

    #
    #
    # -------------- Código de dibujo -----------------------
    # Limpiar la pantalla con su color de fondo
    pantalla.fill(BLANCO)
    # Dibujos
    #
    dibuja_hombrepalitos (pantalla, x, y)


    #
    # ------------ Actualizar la pantalla con lo dibujado ---
    pygame.display.flip()
    # ------------- Limitamos a 60 fotogramas por segundo ---
    reloj.tick(60)

# Para que se cierre la ventna sin colgar el programa
pygame.quit()