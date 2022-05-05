"""
The  main  file for the Model-View-Controller architecture for our game.  It:
   1. Initializes pygame, the screen and a Clock.
   2. Constructs a Game (model), View and Controller.
   3. Runs the game loop.

Team members:
"""
# TODO: Put the names of your entire team in the above doc-string.

import pygame
from Game import Game
from Controller import Controller
from View import View




def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 650))  # TODO: Choose your own size
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    view = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    frame_rate = 60  # TODO: Choose your own frame rate

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        view.draw_everything()


main()
