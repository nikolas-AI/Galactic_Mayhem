class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = 'steelblue'

        #Ship settings
        self.ship_speed_factor = 1.5