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
        self.game.world_objects[self.x, self.y] = self
        self.impassable = False

    def move(self, dx=0, dy=0):
        """ Moves the mob by the given direction. """
        if not self.check_collision(dx, dy):  # Checks for collisions
            self.x += dx
            self.y += dy

    def check_collision(self, dx= 0, dy= 0):
        """ Checks to see if two objects are colliding with each other. """
        if (self.x + dx, self.y + dy) in self.game.world_objects:
            obj = self.game.world_objects[self.x + dx, self.y + dy]
            if obj.impassable:  # Checks to see if the object is impassable
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE
