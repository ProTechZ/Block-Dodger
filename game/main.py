import pygame
from sys import exit
import csv
from button import PlayButton
from constants import SCREEN, WIDTH, HEIGHT, BLOCK_SIZE, get_x_of_centerised_object
from enemies import Enemies
from player import Player
from enemies_wave import EnemiesWave


pygame.init()
pygame.font.init()

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.is_playing = True
        self.num_of_enemies = 15
        self.score = 0

        self.clock = pygame.time.Clock()
        self.ticks = 30

        self.colours = {
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
        }

        self.text_font = pygame.font.SysFont('Montserrat', 40, False)
        self.title_font = pygame.font.SysFont('Montserrat', 80, True)

        self.player = Player(WIDTH / 2, 500, BLOCK_SIZE, BLOCK_SIZE, self)
        self.block_size = self.player.width
        self.enemies = Enemies(self)

        self.enemies_wave = EnemiesWave(self.num_of_enemies,
                                        self.ticks, )
        self.enemy_falling_vel_min = 1
        self.enemy_falling_vel_max = 10

    def __update_enemies(self):
        self.enemies.append_enemies(self.num_of_enemies, self.width - self.block_size, self.block_size)
        self.enemies.display_enemies(self.colours['red'],
                                     self.enemy_falling_vel_min,
                                     self.enemy_falling_vel_max,
                                     self.height, )
    def __update_wave(self):
        self.enemies_wave.wave_counter -= 1
        self.num_of_enemies = self.enemies_wave.get_number_of_enemies_to_draw()
        self.enemies_wave.display_current_wave(self.colours['white'],
                                               (10, 5), )
        
    def __check_arrowkey_press(self, event, arrowkey, direction):
        if event.key == arrowkey:
            self.player.move_player(self.width, self.height, direction)

    def __check_arrowkeys_press(self, event):
        self.__check_arrowkey_press(event, pygame.K_UP, 'up')
        self.__check_arrowkey_press(event, pygame.K_DOWN, 'down')
        self.__check_arrowkey_press(event, pygame.K_LEFT, 'left')
        self.__check_arrowkey_press(event, pygame.K_RIGHT, 'right')
        self.__check_arrowkey_press(event, pygame.K_w, 'up')
        self.__check_arrowkey_press(event, pygame.K_s, 'down')
        self.__check_arrowkey_press(event, pygame.K_a, 'left')
        self.__check_arrowkey_press(event, pygame.K_d, 'right')

    def __screen_loop_starter_code(self):
        self.clock.tick(self.ticks)
        SCREEN.fill(self.colours['black'])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.__check_arrowkeys_press(event)

    def __starting_screen(self):
        while True:
            self.__screen_loop_starter_code()

            rendered_text = self.title_font.render('Block Dodger', True, self.colours['white'])
            SCREEN.blit(rendered_text, (get_x_of_centerised_object(rendered_text.get_width()), 175))

            play_button_size = 75
            play_button = PlayButton(get_x_of_centerised_object(play_button_size), 250, play_button_size,
                                     play_button_size)
            play_button.display(self.colours['green'], self.colours['white'])

            if play_button.is_clicked():
                break

            pygame.display.update()

    def __main_game(self):
        while self.is_playing:
            self.__screen_loop_starter_code()

            self.player.display(self.colours['white'])

            self.__update_enemies()

            for enemy in self.enemies.enemies:
                if self.player.is_collided(enemy):
                    self.is_playing = False # end the game if the player collided
            
            self.__update_wave()

            rendered_text = self.text_font.render(f'Score: {self.score}', True, self.colours['white'])
            SCREEN.blit(rendered_text, (10, 40)) # displaying the rendered text

            pygame.display.update()

    def __record_score(self):
        with open("game/scores.csv", "a") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([self.score])

    def play(self):
        self.__starting_screen()
        self.__main_game()
        self.__record_score()

game = Game(WIDTH, HEIGHT)
game.play()
