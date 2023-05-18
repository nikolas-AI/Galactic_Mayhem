import pygame
from pygame.sprite import Group

from setttings import Settings
from ship import Ship
import game_functions as gf
# from alien import Alien


def run_game():
    #Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    bg = pygame.image.load('images/bg.jfif')
    bg1 = pygame.image.load('images/bg.jfif')
    
    pygame.display.set_caption("The Invaison")

    
    #Make a ship, a group to store bullets in, and a group of aliens.
    ship = Ship(ai_settings, screen )
    bullets = Group()
    # alien = Alien(ai_settings, screen)
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens)

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, bg, bg1, ship, aliens, bullets)
        
        
            
    

run_game()
