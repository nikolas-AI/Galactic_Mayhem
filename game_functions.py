import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """"Resopnd to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """"Resopnd to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
      
def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
           
             

def update_screen(ai_settings, screen, bg, bg1, ship, aliens, bullets):
        """Updates images on the screen and flip to the new screen."""
        #Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        screen.blit(bg, (0,0))
        screen.blit(bg1, (500,0))

        #Redraw all bullets behind ship and aliens.
        for bullet in bullets.sprites():
            bullet.draw_bullets()

        ship.blitme()
        # alien.blitme()
        aliens.draw(screen)

        #Make most recently drawn screen visible
        pygame.display.flip()

def update_bullets(bullets):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet positions.
        bullets.update()

        #Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    #Create a newbullet and add it t the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    
def create_fleet(ai_settings, screen, aliens):
     """Create a full fleet of aliens."""
     #Create an alien and find the number of aliens in a row.
     #Spacing between each alien is equal to one alien width.
     alien = Alien(ai_settings, screen)
     alien_width = alien.rect.width
     available_space_x = ai_settings.screen_width - (2 * alien_width)
     number_aliens_x = int(available_space_x / (2 * alien_width))

     #Create the first row of aliens.
     for alien_number in range(number_aliens_x):
          #Create an alien and place it in the row.
          alien = Alien(ai_settings, screen)
          alien.x = alien_width + 2 * alien_width * alien_number
          alien.rect.x = alien.x
          aliens.add(alien)

