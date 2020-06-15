
import sys

import pygame

class AlienInvasion:
        """overall class to manage game assets and behavior"""

        def __init__(self):
            """initialize game """
            pygame.init()

            self.screen = pugame.display.set_mode(1200,800)
            pygame.display.set_caption("Alien Invasion")

            # set background color
            self.bg_color =(230,230,230)


        def run_game(self):
            """Start main game loop"""
            while True:
                    #watch for keyboard and mouse events
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()

                #redraw screen during each pass through the loop.
                self.screen.fill(self.bg_color)

                #make most recently drawn scene visible
                pygame.display.flip()


    if __name__ == '__main__':
          #make game instance, run game
        ai = AlienInvasion()
        ai.run.game()




