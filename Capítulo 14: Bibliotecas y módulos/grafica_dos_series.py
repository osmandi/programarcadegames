"""
En este ejemplo se muestra como dibujar dos series diferentes de datos
sobre la misma gráfica.
"""
import matplotlib.pyplot as plt

x =  [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

plt.plot(x, y1)
plt.plot(x, y2)

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()