import pygame
import random
import math

from inc_SpriteSheet import SpriteSheet
from inc_Bullet import Bullet

''' Enemy
    (sprite group)

    This class handles the badguys which fires lasers

'''

class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemy_type, start_x, start_y, bullets):
        super().__init__()

        self.shoot_time = pygame.time.get_ticks() + random.randrange(0, 1000)  # delay between firing
        self.gun_loaded = 0  # ready to fire!
        self.speed = -1  # how "fast" we scoot along the screen (negative = left)
        self.type = enemy_type

        self.load_images(self.type, start_x, start_y)

        self.vel_x = 0
        self.vel_y = int(.05)
        self.bullet_angle = float(0)  # floating point precision, important!
        self.bullet_speed = float(0)
        self.bullets = pygame.sprite.Group()
        self.bullet_timer_max = 50
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
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet2.png")
            image = sprite_sheet.get_image(0, 32, 16, 16)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(16, 32, 16, 16)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(32, 32, 16, 16)
            self.animation_frames.append(image)

        if enemy_type > 0 and enemy_type < 5:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet2.png")  #yyyyyyyyyyy
            image = sprite_sheet.get_image(48, 16 * enemy_type, 16, 16) # 1 frame animation
            self.animation_frames.append(image)

        if enemy_type == 10:
            sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)
            image = sprite_sheet.get_image(0, 24, 24, 24);  # (x, y, width, height)
            self.animation_frames.append(image)


        self.image = self.animation_frames[0]  # set initial frame
        self.mask = pygame.mask.from_surface(self.image) # Create a mask for collision
        self.rect = self.image.get_rect()
        self.rect.x = start_x  # enemy init location (horizontal)
        self.rect.y = start_y  # enemy init location (vertical)
        self.frame = 0  # current animation frame
        self.animation_time = 0  # animation delay speed


    def die(self):
        self.type = 0
        self.load_images(self.type, self.rect.x, self.rect.y)


    def update(self):

        #Animation Frames
        if pygame.time.get_ticks() > self.animation_time + 50:
            self.animation_time = pygame.time.get_ticks()
            self.frame = self.frame + 1


        # PowerUps when Dead
        if self.type == 0:  # explodey bits
            if self.frame > 2:
                ran = [1, 6, 7, 8, 9, 10]
                # turn into powerup?
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

        # Enemies
        if self.type == 10:  # Scooter
            self.rect.y -= self.speed  # scoot across the screen this fast

            # if pygame.time.get_ticks() > self.shoot_time + 1000:
            #     self.shoot_time = pygame.time.get_ticks() + random.randrange(0, 1000)
            #     self.gun_loaded = 1

            if self.frame > 2:  # reset animation loop
                self.frame = 0
            self.bullets.update()
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
            # Enemy 10 Attack Patterns and States
            if self.state == "FLY_DOWN":
                self.state_fly_down()
            elif self.state == "ATTACK":
                self.state_attack()

        self.image = self.animation_frames[self.frame]


        # Offscreen, remove this sprite
        if self.rect.y > 250:
            self.kill()
        # if self.rect.y > 240:
        #     self.kill()
        # if self.rect.x < -16:
        #     self.kill()
        # if self.rect.x > 320:
        #     self.kill()
        for bullet in self.bullets:
            if bullet.rect.y >= 250:
                self.bullets.remove(bullet)


    def state_fly_down(self):
        if self.init_State:
            self.init_State = False
        if self.rect.y >= 50:
            self.state = self.states["ATTACK"]
            self.init_State = True


    def state_attack(self):
        # bullet handling
        # if self.rect.y == 50:
        #     self.vel_x *= -1
        # elif self.rect.x + self.rect.width >= 240:
        #     self.vel_x *= -1
        # if self.init_State:
        #     #self.vel_y = 0
        #     self.rect.y = 50
        #     self.rect.x += 1
        # if self.rect.x == 240:
        #     self.rect.x -= 5


        self.bullet_timer -= 1
        if self.bullet_timer < 0:
            self.bullet_timer = self.bullet_timer_max

            # For attack patterns all we need to mess with is just the speed and angle; trig will do the rest

            # Just goes straight down = boring
            if self.attack_pattern == 'STRAIGHT':
                self.bullet_angle = 90  # remember this is in degrees (0 = "right", 90 = "down", 180 = "left", 270 = "up")
                self.bullet_speed = .5  # how fast the bullet travels
                self.shoot()  # actually shoot the freaking bullet
            #
            # # Randomly does angle and speed; not practical
            # if self.attack_pattern == 'RANDOM':  # you gotta do this, come on
            #     self.bullet_angle = random.randrange(0, 360)
            #     self.bullet_speed = float(random.randrange(10, 100) / 10)
            #     self.bullet_timer = 10
            #     self.shoot()
            #
            # # Relies on the timer to make a spiral by drawing points in a circle
            # if self.attack_pattern == 'SPIRAL':
            #     self.bullet_angle += 10
            #     self.bullet_speed = 3
            #     if self.bullet_angle <= (360 * 5):  # 360 = 1 circle
            #         self.bullet_timer = 1  # important! override timer so we can continuously "draw"
            #     else:
            #         self.bullet_angle = 0
            #         self.bullet_timer = self.bullet_timer_max * 2  # take a breath lol
            #     self.shoot()
            #
            # # shoots a round thing
            # if self.attack_pattern == 'CIRCLE':
            #     # bypass the timer completely; we want all bullets for this all at once
            #     self.bullet_speed = .2
            #     for x in range(0, 360, 5):  # start, stop, step; change "step" for circle tightness
            #         self.bullet_angle = x
            #         self.shoot()
            #
            # # it's a square thing, probably
            # if self.attack_pattern == 'SQUARE':
            #     # We are bypassing trig completely; just using "simple" straight lines
            #     # this is the dumb non mathy way to do it lol; compare with next pattern
            #     maximum_speed = 5
            #     # NOTE: since FOR requires ints, you can convert to float for tighter lines
            #     for dot in range(-maximum_speed, maximum_speed, 1):
            #         # Top
            #         new_bullet = Bullet()
            #         new_bullet.vel_x = dot
            #         new_bullet.vel_y = -maximum_speed
            #         new_bullet.float_x = self.rect.x + (self.rect.width // 2)
            #         new_bullet.float_y = self.rect.y + self.rect.height
            #         self.bullets.add(new_bullet)
            #         # Bottom - you could leave out the other three sections and this could just be a normal "spread" shot
            #         new_bullet = Bullet()
            #         new_bullet.vel_x = dot
            #         new_bullet.vel_y = maximum_speed
            #         new_bullet.float_x = self.rect.x + (self.rect.width // 2)
            #         new_bullet.float_y = self.rect.y + self.rect.height
            #         self.bullets.add(new_bullet)
            #         # Left
            #         new_bullet = Bullet()
            #         new_bullet.vel_x = -maximum_speed
            #         new_bullet.vel_y = dot
            #         new_bullet.float_x = self.rect.x + (self.rect.width // 2)
            #         new_bullet.float_y = self.rect.y + self.rect.height
            #         self.bullets.add(new_bullet)
            #         # Right
            #         new_bullet = Bullet()
            #         new_bullet.vel_x = maximum_speed
            #         new_bullet.vel_y = dot
            #         new_bullet.float_x = self.rect.x + (self.rect.width // 2)
            #         new_bullet.float_y = self.rect.y + self.rect.height
            #         self.bullets.add(new_bullet)
            #
            # # shoots directly at the player
            # # NOTE: need to pass player (x,y) to this function in order for this to work
            # # NOTE: should calculate the middle of the sprite, but for readability just keep it to top left
            # if self.attack_pattern == 'TARGET':
            #     # static location just to show targeting working
            #     player_x = 320 // 2
            #     player_y = 320
            #     # atan2 returns the result in radians already
            #     self.bullet_angle = math.degrees(math.atan2(player_y - self.rect.y, player_x - self.rect.x))
            #     self.bullet_speed = .2
            #     self.shoot()
            #
            # # This is probably not practical lol
            # if self.attack_pattern == 'GOLDEN_RULE':
            #     for x in range(0, 360, 5):
            #         self.bullet_angle = x
            #         self.bullet_speed = math.pi * math.radians(x)  # 3.141592...
            #         self.bullet_speed = .2
            #         self.shoot()

        # enemy movement
        # if self.init_State:
        #     self.vel_x = 0
        #     while self.vel_x == 0:
        #         self.vel_x = 2
        #     self.init_State = False
        # if self.rect.x <= 0:
        #     self.vel_x *= -1
        # elif self.rect.x + self.rect.width >= 240:
        #     self.vel_x *= -1

    '''
        Handles adding the bullet to the sprite group; applies trig functions with given variables
    '''

    def shoot(self):
        new_bullet = Bullet()
        new_bullet.vel_x = float(self.bullet_speed * math.cos(math.radians(self.bullet_angle)))
        new_bullet.vel_y = float(self.bullet_speed * math.sin(math.radians(self.bullet_angle)))
        #print("(", new_bullet.vel_x, ", ", new_bullet.vel_y, ")")
        new_bullet.float_x = self.rect.x + (self.rect.width // 2)
        new_bullet.float_y = self.rect.y + self.rect.height
        self.bullets.add(new_bullet)
        print("bullet was shot")



    def draw(self, win):
        win.blit(self.image, self.rect)


