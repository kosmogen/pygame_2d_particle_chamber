import pygame
import math
from pygame.locals import *

class Model(pygame.sprite.Sprite):
    """Represents the model to be subjected to the particle chamber. """
    def __init__(self, screen_width, screen_height, model_img_path):
        """Constructor for Model class.
        Arguments:
            screen_width: the width of the surface to blit to in pixels
            screen_height: the height of the surface to blit to in pixels
            model_img_path: path to a transparent png that acts as a 2D model
        """
        super().__init__()

        self.image = pygame.image.load(model_img_path)
        
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
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.angle = self.angle + 1
            self.display_image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.display_image.get_rect()
        if pressed_keys[K_RIGHT]:
            self.angle = self.angle - 1
            self.display_image = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.display_image.get_rect()

        self.rect.centerx = self.x_pos
        self.rect.centery = self.y_pos


