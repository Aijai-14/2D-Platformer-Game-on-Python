import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=position)

    def shift(self, horizontalShift):
        self.rect.x += horizontalShift