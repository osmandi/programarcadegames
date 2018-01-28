'''
Este es un juego de aventura, las opciones son norte, sur, este y oeste
es como un laberinto en que el de modo texto navegas por toda una mazmorra
utilizando para ello listas
'''
lista_habitaciones = [] #Array vacío

'''
Orden de elementos en la variable habitación de 5 elementos:
    Cadena te texto con la primera habitacion
    Otros cuatro elementos las direccions disponibles en el orden:
        Norte, este, sur u oeste
        utilizar None (sin comillas) para indicar la no disponibilidad
'''

habitacion = ["Estás en una habitación. Existe otra habitacion al norte y un pasillo al este", 3, 1, None, None] #Ver comentario anterior
lista_habitaciones.append (habitacion) #Añade variable habitación a las listas_habitaciones    for j in range(5):
habitacion = ["Estás en un pasillo. Existe una habitación al oeste, un pasillo al norte y una sala al este", 4, 2, None, 0] #Pasillo sur
lista_habitaciones.append (habitacion) #Añade variable habitación a las listas_habitaciones    for j in range(5):
habitacion = ["Estás en una sala. Existe una cocina al norte y un pasillo al oeste", 5, None, None, 1] #Sala
lista_habitaciones.append (habitacion) #Añade variable habitación a las listas_habitaciones    for j in range(5):
habitacion = ["Estás en una segunda habitación. Existe un pasillo al este y una habitación al sur", None, 4, 0, None] #Habitación norte
lista_habitaciones.append (habitacion) #Añade variable habitación a las listas_habitaciones    for j in range(5):
habitacion = ["Sigues en el pasillo. Existe un balcón al norte, una cocina al este, un pasillo al sur y una habitación al oeste", 6, 5, 1, 3] #Pasillo norte
lista_habitaciones.append (habitacion) #Añade variable habitación a las listas_habitaciones    for j in range(5):
habitacion = ["Estás en una cocina. Existe una sala al sur y un pasillo al oeste", None, None, 2, 4] #Cocina
lista_habitaciones.append (habitacion) #Añade variable habitación a las listas_habitaciones    for j in range(5):
habitacion = ["Estás en un balcón. Existe un pasillo al sur", None, None, 4, None] #Balcón
lista_habitaciones.append (habitacion) #Añade variable habitación a las listas_habitaciones    for j in range(5):

habitacion_actual = lista_habitaciones [0]  #Habitación inicial
hecho = False
print ("Para salir telcea 'salir'")

'''
Se puede dismuir el código al agrerar en inicio del bucle
print ()
print (habitacion_actual [0])
'''

while not hecho:
    print ()
    print (habitacion_actual [0])
    entrada= input("¿Hacia dónde quieres ir? ")
    if entrada.lower () == "salir":
        hecho = True
    if entrada.lower () == "norte" or entrada.lower () == "n" or entrada.lower () == "este" or entrada.lower () == "e" or entrada.lower () == "sur" or entrada.lower () == "s" or entrada.lower () == "oeste" or entrada.lower () == "o":

        #Habitación 0
        if habitacion_actual == lista_habitaciones [0]:
            if entrada.lower () == "norte" or entrada.lower () == "n":
                habitacion_actual = lista_habitaciones [3]
            elif entrada.lower () == "este" or entrada.lower () == "e":
                habitacion_actual = lista_habitaciones [1]
            #En caso de ingresar una dirección incorrecta en habitación 0
            else:
                print ("\n---- > No puedes ir en esa dirección")

        #Habitación 1
        elif habitacion_actual == lista_habitaciones [1]:
            if entrada.lower() == "norte" or entrada.lower () == "n":
                habitacion_actual = lista_habitaciones [4]
            elif entrada.lower () == "este" or entrada.lower () == "e":
                habitacion_actual = lista_habitaciones [2]
            elif entrada.lower () == "oeste" or entrada.lower () == "o":
                habitacion_actual = lista_habitaciones [0]
            #En caso de ingresar una dirección incorrecta en habitación 1
            else:
                print ("\n---> No puedes ir en esa dirección")

         #Habitación 2
        elif habitacion_actual == lista_habitaciones [2]:
             if entrada.lower () == "norte" or entrada.lower () == "n":
                 habitacion_actual = lista_habitaciones [5]
             elif entrada.lower () == "oeste" or entrada.lower () == "o":
                habitacion_actual = lista_habitaciones [1]
            #En caso de ingresar una dirección incorrecta
             else:
                print ("\n---> No puedes ir en esa dirección")

        #Habitación 3
        elif habitacion_actual == lista_habitaciones [3]:
            if entrada.lower () == "oeste" or entrada.lower () == "o":
                habitacion_actual = lista_habitaciones[4]
            elif entrada.lower () == "sur" or entrada.lower () == "s":
                habitacion_actual = lista_habitaciones[0]
            #En caso de ingresar una dirección incorrecta
            else:
                print ("\n---> No puedes ir en esa dirección")

        #Habitación 4
        elif habitacion_actual == lista_habitaciones [4]:
            if entrada.lower () == "norte" or entrada.lower () == "n":
                habitacion_actual = lista_habitaciones [6]
            elif entrada.lower () == "este" or entrada.lower () == "e":
                habitacion_actual = lista_habitaciones [5]
            elif entrada.lower () == "sur" or entrada.lower () == "s":
                habitacion_actual = lista_habitaciones [1]
            elif entrada.lower () == "oeste" or entrada.lower () == "o":
                habitacion_actual = lista_habitaciones [3]
            #En caso de ingresar una dirección incorrecta
            else:
                print ("\n--->No puedes ir en esa dirección")

        #Habitación 5
        elif habitacion_actual == lista_habitaciones [5]:
            if entrada.lower () == "sur" or entrada.lower () == "s":
                habitacion_actual = lista_habitaciones [2]
            elif entrada.lower () == "oeste" or entrada.lower () == "o":
                habitacion_actual = lista_habitaciones [4]
            #En caso de ingresar una dirección incorrecta
            else :
                print ("\n---> No puedes ir en es dirección")

        #Habitación 6
        elif habitacion_actual == lista_habitaciones [6]:
            if entrada.lower () == "sur" or entrada_lower () == "s":
                habitacion_actual = lista_habitaciones [4]
            #En caso de ingresar una dirección incorrecta
            else:
                print ("\n---> No puedes ir en esa dirección")

    #En caso de no ingresar la dirección correcta
    else:
        print ()
        print ("------> NO ENTIENDO LO QUE ESCRIBISTE \n")
