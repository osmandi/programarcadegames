"""
Recta con cuatro valores.
Por defecto, el eje x empieza en cero.
"""
import matplotlib.pyplot as plt

y = [1, 3, 8, 4]

plt.plot(y)
plt.ylabel('Valor del Elemento')
plt.xlabel('Número del Elemento')

plt.show()