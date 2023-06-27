from random import randint
import pygame
from constants import SCREEN
pygame.init()

class Enemies:
    def __init__(self, game_object):
        self.game = game_object
        self.enemies = []

    def enemies_pop(self, enemy, height_limit):
        if enemy.top >= height_limit:  # if enemy is at the end of the screen
            self.enemies.pop(self.enemies.index(enemy))
            self.game.score += 1  # add 1 to score for every enemy that dies

    def display_enemies(self, colour, falling_velocity_min, falling_velocity_max, height_limit):
        for enemy in self.enemies:
            enemy.top += randint(falling_velocity_min, falling_velocity_max)
            pygame.draw.rect(SCREEN, colour, enemy)
            self.enemies_pop(enemy, height_limit)

    def append_enemies(self, limit, x_range, block_size):
        while len(self.enemies) < limit:
            enemy_obj = pygame.Rect(
                randint(0, x_range),
                1,
                block_size,
                block_size,
            )

            self.enemies.append(enemy_obj)
