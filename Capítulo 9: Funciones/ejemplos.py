# Ejemplo 1
print ("Ejemplo 1")
def a():
    print("A")

def b():
    print("B")

def c():
    print("C")

a()

# Ejemplo 2
print ("Ejemplo 2")
def a():
    b()
    print("A")

def b():
    c()
    print("B")

def c():
    print("C")

a()

# Ejemplo 3
print ("Ejemplo 3")
def a():
    print("A")
    b()

def b():
    print("B")
    c()

def c():
    print("C")

a()

# Ejemplo 4
print ("Ejemplo 4")
def a():
    print("A empieza con")
    b()
    print("A termina con")

def b():
    print("B empieza con")
    c()
    print("C termina con")

def c():
    print("C empieza y termina con")

a()


# Ejemplo 5
print("Ejemplo 5")
def a(x):
    print("A empieza con, x = ",x)
    b(x + 1)
    print("A termina con, x = ",x)

def b(x):
    print("B empieza con, x = ",x)
    c(x + 1)
    print("C termina con, x = ",x)

def c(x):
    print("C empieza y termina con, x = ",x)

a(5)

# Ejemplo 6
print ("Ejemplo 6")
def a(x):
    x = x + 1

x = 3 #Debe colocarse debajo de la función por si acaso
a(x)

print(x)

# Ejemplo 7
print ("Ejemplo 7")
def a(x):
    x = x + 1
    return x

x = 3
a(x)

print(x)

# Ejemplo 8
print ("Ejemplo 8")
def a(x):
    x = x + 1
    return x

x = 3
x = a(x)

print(x)

# Ejemplo 9
print ("Ejemplo 9")
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)

x = 10
y = 20
a(y, x)

#print(z) Comentado para continuar con los ejemplos

# Ejemplo 10
print ("Ejemplo 10")
def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y

x = 10
y = 20
z = a(x, y)

print(z) #Imprime el primer return en este caso el resultado de x

# Ejemplo 11
print ("Ejemplo 11")
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y

x = 10
y = 20
z = a(x, y)

print(z)

# Ejemplo 12
print ("Ejemplo 12")
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y

x = 10
y = 20

#El primero toma el primer valor y el segundo, obviamente, el segundo
x2, y2 = a(x, y) # La mayoría de lenguajes de programación no admiten esto

print(x2)
print(y2)

# Ejemplo 13
print ("Ejemplo 13")
def a(mis_datos):
    print("función a, mis_datos =  ", mis_datos)
    mis_datos = 20
    print("función a, mis_datos =  ", mis_datos)

mis_datos = 10

print("entorno global, mis_datos = ", mis_datos)
a(mis_datos)
print("entorno global, mis_datos = ", mis_datos)

# Ejemplo 14
print ("Ejemplo 14")
def a(mi_lista):
    print("función a, lista =  ", mi_lista)
    mi_lista = [10, 20, 30]
    print("función a, lista =  ", mi_lista)

mi_lista = [5, 2, 4]

print("entorno global, lista = ", mi_lista)
a(mi_lista)
print("entorno global, lista = ", mi_lista)

# Ejemplo 15
# Concepto nuevo!
# Se describe con más detalle en el Capítulo 13
print ("Ejemplo 15")
def a(mi_lista):
    print("función a, lista =  ", mi_lista)
    mi_lista[0] = 1000
    print("función a, lista =  ", mi_lista)

mi_lista = [5, 2, 4]

print("entorno global, lista = ", mi_lista)
a(mi_lista)
print("entorno global, lista = ", mi_lista)