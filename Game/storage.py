import json
import os

class Storage:
    def __init__(self, folder_name="Record", filename="records.json"):
        self.folder_name = folder_name
        self.filename = filename
        self.filepath = os.path.join(self.folder_name, self.filename)

        # Ensure folder exists
        os.makedirs(self.folder_name, exist_ok=True)

        # Load or create records
        self.records = self._load_records()

    def _load_records(self):
        """Load player records from the JSON file if it exists."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("⚠️ Corrupted records file. Creating a new one.")
                return {}
        return {}

    def save_records(self):
        """Save all player records to the JSON file."""
        with open(self.filepath, "w") as file:
            json.dump(self.records, file, indent=4)

    def get_record(self, player_name):
        """Retrieve a player's record, if it exists."""
        return self.records.get(player_name, None)

    def update_record(self, player_name, time_taken, attempts_left):
        """
        Save or update player's record if it's better than previous.
        Better = less time OR more attempts left.
        """
        new_record = {
            "Time taken (seconds)": round(time_taken, 2),
            "Attempts left": attempts_left
        }

        existing_record = self.records.get(player_name)

        if existing_record:
            old_time = existing_record["Time taken (seconds)"]
            old_attempts = existing_record["Attempts left"]

            # Update only if performance improved
            if time_taken < old_time or attempts_left > old_attempts:
                self.records[player_name] = new_record
        else:
            self.records[player_name] = new_record

        self.save_records()
