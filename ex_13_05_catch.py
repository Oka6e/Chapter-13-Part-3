import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from catcher import Catcher
from baseball import Baseball
from game_stats import GameStats
import game_functions as gf

def run_game():
    """Initializes the game, screen, and settings."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")
    stats = GameStats(ai_settings)

    catcher = Group()
    baseball = Group()

    while True:
        gf.check_events(catcher)

        if stats.game_active:
            gf.update_catcher(ai_settings, screen, catcher)
            gf.update_baseball(ai_settings, stats, screen, catcher, baseball)
            gf.update_screen(ai_settings, screen, catcher, baseball)

run_game()