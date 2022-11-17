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
            # Store all of the game changes here.

            player1.move()
            player2.move()
            
            player1_trail.add_location(player1.x, player1.y) 
            

            # Update window
            window.draw(player1, player2, player1_trail, player2_trail)
        pygame.quit()
        
class Rounds():
    pass

class Game_over():
    pass