import pygame
from Settings import *
import os


def readAnimations(path):
    animations = []

    for _, _, frames in os.walk(path):
        for frame in frames:
            image = pygame.image.load(path + "/" + frame).convert_alpha()
            animations.append(image)

    return animations


# class for player
class Player(pygame.sprite.Sprite):
    # initialize the player attributes and set spawn point in level map.
    def __init__(self, spawnPoint):
        super().__init__()

        # player direction, movement speed, gravity, jumping speed and falling status are initialized
        self.dir = pygame.math.Vector2((0, 0))
        self.speed = 8
        self.gravity = 0.5
        self.jumpingSpeed = -15
        self.isFalling = False
        self.orientationRight = True
        self.onGround = False
        self.onTop = False
        self.onLeft = False
        self.onRight = False

        # load player animation frames into a dictionary
        self.animation = self.getPlayerAnimations()
        # initialize player current animation frame index and animation speed
        self.lastUpdate = 0
        self.frameIndex = 0
        self.animationSpeed = 0.15
        self.state = self.getPlayerState()

        # set player image and spawn point in level map
        self.image = self.animation[self.state][self.frameIndex]  # pygame.image.load("Images/Dude_Monster.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=spawnPoint)

    # This method gets the player animation frames from the sprite sheet and returns them in a dictionary.
    def getPlayerAnimations(self):
        # load sprite sheet images as arrays and set them to variables.
        transparencyColour = (255, 255, 255)
        idlePlayerFrames = idleFrames.images_at(idleFramePos, transparencyColour)
        runPlayerFrames = runFrames.images_at(runFramePos, transparencyColour)
        jumpPlayerFrames = jumpFrames.images_at(jumpFramePos, transparencyColour)
        fallPlayerFrames = fallFrames.images_at(fallFramePos, transparencyColour)

        # idlePlayerFrames = readAnimations("PlayerAnimations/graphics/character/idle")
        # runPlayerFrames = readAnimations("PlayerAnimations/graphics/character/run")
        # jumpPlayerFrames = readAnimations("PlayerAnimations/graphics/character/jump")
        # fallPlayerFrames = readAnimations("PlayerAnimations/graphics/character/fall")

        # create a dictionary of the animations mapping the name of the animation type to the
        # corresponding array of frames and return it
        animations = {"idle": idlePlayerFrames, "run": runPlayerFrames, "jump": jumpPlayerFrames,
                      "fall": fallPlayerFrames}

        return animations

    def animate(self):
        animation = self.animation[self.getPlayerState()]

        # cycle through animation frames based on animation speed
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0

        frame = animation[int(self.frameIndex)]
        if self.orientationRight:
            self.image = frame
        else:
            self.image = pygame.transform.flip(frame, True, False)

        # realign surface with collision object:
        if self.onGround and self.onLeft:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.onGround and self.onRight:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.onGround:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.onTop and self.onLeft:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.onTop and self.onRight:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.onTop:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)


    def getPlayerState(self):
        if self.dir.y < 0:
            return "jump"
        elif self.dir.y > 1:
            return "fall"
        elif self.dir.x != 0 and self.dir.y == 0:
            return "run"
        else:
            return "idle"

    # This method gets the user keyboard input and initiates the intended action.
    def getUserControl(self):
        # gets user keyboard input
        control = pygame.key.get_pressed()

        # check if "A" or "D" is pressed and set player's horizontal direction accordingly
        if control[pygame.K_d]:
            self.dir.x = 1
            self.orientationRight = True
        elif control[pygame.K_a]:
            self.dir.x = -1
            self.orientationRight = False
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
        self.animate()
