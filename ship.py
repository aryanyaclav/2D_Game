import pygame

class Ship:
    def __init__(self, ai_settings, screen):
        #getting the screen in which we want our ship to be
        self.screen = screen
        self.ai_settings = ai_settings

        #loading image of ship and its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #start each ship at position[at the bottom center]
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center  = float(self.rect.centerx)

        #right movement flag of ship
        self.MOVING_RIGHT = False

        #left movement flag of ship
        self.MOVING_LEFT = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """ update the position of the ship based on keypressed or released """
        if self.MOVING_RIGHT and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.MOVING_LEFT and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx