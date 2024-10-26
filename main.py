import maze_solver.gui as gui


def main():
    win = gui.Window(800, 600)
    p1 = gui.Point(100, 100)
    p2 = gui.Point(500, 500)
    line = gui.Line(p1, p2)
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
