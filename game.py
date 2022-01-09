from sys import exit
import pygame
from button import PlayButton
from constants import SCREEN, WIDTH, HEIGHT, BLOCK_SIZE, get_x_of_centerised_object, MONTSERRAT
from enemies import Enemies
from player import Player
from wave import EnemiesWave

pygame.init()
pygame.font.init()


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.is_playing = True
        self.num_of_enemies = 10
        self.score = 0

        self.clock = pygame.time.Clock()
        self.ticks = 20

        self.colours = {
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
        }
        self.font = self.create_font(MONTSERRAT, 40)

        self.player = Player(WIDTH / 2, 500, BLOCK_SIZE, BLOCK_SIZE, self)
        self.block_size = self.player.width
        self.enemies = Enemies(self)

        self.enemies_wave = EnemiesWave(self.num_of_enemies,
                                        self.ticks, )

    @staticmethod
    def quit_game():
        pygame.quit()
        exit()

    @staticmethod
    def create_font(name, size, bold=False):
        return pygame.font.SysFont(name, size, bold)

    def render_text(self, font, text):
        return font.render(text, True, self.colours['white'])

    @staticmethod
    def display_rendered_text(rendered_text, x, y):
        SCREEN.blit(rendered_text, (x, y))

    def game_loop_starter_code(self):
        self.clock.tick(self.ticks)
        SCREEN.fill(self.colours['black'])
        self.event_loop()

    @staticmethod
    def update_screen():
        pygame.display.update()

    def start_game(self):
        while True:
            self.game_loop_starter_code()

            game_title_font = self.create_font(MONTSERRAT, 80, True)
            rendered_text = self.render_text(game_title_font, 'Block Dodger')
            self.display_rendered_text(rendered_text, get_x_of_centerised_object(rendered_text.get_width()), 175)

            play_button_size = 75
            play_button = PlayButton(get_x_of_centerised_object(play_button_size), 250, play_button_size,
                                     play_button_size)
            play_button.display(self.colours['green'], self.colours['white'])

            if play_button.is_clicked():
                break

            self.update_screen()

    def check_arrowkey_press(self, event, arrowkey, direction):
        if event.key == arrowkey:
            self.player.move_player(self.width, self.height, direction)

    def check_arrowkeys_press(self, event):
        self.check_arrowkey_press(event, pygame.K_UP, 'up')
        self.check_arrowkey_press(event, pygame.K_DOWN, 'down')
        self.check_arrowkey_press(event, pygame.K_LEFT, 'left')
        self.check_arrowkey_press(event, pygame.K_RIGHT, 'right')

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                self.check_arrowkeys_press(event)

    def all_enemies_collision_check(self):
        for enemy in self.enemies.enemies:
            self.player.check_collision(enemy)

    def update_enemies(self):
        self.enemies.append_enemies(self.num_of_enemies, self.width - self.block_size, self.block_size)
        self.enemies.display_enemies(self.colours['red'],
                                     1,
                                     self.block_size,
                                     self.height, )

    def update_wave(self):
        self.enemies_wave.wave_counter -= 1
        self.num_of_enemies = self.enemies_wave.get_number_of_enemies_to_draw()
        self.enemies_wave.display_current_wave(self.colours['white'],
                                               (10, 5), )

    def play_game(self):
        while self.is_playing:
            self.game_loop_starter_code()

            self.player.display(self.colours['white'])

            self.update_enemies()
            self.all_enemies_collision_check()
            self.update_wave()

            rendered_text = self.render_text(self.font, f'Score: {self.score}')
            self.display_rendered_text(rendered_text, 10, 40)

            self.update_screen()


game = Game(WIDTH, HEIGHT)
game.start_game()
game.play_game()
