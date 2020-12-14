import pygame
import time
from pygame.locals import *
from Particle import Particle

class ParticleEmitter():
    def __init__(self, screen_width, screen_height, x_col, particles, emit_time_in_sec = 0.5):
        self.last_emit_time = time.time()
        self.emit_time_in_sec = emit_time_in_sec
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x_col = x_col
        self.particles = particles


    def _emit_particle(self):
        particle = Particle(self.screen_width, self.screen_height, self.x_col)
        self.particles.add(particle)

    def update(self):
        if time.time() - self.last_emit_time > self.emit_time_in_sec:
            self._emit_particle()
            self.last_emit_time = time.time()
