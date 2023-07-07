import pygame

# Define the dimensions of the Sudoku grid
GRID_SIZE = 9
CELL_SIZE = 60
GRID_WIDTH = CELL_SIZE * GRID_SIZE
GRID_HEIGHT = CELL_SIZE * GRID_SIZE
WINDOW_WIDTH = GRID_WIDTH + 2
WINDOW_HEIGHT = GRID_HEIGHT + 2

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def find_empty_cell(grid):
    # Find the first empty cell in the grid (represented by 0)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return i, j
    return None


def is_valid(grid, num, row, col):
    # Check if the number is valid in the given row
    for i in range(GRID_SIZE):
        if grid[row][i] == num:
            return False

    # Check if the number is valid in the given column
    for i in range(GRID_SIZE):
        if grid[i][col] == num:
            return False

    # Check if the number is valid in the current 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    # Find the next empty cell in the grid
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # All cells have been filled, puzzle solved

    row, col = empty_cell

    # Try numbers from 1 to 9
    for num in range(1, 10):
        if is_valid(grid, num, row, col):
            grid[row][col] = num

            # Recursively try to solve the remaining puzzle
            if solve_sudoku(grid):
                return True

            # If the current configuration leads to an invalid solution, backtrack
            grid[row][col] = 0

    return False  # No valid solution found


def draw_grid(screen, grid):
    for i in range(GRID_SIZE + 1):
        if i % 3 == 0:
            line_color = BLACK
        else:
            line_color = BLUE

        # Draw horizontal lines
        pygame.draw.line(screen, line_color, (0, i * CELL_SIZE), (GRID_WIDTH, i * CELL_SIZE), 2)

        # Draw vertical lines
        pygame.draw.line(screen, line_color, (i * CELL_SIZE, 0), (i * CELL_SIZE, GRID_HEIGHT), 2)

    font = pygame.font.SysFont(None, 40)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                number = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(number, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoku Solver")

    clock = pygame.time.Clock()

    # Example usage
    grid = [
        [8, 2, 0, 3, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 4],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 6, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [9, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 8, 0, 3, 9]
    ]

    

    solve_sudoku(grid)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(screen, grid)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
