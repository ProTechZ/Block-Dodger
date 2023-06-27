import pygame
pygame.init()

def get_x_of_centerised_object(object_width):
    return WIDTH / 2 - object_width / 2

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Block Dodger')

BLOCK_SIZE = 25
