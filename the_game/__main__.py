"""
Desc: This is the main executable for the game.
By: Lewis
Start date: 09, 05, 2026
"""

# Imports:
from the_game.python_files.classes.GameClass import Game


# Creates the main object.
g = Game()
while g.playing:
    g.new_game()
    g.run_game()
    g.show_game_over_screen()
