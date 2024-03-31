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


    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        """ Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        # watch for keyboard and mouse events.
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
                
        # make the most recently drawn screen visible.
        pygame.display.flip()
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
        