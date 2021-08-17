import pygame
from Fighter import Fighter


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.fighter = Fighter(self.screen)

    def draw(self):
        self.fighter.draw()

    def run_one_cycle(self):
        # print("run one cycle")  # Only for testing
        pass
