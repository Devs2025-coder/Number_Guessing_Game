import random

class GuessNumber:
    def __init__(self, difficulty):
        """Initialize the game with a selected difficulty and random number."""
        self.difficulty = difficulty
        self.attempts = self.set_attempts()
        self.number_to_guess = random.randint(1, 5)  # guessing range is 1–100

    def set_attempts(self):
        """Set number of attempts based on difficulty."""
        if self.difficulty == 1:
            return 10  # Easy
        elif self.difficulty == 2:
            return 8   # Medium
        elif self.difficulty == 3:
            return 5   # Hard
        else:
            raise ValueError("Invalid difficulty level")

    def check_guess(self, guess):
        """Compare user's guess to the number and return hint."""
        if guess > self.number_to_guess:
            return "high"
        elif guess < self.number_to_guess:
            return "low"
        else:
            return "correct"
