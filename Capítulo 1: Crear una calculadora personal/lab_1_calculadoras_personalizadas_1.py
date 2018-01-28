'''
Crear un programa que le pregunte al usuario por la temperatura
en grados Celsius, y que la devuelva en grados Fahrenheit
'''
temp_grado_celsius = float(input("Ingrese temperatura en grados Celsius"))

f = temp_grado_celsius*(9/5)+32
print (temp_grado_celsius, "grados Celsius en grados Fahrenheit es:", f)