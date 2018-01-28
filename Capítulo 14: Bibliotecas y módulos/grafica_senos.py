"""
Uso de la biblioteca numpy para dibujar una función para un determinado
rango de valores.
"""
import numpy
import matplotlib.pyplot as plt

x = numpy.arange(0.0, 2.0, 0.001)
y = numpy.sin(2 * numpy.pi * x)

plt.plot(x, y)

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()