# Sudoku Solver

This Python program solves a Sudoku puzzle using a backtracking algorithm. It provides a graphical user interface using the Pygame library to display the puzzle and its solution.

## Requirements

To run this program, you need to have the following installed:

- Python 3.x
- Pygame library

## Installation

1. Clone this repository or download the source code.

2. Install the Pygame library using pip:

   ```shell
   pip install pygame
   ```

## Usage

1. Open a terminal or command prompt and navigate to the directory where the source code is located.

2. Run the program by executing the following command:

   ```shell
   python sudoku_solver.py
   ```

3. The Sudoku puzzle grid will be displayed on the screen. An example puzzle is already provided in the code.

4. Close the window or press the "X" button to exit the program.

## How It Works

The program employs a backtracking algorithm to solve the Sudoku puzzle. Here's a high-level overview of the algorithm:

1. Find the next empty cell in the grid.

2. Try numbers from 1 to 9 in the empty cell.

3. If a number is valid in the current position, place it in the cell and recursively attempt to solve the remaining puzzle.

4. If the current configuration leads to an invalid solution, backtrack by resetting the cell value to 0 and trying the next number.

5. Repeat steps 1-4 until a valid solution is found or all possibilities have been exhausted.

The Pygame library is used to create the graphical user interface. The `draw_grid` function renders the Sudoku grid on the screen, and the `main` function initializes the Pygame window, handles user events, and updates the display.

## Customization

You can customize the Sudoku puzzle by modifying the `grid` variable in the `main` function. Use 0 to represent empty cells and fill in the numbers for the initial puzzle. The program will solve the puzzle and display the solution on the screen.

Feel free to explore and modify the code to suit your needs!

## Contributing

Contributions, suggestions, improvements, and bug fixes are welcome! Please create a pull request with your changes, and they will be reviewed.

## License

This program is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code.
