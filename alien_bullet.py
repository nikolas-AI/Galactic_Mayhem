import pygame
from pygame.sprite import Sprite

class Alien_Bullet(Sprite):
    """A class to manage bullets fired form the alien"""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet object at the alien's current position."""
        super().__init__()

        self.screen = screen

        #Create a bullet at (0,0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        #Store the bullet's position as a decimal value.
        self.y =float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up in the screen."""
        #Update the decimal position of the bullet.
        self.y += self.speed_factor
        #Update the rect position.
        self.rect.y = self.y

    def draw_alien_bullets(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

