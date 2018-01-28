
file = open("villanos.txt")

lista_nombres = [] # Array vacío para volcar la lista allí
for line in file:
    line = line.strip() # Eliminar espacios vacíos
    lista_nombres.append(line)
    #print (line)


i = 0
while i < len(lista_nombres) and lista_nombres[i] != "Morgana la Arpía":
    i += 1

if i < len(lista_nombres):
    print ("El nombre se encuentra en la posición", i)
else:
    print("El nombre no se halla en la lista")