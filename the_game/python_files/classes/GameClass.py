"""
Desc: This is the file for the main class for the game.
By: Lewis
Start date: 10, 05, 2026
"""

# Imports:
import pygame as pg
import sys
from ..settings.dev_settings import *
from ..settings.colours import *
from .ObstacleClass import Wall
from .PlayerClass import PlayerClass


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        # Pre start vars:
        self.world_objects = {}
        # Variables ready for the groups:
        self.all_sprites = None
        self.obstacles = None
        self.player = None
        # Variable for game play
        self.playing = True
        self.dt = None  # dt means delta time.

    def load_data(self):
        """ Loads the data for the game. """
        pass

    def new_game(self):
        """ Does all the setup for the game.
        Also loads the variables. """
        self.all_sprites = pg.sprite.Group()
        self.obstacles = pg.sprite.Group()
        self.player = PlayerClass(self, (10, 10))
        for x in range(10, 20):
            Wall(self, (x, 5))

    def run_game(self):
        """ Starts the game. """
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.game_events()
            self.game_updates()
            self.game_draw()

    def quit_game(self):
        """ Quits the game. """
        if self.playing:
            self.playing = False
            pg.quit()
            sys.exit()

    def game_updates(self):
        """ Runs the updates for the game. """
        self.all_sprites.update()

    def draw_grid(self):
        """ Draws a specified grid. """
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def game_draw(self):
        """ Runs all the drawing functionality for the game. """
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def game_events(self):
        """ Responsible for handling the game's events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit_game()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit_game()
                # Runs the player movement events:
                if event.key == pg.K_LEFT or event.key == pg.K_a:  # Move left
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT or event.key == pg.K_d:  # Move right
                    self.player.move(dx=1)
                if event.key == pg.K_UP or event.key == pg.K_w:  # Move up
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN or event.key == pg.K_s:  # Move down
                    self.player.move(dy=1)

    def show_start_screen(self):
        """ Shows the start screen for the game. """
        pass

    def show_game_over_screen(self):
        """ Shows the screen that a player sees when the game is over. """
        pass
