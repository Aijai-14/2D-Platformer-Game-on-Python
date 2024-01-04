import pygame
from SpriteSheet import *

pygame.init()

# dimensions of screen
width = 1000
height = 667

# dimensions of block unit in pixels (block is a square)
blockSize = 64

# array representing the level map of the first level
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

# height of the first level in pixels
level1_height = blockSize * len(level_1)

# dictionary that maps level numbers to their respective level maps
level_maps = {1: level_1}

# ------------------------------------------------------------------------------------------------------------------------
# load game assets.
water = pygame.image.load("Images/Game World Assets/Background/BG-4.png")
water = pygame.transform.smoothscale(water, (1000, 300))

sky = pygame.image.load("Images/sky2.png")
sky = pygame.transform.smoothscale(sky, (1000, 1000))

mountains = pygame.image.load("Images/Game World Assets/Background/BG-2.png")
mountains = pygame.transform.smoothscale(mountains, (1000, 600))

# ------------------------------------------------------------------------------------------------------------------------
# Player sprite sheet:
idleFrames = SpriteSheet("PlayerAnimations/PC_Idle.png")
idleFramePos = [(0, 0, 256, 256), (1, 0, 256, 256), (2, 0, 256, 256), (3, 0, 256, 256),
                (0, 1, 256, 256), (1, 1, 256, 256), (2, 1, 256, 256), (3, 1, 256, 256),
                (0, 2, 256, 256), (1, 2, 256, 256), (2, 2, 256, 256), (3, 2, 256, 256),
                (0, 3, 256, 256), (1, 3, 256, 256), (2, 3, 256, 256), (3, 3, 256, 256)]

runFrames = SpriteSheet("PlayerAnimations/PC_Run.png")
runFramePos = [(0, 0, 256, 256), (1, 0, 256, 256), (2, 0, 256, 256), (3, 0, 256, 256),
                (0, 1, 256, 256), (1, 1, 256, 256), (2, 1, 256, 256), (3, 1, 256, 256),
                (0, 2, 256, 256), (1, 2, 256, 256), (2, 2, 256, 256), (3, 2, 256, 256),
                (0, 3, 256, 256), (1, 3, 256, 256), (2, 3, 256, 256), (3, 3, 256, 256),
                (0, 4, 256, 256), (1, 4, 256, 256)]

jumpFrames = SpriteSheet("PlayerAnimations/PC_Jump.png")
jumpFramePos = [(0, 0, 256, 256), (1, 0, 256, 256), (2, 0, 256, 256), (3, 0, 256, 256),
                (4, 0, 256, 256), (5, 0, 256, 256)]

fallFrames = SpriteSheet("PlayerAnimations/PC_Landing.png")
fallFramePos = [(0, 0, 256, 256), (1, 0, 256, 256), (2, 0, 256, 256), (3, 0, 256, 256),
                (0, 1, 256, 256), (1, 1, 256, 256), (2, 1, 256, 256), (3, 1, 256, 256),
                (0, 2, 256, 256), (1, 2, 256, 256), (2, 2, 256, 256), (3, 2, 256, 256),
                (0, 3, 256, 256), (1, 3, 256, 256), (2, 3, 256, 256), (3, 3, 256, 256)]
