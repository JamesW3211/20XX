import pygame

from inc_SpriteSheet import SpriteSheet

class Entity(pygame.sprite.Sprite):
    def __init__(self, enemy_type, start_x, start_y):
        super().__init__()

