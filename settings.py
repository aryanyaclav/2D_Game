class Settings:
    """ a class to store all settings of Alien Invasion """
    def __init__(self):
        self.screen_width=900
        self.screen_height=600
        self.screen_bg_color=(230,230,230)

        #ship setting

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet settings

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1 represent moving right ,-1 represent moving left
        self.fleet_direction = 1