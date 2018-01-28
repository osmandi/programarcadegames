nombre_usuario = input("¿Cuál es tu nombre? ")
if nombre_usuario == "Osmandi":  #Es necesario entre comillas
    print("Tienes un nombre bonito.")
else:
    print("Tu nombre está bien.")

#Para vitar errores al ingresar osmandi (primera letra en minúscula
#utilizar el procedimiento descrito más abajo

# Varias cadenas de texto
#if nombre_usuario == "Paul" or nombre_usuario == "Mary":

'''
Para ignorar las mayúsculas, es recomendable convertir todo a
minúsculas para tomar en cuenta todo lo que el usuario ingrese
nombre_usuario = input(¿Cuál es tu nombre? ")
if nombre_usuario.lower() == "paul":  Debe estar en minúsculas
    print("Tienes un nombre bonito.")
else:
    print("Tu nombre está bien.")
'''