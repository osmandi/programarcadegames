# Comprobar si en el grupo hay un alien verde o si todos son verdes

# Primero definir el alien

class Alien():
    """ Clase que define a un alien"""
    def __init__(self, color, peso):
        """ Constructor. Establece peso y color"""
        self.color = color
        self.peso = peso

# Crear una función que compruebe si posee el rasgo buscando
# Se convierte toda la cadena a color en mayúsculas para evitar
# complicaciones con las minúsculas

def tiene_propiedad(mi_alien):
    """ Comprobamos si un item posee esa propiedad.
    En caso, ¿es verde el alien?"""
    if mi_alien.color.upper() == "VERDE":
        return True
    else:
        return False

# Comprueba si uno de los elementos tiene esa propiedad

def comprueba_si_un_elemento_tiene_propiedad_v1(lista):
    """ Devuelve true si al menos un item tiene esa
    propiedad"""
    i = 0
    while i<len(lista) and not tiene_propiedad(lista[i]):
        i += 1

    if i<len (lista):
        # Se encontró un elemento con esa propiedad
        return True

    if i == len(lista):
        # No existe un elemento con esa propiedad
        return False

# Otra forma

def comprueba_si_un_elemento_tiene_propiedad_v2(lista):
    """ Devuelve True si al menos un item tiene esa propiedad.
    Funciona como v1, pero con menos código"""
    for item in lista:
        if tiene_propiedad(item):
            return True
    return False

# Comprueba si todos los elementos tiene una propiedad

def comprueba_si_todos_los_elementos_tienen_propiedad(lista):
    """ Devuelve true si TODOS los items tiene una propiedad"""
    for item in lista:
        if not tiene_propiedad(item):
            return False

    return True

# Saber cuántos elementos tiene la propiedad

def obtener_elementos_coincidentes(lista):
    """ Construye una lista completamente nueva con todos los
    items que coincidan con nuestra propiedad"""
    lista_coincidencias = []
    for item in lista:
        if tiene_propiedad(item):

            lista_coincidencias.append(item)
    return lista_coincidencias

# Ejecutar funciones

lista_aliens = []
lista_aliens.append(Alien("Verde", 42))
lista_aliens.append(Alien("Rojo", 40))
lista_aliens.append(Alien("Azul", 41))
lista_aliens.append(Alien("Púrpura", 40))

resultado = comprueba_si_un_elemento_tiene_propiedad_v1(lista_aliens)
print("Resultado del test comprueba_si_un_elemento_tiene_propiedad_v1:",resultado )

resultado = comprueba_si_un_elemento_tiene_propiedad_v2 (lista_aliens)
print("Resutado del test comprueba_si_un_elemento_tiene_propiedad_v2:", resultado)

resultado = comprueba_si_todos_los_elementos_tienen_propiedad (lista_aliens)
print ("Resultado del test comprueba_si_todos_los_elementos_tiene_propiedad:", resultado)

resultado = obtener_elementos_coincidentes(lista_aliens)
print("Número de items devueltos por el test obtener elementos coincidentes:", resultado)



