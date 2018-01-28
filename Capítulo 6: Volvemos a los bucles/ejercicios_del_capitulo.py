# Imprimir diez (*) con bucles
print ("Primer ejercicio")
for fila in range (10):
    print ("*", end=" ")

'''Imprime

* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *

'''
print()
print ("Segundo ejercicio")
for fila in range(10):
    print("*", end=" ")
print()
for fila in range(5):
    print("*", end=" ")
print()
for fila in range(20):
    print("*", end=" ")
print()

#Imprimir un cuadrado 10x10 de (*)
print ("Tercer ejercicio")
for fila in range (10):
    print ("*", end="")
    for fila in range (1):
        print ("**********")
print("Tercer ejercicio, corregido")

for fila in range(10):
    for columna in range(10):
        print("*", end=" ")
    print ()  #Esto imprime una línea en blanco antes de cada asterisco

print()

#Usa dos bucles for, uno de ellos anidado, para imprimir un rectángulo de 5 x 10
print ("Cuarto ejercicio")
for fila in range (10):
    for columna in range (5):
        print ("*", end=" ")
    print()

print()

#Usa dos bucles for, uno de ellos anidado, para imprimir un rectángulo de 20x5
print ("Quinto ejercicio")
for fila in range (5):
    for columna in range (20):
        print ("*", end=" ")
    print()

print ()

#Sexto ejercicio
'''
Escribe un código para conseguir

0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9

'''
print ("Sexto ejercicio")
for j in range (10):
    for i in range (10):
        print(i, end=" ")
    print ()


#Séptimo ejercicio

'''
Haz un programa que imprima
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
'''
print()
print ()
print ("Séptimo ejercicio")

for fila in range (10):
    for columna in range(10):
        print(fila, end=" ")
    print ()

#Octavo ejercicio
print()
print()
print ("Octavo ejercicio")
'''
Haz un programa que imprima lo siguiente
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9
'''

for fila in range(10):
    for columna in range(fila+1):
        print (columna,end=" ")
    # Imprimimos una línea den blanco antes de la siguiente fila
    print()

#Ejercicio noveno

'''
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0
'''
print ()
print ()
print ("Ejercicio noveno")
for fila in range(9,-1,-1):
    for espacio in range(fila,10-1):
        print (" ", end=" ")
    for columna in range(fila+1):
        print (columna,end=" ")
    print()

#Ejercicio décimo
print ()
print ()
print ("Ejercicio décimo")

'''
Hacer un programa que imprima
  1   2   3   4   5   6   7   8   9
  2   4   6   8  10  12  14  16  18
  3   6   9  12  15  18  21  24  27
  4   8  12  16  20  24  28  32  36
  5  10  15  20  25  30  35  40  45
  6  12  18  24  30  36  42  48  54
  7  14  21  28  35  42  49  56  63
  8  16  24  32  40  48  56  64  72
  9  18  27  36  45  54  63  72  81
'''

#Resolución correcta
for fila in range(1,10):
    for columna in range(1,10):
        # ¿Un poco de espacio extra?
        if fila*columna < 10:
            print (" ",end="")

        print (fila*columna, end=" ")

    # Esto nos desplaza a la línea siguiente
    print()


#Ejercicio onceavo

'''
Hacer un código que imprima el siguiente programa
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
'''

print()
print()

print ("Onceavo ejercicio")

for fila in range (1,10):
    for espacio in range (fila, 8 +1):
        print (" ", end=" ")
    for columna in range (1,fila+1):
        print(columna, end=" ")
    for adicion in range (2,fila+1):
        print (fila - adicion+1, end=" ")
    print ()

#Doceavo ejercicio
'''
Hacer un código que imprima
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8
      1 2 3 4 5 6 7
        1 2 3 4 5 6
          1 2 3 4 5
            1 2 3 4
              1 2 3
                1 2
                  1
Nota: Se resuelve combinando el problema 11 y 9
'''
print ()
print ()
print ("Doceavo ejercicio")
for fila in range (1,10):
    for espacio in range (fila, 8 +1):
        print (" ", end=" ")
    for columna in range (1,fila+1):
        print(columna, end=" ")
    for adicion in range (2,fila+1):
        print (fila - adicion+1, end=" ")
    print ()
for fila in range(9,-1,-1):
    for espacio in range(fila,10-1):
        print (" ", end=" ")
    for columna in range(fila+1):
        print (columna,end=" ")
    print()

#Solución correcta
print()
for i in range(10):
    # Imprime los espacios del principio
    for j in range(10-i):
        print (" ",end=" ")
    # Cuenta hacia adelante
    for j in range(1,i+1):
        print (j,end=" ")
    # Cuenta atrás
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Fila siguiente
    print()

for i in range(10):
    # Imprime los espacios del principio
    for j in range(i+2):
        print (" ",end=" ")
    # Cuenta atrás
    for j in range(1,9-i):
        print (j,end=" ")
    # Fila siguiente
    print()



#Décimo tercer ejercicio
print ()
print ()
print ("Décimo terecer ejercicio")

'''
Hacer un código que imprima
                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 4 3 2 1
            1 2 3 4 3 2 1
              1 2 3 2 1
                1 2 1
                  1
'''

for fila in range (10):
    for espacio in range (10-fila):
        print (" ", end=" ")
    for columna in range (1,fila+1):
        print(columna, end=" ")
    for columna in range (fila-1,0,-1):
        print (columna, end=" ")
    print ()
for fila in range (1,9):
    for espacio in range (fila+1):
        print (" ", end=" ")
    for columna in range (1,9-fila):
        print (columna, end=" ")
    for columna in range (9-fila,0,-1):
        print (columna, end=" ")
    print()

#Solución de web
print ()
print ()
for i in range(10):
    # Imprimimos espacios al principio de la línea
    for j in range(10-i):
        print (" ",end=" ")
    # Cuenta hacia arriba
    for j in range(1,i+1):
        print (j,end=" ")
    # Cuenta atrás
    for j in range(i-1,0,-1):
        print (j,end=" ")
    #Fila siguiente
    print()

for i in range(10):
    #Imprimimos espacios al principio de la línea
    for j in range(i+2):
        print (" ",end=" ")
    # Cuenta hacia arriba
    for j in range(1,9-i):
        print (j,end=" ")
    # Cuenta atrás
    for j in range(7-i,0,-1):
        print (j,end=" ")
    print()

