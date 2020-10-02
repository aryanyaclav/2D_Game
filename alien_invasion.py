import sys
import pygame
from settings import Settings
from ship import Ship
from alien  import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #initialize screen and pygame,settings
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #make a ship,group of aliens and bullets
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    #create fleet of aliens
    gf.create_fleet(ai_setting, screen, ship, aliens)

    #instance to store game statistics
    stats = GameStats(ai_setting)





    #loop for the gaming window
    while True:

        gf.check_event(ai_setting, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, bullets, aliens)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_setting, screen, ship, aliens, bullets)



run_game()


