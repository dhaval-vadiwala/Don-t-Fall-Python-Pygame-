import pygame

import constants
import platforms

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Space(level1).png").convert()
        self.background.set_colorkey(constants.BLACK)
        self.level_limit = -800
        
        level = [ [platforms.STONE_PLATFORM_MIDDLE, 70, 200],
                  [platforms.STONE_PLATFORM_MIDDLE, 200, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 470, 300],
                  [platforms.STONE_PLATFORM_MIDDLE, 1200, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1270, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1340, 600],
                  [platforms.EXIT_SIGN, 1410, 530],
                  [platforms.STONE_PLATFORM_MIDDLE, 1410, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1480, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1550, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1620, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1690, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1740, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 1750, 560],
                  [platforms.STONE_PLATFORM_MIDDLE, 1750, 520],
                  [platforms.STONE_PLATFORM_MIDDLE, 1750, 480]
                  ]
        
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 290
        block.rect.y = 101
        block.boundary_top = 100
        block.boundary_bottom = 649
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)        
        
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 550
        block.rect.y = 400
        block.boundary_left = 551
        block.boundary_right = 1100
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)      
        
# Create platforms for the level
class Level_02(Level):
    #level 2 definition

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Space-PNG-Pic.gif").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -950

        # Array with type of platform, and x, y location of the platform.
        level = [[ platforms.STONE_PLATFORM_MIDDLE, 70, 600], 
                 [platforms.STONE_PLATFORM_MIDDLE, 100, 200],
                 [platforms.STONE_PLATFORM_MIDDLE, 200, 550],
                 [platforms.STONE_PLATFORM_MIDDLE, 150, 600],
                 [platforms.STONE_PLATFORM_MIDDLE, 1680, 600],
                 [platforms.STONE_PLATFORM_MIDDLE, 1750, 600],
                 [platforms.STONE_PLATFORM_MIDDLE, 1820, 600],
                 [platforms.STONE_PLATFORM_MIDDLE, 1890, 600],
                 [platforms.EXIT_SIGN, 1890, 530]
                 ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 220
        block.rect.y = 150
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)   
        
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 800
        block.rect.y = 101
        block.boundary_top = 100
        block.boundary_bottom = 649
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)         
        
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 400
        block.rect.y = 450
        block.boundary_left = 300
        block.boundary_right = 500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)        
        
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1200
        block.rect.y = 300
        block.boundary_left = 900
        block.boundary_right = 1250
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)   
        
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1550
        block.rect.y = 500
        block.boundary_left = 800
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 310
        block.rect.y = 250
        block.boundary_left = 300
        block.boundary_right = 550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)         

