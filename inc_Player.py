import pygame

from inc_SpriteSheet import SpriteSheet

''' Player

    This class handles the movable spaceship which fires lasers
'''
class Player(pygame.sprite.Sprite):
    ''' Init
        This function is called automatically when we initialize the Class
    '''
    def __init__(self):
        super().__init__()
        self.animation_frames = []
        sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            # player sprites
        image = sprite_sheet.get_image(0, 0, 24, 24);
        self.animation_frames.append(image)
        image = sprite_sheet.get_image(24, 0, 24, 24);
        self.animation_frames.append(image)
        image = sprite_sheet.get_image(48, 0, 24, 24);
        self.animation_frames.append(image)
        image = sprite_sheet.get_image(48, 0, 16, 32);
        self.animation_frames.append(image)



        self.image = self.animation_frames[0] # initial frame
            # create a mask for collision (same for both lasers)
        self.mask = pygame.mask.from_surface(self.image) 

        self.rect = self.image.get_rect() 
        self.rect.x = 150 # player init location (horizontal)
        self.rect.y = 200 # player init location (vertical)
        self.frame = 1 # current animation frame
        self.animation_time = 0 # animation delay speed
        self.shoot_time = 0  # delay between firing

        self.animation_status = "MIDDLE"
        self.fire_delay = 100  # set this to "really slow" to demo the laser angles and stuff
        self.lives = 3


        self.alive = True
        self.alive_timer = 0
        self.rect.x = 150 # player init location (horizontal)
        self.rect.y = 200 # player init location (vertical)
        self.gun_loaded = 0  # ready to fire!
        self.invincible_timer = pygame.time.get_ticks() + 2000
        self.draw_flag = True
        self.ammo_type = 0 # straight bullet
        self.laser_part = 5

    def death(self):
        if self.alive:
            self.alive = False
            self.lives -= 1
            self.alive_timer = pygame.time.get_ticks() + 2000
    '''  Update
        Handles animations and gun timing
    '''
    def update(self):
        if pygame.time.get_ticks() > self.shoot_time + self.fire_delay:
            self.shoot_time = pygame.time.get_ticks()
            self.gun_loaded = 1


        if self.animation_status == "MIDDLE":
            self.frame = 0
        if self.animation_status == "LEFT":
            self.frame = 2
        if self.animation_status == "RIGHT":
            self.frame = 1




        self.image = self.animation_frames[self.frame]

    '''  Move_
        Movement functions; only move in that direction if it doesn't go offscreen
    '''
    def move_right(self):
        if self.rect.x < 296:
            self.rect.x += 3
            self.animation_status = "RIGHT"


    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= 3
            self.animation_status = "LEFT"

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 3

    def move_down(self):
        if self.rect.y < 218:
            self.rect.y += 3

    ''' Draw
        Places the current animation frame image onto the passed screen
    '''
    def draw(self, win):
        if self.alive:
            if self.invincible_timer > 0:
                if self.draw_flag == False:
                    self.draw_flag = True
                else:
                    self.draw_flag = False
            else:
                self.draw_flag = True

            if self.draw_flag == True:
                win.blit(self.image, self.rect)
        # win.blit(self.image, self.rect)
