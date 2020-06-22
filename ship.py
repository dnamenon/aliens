from typing import Any, Union

import pygame
from pygame.surface import SurfaceType
from settings import Settings

class Ship:


    #class for managing the ship

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        # this allows me to me to access all settings (width,length, bgcolor) of the screen within this class
        self.screen_rect = pygame.Rect(ai_game.screen.get_rect())
        # pygame processes every shape as a rectangle, so this is setting the ships's navigable area to the screen shape
        # it allows me to put the ship in the right spot on the screen

        self.image = pygame.image.load("images/ship.bmp")

        #uncolored pixels will not be drawn on to background,
        # so that background of ship image matches the background color
        nocolor = self.image.get_at((0,0))
        self.image.set_colorkey(nocolor)

        self.rect = pygame.Rect(self.image.get_rect())
        # get_rect transforms the space of the image into a rectangle shape that pygame uses as the border of the ship

        # to start each new ship at the bottom center we assign self.rect's middle bottom
        # border to the middle bottom border of the screen

        self.rect.midbottom = self.screen_rect.midbottom


        # Booleans for checking whether the ship is moving left or right.
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        # blit = draw the image into the screen at the spot specified by the self.rect
        self.screen.blit(self.image, self.rect)

    def update(self):
        # update ships position in response to arrow keys
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1


