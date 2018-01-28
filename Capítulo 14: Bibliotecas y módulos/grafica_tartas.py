"""
Crear una gráfica de tarta
"""
import matplotlib.pyplot as plt

# Etiquetas para la gráfica de tarta
etiquetas = ['C', 'Java', 'Objective-C', 'C++', 'C#', 'PHP', 'Python']

# Tamaños para cada etiqueta. Lo usamos para crear un porcentaje
dimensiones = [17, 14, 9, 6, 5, 3, 2.5]

# Para una lista de colores, ver:
# https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/colors.py
colores = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'darkcyan', 'darksage', 'rosybrown']

# ¿Cuán separada ha de estar una porción? Normalmente cero.
separar = (0, 0.0, 0, 0, 0, 0, 0.2)

# Definimos la ratio de aspecto al valor 'equal' para que la tarta dibujada sea circular.
plt.axis('equal')

# Finalmente, dibujamos la tarta
plt.pie(dimensiones, explode = separar, labels = etiquetas, colors = colores,
        autopct = '%1.1f%%', shadow = True, startangle = 90)

plt.show()