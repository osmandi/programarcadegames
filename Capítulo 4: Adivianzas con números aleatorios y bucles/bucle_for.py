#Imprimir cinco veces
for i in range(5):
    print ("No volveré a mascar chicle en clases.")

#La i es la variable que lleva la cuenta de las veces que hemos
#iterado el programa, puede ser cualquier nombre pero suele usarse i

for i in range(5):
    print ("Por favor")
print ("¿Puedo ir al centro comercial?")

#Imprime los números del 0 al 9
for i in range(10):
    print (i)

#Impripir números del 1 al 10 - versión 1
for i in range (1,11):
    print (i)

#Imprime números del 1 al 10 - versión 2
for i in range (10):
    print (i + 1)

#Impripir de dos en dos hasta el 10 - método 1
for i in range (2,12,2):
    print (i)

#Imprimir de dos en dos hasta el 10 - método 2
for i in range(5):
    print((i + 1)*2)

#Cuenta hacia atrás desde 10 hasta 1


#Imprime números de una lista
for i in [2,6,4,2,4,6,7,4]:
    print (i)


# ¿Qué es lo que esto imprime? ¿Por qué?
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Hecho")

#Mantener un total acumulado
total = 0
for i in range(5):
    nuevo_numero = int(input("Introduce un número: " ))
    total += nuevo_numero
print("El total es: ",total)

#Suma acumulada de los números del 1 al 100
# ¿Cuál es el valor de suma?
suma = 0
for i in range(1,101):
    suma = suma + i
print(suma)

#Toma 5 números del usuario y cuenta las veces que se introduce un cero
total = 0
for i in range(5):
    nuevo_numero = int(input( "Introduce un número: "))
    if nuevo_numero == 0:
        total += 1
print("Has introducido ",total," ceros")

print ("")
# ¿Cuál es el valor de a?
a = 0
for i in range(10):
    a=a+1
print(a)

# ¿Cuál es el valor de a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)

# ¿Cuál es el valor de a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a
