from __future__ import (
    annotations,
)  # postpones the evaluation of all annotations until they're needed
from tkinter import Tk, BOTH, Canvas
from typing import Optional


class Point:
    def __init__(self, x: int, y: int) -> None:
        # x=0 -> left of the screen
        # y=0 -> top of the screen
        self.x = x
        self.y = y


class Line:
    def __init__(self, P1: Point, P2: Point) -> None:
        self.P1 = P1
        self.P2 = P2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.P1.x, self.P1.y, self.P2.x, self.P2.y, fill=fill_color, width=2
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title("maze solver")
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)


class Cell:
    def __init__(self, P1: Point, P2: Point, win: Optional[Window] = None) -> None:
        # P(x1,y1) is supposedly the top-left corner
        # P(x2,y2) is supposedly the bottom-right corner
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = P1.x
        self._x2 = P2.x
        self._y1 = P1.y
        self._y2 = P2.y
        self._win = win

    def draw(self) -> None:
        if not self._win:
            return
        if self.has_left_wall:
            self._win.canvas.create_line(
                self._x1, self._y1, self._x1, self._y2, fill="black"
            )
        else:
            self._win.canvas.create_line(
                self._x1, self._y1, self._x1, self._y2, fill="white"
            )

        if self.has_top_wall:
            self._win.canvas.create_line(
                self._x1, self._y1, self._x2, self._y1, fill="black"
            )
        else:
            self._win.canvas.create_line(
                self._x1, self._y1, self._x2, self._y1, fill="white"
            )

        if self.has_right_wall:
            self._win.canvas.create_line(
                self._x2, self._y1, self._x2, self._y2, fill="black"
            )
        else:
            self._win.canvas.create_line(
                self._x2, self._y1, self._x2, self._y2, fill="white"
            )

        if self.has_bottom_wall:
            self._win.canvas.create_line(
                self._x1, self._y2, self._x2, self._y2, fill="black"
            )
        else:
            self._win.canvas.create_line(
                self._x1, self._y2, self._x2, self._y2, fill="white"
            )

    def draw_move(self, to_cell: Cell, undo=False):
        if not self._win:
            return
        line_color = "gray" if undo else "red"

        self_middle_x = (self._x1 + self._x2) / 2
        self_middle_y = (self._y1 + self._y2) / 2
        to_middle_x = (to_cell._x1 + to_cell._x2) / 2
        to_middle_y = (to_cell._y1 + to_cell._y2) / 2

        self._win.canvas.create_line(
            self_middle_x, self_middle_y, to_middle_x, to_middle_y, fill=line_color
        )
