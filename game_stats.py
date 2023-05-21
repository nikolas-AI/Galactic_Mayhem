class GameStats():
    """"Trak statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settigns = ai_settings
        self.reset_stats()
        #Start Alien Invasion in an active state.
        self.game_active = True

        #Start game in inactive state.
        self.game_active == False
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settigns.ship_limit