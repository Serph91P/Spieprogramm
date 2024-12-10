"""
Das Modul `sliding_puzzle.py` definiert die Kernlogik des Sliding-Puzzle-Spiels.

Klasse:
- SlidingPuzzle: Beinhaltet die Spiellogik und Interaktion mit der Spielfeld- und Spielzustandsverwaltung.

Funktionen:
- __init__(self, size=3): Initialisiert das Puzzle mit einer Standardgröße von 3x3.
- initialize_random(self): Erstellt ein zufälliges Puzzle.
- initialize_manual(self): Ermöglicht die manuelle Eingabe eines Puzzle-Layouts.
- display_board(self): Zeigt den aktuellen Zustand des Puzzles an.
- is_valid_move(self, number): Überprüft, ob ein Zug gültig ist.
- make_move(self, number): Führt einen gültigen Zug aus.
- is_solved(self): Prüft, ob das Puzzle gelöst ist.
- save_game(self): Speichert den aktuellen Spielzustand.
"""

import random
import json
import os
from models.board import Board
from models.game_state import GameState

class SlidingPuzzle:
    def __init__(self, size=3):
        """
        Initialisiert ein Sliding Puzzle.

        Argumente:
        - size (int): Die Größe des Spielfelds (z. B. 3 für ein 3x3-Feld).
        """
        self.board = Board(size)
        self.game_state = GameState()
        self.moves = 0

    def initialize_random(self):
        """Erstellt ein zufälliges Layout für das Puzzle."""
        numbers = list(range(1, self.board.size * self.board.size))
        random.shuffle(numbers)
        numbers.append(0)  # Das leere Feld

        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.set_value(i, j, numbers[i * self.board.size + j])
        self._update_empty_pos()

    def initialize_manual(self):
        """Ermöglicht die manuelle Eingabe eines Puzzle-Layouts."""
        numbers = list(range(1, self.board.size * self.board.size)) + [0]
        used_numbers = set()

        print("\nGeben Sie Zahlen (1 bis {}) für jede Position ein (0 für leeres Feld):".format(
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
                            print("Ungültige Zahl oder bereits verwendet!")
                    except ValueError:
                        print("Bitte geben Sie eine gültige Zahl ein!")

    def display_board(self):
        """Zeigt das aktuelle Spielfeld an."""
        print("\nAktuelles Spielfeld:")
        for i in range(self.board.size):
            row = []
            for j in range(self.board.size):
                value = self.board.get_value(i, j)
                row.append(str(value) if value != 0 else " ")
            print(" ".join(row))
        print(f"Züge: {self.moves}")

    def is_valid_move(self, number):
        """Überprüft, ob eine Zahl in das leere Feld verschoben werden kann."""
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.get_value(i, j) == number:
                    return self._is_adjacent(i, j, self.board.empty_pos)
        return False

    def _is_adjacent(self, row1, col1, pos2):
        """Prüft, ob zwei Felder benachbart sind."""
        return (abs(row1 - pos2[0]) == 1 and col1 == pos2[1]) or                (abs(col1 - pos2[1]) == 1 and row1 == pos2[0])

    def make_move(self, number):
        """Führt einen Zug aus, wenn er gültig ist."""
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
        """Prüft, ob das Puzzle gelöst ist."""
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
        """Aktualisiert die Position des leeren Feldes."""
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.get_value(i, j) == 0:
                    self.board.empty_pos = (i, j)
                    return

    def save_game(self):
        """Speichert den aktuellen Spielzustand."""
        self.game_state.save_game(self.board, self.moves)
        print("Spiel gespeichert!")

    def load_saved_game(self):
        """Lädt einen gespeicherten Spielzustand."""
        saved_state = self.game_state.load_game()
        if saved_state:
            self.board.size = saved_state['size']
            self.board.board = saved_state['board']
            self.moves = saved_state['moves']
            self.board.empty_pos = tuple(saved_state['empty_pos'])
            return True
        return False
