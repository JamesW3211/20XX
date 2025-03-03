import random
import pygame
from inc_Star import Star
from inc_Planet import Planet
from inc_Clouds import Cloud

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface((320, 240))
        self.color = (0, 0, 15)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        self.planet_timer = random.randrange(120, 480)
        self.max_planets = 2
        self.current_num_planets = 0



    def update(self):
        self.planets.update()
        for planet in self.planets:
            if planet.rect.y > 240:
                self.planets.remove(planet)
                self.current_num_planets -= 1
        if self.planet_timer <= 0:
            if self.current_num_planets >= self.max_planets:
                pass
            else:
                new_planet = Planet()
                self.planets.add(new_planet)
                self.current_num_planets += 1
                self.planet_timer = random.randrange(120, 480)
        self.stars.update()
        for star in self.stars:
            if star.rect.y >= 320:
                self.stars.remove(star)
        if self.star_timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)
        self.image.fill(self.color)
        self.planets.draw(self.image)
        self.stars.draw(self.image)
        self.planet_timer -= 1
        self.star_timer -= 1

class BG2(pygame.sprite.Sprite):
    def __init__(self):
        super(BG2, self).__init__()
        self.image = pygame.image.load("assets/Images/112829.png")

        self.rect = self.image.get_rect()

        self.rect.y = -3062
        self.vel_x = 0
        self.vel_y = 1/10


    def update(self):

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Clouds(pygame.sprite.Sprite):  # cloud class
    def __init__(self):
        super(Clouds, self).__init__()
        self.image = pygame.Surface((320, 240))
        self.rect = self.image.get_rect()
        self.cloud_timer = random.randrange(120, 480)
        self.vel_x = 0
        self.vel_y = 1

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
