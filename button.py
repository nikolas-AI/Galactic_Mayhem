import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.gt_rect()

        #Set the dimensions and properties of the button.
        self.width, self.heigth1 = 200, 50
        self.button_color =(0, 2555, 0)
        self.text_color =(255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

       
        