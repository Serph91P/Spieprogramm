"""
    Represents a game board of a given size.
    
    The `Board` class manages the state of a game board, including the values of each cell and the position of the empty cell.
    
    Attributes:
        size (int): The size of the game board (e.g. 3 for a 3x3 board).
        board (list[list[int]]): The 2D list representing the values of each cell on the board.
        empty_pos (tuple[int, int]): The row and column indices of the empty cell on the board.
    
    Methods:
        get_value(row: int, col: int) -> int:
            Returns the value of the cell at the given row and column.
        set_value(row: int, col: int, value: int) -> None:
            Sets the value of the cell at the given row and column.
        is_valid_position(row: int, col: int) -> bool:
            Checks if the given row and column indices are within the bounds of the board.
        get_board_state() -> list[list[int]]:
            Returns a copy of the current state of the board.
"""
class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.empty_pos = (size-1, size-1)

    def get_value(self, row, col):
        return self.board[row][col]

    def set_value(self, row, col, value):
        self.board[row][col] = value

    def is_valid_position(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def get_board_state(self):
        return [row[:] for row in self.board]
