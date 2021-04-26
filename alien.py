import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for alien description"""
    def __init__(self, game_settings, screen):
        """Create alien object and define its start position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        # load alien image and set rect atribute
        self.image = pygame.image.load("images/vaenlane.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # set alien position
        self.x = float(self.rect.x)
    def blitme(self):
        """Draw alien at his position"""
        self.screen.blit(self.image, self.rect)