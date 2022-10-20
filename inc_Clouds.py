import random

import pygame



class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.cloud_01 = pygame.image.load('assets/Images/cloud1.png').convert_alpha()
        self.cloud_02 = pygame.image.load('assets/Images/cloud1.png').convert_alpha()
        self.cloud_03 = pygame.image.load('assets/Images/cloud1.png').convert_alpha()
        self.cloud_04 = pygame.image.load('assets/Images/cloud1.png').convert_alpha()
        self.cloud_05 = pygame.image.load('assets/Images/cloud1.png').convert_alpha()
        self.img_clouds = [self.cloud_01,
                            self.cloud_02,
                            self.cloud_03,
                            self.cloud_04,
                            self.cloud_05]
        self.num_clouds = len(self.img_clouds)
        self.img_index = random.randrange(0, self.num_clouds - 1)
        self.image = self.img_clouds[self.img_index]
        # self.scale_value = random.uniform(-0.75, -1.5)
        # self.image = pygame.transform.scale(self.image, (int(self.image.get_width()* self.scale_value),
        #                                     int(self.image.get_width()* self.scale_value)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 320 - self.image.get_width())
        self.rect.y = 0 - self.rect.height
        self.pos_x = random.randrange(0, 320 - self.image.get_width())
        self.pos_y = 0 - self.rect.height
        self.vel_x = 0.0
        self.vel_y = random.uniform(1.5,2.0)

    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)