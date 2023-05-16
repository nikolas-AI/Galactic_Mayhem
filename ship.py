import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and at its starting position."""
        self.screen = screen

        #Load the ship image and get its rect.
        self.image = pygame.image.load('ship.png')
        self.react = self.imagine.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.react.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.buttom

    def bitme(self):