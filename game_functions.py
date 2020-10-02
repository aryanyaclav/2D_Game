import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    """ when key is pressed """
    if event.key == pygame.K_RIGHT:
        ship.MOVING_RIGHT = True

    if event.key == pygame.K_LEFT:
        ship.MOVING_LEFT = True

    if event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)

    #quit the game when q is pressed
    if event.key  == pygame.K_q:
        sys.exit()



def check_keyup_events(event,ship):
    """ when key is released """
    if event.key == pygame.K_RIGHT:
        ship.MOVING_RIGHT = False

    if event.key == pygame.K_LEFT:
        ship.MOVING_LEFT = False

def check_event(ai_setting, screen, ship, bullets):

    for event in pygame.event.get():

        #checking for exit game and exiting
        if event.type == pygame.QUIT:
            sys.exit()

        #if any key is pressed
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event,ai_setting, screen, ship, bullets)

         #if any key is released
        elif event.type == pygame.KEYUP:
           check_keyup_events(event,ship)

def update_screen(ai_setting, screen, ship, aliens, bullets):
    """ update the imgages every time and flip the screen"""
    screen.fill(ai_setting.screen_bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen) #pygame autoamatically draws when called in groups

    pygame.display.flip()

def update_bullets(ai_setting, screen, ship, bullets, aliens):
    """ function to update and get rid of bullets """
    bullets.update()

    # get rid of bullets that disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


    check_bullet_alien_collision(ai_setting, screen, ship, bullets, aliens)



def check_bullet_alien_collision(ai_setting, screen, ship, bullets, aliens):
    # check for any bullet that hit the alien
    # get rid of bullet and alien that collide
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # check if all aliens destroyed and create new fleet
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)

def fire_bullet(ai_setting, screen, ship, bullets):
    """ firing bullet if limit is not reached """
    # adding bullet to the group
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

def get_number_alien_x(ai_setting, alien_width):
    """ number of alien that can fit in one row"""

    available_special_x = ai_setting.screen_width - 2 * alien_width
    number_alien_x = int(available_special_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_setting, ship_height, alien_height):
    """ get the number of rows """
    available_space_y = ai_setting.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    """ create a alien and palce it in a row """
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)



def create_fleet(ai_setting, screen, ship, aliens):
    """ create a full fleet of aliens """
    #create a alien and finds number in a row
    alien = Alien(ai_setting, screen)
    number_alien_x = get_number_alien_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)

    #for rows to create
    for row_number in range(number_rows):
        #create first row of alien
        for alien_number in range(number_alien_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_setting, aliens):
    """ check appropriately if any aliens reach edges"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_setting, aliens)
            break

def change_fleet_direction(ai_setting, aliens):
    """ change the direction of fleet """
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def ship_hit(ai_setting, stats, screen, ship,  aliens, bullets):
    """ Respond to ship hitting alien """
    if stats.ship_left > 0:
        #decrement in ship
        stats.ship_left -= 1

        #empty the group of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create new fleet and center the ship
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting,stats, screen, ship, aliens, bullets)

def update_aliens(ai_setting, stats, screen, ship,  aliens, bullets):
    """ check if fleet at the edge and then update the position of aliens """
    check_fleet_edges(ai_setting, aliens)
    aliens.update()

    #if ship and alien collides
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, screen, ship,  aliens, bullets)

    #look for aliens hitting at the bottom
    check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets)
