"""
Cómo construir una gráfica de barras.
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.bar(x, y)

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()