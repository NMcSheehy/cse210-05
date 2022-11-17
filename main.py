# Import modules #
import pygame
pygame.init()

# Import Classes #
from director import Director
from window import *
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

    # Parent class Objects require (image file path, width, height, x, y, speed)
    player1 = Player1('red_bike_sprite.png', 10, 10, 250, 300, 5)
    player2 = Player2('blue_bike_sprite.png', 10, 10, 750, 500, 5)
    
    # (Game FPS)
    game = Director(60)

    # Start the game
    game.start(window, player1, player2)

if __name__ == '__main__':
    main()