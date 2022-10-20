''' 20XX
    Created by JamesW
    Inspired by 1942, 1943, 1944, 19XX, and so on.
'''
# ---- Imports ----
import os
import pygame
import random

# ---- File Includes ----
from inc_Player import Player
from inc_Enemy import Enemy
from inc_Lasers import Lasers
from inc_Level import Level
from inc_Background import BG
from inc_Background import BG2
from inc_Background import Clouds
from inc_Star import Star
from inc_Bullet import Bullet
from inc_particle_spawner import ParticleSpawner
from inc_Clouds import Cloud


# ----- Initialization -----
# set Environment variables; default initial Window Position
x = 250
y = 125
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

WIDTH = 320
HEIGHT = 240
ratio = 2


screen = pygame.display.set_mode([WIDTH, HEIGHT])
# Copy for our screen that we will draw everything to
draw_screen = screen.copy()

# Window icon
icon = pygame.image.load("assets/Images/icon.png")
pygame.display.set_icon(icon)

# Window mode (scaled up by Ratio)
screen = pygame.display.set_mode([(WIDTH * ratio), (HEIGHT * ratio)])
pygame.display.set_caption('Tutorial Spaceship Shooter')
# Hide the mouse
pygame.mouse.set_visible(False)



bg = BG()
bg_group = pygame.sprite.Group()

bg2 = BG2()
bg_group2 = pygame.sprite.Group()

cloud = Clouds()
clouds_group = pygame.sprite.Group()




background = pygame.Surface([640, 480])

#Initate Pygame
pygame.init()
# Clock is used to cap framerate
clock = pygame.time.Clock()

# Load static images
#background_image = pygame.image.load("assets/Images/background.png").convert()

# Load the font and set the font size
font = pygame.font.Font("assets/Fonts/upheavtt.ttf", 14)

# Load Sound Effect(s) and Music
sfx_player_shoot = pygame.mixer.Sound("assets/Audio/SF1.wav")
sfx_player_shoot.set_volume(0.5)  # change the volume of the sfx, can use for music too
sfx_enemy_die = pygame.mixer.Sound("assets/Audio/SF10.wav")
sfx_enemy_die.set_volume(0.3)  # change the volume of the sfx, can use for music too
# sfx_enemy_die.set_volume(0.1)
# Music
pygame.mixer.music.load("assets/Audio/93727__zgump__tr-loop-0416.wav")




# Setup the sprites
player = Player()  # player (from the inc_Player.py class)


# Sprite Groups are used for multiples of the same thing
enemy_list = pygame.sprite.Group()  # Group of all enemy sprites
laser_list = pygame.sprite.Group()  # Group of all laser sprites
upgrade_group = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
particle_spawner = ParticleSpawner()

# ----- Functions -----
''' Game Text
        Objective
            Handles the fancy stuff for placing pretty text on the screen
        Parameter
            text    the text we want to display
            x       x location of the text
            y       y location of the text
            centered    do fancy math to place the text centered at x
'''


def game_text(text, x, y, centered):
    if centered == True:
        x = (x - len(text) * 4)
    text_render = font.render(text, True, (255, 255, 255))  # RGB
    draw_screen.blit(text_render, [x, y])


''' Main Game Loop
    Everything happens here!
'''


def main():

    player_fire_button = 'UP'  # Polling Key State
    # Setup the level; this should also nuke any previous level data
    level_data = Level()

    # Prepare the sprite groups, make sure they are empty (good to do for new levels)
    enemy_list.empty()
    laser_list.empty()

    player_alive = True  # Flag used to keep the game loop going
    score = 0  # Player's score!
    screen_shake = 0

    # Start the music loop
    # Enable music Loop by passing -1 to "repeat"
    pygame.mixer.music.play(-1)  # Starts the music

    max_clouds = 5
    current_num_clouds = 0
    cloud_timer = pygame.time.get_ticks()



    # Actual game loop
    while player_alive:
        # -- Event handler --
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close the window
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape Key
                    return "quit"

        # Key Polling, handles "key up" and "key down" actions
        key = pygame.key.get_pressed()
        # Player "Fire" button
        if player.alive == True:
            if key[pygame.K_SPACE] == True:  # pressing button
                if player_fire_button == 'UP':
                    player_fire_button = 'PRESSED'

                if player.gun_loaded == 1:
                    if player.ammo_type == 0:
                        player.fire_delay = 150
                    if player.ammo_type == 1:
                        # laser = Lasers(player.rect.x+10, player.rect.y, enemy_list, player.ammo_type, True)
                        # laser.y_force = 1
                        # laser_list.add(laser)
                        # laser = Lasers(player.rect.x+12, player.rect.y, enemy_list, player.ammo_type, True)
                        # laser.y_force = -1
                        # laser_list.add(laser)
                        laser = Lasers(player.rect.x+4 , player.rect.y, enemy_list, player.ammo_type, True)
                        laser_list.add(laser)
                        laser = Lasers(player.rect.x + 18, player.rect.y, enemy_list, player.ammo_type, True)
                        laser_list.add(laser)

                        player.fire_delay = 150
                    if player.ammo_type == 2:
                        laser = Lasers(player.rect.x+10, player.rect.y, enemy_list, player.ammo_type, True)
                        laser.y_force = 1
                        laser_list.add(laser)
                        laser = Lasers(player.rect.x+12, player.rect.y, enemy_list, player.ammo_type, True)
                        laser.y_force = -1
                        laser_list.add(laser)
                        # laser = Lasers(player.rect.x+4 , player.rect.y, enemy_list, player.ammo_type, True)
                        # laser_list.add(laser)
                        # laser = Lasers(player.rect.x + 18, player.rect.y, enemy_list, player.ammo_type, True)
                        # laser_list.add(laser)

                        player.fire_delay = 200
                    if player.ammo_type == 4:
                        player.laser_part -= 1
                        if player.laser_part < 1:
                            player.laser_part = 5
                            player.fire_delay = 150
                        else:
                            player.fire_delay = 50

                    player.gun_loaded = 0  # disable flag
                    sfx_player_shoot.play()

                    # Initialize a new laser, and add it to the group
                    laser = Lasers(player.rect.x+11, player.rect.y, enemy_list, player.ammo_type, True)
                    laser_list.add(laser)

            elif key[pygame.K_SPACE] == False:  # released button
                if player_fire_button == 'DOWN':
                    player_fire_button = 'RELEASE'


        #Player controls
        player.animation_status = 'MIDDLE'
        if key[pygame.K_LEFT]:
            player.move_left()
        if key[pygame.K_RIGHT]:
            player.move_right()
        if key[pygame.K_UP]:
            player.move_up()
        if key[pygame.K_DOWN]:
            player.move_down()

        # -- Game Logic --
        level_data.increment()

        # Enemies
        if level_data.enemy_flag != False:  # spawn an enemy
            enemy = Enemy(level_data.enemy_flag['type'], level_data.enemy_flag['x'], level_data.enemy_flag['y'],
                          bullet_list)
            enemy_list.add(enemy)
            level_data.enemy_flag = False

        if level_data.background_flag != False:  # background

            bg_group.add(bg)
            #background.fill((30, 144, 255))

            #draw_screen.fill((0, 0, 255))
            level_data.background_flag = False

        if level_data.background_flag2 != False:  # background

            bg_group2.add(bg2)
            #background.fill((30, 144, 255))
            print("background was added")



            # draw_screen.fill((0, 0, 255))
            level_data.background_flag2 = False

        if level_data.cloud_flag != False:  # background

            if pygame.time.get_ticks() >= cloud_timer + 4000:

            # if current_num_clouds >= max_clouds:
            #     pass
            # else:
                new_cloud = Cloud()
                print("cloud spawned")
                clouds_group.add(new_cloud)
                current_num_clouds += 1
                cloud_timer = pygame.time.get_ticks()

            # level_data.cloud_flag = False


        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False, pygame.sprite.collide_mask)
        for enemy in enemy_hit_list:
            if enemy.type > 0 and enemy.type < 5:
                sfx_player_shoot.play()
                player.ammo_type = enemy.type
                enemy.kill()

            if enemy.type > 9 :
                enemy.die()
                sfx_player_shoot.play()






        collision_bullets = pygame.sprite.spritecollide(player, bullet_list, False, pygame.sprite.collide_mask)
        for bullet in collision_bullets:
            player.death()

        enemy_player = pygame.sprite.spritecollide(player, enemy_list, False, pygame.sprite.collide_mask)
        for enemy in enemy_player:
            player.death()





        # Lasers
        for laser in laser_list:
            if laser.player_laser == True:  # Player laser hit enemy
                enemy_hit_list = pygame.sprite.spritecollide(laser, enemy_list, False, pygame.sprite.collide_mask)
                for enemy in enemy_hit_list:
                    if enemy.type > 9:
                        # print(enemy.hp)
                        screen_shake = 10
                        particle_spawner.spawn_particles((laser.rect.x, laser.rect.y))
                        enemy.get_hit()



                        score += 100
                        sfx_enemy_die.play()
                    # if enemy.type == 12:
                    #
                    #     particle_spawner.spawn_particles((laser.rect.x, laser.rect.y))
                    #     enemy.die()
                    #     score += 100
                    #     sfx_player_shoot.play()



            if laser.player_laser == False:  # Enemy Laser hits Player
                if pygame.sprite.collide_mask(laser, player):
                    if player.alive and player.invincible_timer == 0:
                        player.death()

        # Handle Player-specific timers here
        if player.alive == False:
            if pygame.time.get_ticks() > player.alive_timer:
                if player.lives > 0:
                    player.respawn()
                else:  # Game Over
                    game_loop = False
        else:
            if pygame.time.get_ticks() > player.invincible_timer:
                player.invincible_timer = 0

        if screen_shake > 0:
            screen_shake -= 1
        render_offset = [0, 0]
        if screen_shake:
            render_offset[0] = random.randint(0, 8) - 4
            render_offset[1] = random.randint(0, 8) - 4


        #UPDATES
        player.update()

        # "update" the sprite groups
        particle_spawner.update()
        enemy_list.update(player)
        laser_list.update()
        level_data.update()
        bg_group.update()
        clouds_group.update()
        bg_group2.update()





        #DRAW TO SCREEN
        draw_screen.fill((0,0,0))

        #draw_screen.blit(background, (0, 0))

        # Draw the sprites
        # Note that these are drawn in the order they are called (overlap!)

        bg_group.draw(draw_screen)

        bg_group2.draw(draw_screen)
        clouds_group.draw(draw_screen)

        bullet_list.draw(draw_screen)
        enemy_list.draw(draw_screen)
        laser_list.draw(draw_screen)
        player.draw(draw_screen)
        level_data.draw(draw_screen)
        particle_spawner.particle_group.draw(draw_screen)





        # UI elements
        # Score
        text = str(score)
        game_text(text, 160, 10, True)

        # Scale the draw screen to display screen
        screen.blit(pygame.transform.scale(draw_screen, screen.get_rect().size), (render_offset))
        # place the screen on the display via pygame
        pygame.display.flip()

        # Limit to 60 fps
        clock.tick(60)

    # Out of the Game Loop
    pygame.mixer.music.stop()  # Stop the music playlist


''' Call the main function
    This section is important because it tells Python what to call when it is run
'''
if __name__ == '__main__':
    main()

# Gracefully shutdown PyGame
pygame.quit()
