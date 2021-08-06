import pygame
# Use statements like the following, but for YOUR classes (each in their own module)
# from Fighter import Fighter
# from Missiles import Missiles
# from Enemies import Enemies


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # Store whatever YOUR game needs, perhaps something like this:
        # self.missiles = Missiles(self.screen)
        # self.fighter = Fighter(self.screen, self.missiles)
        # self.enemies = Enemies(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # Use something like the following, but for the objects in YOUR game:
        # self.fighter.draw()
        # self.missiles.draw()
        # self.enemies.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # Use something like the following, but for the objects in YOUR game:
        # self.missiles.move()
        # self.enemies.move()
        # self.missiles.handle_explosions(self.enemies)
