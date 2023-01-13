from AStar import Grid, Path, Node
from AStar.AsciiPrint.Grid import grid_path_lookup
from AStar.AsciiPrint.Grid._boarder_chars import *


def with_path(grid: Grid, path: Path):
    """
Prints the given grid.
If a node is in the path then there will be a connection to the next node, otherwise just a square.
    :param grid: The grid to print.
    :param path: The path to print with the grid.
    """

    print(TOP_LEFT + HORIZONTAL * grid.x_size + TOP_RIGHT)  # Boarder

    for y in range(grid.y_size):
        print(VERTICAL, end='')  # Boarder

        for x in range(grid.x_size):

            # Not part of the path
            if grid[x, y] not in path.path:
                if grid[x, y].connections:
                    print(' ', end='')
                else:
                    print('█', end='')
                continue

            # Start
            if grid[x, y] is path.start:
                print("S", end='')
                continue

            # End
            if grid[x, y] is path.end:
                print('E', end='')
                continue

            # Part of the path
            me = grid[x, y]
            my_index = path.path.index(me)

            previous: Node | None = None
            following: Node | None = None

            if my_index >= 1:
                previous = path[my_index - 1]

            if my_index < len(path.path) - 1:
                following = path[my_index + 1]

            # Finding which character to use
            lookup = ['0' for _ in range(4)]

            if ((previous is not None) and (previous.y_position < me.y_position)) or (
                    (following is not None) and (following.y_position < me.y_position)):  # Up
                lookup[0] = '1'
            if ((previous is not None) and (previous.y_position > me.y_position)) or (
                    (following is not None) and (following.y_position > me.y_position)):  # Down
                lookup[1] = '1'
            if ((previous is not None) and (previous.x_position < me.x_position)) or (
                    (following is not None) and (following.x_position < me.x_position)):  # Left
                lookup[2] = '1'
            if ((previous is not None) and (previous.x_position > me.x_position)) or (
                    (following is not None) and (following.x_position > me.x_position)):  # Right
                lookup[3] = '1'

            lookup = ''.join(lookup)

            print(grid_path_lookup[lookup], end='')

        print(VERTICAL)  # Newline and Boarder

    print(BOTTOM_LEFT + HORIZONTAL * grid.x_size + BOTTOM_RIGHT)  # Boarder
