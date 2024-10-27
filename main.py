from maze_solver.gui import Window, Point, Cell
from maze_solver.maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 8, 8, 40, 40, win, 0)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()

    win.wait_for_close()


if __name__ == "__main__":
    main()
