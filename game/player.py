import pygame
from constants import SCREEN
pygame.init()

class Player(pygame.Rect):
    def __init__(self, x, y, width, height, game_object):
        self.game = game_object
        super().__init__(x, y, width, height)

    def move_player(self, width, height, direction, ):
        if direction == 'up' and self.top > 1:
            self.y -= self.height

        elif direction == 'down' and self.bottom < height - 1:
            self.y += self.height

        elif direction == 'left' and self.left > 1:
            self.x -= self.width

        elif direction == 'right' and self.right < width - 1:
            self.x += self.width

    def is_collided(self, enemy):
        if self.colliderect(enemy):
            return True

    def display(self, colour):
        pygame.draw.rect(SCREEN, colour, self)
