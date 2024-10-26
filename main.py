from maze_solver.gui import Window, Point, Cell


def main():
    win = Window(800, 600)

    # We'll create a 4x4 grid of cells, each 50x50 pixels
    # Starting at (50,50) with 10 pixels spacing between cells
    cell_size = 50
    start_x = 50
    start_y = 50
    spacing = 10

    # Test cases with different wall combinations
    test_cases = [
        # All walls (default)
        {"left": True, "right": True, "top": True, "bottom": True},
        # No walls
        {"left": False, "right": False, "top": False, "bottom": False},
        # Only vertical walls
        {"left": True, "right": True, "top": False, "bottom": False},
        # Only horizontal walls
        {"left": False, "right": False, "top": True, "bottom": True},
        # Only left wall
        {"left": True, "right": False, "top": False, "bottom": False},
        # Only right wall
        {"left": False, "right": True, "top": False, "bottom": False},
        # Only top wall
        {"left": False, "right": False, "top": True, "bottom": False},
        # Only bottom wall
        {"left": False, "right": False, "top": False, "bottom": True},
        # Three walls (missing left)
        {"left": False, "right": True, "top": True, "bottom": True},
        # Three walls (missing right)
        {"left": True, "right": False, "top": True, "bottom": True},
        # Three walls (missing top)
        {"left": True, "right": True, "top": False, "bottom": True},
        # Three walls (missing bottom)
        {"left": True, "right": True, "top": True, "bottom": False},
    ]

    # Create and draw cells with different configurations
    for i, test_case in enumerate(test_cases):
        # Calculate position for each cell (4 cells per row)
        row = i // 4
        col = i % 4

        x1 = start_x + (cell_size + spacing) * col
        y1 = start_y + (cell_size + spacing) * row
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        # Create cell
        cell = Cell(Point(x1, y1), Point(x2, y2), win)

        # Set wall configuration
        cell.has_left_wall = test_case["left"]
        cell.has_right_wall = test_case["right"]
        cell.has_top_wall = test_case["top"]
        cell.has_bottom_wall = test_case["bottom"]

        # Draw cell
        cell.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()
