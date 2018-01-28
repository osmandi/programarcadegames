# Crea una clase llamada Estrella que imprima:
    # Ha nacido una estrellla, cada vez que sea creada

# Crea una clase llamada Monstruo con atributos salud y nombre
# Añádele un constructor que establezca salud y nombre del objeto
# con datos que se pasen como parámetros


class Estrella():

    def __init__(self):
        print ("¡Ha nacido una estrella")


print ('')
print ('')
miEstrella = Estrella()

class Monstruo():

    def __init__(self):
        self.salud = 0
        self.nombre = ''

miMonstruo = Monstruo()
miMonstruo.salud = 100
miMonstruo.nombre = 'Monster'

print (miMonstruo.salud)
print (miMonstruo.nombre)


# Otra cosa
print ("")
class Pelota():
    x = 0
    y = 0

b1 = Pelota()
b2 = b1

b1.x = 40
b2.x = 50
b1.x += 5
b2.x += 5
print(b1.x, b2.x)




