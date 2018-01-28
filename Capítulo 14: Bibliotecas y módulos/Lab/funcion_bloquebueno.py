from funcion_bloque import *
import random




class BloqueBueno(Bloque):



    def update(self):

        self.rect.x += random.randrange (-3, 4)
        self.rect.y += random.randrange (-3, 4)

