import pygame
from Settings import *


# class for player
class Player(pygame.sprite.Sprite):
    # initialize the player attributes and set spawn point in level map.
    def __init__(self, spawnPoint):
        super().__init__()

        self.animation = {"idle": [], "run": [], "jump": [], "fall": []}  # dictionary to store player animations
        self.getPlayerAnimations()
        self.frameIndex = 0
        self.animationSpeed = 0.15

        self.image = self.animation["idle"][self.frameIndex] #pygame.image.load("Images/Dude_Monster.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=spawnPoint)

        # player direction, movement speed, gravity, jumping speed and falling status are initialized
        self.dir = pygame.math.Vector2((0, 0))
        self.speed = 8
        self.gravity = 0.5
        self.jumpingSpeed = -15
        self.isFalling = False


    def getPlayerAnimations(self):
        idlePlayerFrames = idleFrames.images_at(idleFramePos)
        runPlayerFrames = runFrames.images_at(runFramePos)
        jumpPlayerFrames = jumpFrames.images_at(jumpFramePos)
        fallPlayerFrames = fallFrames.images_at(fallFramePos)

        self.animation["idle"] = idlePlayerFrames
        self.animation["run"] = runPlayerFrames
        self.animation["jump"] = jumpPlayerFrames
        self.animation["fall"] = fallPlayerFrames

    # This method gets the user keyboard input and initiates the intended action.
    def getUserControl(self):
        # gets user keyboard input
        control = pygame.key.get_pressed()

        # check if "A" or "D" is pressed and set player's horizontal direction accordingly
        if control[pygame.K_d]:
            self.dir.x = 1
        elif control[pygame.K_a]:
            self.dir.x = -1
        else:
            self.dir.x = 0

        # check if "W" is pressed and if player is standing on surface to jump.
        if control[pygame.K_w] and self.dir.y <= 0 and not self.isFalling:
            self.jump()
            self.isFalling = True

    # This method applies gravity to the player and makes them fall when not in contact with ground.
    def applyGravity(self):
        self.dir.y += self.gravity
        self.rect.y += self.dir.y

    # This method makes the player jump when called.
    def jump(self):
        self.dir.y = self.jumpingSpeed

    # Override the default update method for sprites for users to control player.
    def update(self):
        self.getUserControl()
