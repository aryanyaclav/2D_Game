class GameStats:
    """ track statsitics of game"""
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()

        #the activation
        self.game_active = True

    def reset_stats(self):
        """ initialise statistics that can change in the game """
        self.ship_left = self.ai_setting.ship_limit