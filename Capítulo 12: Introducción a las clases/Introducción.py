# Al contrario de las variables y funciones cuando se declara una clase
# ésta debe iniciar con letra mayúscula, aunque se puede iniciar con letra minúscula
# no se considera buena práctica

# La def __init__(self) es una función especial llamada constructor la cual se
# ejecuta automáticamente cuando la clase es creada

# El self es algo como el pronombre mi. Al anteponserse a una palabra es como mi
# nombre, mi ciudad, mi función, solo aplica en la clase

# Cadenas de texto se llaman Strings
# Cadenas de números enteros se llaman Integer

# Definir una clase que represente al personaje
class Personaje():
    def __init__(self):
        self.nombre = "Link"
        self.sexo = "Varón"
        self.golpe_puntos_max = 50
        self.golpe_puntos_actuales = 50
        self.velocidad_max = 10
        self.cantidad_blindaje = 8

# Definir una clase dirección
class Direccion():
    def __init__(self):
        self.nombre = ""
        self.via1 = ""
        self.via2 = ""
        self.ciudad = ""
        self.provincia = ""
        self.cod_postal = ""

# Crear una instancia de la clase dirección
# Crea una dirección
casa_direccion = Direccion()

# Establece los campos de la dirección
casa_direccion.nombre = "John Smith"
casa_direccion.via1 = "701 N. C Street"
casa_direccion.ciudad = "Carver Science Building"
casa_direccion.provincia = "IA"
casa_direccion.cod_postal = "50125"


# Para establecer los campos de la clase, el programa debe usar el operador punto.
# Este operador es el punto que está en medio de casa_direccion y el nombre del campo

"""
Errores:

# Crea una dirección
mi_direccion = Direccion()

# Cuidado! Esto no establece el nombre para la dirección!
nombre = "Dr. Craven"

# Esto tampoco
Direccion.nombre = "Dr. Craven"

# Esto sí está bien:
mi_direccion.nombre = "Dr. Craven"
"""

# Trabajar con dos instancias de dirección
# Siguiendo el código anterior
# Crea otra dirección
casa_vacaciones_direccion = Direccion()

# Establece los campos de la nueva dirección
casa_vacaciones_direccion.nombre = "John Smith"
casa_vacaciones_direccion.via1 = "1122 Main Street"
casa_vacaciones_direccion.via2 = ""
casa_vacaciones_direccion.ciudad = "Panama City Beach"
casa_vacaciones_direccion.cod_postal = "32407"

print ("")
print ("La dirección principal del cliente está en " + casa_direccion.ciudad)
print ("Su casa de vacaciones está en " + casa_vacaciones_direccion.ciudad)

print ("\nSeparación")

# Imprime una dirección en pantalla
def imprimir_direccion(direccion):
    print(direccion.nombre)
    # Si existe una via1 en esa dirección, imprímela
    if( len(direccion.via1) > 0 ):
        print (direccion.via1)
    # Si existe una via2 en esa dirección, imprímela
    if( len(direccion.via2) > 0 ):
        print( direccion.via2 )
    print( direccion.ciudad+", "+direccion.provincia+" "+direccion.cod_postal )

imprimir_direccion( casa_direccion )
print()
imprimir_direccion( casa_vacaciones_direccion )

# Todo lo anterior son los atributos que tienen las clases. Pero éstas también
# disponen de métodos, los cuales es una función dentro de una clase

print ("")
print ("-----------")


# Definimos la clase Perro para que ladre
class Perro():
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.peso = 0
    def ladra (self):
        print ("dice Guau", self.nombre)

# El primer parámetro en cualquier método de una clase debe ser self, este
# parámetro es imprescindible aunque la función no haga uso de el

# Ideas que se deben tener en cuenta al crear métodos:
    # Los atributos deben ir primero
    # El primer parámetro, en cualquier método, debe ser self
    # Las definiciones de métodos deben ir indentadas exactamente una tabulación

mi_perro = Perro()

mi_perro.nombre = "Spot"
mi_perro.peso = 20
mi_perro.edad = 3

# Llamar a la función ladrar
mi_perro.ladra()

"""
# Clase Pelota para agregar al código Pygame
class Pelota():
    def __init__(self):
        # --- Atributos de la Clase ---
        # Posición de la pelota
        self.x = 0
        self.y = 0

    # vector Pelota
    self.cambio_x = 0
    self.cambio_y = 0

    # Dimensiones de la Pelota
    self.talla = 10

    # color de la Pelota
    self.color = [255,255,255]

    # --- Métodos para la Clase ---
    def mover(self):
        self.x += self.cambio_x
        self.y += self.cambio_y

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, [self.x, self.y], self.talla )

# Creará la pelota y sus atributos
laPelota = Pelota()
laPelota.x = 100
laPelota.y = 100
laPelota.cambio_x = 2
laPelota.cambio_y = 1
laPelota.color = [255,0,0]

# Agregar esto al bucle principal
laPelota.mover()
laPelota.dibujar(pantalla)
"""

# Herencia
# Definición de clase para barco
class Barco():
    def __init__(self):
        self.tonelaje = 0
        self.nombre = ""
        self.estaAtracado = True

    def atracar(self):
        if self.estaAtracado:
            print("Ya has atracado.")
        else:
            self.estaAtracado = True
            print("Atracando")

    def desatracar(self):
        if not self.estaAtracado:
            print("No estás atracado.")
        else:
            self.estaAtracado = False
            print("Desatracando")

# Estado del atraque de nuestro barco
b = Barco()

b.atracar()
b.desatracar()
b.desatracar()
b.atracar()
b.atracar()

# La herencia consiste en crear una clase que herede los atributos y métodos
# de una clase

class Submarino (Barco):
    def sumergirse (self):
        print ("Sumergirse!")

# Este es el ejemplo de la herencia
b = Submarino()

b.atracar()
b.desatracar()
b.desatracar()
b.atracar()
b.atracar()
b.sumergirse()

# Ejemplo de las Clases Persona, Empleado y Cliente
class Persona():
    def __init__(self):
        self.nombre = ""

class Empleado(Persona):
    def __init__(self):
        self.nombre_del_puesto = ""

class Cliente(Persona):
    def __init__(self):
        self.email = ""

johnSmith = Persona()
johnSmith.nombre = "John Smith"

janeEmpleado = Empleado()
janeEmpleado.nombre = "Empleado Jane"
janeEmpleado.nombre_del_puesto = "Desarrollador Web"

bobCliente = Cliente()
bobCliente.nombre = "Bob Cliente"
bobCliente.email = "enviame@spam.com"

# Los métodos también se heredan
class Persona():
    def __init__(self):
        self.nombre = ""
        print("Persona creada")

class Empleado(Persona):
    def __init__(self):
        self.nombre_del_puesto = ""

class Cliente(Persona):
    def __init__(self):
        self.email = ""

johnSmith = Persona()
janeEmpleado = Empleado()
bobCliente = Cliente()

