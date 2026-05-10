"""
Desc: This is the file for the parent of almost all items and mobs for the game.
By: Lewis
Start date: 09, 05, 2026
"""

# Imports:
import pygame as pg
from ..settings.dev_settings import *
from ..settings.colours import *


class DefaultObject(pg.sprite.Sprite):
    def __init__(self, game, coordinates: tuple[int, int]):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Image related:
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(MY_BLUE)
        self.rect = self.image.get_rect()
        # Coordinate related:
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE

    def move(self, dx=0, dy=0):
        """ Moves the mob by the given direction. """
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE
