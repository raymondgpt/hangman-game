# Hangman Game

A small terminal word-guessing game written in pure Python (no external
dependencies).

## Run

```bash
python main.py
```

Guess one letter at a time. You get 6 wrong guesses before the game is over.

## Test

```bash
python -m unittest discover -s tests
```

## Project layout

```
hangman-game/
├── main.py              # entry point
├── hangman/
│   ├── __init__.py
│   ├── words.py         # word list
│   ├── game.py          # pure game logic
│   └── cli.py           # terminal UI
└── tests/
    └── test_game.py     # unit tests
```

Requires Python 3.8+.
