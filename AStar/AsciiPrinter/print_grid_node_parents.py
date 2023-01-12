from AStar import Grid


def print_grid_node_parents(grid: Grid):
    """
Prints the given grid.
If a node has a parent then there will be an arrow pointing to it, otherwise just a square.
    :param grid: The grid to print.
    """

    print('┌' + '─' * grid.x_size + '┐') # Boarder
    for y in range(grid.y_size):
        print('│', end='')  # Boarder
        for x in range(grid.x_size):

            # If no parent
            if grid[x, y].parent is None:
                if grid[x, y].connections:
                    print(' ', end='')
                else:
                    print('█', end='')
                continue

            child = grid[x, y]
            parent = child.parent

            if parent.x_position > child.x_position:  # To the right
                char = '→'
            elif parent.x_position < child.x_position:  # To the left
                char = '←'
            elif parent.y_position < child.y_position:  # Above
                char = '↑'
            else:  # Below
                char = '↓'

            print(char, end='')

        print('│')  # Newline and Boarder

    print('└' + '─' * grid.x_size + '┘') # Boarder
