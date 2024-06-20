# Snake Game

This is a classic Snake Game implemented using Python's `turtle` graphics library and `pygame` for sound effects. The objective of the game is to eat the food to grow the snake and score points while avoiding collisions with the walls and the snake's own body. The game also includes special meals and power-ups that affect the gameplay.

## Features

- Classic Snake Game mechanics.
- Sound effects for eating food and hitting walls, using `pygame`.
- Randomly appearing special meals (blue circles) and power-ups (yellow squares).
- Score tracking and high score display.
- Variable game speed with a delay that decreases as the snake eats more food.
- Temporary speed boost when a power-up is collected.

## Prerequisites

Make sure you have Python installed on your system. Additionally, you need to install the `pygame` library for sound effects.

You can install `pygame` using pip:

\```sh
pip install pygame
\```

## Files

- `snake_game.py`: The main game script.
- `sounds/eat.mp3`: Sound file played when the snake eats food.
- `sounds/hit.mp3`: Sound file played when the snake hits the wall or itself.

## How to Run

1. Clone the repository:

\```sh
git clone https://github.com/priyeshj1/snake-game.git
\```

2. Navigate to the project directory:

\```sh
cd snake-game
\```

3. Run the game:

\```sh
python snake_game.py
\```

## Controls

- **W**: Move up
- **S**: Move down
- **A**: Move left
- **D**: Move right

## Game Mechanics

- The snake starts at the center of the screen and can be moved using the keyboard controls.
- The red circle represents the food. Eating food increases the snake's length and score.
- The blue circle represents a special meal. Eating it significantly increases the snake's length and score.
- The yellow square represents a power-up. Collecting it temporarily increases the snake's speed.
- If the snake collides with the wall or its own body, the game resets and the score is set to zero.

## Score

- Eating regular food increases the score by 10 points.
- Eating a special meal increases the score by 50 points.
- The high score is tracked and displayed at the top of the screen.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- The game is inspired by the classic Snake Game.
- Sound effects are implemented using the `pygame` library.

## Contributing

Feel free to fork this project, create a new branch, and submit a pull request with your improvements or bug fixes. Any contributions are welcome!

---

Thank you for playing the Snake Game! Enjoy and have fun!
