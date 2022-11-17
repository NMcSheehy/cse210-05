import pygame
from object import *
from director import *
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

    def draw(self, player1, player2):
        # This has to be in order from bottom layer to top layer. 
        # Other wise the back ground will just draw over the scene
        # Background Color
        self.display.fill(self.background)

        # draw players
        self.display.blit(player1.image, (player1.x, player1.y))
        self.display.blit(player2.image, (player2.x, player2.y))
        
        # Change the screen
        pygame.display.update()
        
        
class Wall():
    def __init__(self):
        pass 
    
    def crash():
        pass