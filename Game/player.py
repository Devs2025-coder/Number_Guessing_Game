from Game.storage import Storage

class Player:
    def __init__(self, name="Player"):
        """Initialize a player with name and load their previous record if available."""
        self.name = name
        self.highest_record = {}
        self.storage = Storage()
        self.load_previous_record()

    def load_previous_record(self):
        """Load existing player record from JSON storage."""
        record = self.storage.get_record(self.name)
        if record:
            self.highest_record = record

    def update_record(self, time_taken, attempts_left):
        """Update both local and JSON records when player wins."""
        self.highest_record = {
            "Time taken (seconds)": round(time_taken, 2),
            "Attempts left": attempts_left
        }
        self.storage.update_record(self.name, time_taken, attempts_left)

    def show_record(self):
        """Display the player’s best record."""
        if self.highest_record:
            print(f"\n🏆 Highest Record for {self.name}:")
            for key, value in self.highest_record.items():
                print(f"  {key}: {value}")
        else:
            print("\nNo records yet! Play a game first.")
