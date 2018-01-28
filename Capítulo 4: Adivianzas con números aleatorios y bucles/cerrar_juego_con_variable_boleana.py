hecho = False
while not hecho:
    salir = input ("¿Quieres salir? ")
    if salir == "y" :
        hecho = True;

    ataque = input ("Es que tu elfo ha atacado al dragón? ")
    if ataque == "y":
        print ("Pésima opción, estás muerto.")
        hecho = True;