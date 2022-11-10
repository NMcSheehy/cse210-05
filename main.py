# Import modules #
import pygame
pygame.init()

# Import Classes #
from director import Director
from window import Window
from object import *

## Classes ##
'''
Director
Window
Object
    Player 
        Player 1
            player 1 trail
            player 1 particles
            player 1 score 

        player 2
            player 2 trail
            player 2 particles
            player 2 score

Walls
power ups
rounds
    game over
'''


def main():
    # Load all of your classes

    # (width, height, name, background color (R,G,B))
    window = Window(1000, 750, 'Torn Legends! (definetly not Tron)', (0,0,0))

    # Parrent class Objects require (image file path, width, height, x, y, speed)

    # (Game FPS)
    game = Director(60)

    # Start the game
    game.start(window)

if __name__ == '__main__':
    main()