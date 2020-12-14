import pygame
import math
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
    """Represents the player's ship in asteroids."""
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.image = pygame.image.load('player_ship.png')
        
        self.mask = pygame.mask.from_surface(self.image)

        self.x_pos = screen_width/2 - 25
        self.y_pos = screen_height - 100
        self.y_velocity = 0
        self.x_velocity = 0
        self.angle = 90
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.display_image = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.display_image.get_rect()
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def draw(self, surface):
        surface.blit(self.display_image, self.rect)

    def update(self):
        pass
