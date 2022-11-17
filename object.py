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
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)
        

class Player1(Player):
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)

    def move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.y -= 5
        if key_pressed[pygame.K_a]:
            self.x -= 5
        if key_pressed[pygame.K_s]:
            self.y += 5
        if key_pressed[pygame.K_d]:
            self.x += 5
        
class Player1_trail(Player1):
    def __init__(self, path, width, height, x, y, speed):
        super().__init__(path, width, height, x, y, speed)
        self.locations = [[self.x, self.y]]
    
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
        
    def move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.y -= 5
        if key_pressed[pygame.K_LEFT]:
            self.x -= 5
        if key_pressed[pygame.K_DOWN]:
            self.y += 5
        if key_pressed[pygame.K_RIGHT]:
            self.x += 5

class Player2_trail(Player2):
    pass

class Player2_particles(Player2):
    pass

class Player2_score(Player2):
    pass

class Power_ups():
    pass