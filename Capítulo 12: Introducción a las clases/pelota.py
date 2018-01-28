# Importamos las bibliotecas llamadas 'pygame' y 'random'.
import pygame
import random


# Inicializamos el motor de juegos.
pygame.init()

NEGRO = (0, 0, 0)
ALGO = (200,29,81)
COLORPELOTA = (255, 255, 255)

# Establecemos el largo y ancho de la pantalla.
dimensiones = [400, 400]

pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Pelota con class")


class Pelota():

    def __init__(self):
        # Atributos de la clases, siempre van antes que los métodos
        # Posición de la pelota
        self.x = 0
        self.y = 0

        # Vector pelota
        self.cambio_x = 0
        self.cambio_y = 0

        # Dimensiones de la pelota
        self.talla = 10

        # Color de la pelota
        self.color = [COLORPELOTA]

    # --- Métodos para la clase ----
    def mover(self):
        self.x += self.cambio_x
        self.y += self.cambio_y

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.x, self.y), self.talla)





reloj = pygame.time.Clock()


# Debe ir fuera del bucle principal
laPelota = Pelota()
laPelota.x = 100
laPelota.y = 100
laPelota.cambio_x = 5
laPelota.cambio_y = 1
laPelota.color = (COLORPELOTA)

# Iteramos hasta que el usuario haga click sobre le botón de salida.
while True:

    for evento in pygame.event.get():  # El usuario realizó alguna acción.
        if evento.type == pygame.QUIT: # Si el usuario hizo click sobre salir.
            pygame.quit()
            sys.exit()

    # Establecemos el color de fondo.
    pantalla.fill(ALGO)


    # Moverá y dibujará la pelota
    laPelota.mover()
    laPelota.dibujar(pantalla)


    # Avanzamos y actualizamos con lo que hemos dibujado.
    pygame.display.update()
    reloj.tick(40)

# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
pygame.quit ()