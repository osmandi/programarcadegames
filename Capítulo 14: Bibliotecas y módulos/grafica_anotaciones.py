"""
Anotando sobre la gráfica
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.annotate('Aquí',
             xy = (2, 3),
             xycoords = 'data',
             xytext = (-40, 20),
             textcoords = 'offset points',
             arrowprops = dict(arrowstyle = "->",
                               connectionstyle = "arc, angleA = 0,armA = 30,rad = 10"),
             )

plt.plot(x, y)

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()