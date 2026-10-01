# Chess

A desktop chess game in Python and pygame. You can play against another person on the same machine, or against a bot with three difficulty levels.

The rules (castling, en passant, promotion, check, checkmate, stalemate, insufficient material, repetition and the 50/75-move rules) come from [`python-chess`](https://python-chess.readthedocs.io/). This project handles the board UI and the bot.

## Run it

```sh
pip install -r requirements.txt
python Bot/Bot.py
```

It works from any directory, since piece images are loaded relative to the script.

## Features

- **Player vs Player** or **Player vs Bot**. You play White against the bot.
- **Bot difficulties:**

  | Level | How it picks a move |
  |---|---|
  | Easy | A random legal move |
  | Medium | The most valuable capture available, otherwise a random move |
  | Hard | A 3-ply alpha-beta search over material and simple positional terms (centre control, pawn advancement). It finds short mates and doesn't hang pieces carelessly. It replies in well under a second. |

- The bot's last move is highlighted.
- **Promotion picker:** choose queen, rook, bishop or knight.
- **Draws:** threefold repetition and the fifty-move rule are claimed automatically.
- Clicking another of your own pieces switches the selection.
- Restart with confirmation.

## Project layout

| Path | What it is |
|---|---|
| `Bot/Bot.py` | The game: pygame UI and input handling |
| `Bot/engine.py` | Move selection for each difficulty, plus the game-over messages |
| `tests/test_engine.py` | Tests for the engine (legal moves, mate-in-one, captures, draw claims, speed) |
| `pieces/` | Piece images |
| `legacy/` | Earlier experiments, kept for reference (see below) |

## Tests

```sh
pip install pytest
python -m pytest tests
```

## Legacy scripts

`legacy/` contains earlier versions. They are not maintained:

- `Chess_tkinter.py`: my first chess program, a Tkinter GUI. It has known bugs.
- `Chess_notation.py`: you play by typing algebraic notation instead of clicking pieces.
- `Chess.py`: a pygame version that was meant to show a move list in algebraic notation. The move list doesn't work correctly.

These scripts load images from `pieces/`, so run them from the repository root, e.g. `python legacy/Chess_notation.py`.

## License

MIT, see [LICENSE](LICENSE).
