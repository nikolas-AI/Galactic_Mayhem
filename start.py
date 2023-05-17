import pygame

from setttings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invaison")

    #Setting background color
    # bg_color = (230, 230, 230)

    #Make a ship
    ship = Ship(screen)

    #Start the main loop for the game
    while True:
        gf.check_events()


        #Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Make most recently drawn screen visible
        pygame.display.flip()

run_game()