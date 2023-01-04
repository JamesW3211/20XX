import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        self.image = pygame.image.load("assets/images/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = float(0) # these need to be floating point variables
        self.vel_y = float(0)
        self.float_x = float(0) # holds precision values of Rect x,y
        self.float_y = float(0)


    def update(self):
        self.float_x += self.vel_x # convert float to int, we really don't care about precision here
        self.float_y += self.vel_y
        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)
        if self.rect.y >= 250:
            print("bullet deleted")
            self.kill()
