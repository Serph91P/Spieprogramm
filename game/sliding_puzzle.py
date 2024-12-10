"""
The `SlidingPuzzle` class represents a sliding puzzle game. It provides methods to initialize the game board, display the current state, make valid moves, and check if the puzzle is solved.

The class has the following methods:

- `__init__(self, size=3)`: Initializes a new `SlidingPuzzle` instance with the given board size (default is 3).
- `initialize_random(self)`: Initializes the game board with a random arrangement of numbers.
- `initialize_manual(self)`: Allows the user to manually enter the initial arrangement of numbers on the game board.
- `display_board(self)`: Prints the current state of the game board and the number of moves made.
- `is_valid_move(self, number)`: Checks if a given number can be moved to the empty space on the board.
- `make_move(self, number)`: Moves the given number to the empty space on the board, if the move is valid.
- `is_solved(self)`: Checks if the puzzle is in the solved state.
- `save_game(self)`: Saves the current game state.
"""
import random
from models.board import Board
from models.game_state import GameState

class SlidingPuzzle:
    def __init__(self, size=3):
        self.board = Board(size)
        self.game_state = GameState()
        self.moves = 0

    def initialize_random(self):
        numbers = list(range(1, self.board.size * self.board.size))
        random.shuffle(numbers)
        numbers.append(0)
        
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.set_value(i, j, numbers[i * self.board.size + j])
        self._update_empty_pos()

    def initialize_manual(self):
        numbers = list(range(1, self.board.size * self.board.size)) + [0]
        used_numbers = set()

        print("\nEnter numbers (1 to {}) for each position (0 for empty space):".format(
            self.board.size * self.board.size - 1))
        
        for i in range(self.board.size):
            for j in range(self.board.size):
                while True:
                    try:
                        num = int(input(f"Position [{i}][{j}]: "))
                        if num in numbers and num not in used_numbers:
                            self.board.set_value(i, j, num)
                            used_numbers.add(num)
                            if num == 0:
                                self.board.empty_pos = (i, j)
                            break
                        else:
                            print("Invalid number or already used!")
                    except ValueError:
                        print("Please enter a valid number!")

    def display_board(self):
        print("\nCurrent board:")
        for i in range(self.board.size):
            row = []
            for j in range(self.board.size):
                value = self.board.get_value(i, j)
                row.append(str(value) if value != 0 else " ")
            print(" ".join(row))
        print(f"Moves: {self.moves}")

    def is_valid_move(self, number):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.get_value(i, j) == number:
                    return self._is_adjacent(i, j, self.board.empty_pos)
        return False

    def _is_adjacent(self, row1, col1, pos2):
        return (abs(row1 - pos2[0]) == 1 and col1 == pos2[1]) or \
               (abs(col1 - pos2[1]) == 1 and row1 == pos2[0])

    def make_move(self, number):
        if not self.is_valid_move(number):
            return False

        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.get_value(i, j) == number:
                    self.board.set_value(self.board.empty_pos[0], 
                                       self.board.empty_pos[1], number)
                    self.board.set_value(i, j, 0)
                    self.board.empty_pos = (i, j)
                    self.moves += 1
                    return True
        return False

    def is_solved(self):
        count = 1
        for i in range(self.board.size):
            for j in range(self.board.size):
                if i == self.board.size - 1 and j == self.board.size - 1:
                    return self.board.get_value(i, j) == 0
                if self.board.get_value(i, j) != count:
                    return False
                count += 1
        return True

    def _update_empty_pos(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.get_value(i, j) == 0:
                    self.board.empty_pos = (i, j)
                    return

    def save_game(self):
        self.game_state.save_game(self.board, self.moves)
        print("Game saved!")

def load_saved_game(self):
    saved_state = self.game_state.load_game()
    if saved_state:
        self.board.size = saved_state['size']
        self.board.board = saved_state['board']
        self.moves = saved_state['moves']
        self.board.empty_pos = tuple(saved_state['empty_pos'])
        return True
    return False
