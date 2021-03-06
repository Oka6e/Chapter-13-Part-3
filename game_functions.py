import sys
import pygame

from baseball import Baseball
from catcher import Catcher
from random import randint
from time import sleep

def check_keydown_events(event, catcher):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        for c in catcher:
            c.moving_right = True
    elif event.key == pygame.K_LEFT:
        for c in catcher:
            c.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, catcher):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        for c in catcher:
            c.moving_right = False
    elif event.key == pygame.K_LEFT:
        for c in catcher:
            c.moving_left = False

def check_events(catcher):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)

def update_screen(ai_settings, screen, catcher, baseball):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    catcher.draw(screen)
    baseball.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_baseball(ai_settings, stats, screen, catcher, baseball):
    """Update the positions of the baseball and detect collisions."""
    screen_rect = screen.get_rect()
    baseball.update()
    if len(baseball) == 0:
        new_ball = Baseball(ai_settings, screen)
        new_ball.x = randint(new_ball.rect.width, screen_rect.right - new_ball.rect.width)
        new_ball.rect.x = new_ball.x
        new_ball.y = -2 
        new_ball.rect.y = new_ball.y
        baseball.add(new_ball)
    collisions = pygame.sprite.groupcollide(baseball, catcher, True, False)
    check_baseball_bottom(ai_settings, stats, screen, catcher, baseball)

def update_catcher(ai_settings, screen, catcher):
    screen_rect = screen.get_rect()
    catcher.update(ai_settings, screen)
    if len(catcher) == 0:
        new_catcher = Catcher(ai_settings, screen)
        new_catcher.center = screen_rect.centerx
        new_catcher.rect.centerx = new_catcher.center
        new_catcher.rect.bottom = screen_rect.bottom
        catcher.add(new_catcher)

def check_baseball_bottom(ai_settings, stats, screen, catcher, baseball):
    """Check if the baseball hits the bottom of the screen."""
    screen_rect = screen.get_rect()
    for b in baseball.sprites():
        if b.rect.bottom >= screen_rect.bottom:
            if stats.balls_left > 0:
                stats.balls_left -= 1
                baseball.empty()
                update_baseball(ai_settings, stats, screen, catcher, baseball)
                sleep(0.5)
            else:
                stats.game_active = False
                sys.exit()


    
    
    
        