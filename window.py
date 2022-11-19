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
        
        # draw trails    
        for i in range(len(player1_trail.locations)):
            self.display.blit(player1_trail.image, (player1_trail.locations[i][0], player1_trail.locations[i][1]))
        for j in range(len(player2_trail.locations)):
            self.display.blit(player2_trail.image, (player2_trail.locations[j][0], player2_trail.locations[j][1]))
        
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