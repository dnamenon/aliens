import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    # class managing bullets, it inherits from sprite. the sprite package contains commands that allows us to act
    # on the bullets as a group. I would prefer not to inherit so i may refactor this class to have that
    # feature without having to inherit from sprite

    def __init__(self, ai_game):
        super().__init__()
        # gives bullet access to attributes of game screen and bullet settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet rect at (0,0) and then set correct initial position
        self.rect = pygame.Rect(0,0, self.settings.bullet_speed, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        # update the decimal position of the bullet
        self.y -= self.settings.bullet_speed

        #update rect
        self.rect.y = self.y

    def draw_bullet(self):
        #draw bullet to screen
        pygame.draw.rect(self.screen,self.color,self.rect)

