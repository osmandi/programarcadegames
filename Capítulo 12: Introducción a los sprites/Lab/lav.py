# --- Librerías ---
import pygame, sys, random
from pygame.locals import *


# --- Constantes ---
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0,255,0)


pantalla_largo = 700
pantalla_alto = 500



VELOCIDADMOVIMIENTO = 6




# --- Clases ---

class Bloque(pygame.sprite.Sprite):

    # Constructor. Pasa el color al bloque,
    # y su posición x e y
    def __init__(self, color, largo, alto):
        # Llama al constructor de la clase padre (Sprite)
        pygame.sprite.Sprite.__init__(self)

        # Crea una imagen del bloque y lo rellena de color.
        # Esto podría ser también una imagen cargada desde el disco duro.
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)

        # Obtenemos el objeto rectángulo que posee las dimensiones de la imagen
        # Actualizamos la posición de ese objeto estableciendo los valores para
        # rect.x y rect.y
        self.rect = self.image.get_rect()



class Protagonista(pygame.sprite.Sprite):

    def __init__(self, ancho, alto, color):
        pygame.sprite.Sprite.__init__(self)

        # Dimensiones
        self.image = pygame.Surface([ancho,alto])

        # Color
        self.image.fill (color)

        # Rectangulación
        self.rect = self.image.get_rect()

        # Posicición inicial
        self.rect.x = pantalla_largo // 2
        self.rect.y = pantalla_alto - ancho


        self.moverseIzquierda = False
        self.moverseArriba = False
        self.moverseDerecha = False
        self.moverseAbajo = False

        self.ancho = ancho
        self.alto = alto

        self.puntuacion_maxima = 0

    def update(self):
        """ Actualiza la posición del protagonista. """

        # Mover al jugador
        if self.moverseAbajo and self.rect.bottom < pantalla_alto:
            self.rect.y += VELOCIDADMOVIMIENTO
        if self.moverseArriba and self.rect.top > 0:
            self.rect.y -= VELOCIDADMOVIMIENTO
        if self.moverseIzquierda and self.rect.x > 0:
            self.rect.x -= VELOCIDADMOVIMIENTO
        if self.moverseDerecha and (self.rect.x + self.ancho) < pantalla_largo:
            self.rect.x += VELOCIDADMOVIMIENTO




class Juego():

    def __init__(self):


        """ Esta clase es la instancia del juego"""
        self.puntuacion = 0
        self.game_over = False

        # Lista de sprites
        self.bloque_lista_buenos = pygame.sprite.Group()
        self.bloque_lista_malos = pygame.sprite.Group()
        self.listade_todoslos_sprites = pygame.sprite.Group()

        # Bloques de sprites buenos
        for i in range(50):

            bloque = Bloque(VERDE, 20, 15)

            # Establecemos una ubicación aleatoria para el bloque
            bloque.rect.x = random.randrange(pantalla_largo - 20)
            bloque.rect.y = random.randrange(pantalla_alto - 20)

            # Añadimos el  bloque a la lista de objetos
            self.bloque_lista_buenos.add(bloque)
            self.listade_todoslos_sprites.add(bloque)


        # Bloques de sprites malos
        for i in range(50):

            bloque = Bloque(ROJO, 20, 15)

            # Establecemos una ubicación aleatoria para el bloque
            bloque.rect.x = random.randrange(pantalla_largo - 20)
            bloque.rect.y = random.randrange(pantalla_alto - 20)

            # Añadimos el  bloque a la lista de objetos
            self.bloque_lista_malos.add(bloque)
            self.listade_todoslos_sprites.add(bloque)


        # Creamos un bloque protagonista
        self.protagonista = Protagonista(20, 15, NEGRO)
        self.listade_todoslos_sprites.add(self.protagonista)

        # Golpear bloques malos
        self.bloque_malo = pygame.mixer.Sound("bad_block.wav")

        # Golpear bloque bueno
        self.bloque_bueno = pygame.mixer.Sound("good_block.wav")




    def procesos_de_eventos(self):
        """ Procesa todos los eventos, devuelve TRUE si precisamos salir de la ventana"""

        for evento in pygame.event.get(): # El usuario hizo algo

            if evento.type == QUIT: # Si el usuario pulsó salir
                pygame.quit()
                sys.exit()



            # Control de movimiento del protagonista
            # Al presionar una tecla
            if evento.type == KEYDOWN:
                # Cambiar las variables del teclado
                if evento.key == K_LEFT or evento.key == ord('a'):
                    self.protagonista.moverseDerecha = False
                    self.protagonista.moverseIzquierda = True
                if evento.key == K_RIGHT or evento.key == ord ('d'):
                    self.protagonista.moverseDerecha = True
                    self.protagonista.moverseIzquierda = False
                if evento.key == K_UP or evento.key == ord ('w'):
                    self.protagonista.moverseAbajo = False
                    self.protagonista.moverseArriba = True
                if evento.key == K_DOWN or evento.key == ord ('s'):
                    self.protagonista.moverseAbajo = True
                    self.protagonista.moverseArriba = False


            # Al soltar una tecla
            if evento.type == KEYUP:

                if evento.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if evento.key == K_LEFT or evento.key == ord ('a'):
                    self.protagonista.moverseIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord ('d'):
                    self.protagonista.moverseDerecha = False
                if evento.key == K_UP or evento.key == ord ('w'):
                    self.protagonista.moverseArriba = False
                if evento.key == K_DOWN or evento.key == ord ('s'):
                    self.protagonista.moverseAbajo = False


            if evento.type == MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()






    def logica_de_ejecucion(self):
        """ Este método ejecuta cada fotograma. Actualiza posiciones y comprueba colisiones"""

        if not self.game_over:

            # Mueve todos los sprites
            self.listade_todoslos_sprites.update()



            # Observa si el bloque protagonista ha colisionado con bueno
            lista_impactos_bloques_buenos = pygame.sprite.spritecollide(self.protagonista, self.bloque_lista_buenos, True)



            # Observea si el bloque protagonista ha colisionado con malo
            lista_impactos_bloques_malos = pygame.sprite.spritecollide(self.protagonista, self.bloque_lista_malos, True)


            # Comprobamos la lista de colisiones buenos
            for bloque in lista_impactos_bloques_buenos:
                self.puntuacion -= 1
                self.bloque_bueno.play()
                print( self.puntuacion )

            # Comprobamos la lista de colisiones malos
            for bloque in lista_impactos_bloques_malos:
                self.puntuacion += 1
                self.bloque_malo.play()
                print( self.puntuacion )

            if len(self.bloque_lista_malos) == 0:
                self.game_over = True



    def display_frame(self, pantalla):
        """ Muestra todo el juego sobre la pantalla"""
        pantalla.fill (BLANCO)




        if self.game_over:
            fuente = pygame.font.SysFont("serif", 25)
            texto = fuente.render("Game Over, haz click para volver a jugar", True, NEGRO)
            centrar_x = (pantalla_largo // 2) - (texto.get_width() // 2)
            centrar_y = (pantalla_alto // 2) - (texto.get_height() // 2)
            pantalla.blit (texto, [centrar_x, centrar_y])
            puntuacion = fuente.render("Tu puntuación fue de "+ str(self.puntuacion), True, ROJO)
            centrar_y_puntuacion = centrar_y + 30
            centrar_x_puntuacion = centrar_x + 90
            pantalla.blit(puntuacion, [centrar_x_puntuacion, centrar_y_puntuacion])






        if not self.game_over:

            # Dibujamos todos los sprites
            self.listade_todoslos_sprites.draw(pantalla)
            fuente2 = pygame.font.SysFont("serif", 40)
            marcador = fuente2.render("SCORE: " + str(self.puntuacion), True, NEGRO)
            pantalla.blit(marcador, [0, 0])


        # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()




def main():
    """ Función principal del programa"""
    # Inicializamos Pygame
    pygame.init()

    # Crear ventana de juego
    pantalla=pygame.display.set_mode([pantalla_largo, pantalla_alto])
    pygame.display.set_caption('Captura cuadritos')

    # Ocultamos el puntero del ratón
    pygame.mouse.set_visible(False)

    #  Se usa para establecer cuan rápido se actualiza la pantalla
    reloj = pygame.time.Clock()

    # Instancia del juego
    juego = Juego()



    # Bucle principal
    while True:
        #Procesa los eventos
        juego.procesos_de_eventos()

        # Actualizza las posiciones de los objetos
        juego.logica_de_ejecucion()



        # Dibuja el fotograma actual
        juego.display_frame(pantalla)

        # Limitamos a 20 fotogramas por segundo
        reloj.tick(30)

    # Cierra la ventana y sale
    pygame.quit()


if __name__ == "__main__":
    main()