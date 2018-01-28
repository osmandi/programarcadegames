"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

De:
http://programarcadegames.com/python_examples/f.php?file=plataforma_scroller.py

Vídeo explicativo: http://youtu.be/QplXBw_NK5Y

Parte de la serie:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=plataforma_saltarer.py
http://programarcadegames.com/python_examples/f.php?file=plataforma_scroller.py
http://programarcadegames.com/python_examples/f.php?file=plataforma_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""

import pygame

"""
Constantes globales
"""

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

#  Dimensiones de la pantalla
LARGO_PANTALLA  = 800
ALTO_PANTALLA = 600

class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa la barra inferior que controla el protagonista. """

    # -- Atributos
    # Establecemos el vector velocidad del protagonista
    cambio_x = 0
    cambio_y = 0

     # Lista de todos los sprites contra los que podemos botar
    nivel = None

    # -- Métodos
    def __init__(self):
        """ Función Constructor"""

        # Llama al constructor padre
        pygame.sprite.Sprite.__init__(self)

         # Crea una imagen del bloque y lo rellena con color rojo.
        # También podríamos usar una imagen guardada en disco
        largo = 40
        alto = 60
        self.image = pygame.Surface([largo, alto])
        self.image.fill(ROJO)

        # Establecemos una referencia hacia la imagen rectangular.
        self.rect = self.image.get_rect()

    def update(self):
        """  Desplazamos al protagonista.   """
        # Gravedad
        self.calc_grav()

        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado
            # izquierdo del objeto que hemos tocado
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right

        # Desplazar arriba/izquierda
        self.rect.y += self.cambio_y

        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:

            #Restablecemos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom

            # Detenemos nuestro movimiento vertical
            self.cambio_y = 0

    def calc_grav(self):
        """ Calculamos el efecto de la gravedad.  """
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35

        #Observamos si nos encontramos sobre el suelo.
        if self.rect.y >= ALTO_PANTALLA - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height

    def saltar(self):
        """ Llamado cuando el usuario pulsa el botón de 'saltar'. """

        # Descendemos un poco y observamos si hay una plataforma debajo nuestro.
        # Descendemos 2 píxels (con una plataforma que está  descendiendo, no funciona bien
    # si solo descendemos uno).
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2

        # Si está listo para saltar, aumentamos nuestra velocidad hacia arriba
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA:
            self.cambio_y = -10

    #  Movimiento controlado por el protagonista:
    def ir_izquierda(self):
        """ Es llamado cuando el usuario pulsa la flecha izquierda  """
        self.cambio_x = -6

    def ir_derecha(self):
        """ Es llamado cuando el usuario pulsa la flecha derecha  """
        self.cambio_x = 6

    def stop(self):
        """ Es llamado cuando el usuario abandona el teclado """
        self.cambio_x = 0

class Plataforma(pygame.sprite.Sprite):
    """ Plataforma sobre la que el usuario puede saltar """

    def __init__(self, largo, alto ):
        """ Constructor Plataforma.Asume su construcción cuando el usuario le haya pasado
            un array de 5 números, tal como se ha definido al principio de este código.. """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([largo, alto])
        self.image.fill(VERDE)

        self.rect = self.image.get_rect()

class Nivel():
    """ Esta es una super clase genérica usada para definir un nivel.
        Crea una clase hija para cada nivel con una info específica. """

    def __init__(self, protagonista):
        """ Constructor.  Requerido para cuando las plataformas
            que se desplazan colisionan con el protagonista. """
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista


        # Cuán lejos se ha desplazado a la izquierda/derecha el escenario
        self.desplazar_escenario = 0

    # Actualizamos todo en este nivel
    def update(self):
        """ Actualizamos todo en este nivel."""
        self.listade_plataformas.update()
        self.listade_enemigos.update()

    def draw(self, pantalla):
        """ Dibujamos todo en este nivel. """

        # Dibujamos el fondo
        pantalla.fill(AZUL)

        # Dibujamos todas las listas de sprites que tengamos
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos.draw(pantalla)

    def escenario_desplazar(self, desplazar_x):
        """ Para cuando el usuario se desplaza a la izquierda/derecha y necesitamos mover
        todo: """

        # Llevamos la cuenta de la cantidad de desplamiento
        self.desplazar_escenario += desplazar_x

        # Iteramos a través de todas las listas de sprites y desplazamos
        for plataforma in self.listade_plataformas:
            plataforma.rect.x += desplazar_x

        for enemigo in self.listade_enemigos:
            enemigo.rect.x += desplazar_x

# Creamos las plataformas para el nivel
class Nivel_01(Nivel):
    """ Definición para el nivel 1. """

    def __init__(self, protagonista):
        """ Creamos el nivel 1. """

        # Llamamos al constructor padre
        Nivel.__init__(self, protagonista)

        self.limitedel_nivel = -1000

        # Array con el largo, alto, x, e y de la plataforma
        nivel = [ [210, 70, 500, 500],
                  [210, 70, 800, 400],
                  [210, 70, 1000, 500],
                  [210, 70, 1120, 280],
                  ]


        # Iteramos a través del array anterior y añadimos plataformas
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(bloque)

# Creamos las plataformas para el nivel
class Nivel_02(Nivel):
    """ Definición para el nivel 2. """

    def __init__(self, protagonista):
        """ Creamos el nivel 1. """

        # Llamamos al constructor padre
        Nivel.__init__(self, protagonista)

        self.limitedel_nivel = -1000

        # Array con el largo, alto, x, e y de la plataforma
        nivel = [ [210, 30, 450, 570],
                  [210, 30, 850, 420],
                  [210, 30, 1000, 520],
                  [210, 30, 1120, 280],
                  ]


        # Iteramos a través del array anterior y añadimos plataformas
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(bloque)

def main():
    """ Programa Principal """
    pygame.init()

    # Establecemos el alto y largo de la pantalla
    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA]
    pantalla = pygame.display.set_mode(dimensiones)

    pygame.display.set_caption("Side-scrolling Plataformer")

    # Creamos al protagonista
    protagonista = Protagonista()

    # Creamos todos los niveles
    listade_niveles = []
    listade_niveles.append(Nivel_01(protagonista))
    listade_niveles.append(Nivel_02(protagonista))

    # Establecemos el nivel actual
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]

    listade_sprites_activas = pygame.sprite.Group()
    protagonista.nivel = nivel_actual

    protagonista.rect.x = 340
    protagonista.rect.y = ALTO_PANTALLA - protagonista.rect.height
    listade_sprites_activas.add(protagonista)

    #Iteramos hasta que el usuario hace click sobre el botón de salir.
    hecho = False

    # Usado para gestionar cuán rápido se actualiza la pantalla.
    reloj = pygame.time.Clock()

    # -------- Bucle Principal del Programa  -----------
    while not hecho:
        for evento in pygame.event.get(): # El usuario realizó alguna acción
            if evento.type == pygame.QUIT: #Si el usuario hizo click en salir
                hecho = True # Marcamos como hecho y salimos de este bucle

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    protagonista.ir_izquierda()
                if evento.key == pygame.K_RIGHT:
                    protagonista.ir_derecha()
                if evento.key == pygame.K_UP:
                    protagonista.saltar()

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and protagonista.cambio_x < 0:
                    protagonista.stop()
                if evento.key == pygame.K_RIGHT and protagonista.cambio_x > 0:
                    protagonista.stop()

        # Actualizamos al protagonista.
        listade_sprites_activas.update()

        # Actualizamos los objetos en el nivel
        nivel_actual.update()

        # Si el protagonista se aproxima al borde derecho, desplazamos el escenario a la izquierda(-x)
        if protagonista.rect.x >= 500:
            diff = protagonista.rect.x - 500
            protagonista.rect.x = 500
            nivel_actual.escenario_desplazar(-diff)

        # Si el protagonista se aproxima al borde izquierdo, desplazamos el escenario a la derecha(+x)
        if protagonista.rect.x <= 120:
            diff = 120 - protagonista.rect.x
            protagonista.rect.x = 120
            nivel_actual.escenario_desplazar(diff)

        # Si el protagonista alcanza el final del nivel, pasa al siguiente
        posicion_actual = protagonista.rect.x + nivel_actual.desplazar_escenario
        if posicion_actual < nivel_actual.limitedel_nivel:
            protagonista.rect.x = 120
            if nivel_actual_no < len(listade_niveles)-1:
                nivel_actual_no += 1
                nivel_actual = listade_niveles[nivel_actual_no]
                protagonista.nivel = nivel_actual

        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
        nivel_actual.draw(pantalla)
        listade_sprites_activas.draw(pantalla)

        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

        # Limitamos a 60 fps
        reloj.tick(60)

        # Avanzamos y actualizamos la pantalla que ya hemos dibujado
        pygame.display.flip()

    # Pórtate bien con el IDLE. Si olvidas esta línea, el programa se 'colgará'
    # al salir.
    pygame.quit()

if __name__ == "__main__":
    main()