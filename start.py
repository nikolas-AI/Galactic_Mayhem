import sys 

import pygame

def run_game():
    #Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1000,700))
    pygame.display.set_caption("Alien Invaison")

    #Setting background color
    bg_color = (230, 230, 230)

    #Start the main loop for the game
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #redraw the screen during each pass through the loop
        screen.fill(bg_color)
        
        #Make most recently drawn screen visible
        pygame.display.flip()

run_game()