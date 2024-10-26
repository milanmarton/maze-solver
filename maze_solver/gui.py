from tkinter import Tk, BOTH, Canvas


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

    def draw(self, canvas: Canvas, fill_color: str):
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
