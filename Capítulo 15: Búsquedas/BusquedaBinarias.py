# Búsqueda Binaria
clave = "Morgana la Arpía"
limite_inferior = 0
limite_superior = len(lista_nombres)-1
encontrado = False
while limite_inferior <= limite_superior and not encontrado:
    posicion_intermedia = (limite_inferior+limite_superior) // 2
    if lista_nombres[posicion_intermedia] < clave:
        limite_inferior = posicion_intermedia + 1
    elif lista_nombres[posicion_intermedia] > clave:
        limite_superior = posicion_intermedia - 1
    else:
        encontrado = True

if encontrado:
    print("El nombre se encuentra en la posición", posicion_intermedia)
if not found:
    print("El nombre no se encontraba en la lista.")