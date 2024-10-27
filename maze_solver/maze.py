from maze_solver.gui import Cell, Point, Window
import time
from typing import Optional


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
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._cells = []
        self._create_cells()

    def _create_cell(self, row_num: int, col_num: int) -> Cell:
        x1 = self.x1 + col_num * self.cell_size_x
        y1 = self.y1 + row_num * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        return Cell(p1, p2, self.win)

    def _create_cells(self):
        self._cells = [
            [self._create_cell(row_num, col_num) for col_num in range(self.num_cols)]
            for row_num in range(self.num_rows)
        ]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)

    def _draw_cell(self, row_num: int, col_num: int):
        self._cells[row_num][col_num].draw()
        self._animate()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        end_cell = self._cells[self.num_rows - 1][self.num_cols - 1]

        start_cell.has_top_wall = False
        start_cell.draw()
        end_cell.has_bottom_wall = False
        end_cell.draw()
