"""
Aquí mostramos cómo establecer el estilo de línea y los símbolos.
"""
import matplotlib.pyplot as plt

x =  [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

# Primer carácter: Estilo de línea
# Elegir entre '-', '--',  '-.', ':', 'None', ' ', ”

# Segundo carácter: color
# http://matplotlib.org/1.4.2/api/colors_api.html

# Tercer carácter: forma del símbolo
# http://matplotlib.org/1.4.2/api/markers_api.html

plt.plot(x, y1, '-ro')
plt.plot(x, y2, '--g^')

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()