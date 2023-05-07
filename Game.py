import pygame
import sys
from Settings import *
from Text import Text
from Block import Block
from Level import Level

pygame.init()

# initialize game clock to maintain frame rate
clock = pygame.time.Clock()

# Create game window with custom icon and title
icon = pygame.image.load("Images/GameIcon.jpeg")
pygame.display.set_icon(icon)
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome to The Game")

# Setting up font and generating the title of the game as a surface
gameTitle = pygame.sprite.GroupSingle()
gameTitle.add(Text("Adventure Awaits", 50, (204, 255, 153), 225, 50))

start = pygame.sprite.GroupSingle()
start.add(Text("PLAY", 50, (204, 255, 153), 500, 350))

back = pygame.sprite.GroupSingle()
back.add(Text("Back", 50, (204, 255, 153), 925, 50))

menuBackground = pygame.image.load("Images/MenuBackground.png").convert_alpha()


class Game:
    def __init__(self):
        self.state = "menu"
        self.levelSet = pygame.sprite.Group()
        self.currentLevel = None

    def levels(self):

        offset = 0
        for i in range(5):
            self.levelSet.add(Text(f"Level {i + 1}", 30, (204, 255, 153), 75 + offset, 350))
            offset += 200

    def run(self):
        # This infinite loop allows the game to continue running until the user exits the game.
        while True:

            # This for loop determines if the user wants to quit the game. If they do the game quits and the program terminates
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "menu" and start.sprite.rect.collidepoint(event.pos):
                        self.state = "level_select"

                    elif self.state == "level_select":
                        if back.sprite.rect.collidepoint(event.pos):
                            self.state = "menu"

                        for i in range(len(self.levelSet.sprites())):
                            if self.levelSet.sprites()[i].rect.collidepoint(event.pos):
                                self.state = f"in_level_{i + 1}"
                                display.fill((204, 255, 255))
                                self.currentLevel = Level(level_maps.get(i+1), display)
                                break

                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    if self.state[0:8] == "in_level":
                        self.state = "level_select"

            if self.state == "menu":
                # display the game titles, options and background
                display.blit(menuBackground, (0, 0))
                gameTitle.draw(display)
                start.draw(display)

            if self.state == "level_select":
                display.blit(pygame.transform.flip(menuBackground, True, False), (0, 0))
                gameTitle.draw(display)
                back.draw(display)
                self.levelSet.draw(display)

            if self.state[0:8] == "in_level":
                self.currentLevel.generate()


            # loop continuously updates game screen to reflect current state
            pygame.display.update()

            # sets max FPS to 60 so that while loop occurs no more than 60 times a second
            clock.tick(60)


game = Game()
game.levels()
game.run()
