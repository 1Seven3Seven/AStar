from AStar import Grid, Node
from AStar.AsciiPrint.Grid._boarder_chars import *


def node_parents(grid: Grid, start_node: Node | None = None, end_node: Node | None = None):
    """
Prints the given grid.
If a node has a parent then there will be an arrow pointing to it, otherwise nothing.
    :param grid: The grid to print.
    :param start_node: If provided then the start node is displayed as an 'S'.
    :param end_node: If provided then the end node is displayed as an 'E'.
    """

    print(TOP_LEFT + HORIZONTAL * grid.x_size + TOP_RIGHT)  # Boarder

    for y in range(grid.y_size):
        print(VERTICAL, end='')  # Boarder

        for x in range(grid.x_size):

            # If start or end node
            if grid[x, y] is start_node:
                print('S', end='')
                continue
            if grid[x, y] is end_node:
                print('E', end='')
                continue

            # If no parent
            if grid[x, y].parent is None:
                if grid[x, y].connections:
                    print(' ', end='')
                else:
                    print('█', end='')
                continue

            # Get parent and child in an easier to read form
            child = grid[x, y]
            parent = child.parent

            # Find the direction of the arrow to print
            if parent.x_position > child.x_position:  # To the right
                char = '→'
            elif parent.x_position < child.x_position:  # To the left
                char = '←'
            elif parent.y_position < child.y_position:  # Above
                char = '↑'
            else:  # Below
                char = '↓'

            print(char, end='')

        print(VERTICAL)  # Newline and Boarder

    print(BOTTOM_LEFT + HORIZONTAL * grid.x_size + BOTTOM_RIGHT)  # Boarder
