
"""
Crea un programa que haga o siguiente:
    1:
        Deberás crear al menos dos funciones distintas que dibujen
        un objeto sobre la pantalla. Por ejemplo, dibujar_ave y
        dibujar_árbol. No te vayas dibujar un hombre en palillos,
        eso ya lo hicimos. Crea tu propia figura original. Si ya
        te habías creado tu propio dibujo en el laboratorio
        "Creamos una imagen", puedes adaptarlo perfectamente a este
        laboratorio.

    2:
        Ya en el capítulo 11 tratamos sobre el desplazamiento de
        gráficos usando  el teclado, el mando de juegos y el ratón.
        Escoge dos de ellos para controlar dos objetos diferentes
        sobre la pantalla.

    3:
        En el caso de que escogieras el mando y el teclado,
        asegúrate de poner los controles necesarios para comprobar
        que tu objeto no se salga de la pantalla y se pierda.
"""


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
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)

# Título del programa
pygame.display.set_caption("Mandos de juegos y gráficos")

# Establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# Condición del bucle
hecho = False



# Ocultar el cursor del ratón
pygame.mouse.set_visible(False)

# Velocidad en píxeles por fotograma
x_speed = 0
y_speed = 0
# Posición actual
x_coord = 600
y_coord = 400

"""
Dibujos

------------------------ Círculo --------------------------------------
X y Y, radio
pygame.draw.circle(pantalla, NEGRO, [60, 250], 40)

-------------------- Triángulo --------------------------------------
X y Y del punto inferior a la izquierta, del punto superior y del punto inferior derecho
pygame.draw.polygon(pantalla, NEGRO, [[300, 100], [50, 300],[550, 300]])

-------------------------- Rectángulo -------------------------------------
Rectángulo. El primero es X, el segungo Y, el tercero Ancho, cuarto largo
pygame.draw.rect(pantalla, ROJO, [250, 400, 100, 200])

------------------------------ Elipse --------------------------------------
X y Y, ancho y largo de un rectángulo para dibujar bordes
pygame.draw.ellipse(pantalla, NEGRO, [20, 20, 250, 100], 2)

---------------------- Arcos para formar una elipse -------------------------
Dibujamos un arco como parte de una elipse. Usamos radianes para determinar qué ángulo tenemos que dibujar.
pygame.draw.arc(pantalla, NEGRO, [20, 220, 250, 200], 0, PI / 2, 2)
pygame.draw.arc(pantalla, VERDE, [20, 220, 250, 200], PI / 2, PI, 2)
pygame.draw.arc(pantalla, AZUL, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
pygame.draw.arc(pantalla, ROJO, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)


------------------------- Texto -------------------------------------
Elegimos que tipo de fuente usar; fuente por defecto, y de 25 puntos.
fuente = pygame.font.Font(None, 25)

Creamos el texto. "True" significa texto con antialiasing.
El color es negro. Esto nos crea una imagen de las letras, pero no las coloca sobre la pantalla.
texto = fuente.render("Mi texto", True, NEGRO)

X y Y de la posición del texto
pantalla.blit(texto, [250, 250])

 ------- -------------- Línea --------------------------------------------
X y Y del punto del comienzo y X y Y del fin
pygame.draw.line(pantalla, VERDE, [0, 0], [100, 100], 5)
"""

# Primera función, para dibujar un ave manippulado co mouse
def dibujar_ave (pantalla, x, y):
    # Cabeza
    pygame.draw.circle(pantalla, NEGRO, [x, y], 12)

    # Ala derecha
    pygame.draw.line (pantalla, AZUL, [x-18,y-3], [x+3,y-30],5)

    # Cuerpo
    pygame.draw.ellipse (pantalla, NEGRO, [x-40, y-3, 40, 20])

    # Pico
    pygame.draw.polygon (pantalla, AZUL, [[10+x,2+y],[x,5+y],[15+x,20+y]])

    # Ala izquierda
    pygame.draw.line (pantalla, AZUL, [x-20,y-3],[x-40,y-20],5)

    # Ojo
    pygame.draw.circle (pantalla, BLANCO, [x,y-3], 3)

# Segunda función, para dibujar un árbol manipulado con teclado
def dibujar_arbol (pantalla,x_coord,y_coord):
    # Tallo
    pygame.draw.rect(pantalla, VIOLETA, [x_coord-10,y_coord, 50, 100])

    # Hojas
    pygame.draw.circle (pantalla, VERDE, [x_coord+20,y_coord], 40)
    pygame.draw.circle (pantalla, VERDE, [x_coord+40,y_coord+20], 40)
    pygame.draw.circle (pantalla, VERDE, [x_coord-10,y_coord+20], 40)



# Segunda función para dibujar un árbol



# Evento pygame.KEYDOWN es generado al presionar una tecla
# Evento pygame.KEYUP es generado al soltar una tecla

# ----------------------- Bucle principal del programa-------
while not hecho:
    # -------- Bucle principal de eventos ---------------
    # Cerrar la pantalla de pygame al presionar en la x
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

        # El ususario pulsa una tecla
        if evento.type == pygame.KEYDOWN:
            # Resuelve que ha sido una tecla flecha, por que ajusta
            # su velocidad
            if evento.key == pygame.K_LEFT:
                x_speed = -3
            if evento.key == pygame.K_RIGHT:
                x_speed = 3
            """
            if evento.key == pygame.K_UP:
                y_speed = -3
            if evento.key == pygame.K_DOWN:
                y_speed = 3
            """

        # El ususario suelta una tecla
        if evento.type == pygame.KEYUP:
            # Si se trata de una tecla flecha devuelve el vector a
            # cero
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            if evento.key == pygame.K_RIGHT:
                x_speed = 0
            """
            if evento.key == pygame.K_UP:
                y_speed = 0
            if evento.key == pygame.K_DOWN:
                y_speed = 0
            """

    # ------------ Lógica del juego -------------------------
    # Mueve el objeto de acuerdo a la velocidad del vector
    x_coord += x_speed
    y_coord += y_speed

    # Para que retorne el árbol

    if x_coord >= 701:
        x_coord = 1
    if x_coord <= -100:
        x_coord = 700




    # Controlar un objeto vía ratón
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # Para que no traspase los límites el ave
    if y >= 470:
        y = 470
    if y <= 25:
        y = 25
    if x >= 670:
        x=670
    if x <= 45:
        x=45

    # -------------- Código de dibujo -----------------------
    # Limpiar la pantalla con su color de fondo
    pantalla.fill(BLANCO)
    #


    # Dibujar árbol
    dibujar_arbol (pantalla,x_coord,y_coord)

    # Dibujar ave
    dibujar_ave (pantalla, x, y)

    #
    # ------------ Actualizar la pantalla con lo dibujado ---
    pygame.display.flip()
    # ------------- Limitamos a 60 fotogramas por segundo ---
    reloj.tick(60)

# Para que se cierre la ventna sin colgar el programa
pygame.quit()