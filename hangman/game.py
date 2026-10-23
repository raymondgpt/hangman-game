"""Core Hangman game logic (no I/O, easy to unit test)."""

MAX_WRONG_GUESSES = 6


class HangmanGame:
    """Tracks the state of a single Hangman round."""

    def __init__(self, word, max_wrong=MAX_WRONG_GUESSES):
        self.word = word.lower()
        self.max_wrong = max_wrong
        self.guessed = set()
        self.wrong_guesses = []

    @property
    def revealed(self):
        """The word with unguessed letters masked as underscores."""
        return " ".join(ch if ch in self.guessed else "_" for ch in self.word)

    @property
    def remaining_guesses(self):
        """How many wrong guesses are still allowed."""
        return self.max_wrong - len(self.wrong_guesses)

    @property
    def is_won(self):
        return all(ch in self.guessed for ch in self.word)

    @property
    def is_lost(self):
        return self.remaining_guesses <= 0

    @property
    def is_over(self):
        return self.is_won or self.is_lost

    def guess(self, letter):
        """Record a guess.

        Returns True if the letter is in the word, False otherwise.
        Letters are stored lowercase; duplicate guesses are ignored.
        """
        letter = letter.lower()
        if letter in self.guessed:
            return letter in self.word
        self.guessed.add(letter)
        if letter in self.word:
            return True
        self.wrong_guesses.append(letter)
        return False
