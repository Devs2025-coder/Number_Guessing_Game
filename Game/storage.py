import json
import os

RECORD_DIR = "Record"
RECORD_FILE = os.path.join(RECORD_DIR, "record.json")


class Storage:
    def __init__(self):
        """Ensure the Record folder and file exist."""
        if not os.path.exists(RECORD_DIR):
            os.makedirs(RECORD_DIR)
        if not os.path.exists(RECORD_FILE):
            with open(RECORD_FILE, "w") as f:
                json.dump({}, f, indent=4)

    def _load_all_records(self):
        """Load all player records from file."""
        with open(RECORD_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def _save_all_records(self, records):
        """Save all records back to file."""
        with open(RECORD_FILE, "w") as f:
            json.dump(records, f, indent=4)

    def get_record(self, player_name):
        """Retrieve the record of a specific player."""
        records = self._load_all_records()
        return records.get(player_name)

    def update_record(self, player_name, time_taken, attempts_left):
        """
        Update record for the player.
        A better record means more attempts left or same attempts but less time.
        """
        records = self._load_all_records()
        current = records.get(player_name)

        new_record = {
            "Time taken (seconds)": round(time_taken, 2),
            "Attempts left": attempts_left
        }

        if current:
            prev_time = current.get("Time taken (seconds)")
            prev_attempts = current.get("Attempts left")

            # Compare — better if more attempts left or equal attempts but less time
            if (attempts_left > prev_attempts) or (
                attempts_left == prev_attempts and time_taken < prev_time
            ):
                records[player_name] = new_record
                print(f"\n🎉 New Record for {player_name}! Saved successfully!\n")
            else:
                print("\nRecord not beaten this time. Keep trying!\n")
        else:
            records[player_name] = new_record
            print(f"\n🏅 First record saved for {player_name}!\n")

        self._save_all_records(records)
