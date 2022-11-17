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

    def draw(self, player1, player2, player1_trail, player2_trail):
        # This has to be in order from bottom layer to top layer. 
        # Other wise the back ground will just draw over the scene
        # Background Color
        self.display.fill(self.background)
        
        # draw players
        self.display.blit(player1.image, (player1.x, player1.y))
        self.display.blit(player2.image, (player2.x, player2.y))
        
        # draw trails    
        for i in range(len(player1_trail.locations)):
            if i == 0:
                self.display.blit(player1_trail.image, (player1_trail.locations[i][0], player1_trail.locations[0][1]))
                self.display.blit(player2_trail.image, (player2_trail.x, player2_trail.y))
        
        
        # Change the screen
        pygame.display.update()
        
        
class Wall():
    def __init__(self):
        pass 
    
    def crash():
        pass