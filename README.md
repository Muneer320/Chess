# Chess Project

This project is a chess application that includes a graphical user interface, a bot for playing chess, and various utilities for handling algebraic notations.

## Project Structure
- **Algebraic Notations/** 
  - Chess_notation.py 
  - Chess_tkinter.py 
  - Chess.py 
- **Bot/** 
  - Bot.py 
  - test.py 
- pieces/ 
- README.md

### Algebraic Notations

- **Chess_notation.py**: You play the game by entering the notations not by physically moving the pieces.
- **Chess_tkinter.py**: Provides a Tkinter-based GUI for the chess game. [Primitive version has lots of bbugs, this was the first version I made a long years ago]
- **Chess.py**: Another chess with pygame GUI that I made recently.

### Bot

- **Bot.py**: Implements a chess bot that can play against a human or another bot.

### Pieces

This directory contains all the chess pieces.

## Getting Started

### Prerequisites

- Python 3.x
- Pygame module
- Tkinter (for the GUI)

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project-directory>
    ```

#### Running the Application

To start the chess application with the GUI, run:
```sh
python Bot\Bot.py
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.