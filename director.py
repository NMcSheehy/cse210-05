import pygame
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

    def start(self,window):
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


            # Update window
            window.draw()
        pygame.quit()