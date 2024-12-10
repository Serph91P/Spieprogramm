"""
The main entry point for the Sliding Puzzle game.

This module initializes the game, handles user input, and manages the game loop until the puzzle is solved.
"""
from sliding_puzzle import SlidingPuzzle

def main():
    while True:
        print("\nWelcome to the Sliding Puzzle Game!")
        
        # Get board size
        while True:
            try:
                size = int(input("Enter board size (minimum 2): "))
                if size >= 2:
                    break
                print("Size must be at least 2!")
            except ValueError:
                print("Please enter a valid number!")
        
        game = SlidingPuzzle(size)
        
        # Choose initialization method
        init_choice = input("Choose initialization method:\n1. Random\n2. Manual\nChoice: ")
        if init_choice == '1':
            game.initialize_random()
        else:
            game.initialize_manual()

        def handle_save_game(game):
            game.save_game()
            while True:
                choice = input("Do you want to (q)uit or (c)ontinue playing? ").lower()
                if choice == 'q':
                    return False  # Exit game loop
                elif choice == 'c':
                    return True  # Continue game
                print("Please enter 'q' to quit or 'c' to continue")

        # Main game loop
        while not game.is_solved():
            game.display_board()
            
            action = input("\nEnter number to move or 's' to save game: ")
            
            if action.lower() == 's':
                if not handle_save_game(game):
                    break  # Exit to main menu
                continue
                
            try:
                move = int(action)
                if 1 <= move <= (game.board.size * game.board.size - 1):
                    if not game.make_move(move):
                        print("Invalid move! Choose a number adjacent to the empty space.")
                else:
                    print(f"Please enter a number between 1 and {game.board.size * game.board.size - 1}.")
            except ValueError:
                print("Please enter a valid number or 's' to save.")

        game.display_board()
        print(f"\nCongratulations! You solved the puzzle in {game.moves} moves!")
        
        if input("\nWould you like to play again? (y/n): ").lower() != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
