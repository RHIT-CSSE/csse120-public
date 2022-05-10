import pygame
import random
import time
from Raindrop import Raindrop


class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """
        Creates a Cloud sprite that will produce Raindrop objects.
        The cloud will be moving around.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.image, (self.x, self.y))
        for raindrop in self.raindrops:
            raindrop.draw()

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def add_raindrop(self):
        """
        Adds a Raindrop to the list of raindrops
        so that it looks like the Cloud is raining.
        """
        new_raindrop = Raindrop(self.screen,
                                random.randint(self.x,
                                               self.x + self.image.get_width()),
                                self.y + self.image.get_height() - 8)
        self.raindrops.append(new_raindrop)

    def raindrops_fall(self, mike):
        for raindrop in self.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                self.raindrops.remove(raindrop)
            if raindrop.off_screen():
                self.raindrops.remove(raindrop)