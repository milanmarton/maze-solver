import unittest
from maze_solver.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        """Checks if the maze is created right"""
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_cell_initialization(self):
        """Check if cells are initialized with walls on all sides."""
        num_cols = 5
        num_rows = 5
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        for row in maze._cells:
            for cell in row:
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)

    def test_maze_dimensions(self):
        """Check if the maze has the correct dimensions."""
        num_cols = 8
        num_rows = 8
        cell_size_x = 15
        cell_size_y = 15
        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        self.assertEqual(maze.num_rows, num_rows)
        self.assertEqual(maze.num_cols, num_cols)
        self.assertEqual(maze.cell_size_x, cell_size_x)
        self.assertEqual(maze.cell_size_y, cell_size_y)


if __name__ == "__main__":
    unittest.main()
