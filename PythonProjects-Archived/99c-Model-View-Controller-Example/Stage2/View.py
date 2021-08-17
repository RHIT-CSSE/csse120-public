import pygame
from Game import Game


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.background_color = pygame.Color("black")

    def draw(self):
        # print("draw")  # Only for testing
        self.screen.fill(self.background_color)
        self.game.draw()
        pygame.display.update()
