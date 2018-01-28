import pygame
from funcion_bloque import *

class RectanguloSaltarin(Bloque):






    def update (self):



        self.rect.x += 2
        self.rect.y += 2

        if self.rect.x > 300 or self.rect.x < 0:
            self.rect.x -= 4


