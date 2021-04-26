import pygame
from pygame.sprite import Group

from Settings import Settings
from ship import Ship
from alien import Alien
import functions as gf

def run_game():
    # init game and create display object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    # create ship
    ship = Ship(game_settings, screen)
    bullets = Group()
    #Create alien group
    aliens = Group()
    gf.create_fleet(game_settings, screen, aliens)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        #gf.update_aliens(game_settings, alien)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)
# test game
run_game()