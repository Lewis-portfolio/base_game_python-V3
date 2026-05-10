"""
Desc: This is the file for the player class for the game.
By: Lewis
Start date: 10, 05, 2026
"""

# Imports:
from .MainObjectClass import DefaultObject
from ..settings.dev_settings import *


class PlayerClass(DefaultObject):
    def __init__(self, game, coordinates=(TILE_SIZE, TILE_SIZE)):
        self.groups = game.all_sprites
        DefaultObject.__init__(self, game, coordinates)  # Pulls most of the code from here
