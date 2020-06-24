import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class to represent a single alien
    def __init__(self, ai_game):
        # initialize the alien and set its starting position"
        super().__init__()
        self.screen = ai_game.screen


        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # uncolored pixels will not be drawn on to background,
        # so that background of ship image matches the background color
        nocolor = self.image.get_at((0, 0))
        self.image.set_colorkey(nocolor)

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store horizontal position
        self.x = float(self.rext.x)
