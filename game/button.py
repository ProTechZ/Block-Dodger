import pygame
from constants import SCREEN
pygame.init()

class Button(pygame.Rect):
    def display(self, colour):
        pygame.draw.rect(SCREEN, colour, self, border_radius=self.width // 2)

    def is_clicked(self):
        x, y = pygame.mouse.get_pos()
        return self.collidepoint(x, y) and pygame.mouse.get_pressed(3)[0]  # the second condition checks if mouse is being clicked


class PlayButton(Button):
    @staticmethod
    def calculate_triangle(size, start_x, start_y):
        A = (start_x, start_y)
        B = (start_x + size * 0.8, start_y + size / 2)
        C = (start_x, B[1] + size / 2)
        return A, B, C, A  # return A again at the end because A -> B, B -> C, C -> A

    def display(self, colour, triangle_colour):
        pygame.draw.rect(SCREEN, colour, self, border_radius=self.width // 2)

        triangle_size = self.width * 0.6
        triangle_start_x = self.left + self.width / 3  # starts at the first third of the button
        triangle_start_y = (self.y + self.height / 2) - (triangle_size / 2)  # centers triangle in button
        pygame.draw.polygon(SCREEN, triangle_colour, self.calculate_triangle(triangle_size,
                                                                             triangle_start_x,
                                                                             triangle_start_y))
