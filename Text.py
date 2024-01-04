import pygame


# class for text objects
class Text(pygame.sprite.Sprite):
    # initialize the text object with the font, text colour, text size and position of the text.
    def __init__(self, text, text_size, text_color, x_position, y_position):
        super().__init__()
        self.font = pygame.font.Font("Fonts/PixieFont.ttf", text_size)
        self.image = self.font.render(text, False, text_color)
        self.rect = self.image.get_rect(midbottom=(x_position, y_position))
