import pygame
pygame.init()

class Window():
    # holds the display for the game
    # updates the window every frame
    def __init__(self, width, height, name, background, FPS) -> None:
        self.width = width
        self.height = height
        self.name = name
        self.background = background 
        self.FPS = FPS


        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)

    def draw(self, player, rock, gem, points, speech):
        # This has to be in order from bottom layer to top layer. 
        # Other wise the back ground will just draw over the scene
        # Background Color
        self.display.fill(self.background)

        # Draw player
        self.display.blit(player.image,(player.x, player.y))

        # Draw rock
        self.display.blit(rock.image, (rock.x, rock.y))

        # Draw gem
        self.display.blit(gem.image, (gem.x, gem.y))

        # Update title to show points
        pygame.display.set_caption(f'{self.name} | Score: {points.points}')

        # Displays message
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        text = self.font.render(F'{speech.message}', True, (0,0,0), (255, 255, 255))
        textRect = text.get_rect()
        self.display.blit(text, textRect)

        # Change the screen
        pygame.display.update()