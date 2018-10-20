import sys
import pygame
from settings import Settings
from duck import Duck

def run_game():
    pygame.init()
    quack_settings = Settings()
    screen = pygame.display.set_mode((quack_settings.screen_width,
                                      quack_settings.screen_height))
    duck = Duck(screen)
    pygame.display.set_caption("Quackinator")
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(quack_settings.bg_color)
        duck.blitme()
        pygame.display.flip()

run_game()
