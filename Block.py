import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("Images/block.png").convert_alpha()
        #self.resized = pygame.Surface((size, size))
        #pygame.transform.scale(self.image, (size, size), self.resized)
        self.rect = self.image.get_rect(topleft=position)

    # Override the default update method for level scrolling
    def update(self, horizontalShift):
        self.rect.x += horizontalShift
