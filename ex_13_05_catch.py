import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from catcher import Catcher
from baseball import Baseball
import game_functions as gf

def run_game():
    """Initializes the game, screen, and settings."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")

    catcher = Group()
    baseball = Group()

    while True:
        gf.check_events(catcher)
        gf.update_catcher(ai_settings, screen, catcher)
        gf.update_baseball(ai_settings, screen, catcher, baseball)
        gf.update_screen(ai_settings, screen, catcher, baseball)

run_game()