"""
The  View  file for the Model-View-Controller architecture for our game.
It is called repeatedly by the main game loop.
At each call, it displays a view of the game,
typically by asking the various objects of the Game to draw themselves.

Team members:
"""

import pygame
from Game import Game


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.background_color = pygame.Color("black")  # TODO: Choose your own color

    def draw_everything(self):
        self.screen.fill(self.background_color)
        self.game.draw_game()  # TODO: Implement draw_game in your Game
        pygame.display.update()
