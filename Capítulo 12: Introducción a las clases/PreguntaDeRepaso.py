'''
Crea una clase llamada Gato. Otórgale atributos tales como nombre,
 color, y peso. Dale un método llamado miau

Crea una instancia de la clase gato, completa sus atributos
y llama al método miau

Crea una clase llamada Monstruo. Dale un atributo para nombre y
un atributo entero (int) para salud. Crea un método llamado reducirSalud
que tome un parámetro cantidad y reduzca en esa cantidad la salud de nuestro
monstruo. Dentro de ese método se debe imprimir que el animal ha muerto si su
salud está por debajo de cero
'''


class Gato:

    def __init__(self):
        self.nombre = ""
        self.color = ""
        self.peso = ""

    def miau(self):
        print("Miau")
        print (self.nombre, self.color, self.peso)

class Monstruo():

    def __init__(self):
        # --- Atributos ---
        self.nombre = ''
        self.salud = 0
        self.cantidad = 0

    # ---- Métodos ----
    def reducirSalud(self):
        self.salud -= self.cantidad

        print('Salud del monstruo es ', self.salud)

        if self.salud <= 0:
            print ('Ha muerto el mostruo')




print("")

miGato = Gato()
miGato.nombre = 'Gato1'
miGato.color = 'Amarillo'
miGato.peso = 50

miGato.miau()

print ("")

monstruo1 = Monstruo()
monstruo1.nombre = 'Trogo'
monstruo1.salud = 100
monstruo1.cantidad = 10


while True:
    monstruo1.reducirSalud()

    if monstruo1.salud <= 0:
        break
