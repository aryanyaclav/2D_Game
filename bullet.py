import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ class for all bullets fired from ship """
    def __init__(self,ai_setting,screen,ship):
        """ create bullet object at ship current position """
        super().__init__()
        self.screen = screen

        #create bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullet position as decimal value
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """ Move the  bullet up the screen """
        self.y -= self.speed_factor

        self.rect.y = self.y

    def draw_bullet(self):
        """ draw the bullets """
        pygame.draw.rect(self.screen, self.color, self.rect)
