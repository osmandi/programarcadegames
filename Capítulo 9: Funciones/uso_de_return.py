# Función que imprime el resultado
def imprime_suma(a, b):
    resultado = a + b
    print(resultado)

# Función que devuelve el resultado
def devuelve_suma(a, b):
    resultado = a + b
    return resultado

# Esto imprime en pantalla la suma de 4+4
imprime_suma(4, 4)
print ("---")
# Este no
devuelve_suma(4, 4)
print ("---")
# Esto no introducirá el resultado de la suma en x1
# Obtiene realmente un valor de 'None'
x1 = imprime_suma(4, 4)
print ("---")

# Esto sí lo hará
x2 = devuelve_suma(4, 4)

#Las varaiables creadas dentro de la función Def... solo son creadas dentro
#de la función, cuando terminan la función la variable es borrada