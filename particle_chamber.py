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
        self.FPS = 60
        self.WINDOW_RES = (640, 480)
        self.BG_COLOR = (0, 0, 0) # RGB for black

        pygame.init()
        self.FramePerSec = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode(self.WINDOW_RES)

    def game_loop(self):
        """Main game loop."""
        # fixed sprites
        self.player_ship = Model(*self.WINDOW_RES, 'player_ship.png')
        self.player_ship.update()

        # Initial asteroids
        self.particles = pygame.sprite.Group()
        self.emitter = ParticleEmitter(*self.WINDOW_RES, 320, self.particles)

        # Particle generators
        # particle = Particle(*self.WINDOW_RES, 320)
        # self.particles.add(particle)

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Update sprites
            self.emitter.update()
            self.player_ship.update()
            for asteroid in self.particles:
                asteroid.update()

            # Draw sprites
            self.DISPLAYSURF.fill(self.BG_COLOR)
            self.player_ship.draw(self.DISPLAYSURF)
            for asteroid in self.particles:
                asteroid.draw(self.DISPLAYSURF)

            # Detect collision between player and any asteroids
            if pygame.sprite.spritecollideany(self.player_ship, self.particles, pygame.sprite.collide_mask):
                # TODO: animate particle bounce
                pass

            pygame.display.update()
            self.FramePerSec.tick(self.FPS)

if __name__ == '__main__':
    game = ParticleChamber()
    game.game_loop()