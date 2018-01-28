# Importamos la librería de pygame
import pygame

# Iniciamos pygame
pygame.init()

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VIOLETA = (98,0,255)



# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)

# Título del programa
pygame.display.set_caption ("Mandos de juegos y gráficos")


# Establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# Condición del bucle
hecho = False



# ----------------------- Bucle principal del programa-------
while not hecho:
    # -------- Bucle principal de eventos ---------------
    # Cerrar la pantalla de pygame al presionar en la x
    for evento in pygame.event.get():
        if evento.type == pygame.quit():
            hecho = True
    # ------------ Lógica del juego -------------------------
    #
    #
    #
    #
    #
    # -------------- Código de dibujo -----------------------
    # Limpiar la pantalla con su color de fondo
    pantalla.fill(NEGRO)
    #
    #
    #
    #
    # ------------ Actualizar la pantalla con lo dibujado ---
    pygame.display.flip()
    # ------------- Limitamos a 60 fotogramas por segundo ---
    reloj.tick(60)

# Para que se cierre la ventna sin colgar el programa
pygame.quit()