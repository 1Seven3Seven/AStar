from Connection import Connection
from Node import Node


class Grid:
    def __init__(self, x_size: int, y_size: int):
        # Store size
        self.x_size: int = x_size
        self.y_size: int = y_size

        # Populate the grid
        self.grid: list[list[Node]] = [[Node() for _ in range(x_size)] for _ in range(y_size)]

        # Add horizontal connections
        for y in range(y_size):
            for x in range(x_size - 1):
                new_connection = Connection(self.grid[y][x], self.grid[y][x + 1], 1)
                self.grid[y][x].connections.append(new_connection)
                self.grid[y][x + 1].connections.append(new_connection)

        # Add vertical connections
        for y in range(y_size - 1):
            for x in range(x_size):
                new_connection = Connection(self.grid[y][x], self.grid[y + 1][x], 1)
                self.grid[y][x].connections.append(new_connection)
                self.grid[y + 1][x].connections.append(new_connection)
