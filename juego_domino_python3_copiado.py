def main():
    jugA= Jugador()
    jugB= Jugador()
    listajugadores=[jugA,jugB]
    print ""
    print "-------------------------------"
    print "-        Tonero de domino     -"
    print "-------------------------------"
    print "1- A 2 partidas"
    print "2- A 4 partidas"
    print "3- Al primero que llegue a 100 puntos"
    respuesta=int(raw_input("Elige tipo de torneo:"))
    #elijo tipo de jugadores Humano o Cpu (y su inteligencia)
    jugA,jugB = elegirJugadores()
    if respuesta==1:
        for f in range(2):
            jugA,jugB = partida( jugA,jugB)
            jugA.MarcadorGeneral += jugA.marcador
            jugB.MarcadorGeneral +=jugB.marcador
        print "Final:"
        print jugA.marcador,jugB.marcador
    elif respuesta==2:
        for f in range(4):
            jugA,jugB = partida( jugA,jugB)
            jugA.MarcadorGeneral += jugA.marcador
            jugB.MarcadorGeneral +=jugB.marcador
        print "Final:"
        print jugA.marcador,jugB.marcador
    elif respuesta==3:
        punto=0
        while (punto<100):
            jugA,jugB=partida( jugA,jugB)
            jugA.MarcadorGeneral += jugA.marcador
            jugB.MarcadorGeneral +=jugB.marcador
            if jugA.marcador>100 or jugB.marcador>100:
                print "Final puntuacion:"
                print "Jugador A: ",jugA.marcador,"Jugador B:",jugB.marcador
                punto=120



    pass


if __name__ == '__main__':
    main()