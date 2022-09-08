import pygame

from inc_SpriteSheet import SpriteSheet

''' Lasers

    Handles both the player laser, and the enemy laser
'''
class Lasers(pygame.sprite.Sprite):
    ''' Init
        This function is called automatically when we initialize the Class
    '''
    def __init__(self, init_x, init_y, enemy_list, ammo_type, player_laser):
        super().__init__()

        self.frames = []

        sprite_sheet = SpriteSheet("assets/Images/sprite_sheet.png")
            # player bullet (blue)
        image = sprite_sheet.get_image(24, 24, 2, 10)
        self.frames.append(image) # Frame 1 = player
            # enemy bullet (red)
        image = sprite_sheet.get_image(24, 36, 2, 10)
        self.frames.append(image) # Frame 2 = Enemy
        image = sprite_sheet.get_image(24, 38, 2, 10)
        self.frames.append(image)  # Frame 2 = Enemy


        self.mask = pygame.mask.from_surface(image) # create a mask for collision (same for both lasers)

        self.rect = image.get_rect()


        self.player_laser = player_laser  # type of bullet (True = player, False = enemy)
        self.ammo = ammo_type



        # Set the laser starting position to the x,y values we were passed
        self.x_float = init_x
        self.y_float = init_y
        self.rect.x = int(self.x_float)
        self.rect.y = int(self.y_float)

        # These are used for math functions
        self.x_force = 0  # affects force applied on x value
        self.y_force = 0  # force on y value
        self.angle = 0  # angle of the laser
        self.speed = 4  # speed of the laser

        # Call special functions
        if self.ammo == 0:  # "Straight"
            self.x_force = self.speed
            self.y_force = 0
        elif self.ammo == 1:  # "Homing"
            self.x_force = self.speed


    '''  Update
        Handles animations and gun timing
    '''

    def update(self):
        # Move the laser

        if self.ammo == 0 or self.ammo == 4:  # This is the "standard" linear way
            if self.player_laser == True:  # player
                self.rect.y -= self.speed
            else:  # enemy
                self.rect.y += 2

        elif self.ammo == 1:  # spread Shot
            self.rect.x += self.x_force
            self.rect.y += self.y_force

        if self.player_laser == True:  # Determine bullet sprite
            self.image = self.frames[self.ammo + 1]
        else:
            self.image = self.frames[0]

        # bullet offscreen
        if self.rect.x < -16:
            self.kill()
        if self.rect.x > 320:
            self.kill()

    ''' Draw
        Places the current animation frame image onto the passed screen
    '''
    def draw(self, win):
        win.blit(self.image, self.rect)
