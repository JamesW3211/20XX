import pygame
import random
import json

from inc_SpriteSheet import SpriteSheet
from inc_Sprite import Sprite




class Level(object):

    def __init__(self):
        super().__init__()

        # Distance is used to go through the script
        self.distance = 0
        self.distance_timer = pygame.time.get_ticks()

        # Load the script [from file]
        self.script = {
            100: {'name': "ENEMY", 'type': 10, 'x': 100, 'y': 200},
            150: {'name': "ENEMY", 'type': 10, 'x': 320, 'y': -200},
            200: {'name': "ENEMY", 'type': 10, 'x': 320, 'y': -200},

        }
        # Flag variables signal when to spawn things outside of the level handler
        self.enemy_flag = False

        # Load the sprite sheet, depending on the "type"

        # Unique objects
        self.objects = pygame.sprite.Group()

    def increment(self):
        # Increment the distance, which is the key of the script dictionary
        if pygame.time.get_ticks() > self.distance_timer + 1:
            self.distance_timer = pygame.time.get_ticks()
            self.distance += 1

        if self.distance in self.script:
            print("activated: ", self.script[self.distance])
            # Handle Script Keywords
            if self.script[self.distance] == "ENEMY":
                self.enemy_flag = True
            del (self.script[self.distance])

    '''  Update
        Handles animations and gun timing
    '''

    def update(self):

        self.objects.update()


    def draw(self, win):

        self.objects.draw(win)



