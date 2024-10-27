# Maze Solver

A Python application that generates and solves mazes using a recursive depth-first search (DFS) algorithm. The application includes a graphical interface that visualizes both the maze generation and solving process in real-time.

## Features

- Random maze generation using recursive backtracking
- Interactive GUI built with Tkinter
- Real-time visualization of maze generation and solving process
- Customizable maze dimensions and cell sizes
- Automated maze solving using depth-first search
- Comprehensive test suite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/milanmarton/maze-solver.git
cd maze-solver
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main application:

```bash
python main.py
```

The application will open a window displaying:

- The maze generation process in real-time
- The solving algorithm's path-finding visualization
- The final solution path highlighted in red

You can customize the maze parameters by modifying the arguments in `main.py`:

```python
maze = Maze(
    x1=20,           # Starting X coordinate
    y1=20,           # Starting Y coordinate
    num_rows=14,     # Number of rows in the maze
    num_cols=19,     # Number of columns in the maze
    cell_size_x=40,  # Cell width in pixels
    cell_size_y=40,  # Cell height in pixels
    win=window       # Window instance
)
```

You can also customize the animation speed by modifying two constants in `maze.py`:

```python
ANIMATION_SPEED = 0.15  # solving speed
CREATION_ANIMATION_SPEED = 0.001  # maze generation
```

## Running Tests

The project includes a comprehensive test suite to verify the maze generation and solving functionality:

```bash
python -m unittest discover tests
```

## Project Structure

```
maze_solver/
├── maze_solver/
│   ├── __init__.py
│   ├── gui.py      # GUI components and window management
│   └── maze.py     # Maze generation and solving algorithms
├── tests/
│   ├── __init__.py
│   └── test_maze.py
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

## How It Works

1. **Maze Generation**: Uses a recursive depth-first search algorithm with backtracking to generate the maze:

   - Starts from the top-left cell
   - Randomly chooses unvisited neighboring cells
   - Breaks walls between cells to create paths
   - Backtracks when reaching dead ends

2. **Maze Solving**: Implements a depth-first search to find a path from start to finish:
   - Explores possible paths from the entrance
   - Marks the current path in red
   - Backtracks and marks failed paths in gray
   - Highlights the successful path from entrance to exit

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
