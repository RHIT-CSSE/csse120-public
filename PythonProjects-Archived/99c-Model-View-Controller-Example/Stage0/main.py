import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 650))
    clock = pygame.time.Clock()
    frame_rate = 60

    while True:
        clock.tick(frame_rate)
        events = pygame.event.get()
        exit_if_quit_event(events)
        pygame.display.update()


def exit_if_quit_event(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()


main()
