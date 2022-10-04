import pygame
from inc_particle import Particle
import random




class ParticleSpawner:
    def __init__(self):
        self.particle_group = pygame.sprite.Group()

    def update(self):
        self.particle_group.update()

    def spawn_particles(self, pos):
        random_number = random.randrange(3, 10)
        for num_particles in range(random_number):
            new_particle = Particle()
            new_particle.rect.x = pos[0]
            new_particle.rect.y = pos[1]
            self.particle_group.add(new_particle)