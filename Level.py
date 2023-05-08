import pygame
from Block import Block
from Player import Player
from Settings import *


class Level:
    def __init__(self, level_map, surface):
        self.blocks = None
        self.display_surface = surface
        self.setup(level_map)

        # determines the number of pixels to scroll through
        self.levelShift = 0

    def setup(self, level_map):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # loop through level array and create block sprites to create level map
        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                currentPosition = (col_index * blockSize, row_index * blockSize)
                if col == 'X':
                    block = Block(currentPosition)
                    self.blocks.add(block)

                elif col == 'P':
                    player = Player(currentPosition)
                    self.player.add(player)

    def levelScroll(self):
        player = self.player.sprite
        playerPosX = player.rect.centerx
        playerDir = player.dir.x

        if playerPosX < (width // 5) and playerDir < 0:
            self.levelShift = 8
            player.speed = 0

        elif playerPosX > (4 * width // 5) and playerDir > 0:
            self.levelShift = -8
            player.speed = 0

        else:
            self.levelShift = 0
            player.speed = 8


    def horizontalCollisions(self):
        player = self.player.sprite

        # applies horizontal movement
        player.rect.x += player.dir.x * player.speed

        # checks for horizontal collision with blocks
        for block in self.blocks.sprites():
            if block.rect.colliderect(player.rect):
                if player.dir.x < 0:
                    player.rect.left = block.rect.right
                elif player.dir.x > 0:
                    player.rect.right = block.rect.left

    def verticalCollisions(self):
        player = self.player.sprite

        # applies player falling motion
        player.applyGravity()

        # checks for vertical collision with blocks
        for block in self.blocks.sprites():
            if block.rect.colliderect(player.rect):
                if player.dir.y > 0:
                    player.rect.bottom = block.rect.top
                    player.dir.y = 0
                    player.isFalling = False
                elif player.dir.y < 0:
                    player.rect.top = block.rect.bottom
                    player.dir.y = 0

    def generate(self):

        self.display_surface.fill("Black")
        self.display_surface.blit(pygame.transform.scale_by(sky, 1), (-200, 0))
        #self.display_surface.blit(pygame.transform.scale_by(water, 5), (0, 600))
        # for creating level map
        self.blocks.update(self.levelShift)
        self.blocks.draw(self.display_surface)

        # player camera
        self.levelScroll()

        # for positioning player on screen
        self.player.update()
        self.horizontalCollisions()
        self.verticalCollisions()
        self.player.draw(self.display_surface)
