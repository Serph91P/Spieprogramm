"""
Das Modul `game_state.py` verwaltet den Spielzustand für das Sliding-Puzzle-Spiel.

Klasse:
- GameState: Verantwortlich für das Speichern und Laden des Spielzustands.

Funktionen:
- __init__(self): Initialisiert die Klasse und legt den Standard-Speicherdateinamen fest.
- save_game(self, board, moves): Speichert den aktuellen Spielzustand in einer Datei.
- load_game(self): Lädt den gespeicherten Spielzustand aus der Datei.
"""

import json
import os

class GameState:
    def __init__(self):
        """
        Initialisiert den Spielzustand.

        Attribute:
        - moves (int): Die Anzahl der gemachten Züge im aktuellen Spiel.
        - save_file (str): Der Name der Datei, in der der Zustand gespeichert wird.
        """
        self.moves = 0
        self.save_file = "puzzle_save.json"

    def save_game(self, board, moves):
        """
        Speichert den aktuellen Zustand des Spiels in der Datei.

        Argumente:
        - board (Board): Der aktuelle Zustand des Spielfelds.
        - moves (int): Die Anzahl der gemachten Züge.
        """
        game_state = {
            'size': board.size,
            'board': board.board,
            'moves': moves,
            'empty_pos': board.empty_pos
        }
        with open(self.save_file, 'w') as f:
            json.dump(game_state, f)

    def load_game(self):
        """
        Lädt einen gespeicherten Zustand aus der Datei.

        Rückgabe:
        - dict: Der gespeicherte Zustand des Spiels, falls vorhanden.
        - None: Falls keine gespeicherte Datei existiert.
        """
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as f:
                return json.load(f)
        return None