from funcion_bloque import *
import random

class BloqueMalo (Bloque):

    def update(self):

        self.rect.y += 2

        if self.rect.y > 710:
            self.rect.y = -20
            self.rect.x = random.randrange (0, 501)
