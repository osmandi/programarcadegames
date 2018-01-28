# Ejemplo de una clase con un constructor
class Perro():
    def __init__(self):
        self.nombre = ""

    # Llamada al constructor
    # cuando creamos un objeto de este tipo
    def __init__(self):
        print("Ha nacido un perro nuevo!")

# Para separar del mensaje al iniciar
print ("")
# Esto crea al perro
mi_perro = Perro()

# Para darle el nombre al perro
# Constructor que toma un dato para inicializar la clase
class Perro():

    # Llamada al constructor
    # cuando creamos un objeto de este tipo
    def __init__(self, nombre_nuevo):
        self.nombre = nombre_nuevo

# Esto crea al perro
mi_perro = Perro("Spot")

# Imprime el nombre para verificar que así ha sido
print(mi_perro.nombre)

# Esta línea producirá un error porque
# el nombre no ha sido introducido.
#suPerro = Perro()

