import pygame
import sys
from Game import Game


class Controller:
    def __init__(self, game: Game):
        self.game = game

    def get_and_handle_events(self):
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)
        print(events)  # Only for testing

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
