import pygame
import time


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename,
                 without_umbrella_filename):
        """
        Creates a Hero sprite (Mike) that does not move.
        If hit by rain he'll put up his umbrella.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_without_umbrella = pygame.image.load(
            without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        current_image = self.image_without_umbrella

        if time.time() - self.last_hit_time < 1.0:
            current_image = self.image_with_umbrella

        self.screen.blit(current_image, (self.x, self.y))

    def hit_by(self, raindrop):
        """
        Returns true if the given raindrop is hitting this Hero,
        otherwise false.
        """
        hero_hit_box = pygame.Rect(self.x, self.y,
                                   self.image_with_umbrella.get_width(),
                                   self.image_with_umbrella.get_height())
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)
