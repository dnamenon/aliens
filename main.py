import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize game """
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen.fill(self.settings.bg_color)
        print(self.screen)
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Start main game loop"""
        while True:
            # watch for keyboard and mouse events
            self._check_events()

            #ship movement
            self.ship.update()

            self.bullets.update()

            # redraw screen during each pass through the loop.
            self._update_screen()


            #bullet handler
            self._update_bullets()



    #helper methods, refactoring run_game
    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #quit game if q is pressed
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # get rid of old bullets
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)



    def _update_screen(self):
        # redraw screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # make most recently drawn scene visible
        pygame.display.flip()





if __name__ == '__main__':
    # make game instance, run game
    ai = AlienInvasion()
    # pygame.mixer.init()
    # pygame.mixer.music.load('donk.mp3')
    # pygame.mixer.music.play()
    ai.run_game()
