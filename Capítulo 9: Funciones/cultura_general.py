
# Crea la variable x y la establece a 44
x = 44

# Define una función elemental que imprime x
def f():
    '''De agregarse el siguiente comentario, la función fala porque
    desconoce el valor de x    '''
    #x += 1
    print(x)

# Llamada a la función
f()


# Define una función elemental que imprime x
def f(x):
    x += 1
    print(x)

# Establece y
y = 10
# Llamada a la función
f(y)
# Imprime y para ver si ha cambiado
print(y)

"""Similar al anterior"""
#  Define una función elemental que imprime x
def f(x):
    x += 1
    print(x)

# Establece x
x = 10
# Llamada a la función
f(x)
# Imprime x para ver si ha cambiado
print(x)

"""Funciones que llaman a otras funciones"""

#Es muy posible que una función llame a otra función.
#Por ejemplo, digamos que hemos definido funciones como las siguientes:

'''
def brazo_fuera(cual_brazo, palmas_arriba_o_abajo):
    # el código vendría aquí

def agarrar_mano(mano, brazo):
    # el código vendría aquí

#Luego podríamos tener otra función que llamara a las dos anteriores:
def macarena():
    brazo_fuera("derecho", "abajo")
    brazo_fuera("izquierdo", "abajo")
    brazo_fuera("derecho", "arriba")
    brazo_fuera("izquierdo", "arriba")
    agarrar_mano("derecha", "brazo izquierdo")
    agarrar_mano("izquierda", "brazo derecho")
    # etc
'''


'''
Las variables con cero identación se llaman VARIABLES GLOBALES
no es lo adecuado, puesto que de haber un error o una modificación  se debe
revisar todo el código del programa para encontrarlo. Es por ello que es
recomendable crear esa variable dentro de una función para así manterlo
organizado. Por ejemplo
'''

def main():
    print("Hola mundo.")

main()

#Esto no lo entendí
#Uso adecuado de la función main
def main():
    print("Hola Mundo.")

if __name__ == "__main__":
    main()