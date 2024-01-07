import pygame
import sys
from Settings import *
from Text import Text
from Block import Block
from Level import Level

pygame.init()

# initialize game clock to maintain frame rate
clock = pygame.time.Clock()

# Set the initial prompts for the game on the menu screen.
gameTitle = pygame.sprite.GroupSingle()
gameTitle.add(Text("Ninja Crawler", 50, (204, 255, 153), 225, 50))

start = pygame.sprite.GroupSingle()
start.add(Text("PLAY", 50, (204, 255, 153), 500, 350))

back = pygame.sprite.GroupSingle()
back.add(Text("Back", 50, (204, 255, 153), 925, 50))

# create a background for main menu
menuBackground = pygame.image.load("Images/MenuBackground.png").convert_alpha()


# class that controls the game
class Game:
    # initialize the game interface and set the initial state to menu
    def __init__(self):
        self.state = "menu"

        # create a sprite group for the level select buttons and set the current level to None
        self.levelSet = pygame.sprite.Group()
        self.currentLevel = None

    # This method creates the level select buttons and adds them to the levelSet sprite group
    def levels(self):

        offset = 0
        for i in range(5):
            self.levelSet.add(Text(f"Level {i + 1}", 30, (204, 255, 153), 100 + offset, 350))
            offset += 200

    # This method runs the game
    def run(self):
        # This infinite loop allows the game to continue running until the user exits the game.
        while True:
            # This for loop checks for events that occur in the game
            for event in pygame.event.get():
                # This if statement checks if the user has exited the game and stops the program if they have exited.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if "PLAY" is clicked on the menu screen, the state is changed to level_select screen
                    if self.state == "menu" and start.sprite.rect.collidepoint(event.pos):
                        self.state = "level_select"

                    elif self.state == "level_select":
                        # if "Back" is clicked on the level_select screen, the state is changed to menu screen
                        if back.sprite.rect.collidepoint(event.pos):
                            self.state = "menu"

                        # otherwise, the level that was clicked on is loaded
                        for i in range(len(self.levelSet.sprites())):
                            if self.levelSet.sprites()[i].rect.collidepoint(event.pos):
                                self.state = f"in_level_{i + 1}"
                                self.currentLevel = Level(level_maps.get(i+1), display)
                                break

                # if "q" is pressed, the level closes and takes user back to level select screen
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    if self.state[0:8] == "in_level":
                        self.state = "level_select"

                # if "r" is pressed, the level resets and player respawns
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    if self.state[0:8] == "in_level":
                        self.currentLevel.setup(level_maps.get(int(self.state[9])))

            # if the state is menu, then the menu screen is displayed
            if self.state == "menu":
                # display the game titles, options and background
                display.blit(menuBackground, (0, 0))
                gameTitle.draw(display)
                start.draw(display)

            # if the state is level_select, then the level select screen is displayed
            if self.state == "level_select":
                display.blit(menuBackground, (0, 0))
                gameTitle.draw(display)
                back.draw(display)
                self.levelSet.draw(display)

            # if the state is "in_level_[integer]", then the level is displayed
            if self.state[0:8] == "in_level":
                self.currentLevel.generate()

            # loop continuously updates game screen to reflect current state
            pygame.display.update()

            # sets max FPS to 60 so that while loop occurs no more than 60 times a second
            clock.tick(60)


# create a game object and run the game.
game = Game()
game.levels()
game.run()
