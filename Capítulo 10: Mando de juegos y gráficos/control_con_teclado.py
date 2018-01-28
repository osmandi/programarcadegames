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
    pygame.draw.ellipse(pantalla, NEGRO, [1 + x, y, 10, 10], 0)

    # Piernas
    pygame.draw.line(pantalla, NEGRO ,[5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(pantalla, NEGRO, [5+ x, 17 + y], [x, 27 + y], 2)

    # Cuerpo
    pygame.draw.line(pantalla, ROJO, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Brazos
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [1 + x, 17 + y], 2)

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

# Velocidad en píxeles por fotograma
x_speed = 0
y_speed = 0
# Posición actual
x_coord = 10
y_coord = 10


"""
Códigos de teclado

 Código Pygame	ASCII	Nombre Común
K_BACKSPACE	\b	retroceso
K_RETURN	\r	volver
K_TAB	\t	tab
K_ESCAPE	^[	escape
K_SPACE	 	espacio
K_COMMA	,	coma
K_MINUS	-	menos
K_PERIOD	.	punto
K_SLASH	/	barra
K_0	0	0
K_1	1	1
K_2	2	2
K_3	3	3
K_4	4	4
K_5	5	5
K_6	6	6
K_7	7	7
K_8	8	8
K_9	9	9
K_SEMICOLON	;	punto y coma
K_EQUALS	=	igual
K_LEFTBRACKET	[	corchete izquierdo
K_RIGHTBRACKET	]	corchete derecho
K_BACKSLASH	\	contrabarra
K_BACKQUOTE	`	tilde grave
K_a	a	a
K_b	b	b
K_c	c	c
K_d	d	d
K_e	e	e
K_f	f	f
K_g	g	g
K_h	h	h
K_i	i	i
K_j	j	j
K_k	k	k
K_l	l	l
K_m	m	m
K_n	n	n
K_o	o	o
K_p	p	p
K_q	q	q
K_r	r	r
K_s	s	s
K_t	t	t
K_u	u	u
K_v	v	v
K_w	w	w
K_x	x	x
K_y	y	y
K_z	z	z
K_DELETE	delete	
K_KP0	keypad	0 teclado numérico
K_KP1	keypad	1 teclado numérico
K_KP2	keypad	2 teclado numérico
K_KP3	keypad	3 teclado numérico
K_KP4	keypad	4 teclado numérico
K_KP5	keypad	5 teclado numérico
K_KP6	keypad	6 teclado numérico
K_KP7	keypad	7 teclado numérico
K_KP8	keypad	8 teclado numérico
K_KP9	keypad	9 teclado numérico
K_KP_PERIOD	.	punto teclado numérico
K_KP_DIVIDE	/	dividir teclado numérico
K_KP_MULTIPLY	*	multiplicar teclado numérico
K_KP_MINUS	-	restar teclado numérico
K_KP_PLUS	+	sumar teclado numérico
K_KP_ENTER	\r	intro teclado numérico
K_KP_EQUALS	=	igual teclado numérico
K_UP	up	arriba
K_DOWN	down	abajo
K_RIGHT	right	derecha
K_LEFT	left	izquierda
K_INSERT	insert	insertar
K_HOME	home	inicio
K_END	end	fin
K_PAGEUP	page	página arriba
K_PAGEDOWN	page	página abajo
K_F1	F1	
K_F2	F2	
K_F3	F3	
K_F4	F4	
K_F5	F5	
K_F6	F6	
K_F7	F7	
K_F8	F8	
K_F9	F9	
K_F10	F10	
K_F11	F11	
K_F12	F12	
K_NUMLOCK	numlock	bolqnum
K_CAPSLOCK	capslock	bloqmayus
K_RSHIFT	right	shift
K_LSHIFT	left	shift
K_RCTRL	right	ctrl
K_LCTRL	left	ctrl
K_RALT	right	alt
K_LALT	left	alt
"""



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
            if evento.key == pygame.K_UP:
                y_speed = -3
            if evento.key == pygame.K_DOWN:
                y_speed = 3
        # El ususario suelta una tecla
        if evento.type == pygame.KEYUP:
            # Si se trata de una tecla flecha devuelve el vector a
            # cero
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            if evento.key == pygame.K_RIGHT:
                x_speed = 0
            if evento.key == pygame.K_UP:
                y_speed = 0
            if evento.key == pygame.K_DOWN:
                y_speed = 0

    # ------------ Lógica del juego -------------------------
    # Mueve el objeto de acuerdo a la velocidad del vector
    x_coord += x_speed
    y_coord += y_speed
    # Para que traspase el los límites
    if x_coord >= 400:
        x_coord = 1
    if x_coord <= 0:
        x_coord = 400
    # Para que no traspase los límites
    if y_coord >= 470:
        y_coord = 470
    if y_coord <= 0:
        y_coord = 0
    # -------------- Código de dibujo -----------------------
    # Limpiar la pantalla con su color de fondo
    pantalla.fill(BLANCO)
    # Dibuja hombre de palitos
    dibuja_hombrepalitos (pantalla, x_coord, y_coord)


    #
    # ------------ Actualizar la pantalla con lo dibujado ---
    pygame.display.flip()
    # ------------- Limitamos a 60 fotogramas por segundo ---
    reloj.tick(60)

# Para que se cierre la ventna sin colgar el programa
pygame.quit()