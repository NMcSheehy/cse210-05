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


power ups
rounds
    game over
'''


def main():
    # Load all of your classesd
    

    # (width, height, name, background color (R,G,B))
    window = Window(1000, 750, 'Torn Legends! (definetly not Tron)', (0,0,0))

    # Parent class Objects require (image file path, width, height, x, y, speed)
    player1 = Player1('red_bike_sprite.png', 10, 10, 250, 250, 5)
    player2 = Player2('blue_bike_sprite.png', 10, 10, 750, 500, 5)
    player = Player("White.png", 0, 0, 0, 0, 0)
    player1_trail = Player1_trail('red_trail.png', 10, 10, player1.x, player1.y)
    player2_trail = Player2_trail('blue_trail.png', 10, 10, player2.x, player2.y)
    
    # (Game FPS)
    game = Director(60)
    
    # Start the game
    game.start(window, player1, player2, player1_trail, player2_trail, player)

if __name__ == '__main__':
    main()