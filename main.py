from Game.game_controller import Game  # Import the main controller class

def main():
    """Main entry point for the Number Guessing Game."""
    game = Game()
    game.start()  # Starts the full gameplay loop (includes record viewing, difficulty, etc.)

if __name__ == "__main__":
    main()
