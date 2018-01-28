"""
Recta con cuatro valores.
Ahora especificamos unos valores para el eje x también.
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.plot(x, y)

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()