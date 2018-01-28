#Nunca llamar un programa como pygame..py
#Importar la librería
import pygame

#Inicializa el motor de juegos
pygame.init()

#Las constantes se escriben en mayúsuculas
# Definir algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)

#Están escritas en mayúsculas porque son constantes, no cambian
#Si fuera un cielo que cambia por el Sol, sería en minúsuculas porque cambian

#Abrir y establecer las dimensiones de una ventana
dimensiones = (700, 500)
pantalla = pygame.display.set_mode(dimensiones)

#Establecer el título de la ventana
pygame.display.set_caption("Super Juego del Profesor Craven")

#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Esto que indica que hemos acabado y sale de este bucle
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO


    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO


    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

#Muestra de bucle de eventos - Correcto
for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        print("El usuario solicitó salir.")
    elif evento.type == pygame.KEYDOWN:
        print("El usuario presionó una tecla.")
    elif evento.type == pygame.KEYUP:
        print("El usuario soltó una tecla.")
    elif evento.type == pygame.MOUSEBUTTONDOWN:
        print("El usuario presionó un botón del ratón")


#Muestra de bucle incorrecto
# Este es un bucle de eventos
for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        print("El usuario solicitó salir.")
    elif evento.type == pygame.KEYDOWN:
        print("El usuario presionó una tecla.")
    elif evento.type == pygame.KEYUP:
        print("El usuario soltó una tecla.")

# Aquí el programador ha pegado otro bucle de eventos
# en el programa. Esto es INCORRECTO. Los eventos ya han sido
# procesados.

for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        print("El usuario solicitó salir.")
    elif evento.type == pygame.MOUSEBUTTONDOWN:
        print("El usuario presionó un botón del ratón")

#Cierre correcto de un programa Pygame
pygame.quit()

# Limpia la ventana y establece el color del fondo
pantalla.fill(BLANCO)

# Avanza y actualiza la pantalla con lo que hemos dibujado.
pygame.display.flip()

#Dibuja en la pantalla una línea verde desde (0, 0) hasta (100, 100)
# y 5 píxeles de grosor.
pygame.draw.line(pantalla, VERDE, [0, 0], [100, 100], 5)

# Dibuja sobre la pantalla varias líneas desde (0, 10) hasta (100, 110)
# de 5 píxeles de grosor usando un bucle while
desplazar_y = 0
while  desplazar_y < 100:
    pygame.draw.line(pantalla, ROJO, [0, 10 + desplazar_y], [100, 110 + desplazar_y], 5)
    desplazar_y = desplazar_y + 10

# Dibuja sobre la pantalla varias líneas desde (0, 10) hasta (100, 110)
# de 5 píxeles de grosor usando un bucle for
for desplazar_y in range(0, 100, 10):
    pygame.draw.line(pantalla,ROJO, [0, 10 + desplazar_y], [100, 110 + desplazar_y], 5)

for i in range(200):

    radianes_x = i / 20
    radianes_y = i / 6

    x = int( 75 * math.sin(radianes_x)) + 200
    y = int( 75 * math.cos(radianes_y)) + 200

    pygame.draw.line(pantalla, NEGRO, [x, y], [x + 5, y], 5)

# Dibuja un rectángulo.
pygame.draw.rect(pantalla, NEGRO, [20, 20, 250, 100], 2)

# Representa una elipse, usando un rectángulo como perímetro exterior
pygame.draw.ellipse(pantalla, NEGRO, [20, 20, 250, 100], 2)

# Representa un arco como parte de una elipse. Usamos radianes para determinar qué
# ángulo dibujar.
pygame.draw.arc(pantalla, VERDE, [100, 100, 250, 200], pi/2, pi, 2)
pygame.draw.arc(pantalla, NEGRO, [100, 100, 250, 200], 0, pi/2, 2)
pygame.draw.arc(pantalla, ROJO, [100, 100, 250, 200], 3*pi/2, 2*pi, 2)
pygame.draw.arc(pantalla, AZUL, [100, 100, 250, 200], pi, 3*pi/2, 2)

# Esto dibuja un triángulo usando el comando polygon
pygame.draw.polygon(pantalla, NEGRO, [[100, 100],[0, 200],[200, 200]], 5)

# Selecciona la fuente. Fuente Default, tamaño 25 pt.
fuente = pygame.font.Font(None, 25)

# Reproduce el texto. "True" significa texto suavizado(anti-aliased).
# El color es Negro. Recordemos que ya hemos definido anteriormente la variable NEGRO
# como una lista de (0, 0, 0)
# Observación: Esta línea crea una imagen de las letras,
# Pero aún no la pone sobre la pantalla.
texto = fuente.render("Mi texto", True, NEGRO)

# Coloca la imagen del texto sobre la pantalla en 250 x 250
pantalla.blit(texto, [250, 250])

#Imprimer número en pantalla
texto = fuente.render("Número: " + str(numero), True, NEGRO)

