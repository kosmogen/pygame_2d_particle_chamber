import pygame
import math
from pygame.locals import *

class Particle(pygame.sprite.Sprite):
    """Represents a single particle that bounces when it collides with the model."""
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.image = pygame.Surface((1,1))
        self.image.fill((0, 255, 0))
        
        self.mask = pygame.mask.from_surface(self.image)

        self.x_pos = screen_width/2 - 25
        self.y_pos = 0
        self.y_velocity = 1
        self.x_velocity = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.rect = self.image.get_rect()
        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        # Update sprite position
        self.x_pos = self.x_pos + self.x_velocity
        self.y_pos = self.y_pos + self.y_velocity

        # Make sure the ship wraps around when it reaches the edge of the screen
        if self.y_velocity > 0 and self.y_pos > self.screen_height:
            self.kill()
        if self.y_velocity < 0 and self.y_pos < 0:
            self.kill()
        if self.x_velocity > 0 and self.x_pos > self.screen_width:
            self.kill()
        if self.x_velocity < 0 and self.x_pos < 0:
            self.kill()

        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos
