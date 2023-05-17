import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and at its starting position."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.ai_settings = ai_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.ship_rect = self.image.get_rect()


        #Start each new ship at the bottom center of the screen.
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center.
        self.center = float(self.ship_rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's center value, not the rect
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.ship_rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Update rect object from sef.center.
        self.ship_rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.ship_rect)
