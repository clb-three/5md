# To run:

Due to some caveats of the Python module system, we need to run the module rather than the Python file.
This way, the Python interpreter is aware of the entire `model` package.
Make sure you run inside the root of the project (`5md/`), not inside `5md/model`.

`python -m model.gameloop`

# Usage:

Type commands until the game is over. A command is a line, ending when the user presses `ENTER`.

# Commands:

- Player commands e.g. `benji play shield`:
  - `<player> play <card>`: Make a player play a card against the current enemy
  - `<player> discard <card>`: Make a player discard a card
  - `<player> draw`: Make a player draw from their deck
- `<empty>`: Redo the last command
- `nuke`: Instagib the current monster
- `<3`: Surprise~
- `quit`: Quit the game
