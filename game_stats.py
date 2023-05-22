class GameStats():
    """"Trak statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settigns = ai_settings
        self.reset_stats()
        
        #Start game in inactive state.
        self.game_active = False

        #High scores should never be rest.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settigns.ship_limit
        self.score = 0
        self.level = 1
        self.lv =(f'lv: {self.level}')
