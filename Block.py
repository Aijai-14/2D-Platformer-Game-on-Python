import pygame


# class for block objects
class Block(pygame.sprite.Sprite):
    # initialize the block object with the position of the sprite rectangle
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("Images/Game World Assets/Ground/6.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=position)

    # Override the default update method for level scrolling;
    # This method shifts the block horizontally by the amount specified by the horizontalShift parameter
    def update(self, horizontalShift):
        self.rect.x += horizontalShift
