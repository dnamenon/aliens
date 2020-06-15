
import sys

import pygame

from settings import Settings

class AlienInvasion:
        """overall class to manage game assets and behavior"""

        def __init__(self):
            """initialize game """
            pygame.init()
            self.settings = Settings()



            self.screen = pygame.display.set_mode(
                (self.settings.screen_width,self.settings.screen_height)
            )
            pygame.display.set_caption("Alien Invasion")




        def run_game(self):
            """Start main game loop"""
            while True:
                    #watch for keyboard and mouse events
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()

                #redraw screen during each pass through the loop.
                self.screen.fill(self.settings.bg_color)

                #make most recently drawn scene visible
                pygame.display.flip()


    if __name__ == '__main__':
          #make game instance, run game
        ai = AlienInvasion()
        ai.run.game()




