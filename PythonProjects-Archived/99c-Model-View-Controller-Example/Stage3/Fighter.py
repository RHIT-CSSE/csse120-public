import pygame


class Fighter:
    def __init__(self, screen: pygame.Surface, speed=5):
        self.screen = screen
        self.image = pygame.image.load("fighter.png")

        # Fighter starts centered horizontally near the bottom of screen.
        self.x = (self.screen.get_width() - self.image.get_width()) // 2
        self.y = self.screen.get_height() - self.image.get_height() - 5

        self.speed = speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        # print("left")  # Only for testing
        if self.x > -self.image.get_width() / 2:
            self.x = self.x - self.speed

    def move_right(self):
        # print("right")  # Only for testing
        if self.x < self.screen.get_width() - self.image.get_width() / 2:
            self.x = self.x + self.speed
