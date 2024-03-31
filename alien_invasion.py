import sys
import pygame
from ship import Ship
from settings import Settings

class AlienInvasion:
    """ Overall class to manage game assets and behavior."""

    def __init__(self):
        """ Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            # watch for keyboard and mouse events.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)

            self.ship.blitme()
                    
            # make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
        