import pygame
from Block import Block
from Player import Player
from Settings import *


# class to create and display a level
class Level:
    def __init__(self, levelArray, surface):
        # initialize the block structure of level to None, the player to None
        # and the display surface to the game window.
        self.blocks = None
        self.player = None
        self.display_surface = surface

        # draw the level based on the level structure given by the array levelArray
        self.setup(levelArray)

        # determines the number of pixels to scroll through when character moves through level
        self.levelShift = 0

        self.collisionX = 0

    # This method creates the map of the level and adds the player to the level
    def setup(self, level_map):
        # create sprite groups for blocks and player
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # loop through level array and create block sprites to create level map
        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                # calculate the position of the block in screen space.
                currentPosition = (col_index * blockSize, row_index * blockSize)

                # check what the value in the array is and create the appropriate sprite and add it to the level
                if col == 'X':
                    block = Block(currentPosition)
                    self.blocks.add(block)
                elif col == 'P':
                    player = Player(currentPosition)
                    self.player.add(player)

    # This method shifts the level horizontally when the player reaches the edge of the screen.
    def levelScroll(self):
        # get the player sprite and its x position and horizontal direction
        player = self.player.sprite
        playerPosX = player.rect.centerx
        playerDir = player.dir.x

        # check if player is at the edge of the screen on either side and set the levelShift accordingly;
        # otherwise set the levelShift to 0 so player can move freely.
        if playerPosX < (width // 5) and playerDir < 0:
            self.levelShift = 8
            player.speed = 0
        elif playerPosX > (4 * width // 5) and playerDir > 0:
            self.levelShift = -8
            player.speed = 0
        else:
            self.levelShift = 0
            player.speed = 8

    # This method checks for horizontal collisions between the player and blocks in the level.
    def horizontalCollisions(self):
        player = self.player.sprite

        # applies horizontal movement
        player.rect.x += player.dir.x * player.speed

        # checks for horizontal collision with blocks in levels
        for block in self.blocks.sprites():
            if block.rect.colliderect(player.rect):
                # based on player direction align player with block against the direction of movement.
                if player.dir.x < 0:
                    player.rect.left = block.rect.right
                    player.onLeft = True
                    self.collisionX = player.rect.left
                elif player.dir.x > 0:
                    player.rect.right = block.rect.left
                    player.onRight = True
                    self.collisionX = player.rect.right

        if player.onLeft and (player.dir.x >= 0 or player.rect.left < self.collisionX):
            player.onLeft = False
        if player.onRight and (player.dir.x <= 0 or player.rect.right > self.collisionX):
            player.onRight = False

    # This method checks for vertical collisions between the player and blocks in the level.
    def verticalCollisions(self):
        player = self.player.sprite

        # applies player falling motion
        player.applyGravity()

        # checks for vertical collision with blocks
        for block in self.blocks.sprites():
            if block.rect.colliderect(player.rect):
                # based on player direction align player with block against the direction of movement.
                # if the collision is below then isFalling is set to False to indicate that the player is on the ground.
                if player.dir.y > 0:
                    player.rect.bottom = block.rect.top
                    player.dir.y = 0
                    player.isFalling = False
                    player.onGround = True
                elif player.dir.y < 0:
                    player.rect.top = block.rect.bottom
                    player.dir.y = 0
                    player.onTop = True

        if player.onGround and player.dir.y < 0 or player.dir.y > 1:
            player.onGround = False

        if player.onTop and player.dir.y > 0:
            player.onTop = False

    # This method generates the level and displays it on the screen.
    def generate(self):
        # display the background
        self.display_surface.fill("Black")
        self.display_surface.blit(sky, (0, -400))
        self.display_surface.blit(mountains, (0, 200))
        self.display_surface.blit(water, (0, 375))

        # shift the level if needed and draw the blocks to screen
        self.blocks.update(self.levelShift)
        self.blocks.draw(self.display_surface)

        # move the level based on player position if needed.
        self.levelScroll()

        # user controls player and game checks for collisions to draw player properly to the screen.
        self.player.update()
        self.horizontalCollisions()
        self.verticalCollisions()
        self.player.draw(self.display_surface)
