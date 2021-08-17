import pygame
import sys
from Game import Game


class Controller:
    def __init__(self, game: Game):
        self.game = game

    def get_and_handle_events(self):
        """ Left/Right arrow keys move the Fighter left/right. """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)
        print(events)  # Only for testing

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.game.fighter.move_left()
        if pressed_keys[pygame.K_RIGHT]:
            self.game.fighter.move_right()

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
