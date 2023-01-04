import pygame
import random
import math

from inc_SpriteSheet import SpriteSheet
from inc_Bullet import Bullet
from inc_Player import Player
from pygame import Vector2

''' Enemy
    (sprite group)

    This class handles the badguys which fires lasers

'''



class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemy_type, start_x, start_y, bullets):
        super().__init__()



        self.speed = -1  # how "fast" we scoot along the screen (negative = left)
        self.type = enemy_type

        self.load_images(self.type, start_x, start_y)

        self.vel_x = 0
        self.vel_y = int(.09)
        self.bullet_angle = float(0)  # floating point precision, important!
        self.bullet_speed = float(0)

        self.bullet_timer_max = 100
        self.bullet_timer = self.bullet_timer_max

        self.attack_pattern = 'STRAIGHT'

        self.states = {"FLY_DOWN": "FLY_DOWN",
                       "ATTACK": "ATTACK"}
        self.state = self.states["FLY_DOWN"]
        self.init_State = True
        self.bullets = bullets


    def load_images(self, enemy_type, start_x, start_y):
        # Images and Animations for Enemy Planes
        self.animation_frames = [] # empty list to hold all sprite frames
        if enemy_type == 0:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet16.png")
            image = sprite_sheet.get_image(0, 0, 33, 33)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 0, 33, 33)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(33, 0, 33, 33)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(66, 0, 33, 33)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(66, 0, 33, 33)
            self.animation_frames.append(image)

        if enemy_type > 0 and enemy_type < 5:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet2.png")  #yyyyyyyyyyy
            image = sprite_sheet.get_image(48, 16 * enemy_type, 16, 16) # 1 frame animation
            self.animation_frames.append(image)

        if enemy_type == 10:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            image = sprite_sheet.get_image(48, 48, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(24, 48, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 48, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            self.hp = 3

        if enemy_type == 12:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            self.hp = 25

        if enemy_type == 13:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            image = sprite_sheet.get_image(48, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(48, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(48, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            self.hp = 5

        if enemy_type == 14:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            self.hp = 5

        if enemy_type == 15:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet21.png")
            image = sprite_sheet.get_image(0, 0, 105, 64);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(105, 0, 105, 64);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(210, 0, 105, 64);  # (x, y, width, height)
            self.animation_frames.append(image)
            self.hp = 100

        if enemy_type == 16:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            self.hp = 5


        self.image = self.animation_frames[0]  # set initial frame
        self.mask = pygame.mask.from_surface(self.image) # Create a mask for collision
        self.rect = self.image.get_rect(center = (start_x, start_y))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.target_x, target_y = (100, 100)
        self.enemy_velocity = 3
        self.max_velocity = 3
        # self.angle_radians = math.atan2(target_x - enemy_x, target_y - enemy_y)  # arctangent (trignometry!)
        # self.angle_degrees = math.degrees(angle_radians)  # magic!


        # self.rect.x = start_x  # enemy init location (horizontal)
        # self.rect.y = start_y  # enemy init location (vertical)

        self.frame = 0  # current animation frame
        self.animation_time = 0  # animation delay speed

    def get_hit(self):
        self.hp -= 1 #Subtract Hp is enemy is hit
        if self.hp <= 0:
            self.die()

    def die(self):
        self.type = 0
        self.frame = 0
        self.load_images(self.type, self.rect.x, self.rect.y)

    def update(self, player):

        # PowerUps when Dead
        if self.type == 0:  #Explosion
            # Animation Frames
            if pygame.time.get_ticks() > self.animation_time + 50:
                self.animation_time = pygame.time.get_ticks()
                self.frame = self.frame + 1

                self.image = self.animation_frames[self.frame]
            if self.frame > 3: #A powerup badge is generated
                ran = [1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                powerup = random.choice(ran)
                if powerup < 5:
                    print("Powerup type: ", powerup)
                    self.type = powerup
                    self.load_images(self.type, self.rect.x, self.rect.y)
                else:
                    print('ded: ', powerup)
                    self.kill()
                    return

        # Powerups
        if self.type > 0 and self.type < 5:
            self.rect.y += 1;
            self.frame = 0

        # Enemy Types and Behavior
        if self.type == 10:  #Kamikaze enemy

            self.rect.y -= self.speed

            if self.frame > 2:  # reset animation loop
                self.frame = 0
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
            if self.rect.y >= 10: #Enemy accelerates quickly if past 10 pixels
                self.vel_y += .2 #Double enemy speed

            self.image = self.animation_frames[self.frame]

        if self.type == 12:  #Enemy flys down, shoots, leaves
            self.rect.y -= self.speed  # scoot across the screen this fast



            if self.frame > 2:  # reset animation loop
                self.frame = 0



            # enemy movement(diagonal flight pattern)
            if self.init_State:
                self.vel_x = 0
                while self.vel_x == 0:
                    self.vel_x = 2
                self.init_State = False
            if self.rect.x <= 0:
                self.vel_x *= -1
            elif self.rect.x + self.rect.width >= 320:
                self.vel_x *= -1

            self.rect.x += self.vel_x
            self.rect.y += self.vel_y


            self.image = self.animation_frames[self.frame]

        if self.type == 13:  #Enemy that tracks player movement
            self.rect.y -= -2
            if self.rect.x < player.rect.x:
                self.rect.x += int(2.0)
            if self.rect.x > player.rect.x:
                self.rect.x -= int(2.0)
            if self.frame > 2:  # reset animation loop
                self.frame = 0

            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
            # self.update_pos()



            self.image = self.animation_frames[self.frame]

        if self.type == 14:  #Enemy with a tri-shot

            # self.rect.y -= self.speed
            self.attack_pattern = 'TRI_SHOT' #Enemy shoots a tri-shot

            if self.frame > 2:  # reset animation loop
                self.frame = 0

            # Enemy 14 Attack Patterns and States
            if self.state == "FLY_DOWN":
                self.state_fly_down()
            elif self.state == "ATTACK":
                self.state_attack()

            self.vel_y = 1
            if self.pos == (10,0):
                self.vel_y =3


            # self.rect.x += self.vel_x
            # self.rect.y += self.vel_y
            self.update_pos()
            # print(self.rect)
            self.image = self.animation_frames[self.frame]

        if self.type == 15:  #Another Level Testing Scrolling Background

            self.rect.y -= self.speed

            if pygame.time.get_ticks() > self.animation_time + 50:
                self.animation_time = pygame.time.get_ticks()
                self.frame = self.frame + 1

            if self.frame > 2:  # reset animation loop
                self.frame = 0
            self.image = self.animation_frames[self.frame]

        if self.type == 16:  #Kamikaze enemy

            self.rect.y -= self.speed



            self.image = self.animation_frames[self.frame]


        # Offscreen, remove this sprite
        if self.rect.y > 250:
            self.kill()

    def update_pos(self):
        self.pos += Vector2(self.vel_x, self.vel_y)
        self.rect.x = round(self.pos.x)
        self.rect.y = round(self.pos.y)

    def state_fly_down(self):
        if self.init_State:
            self.state = self.states["ATTACK"]

    def state_attack(self):

        self.bullet_timer -= 1
        if self.bullet_timer < 0:
            self.bullet_timer = self.bullet_timer_max


            if self.attack_pattern == 'STRAIGHT':
                self.bullet_angle = 90  #This is in degrees (0 = "right", 90 = "down", 180 = "left", 270 = "up")
                self.bullet_speed = 4  #How fast the bullet travels
                self.shoot()  #Calls the function that shoots the bullet

            if self.attack_pattern == 'SPIRAL':
                self.bullet_angle += 10
                self.bullet_speed = 3
                if self.bullet_angle <= (360 * 5):  # 360 = 1 circle
                    self.bullet_timer = 1  # important! override timer so we can continuously "draw"
                else:
                    self.bullet_angle = 0
                    self.bullet_timer = self.bullet_timer_max * 2  #Delays firing
                self.shoot()

            if self.attack_pattern == 'TRI_SHOT':

                self.bullet_timer = 300
                self.bullet_angle = 70
                self.bullet_speed = 2
                self.shoot()

                self.bullet_angle = 110
                self.bullet_speed = 2
                self.shoot()

                self.bullet_angle = 90
                self.bullet_speed = 2
                self.shoot()

            if self.attack_pattern == 'RANDOM':  # you gotta do this, come on
                self.bullet_angle = random.randrange(0, 360)
                self.bullet_speed = float(random.randrange(10, 100) / 10)
                self.bullet_timer = 10
                self.shoot()

    def shoot(self):
        new_bullet = Bullet()
        new_bullet.vel_x = float(self.bullet_speed * math.cos(math.radians(self.bullet_angle)))
        new_bullet.vel_y = float(self.bullet_speed * math.sin(math.radians(self.bullet_angle)))
        new_bullet.float_x = self.rect.x + (self.rect.width // 2 - 4)
        new_bullet.float_y = self.rect.y + self.rect.height - 8
        self.bullets.add(new_bullet)
        print("bullet was shot")

    def draw(self, win):
        win.blit(self.image, self.rect)

