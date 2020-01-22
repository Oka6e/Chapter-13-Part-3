import pygame

class Settings():
    """Class to store settings."""

    def __init__(self):
        """Initializes the game's settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
    
        # Catcher settings.
        self.catcher_speed_factor = 1.5

        # Baseball settings.
        self.baseball_drop_speed = float(1 / 2)
        self.ball_limit = 2