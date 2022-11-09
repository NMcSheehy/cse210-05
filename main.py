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

    # No paramaters
    game = Director()

    # (width, height, name, background, FPS)
    window = Window()

    # Parrent class Objects require (image file path, width, height, x, y, speed)

if __name__ == '__main__':
    main()