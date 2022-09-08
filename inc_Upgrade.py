import pygame


class Upgrade(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super(Upgrade, self).__init__(groups)
        self.image = pygame.image.load("assets/Images/speed.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect(center = pos)

        self.vel_x = 0
        self.vel_y = 1

    def update(self):

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
