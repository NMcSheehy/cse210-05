# Import modules
import pygame
pygame.init()

# Import Classes
from director import Director
from window import Window
from object import Object

def main():
    print('Hello World!')
    # Load all of your classes

    # (width, height, name, background color (R,G,B))
    window = Window(500, 500, 'window', (0,0,0))

    # Parrent class Objects require (image file path, width, height, x, y, speed)

    # (Game FPS)
    game = Director(60)

    # Start the game
    game.start(window)

if __name__ == '__main__':
    main()