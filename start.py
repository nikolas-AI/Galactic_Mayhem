import sys 

import pygame

from setttings import Settings
from ship import Ship

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invaison")

    #Setting background color
    bg_color = (230, 230, 230)

    #Make a ship
    ship = Ship(screen)
    
    #Start the main loop for the game
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        #Make most recently drawn screen visible
        pygame.display.flip()

run_game()