import pygame
pygame.init()
from director import *

class Object():
    # Parent class for creating objects on screen
    def __init__(self, path, width, height, x, y, speed):
        self.path = path
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.playing = True

        # Load in image / hitbox
        self.image_l = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image_l, (self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        
class Player(Object):
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)
    
    def move(self, playing):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.QUIT]:
            playing = False
        return playing
        
class Player1(Player):
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)
        self.direction = "right"
        
    def move(self):
        
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.K_w]:
            self.direction = "up"
        elif key_pressed[pygame.K_a]:
            self.direction = "left"
        elif key_pressed[pygame.K_s]:
            self.direction = "down"
        elif key_pressed[pygame.K_d]:
            self.direction = "right"
            
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "down":
            self.y += self.speed
        if self.direction == "right":
            self.x += self.speed
        
        
    def crash_wall(self, x, y, playing):
        if x <=0 or x >= 1000:
            playing = False
        if y <= 0 or y >= 750:
            playing = False
        return playing
            
    def crash_trail(self, x, y, playing, player1_trail, player2_trail):
        
        for trail in player1_trail.locations:
            if [x,y] == trail:
                playing = False
        for trail in player2_trail.locations:
            if [x,y] == trail:
                playing = False
        return playing
            
class Player1_trail():
    def __init__(self, path, width, height, x, y):
        self.x = x
        self.y = y
        self.path = path
        self.width = width
        self.height = height
        self.locations = [[self.x, self.y]]
        
        self.image_l = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image_l, (self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def add_location(self, new_x, new_y):
        self.locations.append([new_x, new_y])

class Player1_particles(Player1):
    pass

class Player1_score(Player1):
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)

class Player2(Player):
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)
        self.direction = "left"
        
    def move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.direction = "up"
        if key_pressed[pygame.K_LEFT]:
            self.direction = "left"
        if key_pressed[pygame.K_DOWN]:
            self.direction = "down"
        if key_pressed[pygame.K_RIGHT]:
            self.direction = "right"

    
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "down":
            self.y += self.speed
        if self.direction == "right":
            self.x += self.speed
    
    def crash_wall(self, x, y, playing):
        print(x)
        if x <=0 or x >= 1000:
            playing = False
        if y <= 0 or y >= 750:
            playing = False
        return playing
            
    def crash_trail(self, x, y, playing, player1_trail, player2_trail):
        
        for trail in player1_trail.locations:
            if [x,y] == trail:
                playing = False
        for trail in player2_trail.locations:
            if [x,y] == trail:
                playing = False
        return playing

class Player2_trail():
    def __init__(self, path, width, height, x, y):
        self.x = x
        self.y = y
        self.path = path
        self.width = width
        self.height = height
        self.locations = [[self.x, self.y]]
        
        self.image_l = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image_l, (self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def add_location(self, new_x, new_y):
        self.locations.append([new_x, new_y])

class Player2_particles(Player2):
    pass

class Player2_score(Player2):
    pass

class Power_ups():
    pass