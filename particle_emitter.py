import pygame
import time
from pygame.locals import *
from Particle import Particle

class ParticleEmitter():
    """Emites a particle on a predefined interval."""
    def __init__(self, screen_width, screen_height, x_col, y_pos, particles, emit_time_in_sec = 1):
        """Constructor for ParticleEmitter class
        Arguments:
            screen_width: the width of the surface to blit to in pixels
            screen_height: the height of the surface to blit to in pixels
            x_pos: the x position to start in
            y_pos: the initial y position
            particles: the particles group to add the emitted particle to
            emit_time_in_sec: the interval (in seconds) to emit a new particle on. optional.
        """
        self.last_emit_time = time.time()
        self.emit_time_in_sec = emit_time_in_sec
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x_col = x_col
        self.y_pos = y_pos
        self.particles = particles
        self._emit_particle()


    def _emit_particle(self):
        particle = Particle(self.screen_width, self.screen_height, self.x_col, self.y_pos)
        self.particles.add(particle)

    def update(self):
        if time.time() - self.last_emit_time > self.emit_time_in_sec:
            self._emit_particle()
            self.last_emit_time = time.time()
