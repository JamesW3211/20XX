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
            201: {'name': "BACKGROUND", 'type': 11, 'x': 0, 'y': 0},
            300: {'name': "ENEMY", 'type': 10, 'x': 80, 'y': -50},
            310: {'name': "ENEMY", 'type': 10, 'x': 100, 'y': -50},
            320: {'name': "ENEMY", 'type': 10, 'x': 120, 'y': -50},

            530: {'name': "ENEMY", 'type': 10, 'x': 130, 'y': -50},
            540: {'name': "ENEMY", 'type': 10, 'x': 150, 'y': -50},
            550: {'name': "ENEMY", 'type': 10, 'x': 170, 'y': -50},

            650: {'name': "ENEMY", 'type': 13, 'x': 200, 'y': -50},
            660: {'name': "ENEMY", 'type': 13, 'x': -40, 'y': -50},
            670: {'name': "ENEMY", 'type': 13, 'x': 230, 'y': -50},
            700: {'name': "ENEMY", 'type': 13, 'x': 40, 'y': -50},
            720: {'name': "ENEMY", 'type': 13, 'x': 150, 'y': -50},
            730: {'name': "ENEMY", 'type': 13, 'x': 330, 'y': -50},
            740: {'name': "ENEMY", 'type': 13, 'x': 150, 'y': -50},
            750: {'name': "ENEMY", 'type': 13, 'x': 40, 'y': -50},

            # 800: {'name': "ENEMY", 'type': 10, 'x': 50, 'y': -50},
            # 850: {'name': "ENEMY", 'type': 10, 'x': 100, 'y': -50},
            # 900: {'name': "ENEMY", 'type': 10, 'x': 120, 'y': -50},
            # 920: {'name': "ENEMY", 'type': 10, 'x': 160, 'y': -50},
            # 940: {'name': "ENEMY", 'type': 10, 'x': 190, 'y': -50},
            # 960: {'name': "ENEMY", 'type': 10, 'x': 210, 'y': -50},
            # 961: {'name': "ENEMY", 'type': 10, 'x': 230, 'y': -50},

            1000: {'name': "ENEMY", 'type': 10, 'x': 20, 'y': -50},
            1010: {'name': "ENEMY", 'type': 10, 'x': 40, 'y': -50},
            1020: {'name': "ENEMY", 'type': 10, 'x': 60, 'y': -50},
            1030: {'name': "ENEMY", 'type': 10, 'x': 80, 'y': -50},
            1050: {'name': "ENEMY", 'type': 10, 'x': 120, 'y': -50},
            1060: {'name': "ENEMY", 'type': 10, 'x': 140, 'y': -50},
            1070: {'name': "ENEMY", 'type': 10, 'x': 160, 'y': -50},
            1100: {'name': "ENEMY", 'type': 10, 'x': 180, 'y': -50},
            1160: {'name': "ENEMY", 'type': 10, 'x': 200, 'y': -50},
            1170: {'name': "ENEMY", 'type': 10, 'x': 220, 'y': -50},
            1180: {'name': "ENEMY", 'type': 10, 'x': 240, 'y': -50},
            1190: {'name': "ENEMY", 'type': 10, 'x': 260, 'y': -50},

            1200: {'name': "ENEMY", 'type': 12, 'x': 150, 'y': -50},
            1250: {'name': "ENEMY", 'type': 12, 'x': 20, 'y': -50},
            1300: {'name': "ENEMY", 'type': 12, 'x': 250, 'y': -50},

            1500: {'name': "ENEMY", 'type': 10, 'x': 0, 'y': -50},
            1502: {'name': "ENEMY", 'type': 10, 'x': 50, 'y': -50},
            1510: {'name': "ENEMY", 'type': 10, 'x': 100, 'y': -50},
            1520: {'name': "ENEMY", 'type': 10, 'x': 150, 'y': -50},
            1530: {'name': "ENEMY", 'type': 10, 'x': 200, 'y': -50},
            1540: {'name': "ENEMY", 'type': 10, 'x': 250, 'y': -50},
            1550: {'name': "ENEMY", 'type': 10, 'x': 300, 'y': -50},
            1650: {'name': "ENEMY", 'type': 12, 'x': 150, 'y': -50},
            1700: {'name': "ENEMY", 'type': 12, 'x': 20, 'y': -50},

            1725: {'name': "ENEMY", 'type': 13, 'x': 230, 'y': -50},
            1750: {'name': "ENEMY", 'type': 13, 'x': 40, 'y': -50},
            1800: {'name': "ENEMY", 'type': 13, 'x': 230, 'y': -50},
            1825: {'name': "ENEMY", 'type': 13, 'x': 40, 'y': -50},
            2050: {'name': "BACKGROUND2", 'type': 15, 'x': 0, 'y': 0},
            2225: {'name': "ENEMY", 'type': 13, 'x': 230, 'y': -50},
            2250: {'name': "ENEMY", 'type': 13, 'x': 40, 'y': -50},
            2200: {'name': "ENEMY", 'type': 13, 'x': 230, 'y': -50},
            5025: {'name': "ENEMY", 'type': 13, 'x': 40, 'y': -50},
            5000: {'name': "ENEMY", 'type': 10, 'x': 80, 'y': -50},
            5010: {'name': "ENEMY", 'type': 10, 'x': 100, 'y': -50},
            5020: {'name': "ENEMY", 'type': 10, 'x': 120, 'y': -50},

            3330: {'name': "ENEMY", 'type': 10, 'x': 130, 'y': -50},
            3340: {'name': "ENEMY", 'type': 10, 'x': 150, 'y': -50},
            3350: {'name': "ENEMY", 'type': 10, 'x': 170, 'y': -50},

        }
        # Flag variables signal when to spawn things outside of the level handler
        self.enemy_flag = False
        self.background_flag = False
        self.background_flag2 = False
        self.cloud_flag = False

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
            if self.script[self.distance]["name"] == "ENEMY":
                self.enemy_flag = self.script[self.distance]
            if self.script[self.distance]["name"] == "BACKGROUND":
                self.background_flag = True
            if self.script[self.distance]["name"] == "BACKGROUND2":
                self.background_flag2 = True
                self.cloud_flag = True
            del (self.script[self.distance])




    '''  Update
        Handles animations and gun timing
    '''

    def update(self):

        self.objects.update()


    def draw(self, win):

        self.objects.draw(win)



