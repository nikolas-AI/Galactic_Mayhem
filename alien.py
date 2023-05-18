import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initailizing the alien and set its starting position."""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alienb.png')
        self.image = pygame.transform.scale(self.image, (60,60))
        self.alien_rect = self.image.get_rect()

        #Start each new alien near the top left of the screen.
        self.alien_rect.x = self.alien_rect.width
        self.alien_rect.y = self.alien_rect.height

        #Store the alien's exact position.
        self.x = float(self.alien_rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.alien_rect)

