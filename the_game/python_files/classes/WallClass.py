"""
Desc: This is the wall class for the game.
By: Lewis
Start date: 09, 05, 2026
"""

# Imports:
import pygame as pg
from ..settings.colours import *
from ..settings.dev_settings import *


class Wall(pg.sprite.Sprite):
    t_size = TILE_SIZE

    def __init__(self, game, coordinates: tuple[int, int], spr_size: tuple[int, int] = (t_size, t_size)) -> None:
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.surface.Surface(spr_size)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        # Coordinate related
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.rect.x = coordinates[0] * TILE_SIZE
        self.rect.y = coordinates[1] * TILE_SIZE
