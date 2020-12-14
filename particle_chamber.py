""" Main file of asteroids."""
import pygame
import sys
import time
from pygame.locals import *
from Model import Model
from Particle import Particle
from particle_emitter import ParticleEmitter

class ParticleChamber:
    """Contains all the variables and methods for running the main game loop."""
    def __init__(self):
        self.FPS = 25
        self.WINDOW_RES = (640, 480)
        self.BG_COLOR = (0, 0, 0) # RGB for black
        self.particle_x_step_res = 5

        pygame.init()
        self.FramePerSec = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode(self.WINDOW_RES)

    def game_loop(self):
        """Main game loop."""
        # fixed sprites
        self.model = Model(*self.WINDOW_RES, 'player_ship.png')
        self.model.update()

        # Particle emitters
        self.particles = pygame.sprite.Group()
        self.emitters = []
        for x_col in range(self.model.rect.left - (self.particle_x_step_res * 3), 
                            self.model.rect.right + (self.particle_x_step_res * 3), self.particle_x_step_res):
            emitter = ParticleEmitter(*self.WINDOW_RES, x_col, self.model.rect.top - 100, self.particles)
            self.emitters.append(emitter)

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Update sprites
            for emitter in self.emitters:
                emitter.update()
            self.model.update()
            for particle in self.particles:
                particle.update()

            # Draw sprites
            self.DISPLAYSURF.fill(self.BG_COLOR)
            self.model.draw(self.DISPLAYSURF)
            for particle in self.particles:
                particle.draw(self.DISPLAYSURF)

            # Detect collision between player and any asteroids
            if pygame.sprite.spritecollideany(self.model, self.particles, pygame.sprite.collide_mask):
                # TODO: animate particle bounce
                pass

            pygame.display.update()
            self.FramePerSec.tick(self.FPS)

if __name__ == '__main__':
    game = ParticleChamber()
    game.game_loop()