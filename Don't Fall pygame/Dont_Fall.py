"""
Dhaval Vadiwala
Dr. Sun
Pygame Final Project 

Code used as template located at: 
http://programarcadegames.com/python_examples/en/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame
import random

import constants
import levels

from player import Player
from time import sleep
    
def main():
    """ Main Program """
    pygame.init()
    
    pygame.font.init() # you have to call this at the start, 
                       # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    
    #loads the sound and music files, playing the background music
    jump_sound = pygame.mixer.Sound("jump_06.wav")
    death_sound = pygame.mixer.Sound("Scream And Die Fx-SoundBible.com-299479967.wav")
    
    pygame.mixer.music.load("Medley1.wav")
    pygame.mixer.music.play( -1, 0.0 )     
    
    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Don't FALL ):")
    
        
    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 80
    player.rect.y = 200
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_SPACE:
                    player.jump()
                    jump_sound.play()
                if event.key == pygame.K_r:
                    main()               

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                           
        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 50:
            diff = 50 - player.rect.x
            player.rect.x = 50
            current_level.shift_world(diff)
            
        # If the player falls off the platforms, reset to the beginning of the game
        if player.rect.y >= 600:
            
            textsurface = myfont.render('You fell! Oh no! Game will reset in 3 seconds!', True, constants.WHITE, constants.BLACK)
            textr = textsurface.get_rect()
            textr.center = (600, 350)
            screen.fill(constants.BLACK)
            death_sound.play()
            
            screen.blit(textsurface,textr)
            
            pygame.display.update()
            
            sleep(3.0)
            main()
        
        #Finds the position of the player and displays a message if player reached the end of level 2
        current_position = player.rect.x + current_level.world_shift
        if current_level_no == 1 and current_position < current_level.level_limit:
            
            textsurface1 = myfont.render('You reached the end of the game! Congrats!', True, constants.WHITE, constants.BLACK)
            textr1 = textsurface1.get_rect()
            textr1.center = (600, 350)
            screen.fill(constants.BLACK)            
            
            screen.blit(textsurface1,textr1)
            
            pygame.display.update()
            
            sleep(3.0)
            
            done = True
            
            pygame.quit()
            
        # If the player gets to the end of the level, go to the next level
        current_position1 = player.rect.x + current_level.world_shift
        if current_position1 < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
