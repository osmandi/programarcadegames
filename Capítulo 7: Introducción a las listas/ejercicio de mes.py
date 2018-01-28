'''
Imprime la abreviatura (de tres letras) para el número de mes que
introduzca el usuario. (Calcula la posición inicial en la cadena, luego, usa
la información que hemos aprendido para imprimir la subcadena correcta)
'''

print() #Separar del encabezado
meses = "EneFebMarAbrMayJunJulAgoSepOctNovDic"

n = int(input("Introduce un número de mes: "))

print (meses[n*3-3: n*3])

