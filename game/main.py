"""
Das Hauptmodul des Sliding-Puzzle-Spiels.
- Hier wird der Einstiegspunkt des Spiels definiert.
- Beinhaltet das Menü, die Benutzerinteraktion und die Spielschleife.

Funktionen:
- main(): Führt das Spiel aus, bietet Optionen zum Starten, Laden oder Beenden.
"""

from sliding_puzzle import SlidingPuzzle

def main():
    while True:
        print("\nWillkommen zum Sliding Puzzle!")

        # Hauptmenü mit Optionen
        choice = input("Was möchten Sie tun?\n1. Neues Spiel starten\n2. Spiel laden\n3. Beenden\nEingabe: ")

        if choice == '3':
            break

        if choice == '2':
            game = SlidingPuzzle()
            if game.load_saved_game():
                print("Spiel erfolgreich geladen!")
            else:
                print("Kein gespeichertes Spiel gefunden!")
                continue
        else:
            # Abfrage der Spielfeldgröße
            while True:
                try:
                    size = int(input("Geben Sie die Spielfeldgröße ein (min. 2): "))
                    if size >= 2:
                        break
                    print("Die Größe muss mindestens 2 sein!")
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein!")

            game = SlidingPuzzle(size)

            # Auswahl der Initialisierungsmethode
            init_choice = input("Wählen Sie die Initialisierungsmethode:\n1. Zufällig\n2. Manuell\nEingabe: ")
            if init_choice == '1':
                game.initialize_random()
            else:
                game.initialize_manual()

        # Speichern-Option verwalten
        def handle_save_game(game):
            game.save_game()
            while True:
                choice = input("Möchten Sie (q)uit beenden oder (c)ontinue weiterspielen? ").lower()
                if choice == 'q':
                    return False  # Spielschleife verlassen
                elif choice == 'c':
                    return True  # Spiel fortsetzen
                print("Bitte 'q' für Beenden oder 'c' für Fortsetzen eingeben.")

        # Hauptspielschleife
        while not game.is_solved():
            game.display_board()

            action = input("\nGeben Sie eine Zahl zum Verschieben oder 's' zum Speichern ein: ")

            if action.lower() == 's':
                if not handle_save_game(game):
                    break  # Zurück ins Hauptmenü
                continue

            try:
                move = int(action)
                if 1 <= move <= (game.board.size * game.board.size - 1):
                    if not game.make_move(move):
                        print("Ungültiger Zug! Wählen Sie eine Zahl, die neben dem leeren Feld liegt.")
                else:
                    print(f"Bitte eine Zahl zwischen 1 und {game.board.size * game.board.size - 1} eingeben.")
            except ValueError:
                print("Bitte eine gültige Zahl oder 's' eingeben.")

        game.display_board()
        print(f"\nHerzlichen Glückwunsch! Sie haben das Puzzle in {game.moves} Zügen gelöst!")

        if input("\nMöchten Sie erneut spielen? (y/n): ").lower() != 'y':
            break

    print("Danke fürs Spielen!")

if __name__ == "__main__":
    main()