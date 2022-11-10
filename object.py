import pygame
pygame.init()

class Object():
    # Parrent class for creating objects on screen
    def __init__(self, path, width, height, x, y, speed):
        self.path = path
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed

        # Load in image / hitbox
        self.image_l = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image_l, (self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def crash():
        pass
        
        
class Player(Object):
    pass

class Player1(Player):
    pass

class Player1_trail(Player1):
    pass

class Player1_particles(Player1):
    pass

class Player1_score(Player1):
    pass

class Player2(Player):
    pass

class Player2_trail(Player2):
    pass

class Player2_particles(Player2):
    pass

class Player2_score(Player2):
    pass

class Power_ups():
    pass