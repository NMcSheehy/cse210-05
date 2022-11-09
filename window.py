import pygame
pygame.init()

class Window():
    # holds the display for the game
    # updates the window every frame
    def __init__(self, width, height, name, background) -> None:
        self.width = width
        self.height = height
        self.name = name
        self.background = background 


        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)

    def draw(self):
        # This has to be in order from bottom layer to top layer. 
        # Other wise the back ground will just draw over the scene
        # Background Color
        self.display.fill(self.background)

        # Change the screen
        pygame.display.update()