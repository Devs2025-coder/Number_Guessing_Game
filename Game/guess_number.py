import random

class GuessNumber:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.attempts = self.set_attempts()
        self.number_to_guess = random.randint(1, 100)

    def set_attempts(self):
        if self.difficulty == 1:
            return 10
        elif self.difficulty == 2:
            return 8
        elif self.difficulty == 3:
            return 5
        else:
            raise ValueError("Invalid difficulty level")

    def check_guess(self, guess):
        if guess > self.number_to_guess:
            return "high"
        elif guess < self.number_to_guess:
            return "low"
        else:
            return "correct"
