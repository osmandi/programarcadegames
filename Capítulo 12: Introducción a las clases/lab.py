# Clases y gráficos

'''
Instrucciones:
    1.- Empieza un nuevo programa pygame
    2.- Justo antes de que definamos los colores, crea una clase
    llamada "Rectángulo":
        Añade los atributos x e y, loscuales serán usados para
        almacenar la posición del objet

        Crea un método "dibujar". Haz que el método cree un
        rectángulo de 10x10 en la ubicación almacenada en x e y.
        No te olvides de usar self. antes de las variables.
        El método necesitará tomar una referencia a PANTALLA, de
        forma que la función pygame.draw.rect pueda dibujar
        el rectángulo sobre la pantalla indicada

    3.- Antes del bubcle del programa, crea una variable llamada
    "miObjeto" igualándola a una instancia nueva de RECTÁNGULO

    4.- Dentro del bucle del programa, llama al método dibujar()
    de miObjeto

    5.- Comprobamos: Asgúrate de que tu programa funciona y que
    la salida se parece a la figura 33.3 (Rectángulo en la esquina
    superior izquierda)

    6.- Justo después de que el programa cree la instancia para
    RECTÁNGULO, establece los valores para x e y, en algo como
    100, 200. Vuelve a ejecutar el programa y comprueba que
    el rectángulo se ha desplazado a las nuevas coordenadas

    7.- Añade unos atributos de largo y alto a la clase. Dibuja
    el rectángulo usando esos nuevos atributos. Vuelve a ejecutar
    el programa y comprueba que funciona

    8.- Hagamos que el objeto se mueva:

        Añade los atributos para cambio_x y cambio_y

        Crea un método nuevo llamado mover(), el cual ajuste
        x e y basándose en cambio_x y cambio_y. (Observa que
        el método "mover", no necesitará "pantalla" como
        parámetro, ya que no dibuja nada sobre ella)

        Establece los valores de cambio_x y cambio_y de
        miObjeto a 2 y 2

        En el bucle principal del programa, llama al método
        mover()

        Comprueba que el objeto se mueve

    9.- Distribuye el objeto al azar:

        Importamos la biblioteca random

        Establece la localización de x como un número aleatorio
        entre 0 y 700. Hazlo dentro del bucle donde creaste
        el objeto. No vayas a hacerlo en e lugar del campo
        definido en la clase. La plantilla para laclase se crea
        una sola vez y usará los mismos números aleatorios para
        cada objeto que creemos

        Establece la localización de x como un número aleatorio
        entre 0 y 500

        Establece los valores para largo y alto como un número
        aleatoio entre 20 y 70

        Establece los valores para cambio_x y cambio_y como
        números aleatorios entre -3 y 3

        Ejecuta el programa y comprueba que se parece a la
        Figura 33.4

    10.- Crear y mostrar una lista de objetos:

        Antes del código que crea miObjeto, créate una lista vacía
        llamada miLista

        Crea un bucle for que itere 10 veces

        Coloca el código que crea miObjeto dentro del bucle for

        Adjunta (append) miObjeto a miLista

        Dentro del bucle principal, itera sobre cada objeto
        de miLista

        Llama a los métodos dibujar y mover para cada objeto
        de la lista:

            Asegúrate de que el código llama al método dibujar
            del elemento extraído por el bucle, no vayas
            a usar miObjeto.dibujar(). Este es uno de los
            errores más habituales

        Ejecuta el programa y comprueba que se parece a la
        Figura 33.5

    11.- Utiliza la herencia:

        A continuación de la clase RECTÁNGULO, crea una nueva
        clase llamada ELIPSE

        Haz que la clase RECTÁNGULO sea la clase padre de ELIPSE (meter RECTANGULO en paréntesis de ELIPSE)

        Crea un método nuevo que dibuje una elipse en lugar
        de un rectángulo

        Crea un nuevo bucle que añada 10 instancias de ELIPSE
        a miLista además de 10 rectángulos. (Utiliza dos
        bucles por separado)

        Asegúrate de no crear una nueva lista, tan solo añádelos
        a miLista

        Además, como los rectángulos y elipses fueron añadidos
        a la misma lista, solo necesitarás un bucle para
        recorrerla y dibujarlos a ambos. No cometas el error
        de tener dos bucles, uno para los rectángulos y otro para
        elipses. No funciona de esa manera

        Ejecuta el programa y comprueba que se parece a la figura 33.6

    12.- Vamos a ponerle color:

        Modifica el programa de forma que color sea un atributo
        de RECTÁNGULO

        Dibuja los rectángulos y elipses usando el nuevo color

        Dentro de los bucles for, haz que las formas tengan
        colores aleatorios. Recuerda, los colores los
        especificamos como tres números dentro de una lista,
        por ello necesitarás una lista con tres números
        aleatorios (r,v,a)

        Ejecuta el programa y comprueba que se parece a
        la figura 33.7

    13.- Inténtalo ahora con más de 10 objetos de cada tipo. La
    figura 33.8 muestra 1,000 formas

    14.- ¡Haz acabado! Enciende tu programa

'''


import pygame, sys, time, random
from pygame.locals import *

# Dibujar un rectángulo
class Rectangulo():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.ancho = 0
        self.alto = 0
        self.cambio_x = 0
        self.cambio_y = 0
        self.color = [0,0,0]

    def mover(self):
        self.x += self.cambio_x
        self.y += self.cambio_y

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, pygame.Rect (self.x, self.y, self.ancho, self.alto))

# Dibujar elipse
class Elipse(Rectangulo): # Clase Padre Rectángulo, hereda atributos y métodos

    def dibujar(self, pantalla):
        pygame.draw.ellipse(pantalla, self.color, [self.x, self.y, self.ancho, self.alto])

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
pygame.display.set_caption("Mi Primer juego en Informática")




# Se usa para establecer cuan rápido se actualiza la pantalla

reloj = pygame.time.Clock()

# Lista de objetos vacía que tendrá rectángulos y elipses
miLista = []

for i in range(1000):

    # Rectángulo
    miObjeto = Rectangulo()
    miObjeto.x = random.randint(0, 700)
    miObjeto.y = random.randint(0, 500)
    miObjeto.ancho = random.randint(20, 70)
    miObjeto.alto = random.randint(20, 70)
    miObjeto.cambio_x = random.randint(-3, 3)
    miObjeto.cambio_y = random.randint(-3, 3)
    miObjeto.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] # Colores al azar
    miLista.append(miObjeto)

for i in range(1000):

    # Elipse
    miOtroObjeto = Elipse()
    miOtroObjeto.x = random.randint(0, 700)
    miOtroObjeto.y = random.randint(0, 500)
    miOtroObjeto.ancho = random.randint(20, 70)
    miOtroObjeto.alto = random.randint(20, 70)
    miOtroObjeto.cambio_x = random.randint(-3, 3)
    miOtroObjeto.cambio_y = random.randint(-3, 3)
    miOtroObjeto.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    miLista.append(miOtroObjeto)


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

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Itera cada objetode miLista para dibujar y mover
    for objeto in miLista:
        objeto.mover()
        objeto.dibujar(pantalla)




    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()