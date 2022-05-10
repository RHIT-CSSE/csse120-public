import pygame
import random


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)

    def move(self):
        """
        Move the self.y value of the Raindrop down the screen (y increase)
        at the self.speed.
        """
        self.y = self.y + self.speed

    def off_screen(self):
        """
        Returns true if the Raindrop y value is not shown on the screen,
        otherwise false.
        """
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen, (0, 0, 127), (self.x, self.y),
                         (self.x, self.y + 5), 2)