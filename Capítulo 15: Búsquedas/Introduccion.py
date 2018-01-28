file = open("villanos.txt")

lista_nombres = [] # Array vacío para volcar la lista allí
for line in file:
    line = line.strip() # Eliminar espacios vacíos
    lista_nombres.append(line)
    #print (line)

for nombre in lista_nombres:
    print (nombre)

""" Debe cerrarse el archivo al abrirlo, puesto que en Windows
existe un límite de cuántos archivos pueden estar abiertos,
puesto que evitará que otros programas lo usen"""

# Cerramos el archivo
file.close()