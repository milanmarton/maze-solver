from maze_solver.gui import Window, Point, Cell
from maze_solver.maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(20, 20, 14, 19, 40, 40, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
