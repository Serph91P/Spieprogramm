"""
Manages the state of the game, including saving and loading the game board, moves, and other relevant information.

The `GameState` class provides methods to save the current game state to a file, and load a previously saved game state from a file.

Attributes:
    moves (int): The number of moves made in the current game.
    save_file (str): The filename to use for saving and loading the game state.

Methods:
    save_game(board, moves):
        Saves the current game state to the specified save file.
        
        Args:
            board (Board): The current state of the game board.
            moves (int): The number of moves made in the current game.
"""
import json
import os

class GameState:
    def __init__(self):
        self.moves = 0
        self.save_file = "puzzle_save.json"

    def save_game(self, board, moves):
        game_state = {
            'size': board.size,
            'board': board.board,
            'moves': moves,
            'empty_pos': board.empty_pos
        }
        with open(self.save_file, 'w') as f:
            json.dump(game_state, f)

    def load_game(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as f:
                return json.load(f)
        return None
