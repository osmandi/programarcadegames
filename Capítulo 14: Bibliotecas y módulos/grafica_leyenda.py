import matplotlib.pyplot as plt

x =  [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

plt.plot(x, y1, label = "Serie 1")
plt.plot(x, y2, label = "Serie 2")

leyenda = plt.legend(loc = 'upper center', shadow = True, fontsize = 'x-large')
leyenda.get_frame().set_facecolor('#00FFCC')

plt.ylabel('Valor del Elemento')
plt.xlabel('Elemento')

plt.show()