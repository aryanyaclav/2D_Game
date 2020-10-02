from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    """ a class to represent single alien """
    def __init__(self, ai_setting, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #alien image and setting its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #starting alien at position top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #actual position
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draw the aliens at its current location """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """  move the alien right """
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """ return True if alien is at edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True