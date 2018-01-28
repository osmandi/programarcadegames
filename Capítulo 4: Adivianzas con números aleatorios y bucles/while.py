#Uso de un bucle for para imprimir los números del 0 al 9

for i in range(10):
    print(i)

#Uso de un bucle while para imprimir los números del 0 al 9

i = 0
while i < 10:
    print(i)
    i = i + 1

#No usar la función range con while

#Incremento con while
i = 0
while i < 10:
    print(i)
    i += 1

#No cierra hasta que el usuario lo solicita
salir = "n"
while salir == "n":
    salir = input ("¿Quieres salir? s/n ")