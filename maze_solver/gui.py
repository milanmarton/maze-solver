from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("maze solver")
        self.canvas = Canvas(
            self.root, width=self.width, height=self.height, bg="white"
        )
        self.canvas.pack(fill="both", expand=True)
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
