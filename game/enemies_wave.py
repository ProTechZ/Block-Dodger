import pygame
from constants import SCREEN
pygame.init()
pygame.font.init()

class EnemiesWave:
    def __init__(self, num_of_enemies, ticks):
        self.num_of_enemies = num_of_enemies
        self.ticks = ticks

        self.wave = 1
        self.wave_counter = 5 * self.ticks  # variable for internal use

    def display_current_wave(self, colour, coordinates):
        font = pygame.font.SysFont('Montserrat', 40)
        text = font.render(f'Wave {self.wave}', True, colour)
        SCREEN.blit(text, coordinates)

    def get_number_of_enemies_to_draw(self):
        self.check_if_wave_over()

        return self.num_of_enemies

    def check_if_wave_over(self):
        if self.wave_counter == 0:
            self.wave_counter = 5 * self.ticks
            self.wave += 1
            self.num_of_enemies += 1
