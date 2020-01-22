import pygame
from pygame.sprite import Sprite

class Baseball(Sprite):
    """A class to represent a baseball."""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the baseball image and set its rect attribute.
        self.image = pygame.image.load('images/baseball.bmp')
        self.rect = self.image.get_rect()

        # Start each new baseball at a random position at the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the baseball at tis current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Dropping the baseball."""
        self.y += self.ai_settings.baseball_drop_speed
        if self.y >= self.ai_settings.screen_height:
            self.y = -self.rect.height
        self.rect.y = self.y