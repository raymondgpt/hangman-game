"""Terminal user interface for Hangman."""

import os
import random
import sys

from .game import HangmanGame
from .words import WORDS

# ASCII art, index = number of wrong guesses (0..6). Stage 6 = game over.
HANGMAN_STAGES = [
    r"""
  +---+
      |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

BANNER = r"""
 _   _                                         
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       
"""


def clear_screen():
    """Clear the terminal, working on Windows and POSIX shells."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def draw(game):
    """Print the hangman figure, revealed word, and guess status."""
    print(HANGMAN_STAGES[len(game.wrong_guesses)])
    print("Word:   ", game.revealed)
    used = " ".join(sorted(game.guessed)) if game.guessed else "-"
    print("Used:    ", used)
    print("Lives left:", game.remaining_guesses)
    print()


def run_cli():
    """Play rounds of Hangman until the player quits."""
    clear_screen()
    print(BANNER)
    while True:
        word = random.choice(WORDS)
        game = HangmanGame(word)

        while not game.is_over:
            draw(game)
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter (a-z).")
                input("Press Enter to continue...")
                continue

            if guess in game.guessed:
                print(f"You already guessed '{guess}'.")
                input("Press Enter to continue...")
                continue

            game.guess(guess)

        clear_screen()
        draw(game)
        if game.is_won:
            print(f"You won! The word was '{game.word}'.")
        else:
            print(f"You lost! The word was '{game.word}'.")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        clear_screen()
