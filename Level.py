import pygame
from Block import Block
from Settings import blockSize


class Level:
    def __init__(self, level_map, surface):
        self.blocks = None
        self.screen = surface
        self.setup(level_map)

        # determines the number of pixels to scroll through
        self.levelShift = 0

    def setup(self, level_map):
        self.blocks = pygame.sprite.Group()

        # loop through level array and create block sprites to create level map
        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                if col == 'X':
                    block = Block((col_index * blockSize, row_index * blockSize), blockSize)
                    self.blocks.add(block)


    def generate(self):
        self.blocks.update(self.levelShift)
        self.blocks.draw(self.screen)
