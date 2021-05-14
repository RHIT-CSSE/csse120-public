import pygame


class Fighter:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.image = pygame.image.load("fighter.png")

        # Fighter starts centered horizontally near the bottom of screen.
        self.x = (self.screen.get_width() - self.image.get_width()) // 2
        self.y = self.screen.get_height() - self.image.get_height() - 5

    def draw(self):
        # print("draw fighter")  # Only for testing
        self.screen.blit(self.image, (self.x, self.y))
