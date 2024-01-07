import pygame

pygame.init()

# dimensions of screen
width = 1000
height = 667

# Create game window with custom icon and title
icon = pygame.image.load("Images/GameIcon.jpeg")
pygame.display.set_icon(icon)
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First 2D Platformer Game!")

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
""" This class handles sprite sheets
This was taken from www.scriptefun.com/transcript-2-using
sprite-sheets-and-drawing-the-background
I've added some code to fail if the file wasn't found..
Note: When calling images_at the rect is the format:
(x, y, x + offset, y + offset)"""


class SpriteSheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey=None):
        """Loads image from x,y,x+offset,y+offset"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha() #pygame.SRCALPHA
        image.blit(self.sheet, (0, 0), rect)
        image = pygame.transform.smoothscale_by(image, 0.6)

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a series of images and return them as a list
    def images_at(self, rects, colorkey=None):
        """Loads multiple images, supply a list of coordinates"""
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        """Loads a strip of images and returns them as a list"""
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


# ------------------------------------------------------------------------------------------------------------------------
# Player sprite sheet: (100, 65), ()
idleFrames = SpriteSheet("PlayerAnimations/PC_Idle.png")
idleFramePos = [(76, 70, 90, 120), (310, 70, 125, 120), (560, 70, 135, 120), (820, 70, 130, 120),
               (76, 335, 96, 100), (310, 335, 125, 100), (560, 335, 135, 100), (820, 335, 130, 100),
               (76, 590, 96, 105), (310, 590, 125, 105), (560, 590, 125, 105), (820, 590, 130, 105),
               (76, 840, 96, 115), (310, 840, 125, 115), (560, 840, 125, 115), (820, 840, 130, 115)]

# (1, 0, 256, 256), (2, 0, 256, 256), (3, 0, 256, 256),
#                 (0, 1, 256, 256), (1, 1, 256, 256), (2, 1, 256, 256), (3, 1, 256, 256),
#                 (0, 2, 256, 256), (1, 2, 256, 256), (2, 2, 256, 256), (3, 2, 256, 256),
#                 (0, 3, 256, 256), (1, 3, 256, 256), (2, 3, 256, 256), (3, 3, 256, 256)

runFrames = SpriteSheet("PlayerAnimations/PC_Run.png")
runFramePos = [(76, 70, 90, 120), (310, 70, 125, 120), (560, 70, 135, 120), (820, 70, 130, 120),
               (76, 335, 96, 100), (310, 335, 125, 100), (560, 335, 135, 100), (820, 335, 130, 100),
               (76, 590, 96, 105), (310, 590, 125, 105), (560, 590, 125, 105), (820, 590, 130, 105),
               (76, 840, 96, 115), (310, 840, 125, 115), (560, 840, 125, 115), (820, 840, 130, 115),
               (76, 1100, 96, 115), (310, 1100, 125, 115)]

jumpFrames = SpriteSheet("PlayerAnimations/PC_Jump.png")
jumpFramePos = [(76, 70, 90, 120), (310, 70, 125, 120), (560, 70, 135, 120), (820, 70, 130, 120),
               (76, 335, 96, 100), (310, 335, 125, 100)]

fallFrames = SpriteSheet("PlayerAnimations/PC_Landing.png")
fallFramePos = [(76, 70, 90, 120), (310, 70, 125, 120), (560, 70, 135, 120), (820, 70, 130, 120),
               (76, 335, 96, 100), (310, 335, 125, 100), (560, 335, 135, 100), (820, 335, 130, 100),
               (76, 590, 96, 105), (310, 590, 125, 105), (560, 590, 125, 105), (820, 590, 130, 105),
               (76, 840, 96, 115), (310, 840, 125, 115), (560, 840, 125, 115), (820, 840, 130, 115)]
