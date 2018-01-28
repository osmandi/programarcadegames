print ("\n \n \n")


'''
En el siguiente código, el programa imprimirá “Hace calor fuera”
aun cuando el usuario introduzca 120 grados. ¿Por qué?
¿De qué forma podemos corregir el código?

Original
temperatura = int(input("¿Cuál es la temperatura en Fahrenheit? "))
if temperatura > 90:
    print("Hace calor fuera")
elif temperatura > 110:
    print("¡Caramba, casi podemos freír un huevo sobre el asfalto!")
elif temperatura < 30:
    print("Hace frío fuera")
else:
    print("Se está bien afuera")
print ("Hecho")
'''

#Correción:

temperatura = int(input("¿Cuál es la temperatura en Fahrenheit? "))
if temperatura > 110:
    print("¡Caramba, casi podemos freír un huevo sobre el asfalto!")
elif temperatura > 90:
    print("Hace calor fuera")

elif temperatura < 30:
    print("Hace frío fuera")
else:
    print("Se está bien afuera")
print ("Hecho")