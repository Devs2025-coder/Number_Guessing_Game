Here’s a **professional `README.md`** for your **Number Guessing Game (OOP Version)** project — written in a clean and developer-friendly format 👇

---

```markdown
# 🎮 Number Guessing Game (CLI Version)

An interactive **Number Guessing Game** built in **Python**, designed using the principles of **Object-Oriented Programming (OOP)**.  
The game challenges the player to guess a random number between **1 and 100** with limited attempts based on the chosen difficulty level.  
It also stores the **highest record** (best time and attempts) in a JSON file for future reference.

---

## Project URL:
https://roadmap.sh/projects/number-guessing-game

## 🧠 Features

- 🎯 **Three Difficulty Levels:**
  - Easy → 10 chances  
  - Medium → 8 chances  
  - Hard → 5 chances  

- 📁 **Automatic Record Saving:**
  - Stores player's best performance (`time` and `attempts`) in a `record.json` file.
  - The file is safely stored inside a `Record` folder.

- 🧍‍♂️ **Player Profile:**
  - Players can enter their name.
  - View their previous records before playing.

- 🧩 **OOP Structure:**
  - Follows clean modular design with separate classes for `Player`, `Game`, and `GuessNumber`.
  - Encapsulated storage management system for saving and loading records.

- 🔁 **Replay Option:**
  - Option to play multiple rounds in one session.

---

## 🗂️ Folder Structure

```

NumberGuessingGame/
│
├── main.py
├── logo.py
│
├── Game/
│   ├── **init**.py
│   ├── game_controller.py
│   ├── guess_number.py
│   ├── player.py
│   └── storage.py
│
└── Record/
└── record.json

````

---

## 🚀 How to Run the Game

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git
````

2. **Navigate to the project folder:**

   ```bash
   cd number-guessing-game
   ```

3. **Run the game:**

   ```bash
   python main.py
   ```

4. **Follow the on-screen instructions** to select difficulty, make guesses, and view your record.

---

## ⚙️ Technical Overview

| Component            | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| `main.py`            | Entry point of the application. Runs the game.                      |
| `game_controller.py` | Controls the game logic, difficulty, and flow.                      |
| `guess_number.py`    | Handles random number generation and guess validation.              |
| `player.py`          | Manages player data and record updates.                             |
| `storage.py`         | Handles saving and loading JSON records inside the `Record` folder. |
| `logo.py`            | Contains ASCII art or banner displayed when the game starts.        |

---

## 🏆 Record System

* All player records are stored in:

  ```
  Record/record.json
  ```
* Automatically created on first run.
* Updates only if the player achieves a **better record** (less time or fewer attempts).

---

## 💡 Example Gameplay

```
🎮 Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.
Please select the difficulty level:
 1. Easy (10 Chances)
 2. Medium (8 Chances)
 3. Hard (5 Chances)

✅ You selected Medium level.
You have 8 chances to guess the correct number.

Enter your guess: 45
📉 Your guess is too low.

Enter your guess: 68
📈 Your guess is too high.

Enter your guess: 52
🎉 Congrats Jeet! You guessed the number correctly in 6.21 seconds!
```

---

## 🧰 Requirements

* Python 3.8 or above
* Works on Windows, macOS, and Linux (no external dependencies required)

---

## 🧑‍💻 Author

**Jeet** — Engineer & Python Developer
💼 Passionate about writing clean, modular, and scalable Python applications.
📧 *You can connect with me for collaborations or feedback.*

---

⭐ **If you liked this project, don’t forget to star the repository!**
