import time
from Game.player import Player
from Game.guess_number import GuessNumber
import logo  # assuming logo.logo exists

class Game:
    def __init__(self):
        print(logo.logo)
        print("\n🎮 Welcome to the Number Guessing Game!")
        name = input("Enter your name: ").strip().title() or "Player"
        self.player = Player(name)

    def welcome_message(self):
        print("\nI'm thinking of a number between 1 and 100.")
        print("Please select the difficulty level:")
        print(" 1. Easy (10 Chances)")
        print(" 2. Medium (8 Chances)")
        print(" 3. Hard (5 Chances)\n")

    def ask_to_view_record(self):
        """Ask user if they want to see their record."""
        choice = input(f"\nHey {self.player.name}, would you like to view your past record? (yes/no): ").strip().lower()
        if choice == "yes":
            self.player.show_record()
        else:
            print("Alright, let's continue!\n")

    def select_difficulty(self):
        while True:
            try:
                diff = int(input("Enter your choice (1-3): "))
                if diff not in [1, 2, 3]:
                    raise ValueError
                return diff
            except ValueError:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")

    def play(self):
        self.welcome_message()
        self.ask_to_view_record()

        difficulty = self.select_difficulty()
        game_session = GuessNumber(difficulty)

        print(f"\n✅ You selected {'Easy' if difficulty == 1 else 'Medium' if difficulty == 2 else 'Hard'} level.")
        print(f"You have {game_session.attempts} chances to guess the correct number.\n")

        start_time = time.time()

        while game_session.attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue

            result = game_session.check_guess(guess)

            if result == "high":
                print("📈 Your guess is too high.\n")
            elif result == "low":
                print("📉 Your guess is too low.\n")
            else:
                end_time = time.time()
                time_taken = end_time - start_time
                print(f"🎉 Congrats {self.player.name}! You guessed the number correctly in {time_taken:.2f} seconds!")
                self.player.update_record(time_taken, game_session.attempts)
                break

            game_session.attempts -= 1
            print(f"Attempts left: {game_session.attempts}\n")

        if game_session.attempts == 0:
            print(f"💀 You are out of attempts! The correct number was {game_session.number_to_guess}.")

        # Ask if they want to see updated record
        view_after = input("\nWould you like to see your updated record? (yes/no): ").strip().lower()
        if view_after == "yes":
            self.player.show_record()
        else:
            print("Okay, record saved silently. 😊")

    def start(self):
        play_again = "yes"
        while play_again == "yes":
            self.play()
            play_again = input("\nEnter 'yes' to play again or anything else to quit: ").strip().lower()
        print("\n👋 Thanks for playing! See you again.")
