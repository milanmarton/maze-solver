from maze_solver.gui import Cell, Point, Window
import time
import random
from typing import Optional

ANIMATION_SPEED = 0.15  # solving speed
CREATION_ANIMATION_SPEED = 0.001  # maze generation


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Optional[Window] = None,
        seed=None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)  # Set the seed for random number generation
        self._create_cells()

    def _create_cell(self, row_num: int, col_num: int) -> Cell:
        x1 = self.x1 + col_num * self.cell_size_x
        y1 = self.y1 + row_num * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        return Cell(p1, p2, self.win)

    def _create_cells(self) -> None:
        self._cells = [
            [self._create_cell(row_num, col_num) for col_num in range(self.num_cols)]
            for row_num in range(self.num_rows)
        ]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col, CREATION_ANIMATION_SPEED)

    def _draw_cell(
        self, row_num: int, col_num: int, animation_speed: float = ANIMATION_SPEED
    ) -> None:
        self._cells[row_num][col_num].draw()
        self._animate(animation_speed)

    def _animate(self, animation_speed: float = ANIMATION_SPEED) -> None:
        if not self.win:
            return
        self.win.redraw()
        time.sleep(animation_speed)

    def _break_entrance_and_exit(self) -> None:
        start_cell = self._cells[0][0]
        end_cell = self._cells[self.num_rows - 1][self.num_cols - 1]

        start_cell.has_top_wall = False
        start_cell.draw()
        end_cell.has_bottom_wall = False
        end_cell.draw()

    def _break_walls_r(self, row: int, col: int) -> None:
        # breaking walls using DFS

        # mark current cell as visited
        self._cells[row][col].visited = True

        while True:
            possible_directions = []

            if row > 0 and not self._cells[row - 1][col].visited:
                possible_directions.append((row - 1, col, "up"))
            if row < self.num_rows - 1 and not self._cells[row + 1][col].visited:
                possible_directions.append((row + 1, col, "down"))
            if col > 0 and not self._cells[row][col - 1].visited:
                possible_directions.append((row, col - 1, "left"))
            if col < self.num_cols - 1 and not self._cells[row][col + 1].visited:
                possible_directions.append((row, col + 1, "right"))

            # dead end
            if len(possible_directions) == 0:
                self._draw_cell(row, col, CREATION_ANIMATION_SPEED)
                return

            next_row, next_col, dir = random.choice(possible_directions)

            current_cell = self._cells[row][col]
            next_cell = self._cells[next_row][next_col]

            if dir == "up":
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif dir == "down":
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif dir == "left":
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif dir == "right":
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False

            # draw the current cell
            self._draw_cell(row, col, CREATION_ANIMATION_SPEED)

            # recursively call the next cell
            self._break_walls_r(next_row, next_col)

    def _reset_cells_visited(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._cells[row][col].visited = False

    def solve(self) -> bool:
        self._reset_cells_visited()
        return self._solve_r(0, 0)

    def _solve_r(self, row: int, col: int) -> bool:
        if not self.win:
            return False

        self._animate()

        current_cell = self._cells[row][col]
        current_cell.visited = True

        # end cell check
        if row == self.num_rows - 1 and col == self.num_cols - 1:
            return True

        directions = [
            (-1, 0, "has_top_wall"),  # up
            (0, 1, "has_right_wall"),  # right
            (1, 0, "has_bottom_wall"),  # down
            (0, -1, "has_left_wall"),  # left
        ]

        for delta_row, delta_col, wall_attr in directions:
            new_row = row + delta_row
            new_col = col + delta_col

            # check if new cell is within bounds
            if 0 <= new_row < self.num_rows and 0 <= new_col < self.num_cols:
                next_cell = self._cells[new_row][new_col]

                # check that there is no wall and the next cell is not visited
                if not getattr(current_cell, wall_attr) and not next_cell.visited:
                    current_cell.draw_move(next_cell)
                    # self._animate()

                    # recursively try this path
                    if self._solve_r(new_row, new_col):
                        return True

                    # if path didn't work, undo the move
                    current_cell.draw_move(next_cell, undo=True)
                    # self._animate()

        return False
