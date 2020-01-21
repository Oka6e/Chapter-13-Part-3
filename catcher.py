import pygame
from pygame.sprite import Sprite

class Catcher(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the catcher and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the catcher image and get its rect.
        self.image = pygame.image.load('images/catcher.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new catcher at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the catcher's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self, ai_settings, screen):
        """Update the catcher's position baed on the movement flag."""
        # Update the catcher's center value, not the rect.
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += self.ai_settings.catcher_speed_factor
        if self.moving_left and self.rect.left >= 0:
            self.center -= self.ai_settings.catcher_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the catcher at its current location."""
        self.screen.blit(self.image, self.rect)