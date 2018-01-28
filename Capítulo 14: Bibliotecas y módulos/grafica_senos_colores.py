"""
Uso de 'fill' para rellenar una gráfica
"""
import numpy
import matplotlib.pyplot as plt

x = numpy.arange(0.0, 2.0, 0.001)
y = numpy.sin(2 * numpy.pi * x)

plt.plot(x, y)

# 'b' significa azul. 'alpha' es la transparencia.
plt.fill(x, y, 'b', alpha = 0.3)

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()