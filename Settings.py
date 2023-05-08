import pygame

pygame.init()

# dimensions of screen
width = 1000
height = 667

blockSize = 64

level_1 = [
    '                            ',
    '                            ',
    '                            ',
    ' XX    XXX            XX    ',
    ' XX P                       ',
    ' XXXX         XX         XX ',
    ' XXXX       XX              ',
    ' XX    X  XXXX    XX  XX    ',
    '       X  XXXX    XX  XXX   ',
    '    XXXX  XXXXXX  XX  XXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXX  ']

level1_height = blockSize * len(level_1)

level_maps = {1: level_1}

water = pygame.image.load("Images/water.png")
sky = pygame.image.load("Images/sky2.png")
