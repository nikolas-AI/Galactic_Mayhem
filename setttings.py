class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = 'steelblue'

        #Ship settings
        self.ship_speed_factor = 1
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 'Red'
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed_factor = 0.50
        self.fleet_drop_speed =200
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
