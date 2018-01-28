#Juego de camello

#Librería para números aleatorios
import random

#Mensaje de entrada
print ("\n")
print ("¡Bienvenido al Camello!")
print ("Has robado un camello para atraversar el gran desierto del Mobi.")
print ("¡Los nativos quieren que les devuelvas su camello y salen en persecución tuya!")
print ("Tendrás que sobrevivir al desiert y correr más que los nativos")

#Variables
hecho = False
millas_recorridas = 0
sed = 0
cansancio_del_camello = 0
distancia_nativos = 100  #Arregalar millas detrás del sujeto
cantidad_en_cantimplora = 3
veces_bebido_en_cantimplora = 0
oportunidad_oasis = 0

#Bucle while que iterará mientras hecho sea False
while not hecho:
    if millas_recorridas >= 200:
        hecho = True
        print ("¡Felicidades cruzaste el desierto!")
    elif sed > 6:
        print ("Haz muerto de sed")
        hecho = True
    elif cansancio_del_camello > 8:
        print ("Tu camello ha muerto\n")
        hecho = True
    elif distancia_nativos <= 0:
        print ("¡Los nativos te han capturado!\n")
        hecho = True
    else:
        if sed >4 and sed <= 6:
            print ("ESTÁS SEDIENTO\n")
        if cansancio_del_camello > 5 and cansancio_del_camello <= 8:
            print ("TU CAMELLO ESTÁ CANSADO\n")
        if distancia_nativos <= 15 and distancia_nativos >= 0:
            print ("¡LOS NATIVOS SE ESTÁN ACERCANDO!\n")
        usuario_elige = input ("\nA. Beber de la cantimplora \nB. Velocidad moderada hacia adelante \nC. A toda velocidad hacia adelante \nD. Para y descansa \nE. Comprueba tu estado \nQ. Salir \n¿Qué eliges? ")
        if usuario_elige.lower()== "q":  #Sale del juego
            hecho = True
        elif usuario_elige.lower() == "e":  #Pregunta por estado
            print ("\nMillas recorridas: ", millas_recorridas)
            print ("Veces que ha bebido de la cantimplora: ", veces_bebido_en_cantimplora)
            print ("Los nativos están a", distancia_nativos, "millas detrás de ti\n")

        elif usuario_elige.lower() == "d":  #Parar y descansar
            cansancio_del_camello = 0
            print ("\nEl camello te lo agradece\n")
            distancia_nativos -= random.randrange (7,19)

        elif usuario_elige.lower() == "c":  #A toda velocidad
            oportunidad_oasis += random.randrange(1,21)
            if oportunidad_oasis == 7:
                cantidad_en_cantimplora = 3
                sed = 0
                cansancio_del_camello = 0
                print ("\n¡ENCONTRASTE UN OASIS! \nTu cantimplora está llena \nNo tienes sed \nY tu camello ha descansado\n")
            millas_recorridas += random.randrange (10,21)
            print ("\nHaz recorrido", millas_recorridas,"millas \n")
            sed += 1
            cansancio_del_camello += random.randrange (1,4)
            distancia_nativos -= random.randrange(1,6)


        elif usuario_elige.lower() == "b":  #Velocidad moderada
            oportunidad_oasis += random.randrange(1,21)
            if oportunidad_oasis == 7:
                cantidad_en_cantimplora = 3
                sed = 0
                cansancio_del_camello = 0
                print ("\n¡ENCONTRASTE UN OASIS! \nTu cantimplora está llena \nNo tienes sed \nY tu camello ha descansado\n")
            millas_recorridas += random.randrange(5,13)
            print ("\nHaz recorrido", millas_recorridas,"millas\n")
            sed += 1
            cansancio_del_camello += 1
            distancia_nativos -= random.randrange(1,11)

        elif usuario_elige.lower() == "a":
            if cantidad_en_cantimplora > 0 and sed == 0:
                print ("\nOye, no tienes sed\n")
            elif cantidad_en_cantimplora > 0:
                cantidad_en_cantimplora -= 1
                sed = 0
                print ("")
            else:
                print ("\nNo tienes agua en la cantimplora\n")












