import pygame
from window import *
from object import *
pygame.init()


class Director():
    # Manages the game (movement / collision)
    # holds the loop
    # keeps the game playing
    def __init__(self, FPS) -> None:
        self.playing = True
        self.crash1 = True
        self.crash2 = True
        self.crash3 = True
        self.crash4 = True
        self.FPS = FPS

        # Setup the game clock (FPS)
        self.clock = pygame.time.Clock()

    def start(self, window, player1, player2, player1_trail, player2_trail):
        # holds game loop aslong as self.playing is True
        while self.playing:
            # Make sure Frame Rate doesn't go over FPS
            self.clock.tick(self.FPS)

            # Keep track of the in game events
            for event in pygame.event.get():

                # Event: Quit game
                if event.type == pygame.QUIT:
                    self.playing = False
                    
                if self.crash1 == False:
                    self.playing = False
                
                if self.crash2 == False:
                    self.playing = False
                    
                if self.crash3 == False:
                    self.playing = False
                
                if self.crash4 == False:
                    self.playing = False
            
            # Store all of the game changes here.

            player1.move()
            player2.move()
            
            
            
            self.crash1 = player1.crash_wall(player1.x, player1.y, self.crash1)
            self.crash2 = player2.crash_wall(player2.x, player2.y, self.crash2)
            self.crash3 = player1.crash_trail(player1.x, player1.y, self.crash3, player1_trail, player2_trail)
            self.crash4 = player1.crash_trail(player2.x, player2.y, self.crash4, player1_trail, player2_trail)
            
            player1_trail.add_location(player1.x, player1.y) 
            player2_trail.add_location(player2.x, player2.y)
            # Update window
            window.draw(player1, player2, player1_trail, player2_trail)
        pygame.quit()
        
class Rounds():
    pass

class Game_over():
    pass