"""
Das Modul `board.py` definiert die Spielfeldlogik für das Sliding-Puzzle.

Klasse:
- Board: Repräsentiert das Spielfeld des Puzzles und verwaltet die Werte und Position des leeren Felds.

Funktionen:
- __init__(self, size): Initialisiert ein Spielfeld der angegebenen Größe.
- get_value(self, row, col): Gibt den Wert eines bestimmten Feldes zurück.
- set_value(self, row, col, value): Setzt den Wert eines bestimmten Feldes.
- is_valid_position(self, row, col): Überprüft, ob eine Position innerhalb des Spielfelds liegt.
- get_board_state(self): Gibt den aktuellen Zustand des Spielfelds als Kopie zurück.
"""

class Board:
    def __init__(self, size):
        """
        Initialisiert ein Spielfeld mit gegebener Größe.

        Argumente:
        - size (int): Die Größe des Spielfelds (z. B. 3 für ein 3x3-Feld).
        """
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.empty_pos = (size - 1, size - 1)  # Leeres Feld standardmäßig unten rechts

    def get_value(self, row, col):
        """
        Gibt den Wert an der angegebenen Position zurück.

        Argumente:
        - row (int): Die Zeile der Position.
        - col (int): Die Spalte der Position.

        Rückgabe:
        - int: Der Wert an der angegebenen Position.
        """
        return self.board[row][col]

    def set_value(self, row, col, value):
        """
        Setzt den Wert an der angegebenen Position.

        Argumente:
        - row (int): Die Zeile der Position.
        - col (int): Die Spalte der Position.
        - value (int): Der neue Wert für die Position.
        """
        self.board[row][col] = value

    def is_valid_position(self, row, col):
        """
        Überprüft, ob die Position innerhalb des Spielfelds liegt.

        Argumente:
        - row (int): Die Zeile der Position.
        - col (int): Die Spalte der Position.

        Rückgabe:
        - bool: True, wenn die Position gültig ist, sonst False.
        """
        return 0 <= row < self.size and 0 <= col < self.size

    def get_board_state(self):
        """
        Gibt eine Kopie des aktuellen Spielfelds zurück.

        Rückgabe:
        - list[list[int]]: Der Zustand des Spielfelds.
        """
        return [row[:] for row in self.board]