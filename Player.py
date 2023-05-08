import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, spawnPoint):
        super().__init__()
        self.image = pygame.image.load("Images/Dude_Monster.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=spawnPoint)

        # player movement and velocity
        self.dir = pygame.math.Vector2((0, 0))
        self.speed = 8
        self.gravity = 0.5
        self.jumpingSpeed = -15
        self.isFalling = False

    def getUserControl(self):
        control = pygame.key.get_pressed()

        if control[pygame.K_d]:
            self.dir.x = 1

        elif control[pygame.K_a]:
            self.dir.x = -1

        else:
            self.dir.x = 0

        if control[pygame.K_w] and self.dir.y <= 0 and not self.isFalling:
            self.jump()
            self.isFalling = True

    def applyGravity(self):
        self.dir.y += self.gravity
        self.rect.y += self.dir.y

    def jump(self):
        self.dir.y = self.jumpingSpeed

    # Override the default update method for player movement
    def update(self):
        self.getUserControl()
