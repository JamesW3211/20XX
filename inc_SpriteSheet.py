import pygame

''' SpriteSheet
    Class used to grab images out of a sprite sheet

    Loads an image, and cuts out the "sprite" from a sprite sheet
'''
class SpriteSheet(object):
    ''' Init
        This function is called automatically when we initialize the Class
    '''
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    ''' get_image

        This function converts a loaded image and cuts out the sprite
    '''
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey((0, 0, 0))

        return image

