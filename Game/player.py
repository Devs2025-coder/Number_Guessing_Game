from Game.storage import Storage

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.highest_record = {}
        self.storage = Storage()
        self.load_previous_record()

    def load_previous_record(self):
        record = self.storage.get_record(self.name)
        if record:
            self.highest_record = record

    def update_record(self, time_taken, attempts_left):
        """Update both local and JSON records."""
        self.highest_record = {
            "Time taken (seconds)": round(time_taken, 2),
            "Attempts left": attempts_left
        }
        self.storage.update_record(self.name, time_taken, attempts_left)

    def show_record(self):
        if self.highest_record:
            print("\n🏆 Highest Record:")
            for key, value in self.highest_record.items():
                print(f"{key}: {value}")
        else:
            print("\nNo records yet! Play a game first.")
