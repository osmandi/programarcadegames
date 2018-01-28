# ================== Taller de laboratorio 9 =========================

# Este programa tiene varias partes a continuación la descripción de
# cada una de ellas

# ----------------------- Parte 1 -----------------------------------
"""
Escribe una función llamada min, que reciba tres números y que devuelva
el menor de los tres Si se repitiera algún valor, no importa, debe
seguir devolviendo el más pequeño. Una vez que hayaz acabado, copia
y/o pega el siguiente código y comprueba que la funció que te has
creado, hace lo esperado:

print (min(4,7,5))
print (min(4,5,5))
print (min(4,4,4))
pint (min(-2,-6-100))
print (min("Z", "B", "A"))

Deberías tener los siguientes resultados:
    4
    4
    4
    -100
    A

La función debería devolver el valor, no imprimirlo. Aunque ya existe
una función interna en Pytho llamada min, no la uses. Utiliza, por
favor, declaraciones if para construirte tu propia función. Deja a
la vista las declaraciones de prueba para que el instructor pueda
verificar tu programa
"""

print()
print ("Este es el ejercicio de la primera parte")

def min(x,y,z):
    if y > x < z:
        return x
    elif x > y and y < z:
        return y
    else:
        return z

print ()
print (min(4,7,5), "Debe imprimir 4")
print (min(4,5,5), "Debe imprimir 4")
print (min(4,4,4), "Debe imprimir 4")
print (min(-2,-6,-100), "Debe imprimir -100")
print (min("Z", "B", "A"), "Debe imprimir A")

# ------------------------- Parte 2 ---------------------------------
"""
Escribe una función llamada caja, la cual representará cajas según la
altura y largo proporcionados a la función. Una vez que hayas acabado,
copia/pega el siguiente código y comprueba que la función que te has
creado, hace lo esperado:

caja (7,5)  # Representa una caja de 7 x 5
print ()  # Línea en blanco
caja (3,2)  # Representa una caja 3 x 2
print ()  # Línea en blanco
caja (3,10)  # Representa una caja 2 x 10

Deberías obtener estos resultados con el código de ejemplo:

*****
*****
*****
*****
*****
*****
*****

**
**
**

**********
**********
**********

En el capítulo 6 se trató al respecto
"""
print ()
print ("Esta es la segunda parte")

def caja (x,y):
    for i in range(x):
        for j in range (y):
            print ("*", end = "")
        print()

caja (7,5)  # Representa una caja de 7 x 5
print ()  # Línea en blanco
caja (3,2)  # Representa una caja 3 x 2
print ()  # Línea en blanco
caja (3,10)  # Representa una caja 2 x 10


# ------------------------ Parte 3 ----------------------------------
"""
Escribe una función llamada ENCONTRAR, la cual tomará una lista de
números, lista, junto a un número, CLAVE. Deberá buscar en esa lista
el número contenido en CLAVE. Cada vez que tu función encuentre el
valor clave, imprimirá la posición de esa clave en el array. Deberás
conjugar tres variables: Una para la lista, otra para la clave y la
última para la posición en la que te encuentras en la lista.

Este código se parece al que vimos en el Capítulo 7, donde iterábamos
a través de una lista usando funcions RANGE y LEN. Empieza con ese
código y modifica la función PRINT, de modo que demuestre cada elemento
junto a su posición. Luego, en lugar de solo imprimir cada número,
añade una declaración if para que solo imprima el número que nos
interesa.

Copia/pega este código y compruébalo

lista = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

encontrar(lista, 12)
encontrar(lista, 91)
encontrar(lista, 80)

Comprueba tus resultados:

Hemos encontrado un 12 en la posición 11
Hemos encontrado un 12 en la posición 13
Hemos encontrado un 91 en la posición 5

Utiliza un bucle for, junto con una variable índice y una función
range. Dentro del bucle, usa una declaración if. La función se puede
escibir en unas cuatro líneas de código
"""
print ()
print ("Este es el ejercicio de la tercera parte")

lista = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

def encontrar (lista, valor_clave):
    for i in range(len(lista)):
        if lista[i] == valor_clave:
            print("Hemos encontrardo un", valor_clave,
                "en la posición ", i)

encontrar (lista, 12)
encontrar(lista, 91)
encontrar(lista, 80)

# ------------------------- Parte 4 ----------------------------------
"""
Escribe un programa que contenga lo siguiente:
    Funciones:
        Escribe una función llamada CREAR_LISTA que reciba las
        dimensiones de una lista y que luego devuelva una lista con
        números aleatorios del 1-6. Por ejemplo; crear_lista (5)
        debería devolver 5 números aleatorios entre 1-6. (Recuerda que
        e el Capítulo 7 hay un código que deustra cómo hacer algo
        parecido: Crear una lista a partir de 5 números introducidos
        por el usuario. Aquí, en lugar de preguntarle al usuario,
        necesitarás crear números aleatorios.)
        Para comprobar tu función, utiliza el siguiente código:
            mi_lista = crear_lista (5)
            print (mi_lista)
        Con ello deberías obtener cinco elementos aleatorios parecidos
        a estos:
            [2,5,1,6,3]

        Escribe una función llamada CONTAR_LISTA, que tome como
        parámetor una lista y un número. La función deberá devolver
        el número de veces que el mencionado número aparace en la
        lista.
        Para comprobar tu función, utiliza el siguiente código:
            contar = contar_lista([1,2,3,3,3,4,2,1],3)
            print(contar)
        Con ello deberías obtener algo parecido a esto:
            3

        Escribe una función llamada PROMEDIO_LISTA, que devuelva el
        promedio de la lista pasada como parámetro.
        Para comprobar tu función, utiliza el siguiente código:
            promedio=promerdio_lista([1,2,3])
            print (promedio)
        Con ello deberías obtener algo parecido a esto:
            2

    Bien, ahora que ya tienes las tres funciones anteriores, úsalas
    todas en un solo programa que:
        Cree una lsta de 10,000 números aleatorios entre 1 y 6. Esto
        debería ocuparte una sola línea de código (Usa a función
        creada anteiormente en el taller)

        Imprima las veces que aparecen los números 1 y 6. (Es decir,
        imprime las veces que aparece el 1 en esos 10,000 números. Lo
        mismo para 2-6)

        Imprima el promedio de esos 10,000 números aleatorios
"""
print ()
print ("Este es el ejercicio de la parte 4")

import random

# Primera función
print ("Primera función")
def crear_lista (dimensiones):
    # Para establecer las dimensiones de la lista y así crear un rango
    lista = [0]*dimensiones
    for i in range (len (lista)):
        #Elige un valor entre 1 y 6 que ingresa en la lista
        lista [i] += lista [i] + random.randrange(1,7)
    # Retornamos el valor para poder imprimir
    return lista

mi_lista = crear_lista (5)
print (mi_lista)


# Segunda función
print ("Segunda función")
def contar_lista (lista, valor_clave):
    numero_de_veces = 0
    for i in range (len(lista)):
        if lista [i] == valor_clave:
            numero_de_veces += 1
    return numero_de_veces

contar = contar_lista([1,2,3,3,3,4,2,1],3)
print(contar)


# Tercera función
print ("Tercera función")
def promedio_lista (lista):
    total_lista = 0
    promedio = 0
    for i in range (len (lista)):
        total_lista += lista [i]
    promedio = total_lista // len(lista)
    return promedio

promedio=promedio_lista([1,2,3])
print (promedio)

# Programa
print ("Programa")
lista_final = crear_lista (10000)

for i in range (1,7):
    contar_numeros = contar_lista (lista_final,i)
    print ("Existen",contar_numeros, "veces el número",i)

promedio_lista_programa = promedio_lista (lista_final)
print ("Promedio de esos 10,000 números aleatorios son",
    promedio_lista_programa)