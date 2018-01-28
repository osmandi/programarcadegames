def volumen_esfera(radio):
    pi = 3.141592653589
    volumen = (4 / 3) * pi * radio ** 3
    print("El volumen es ", volumen)

#La función debe llamarse, de lo contrario no se ejecutará
volumen_esfera (22)

# --- Función que imprime el volumen de un cilindro

def volumen_cilindro(radio, altura):
    pi = 3.141592653589
    volumen = pi * radio ** 2 * altura
    print("El volumen del cilindro es ", volumen)

volumen_cilindro (12, 3) #El primero es radio y el segundo altura

# --- Función que devuelve el volumen de un cilindro

def volumen_cilindro(radio, altura):
    pi = 3.141592653589
    volumen = pi * radio ** 2 * altura
    return volumen

# return no es una función, su utiliad es que permite ser reutilizada

volumen_pack_seis = volumen_cilindro (2.5,5)*6