import pygame

class Bloque(pygame.sprite.Sprite):

    # Constructor. Pasa el color al bloque,
    # y su posición x e y
    def __init__(self, color, largo, alto):
        # Llama al constructor de la clase padre (Sprite)
        pygame.sprite.Sprite.__init__(self)

        # Crea una imagen del bloque y lo rellena de color.
        # Esto podría ser también una imagen cargada desde el disco duro.
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)

        # Obtenemos el objeto rectángulo que posee las dimensiones de la imagen
        # Actualizamos la posición de ese objeto estableciendo los valores para
        # rect.x y rect.y
        self.rect = self.image.get_rect()