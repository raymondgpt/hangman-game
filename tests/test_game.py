"""Unit tests for the core game logic (stdlib unittest, no deps)."""

import unittest

from hangman.game import HangmanGame


class TestHangmanGame(unittest.TestCase):
    def test_correct_guess_reveals_letter(self):
        game = HangmanGame("cat")
        self.assertTrue(game.guess("a"))
        self.assertEqual(game.revealed, "_ a _")

    def test_wrong_guess_reduces_lives(self):
        game = HangmanGame("cat")
        self.assertFalse(game.guess("z"))
        self.assertEqual(game.remaining_guesses, 5)

    def test_duplicate_guess_is_ignored(self):
        game = HangmanGame("cat")
        game.guess("z")
        lives_after_first = game.remaining_guesses
        game.guess("z")
        self.assertEqual(game.remaining_guesses, lives_after_first)

    def test_win_detection(self):
        game = HangmanGame("cat")
        for letter in "cat":
            game.guess(letter)
        self.assertTrue(game.is_won)
        self.assertTrue(game.is_over)

    def test_loss_detection(self):
        game = HangmanGame("cat", max_wrong=6)
        for letter in "xyzquv":
            game.guess(letter)
        self.assertTrue(game.is_lost)
        self.assertTrue(game.is_over)


if __name__ == "__main__":
    unittest.main()
