from ._Connection import Connection
from ._Node import Node


class Grid:
    def __init__(self, x_size: int, y_size: int):
        # Store size
        self.x_size: int = x_size
        self.y_size: int = y_size

        # Populate the grid
        self.grid: list[list[Node]] = [[Node(x, y) for x in range(x_size)] for y in range(y_size)]

        # Add horizontal connections
        for y in range(y_size):
            for x in range(x_size - 1):
                Connection.create_connection_between(self.grid[y][x], self.grid[y][x + 1], 1)

        # Add vertical connections
        for y in range(y_size - 1):
            for x in range(x_size):
                Connection.create_connection_between(self.grid[y][x], self.grid[y + 1][x], 1)

    def __getitem__(self, coords: tuple[int, int]) -> Node:
        """
Returns the node at the given coordinates.
Raises an IndexError of the coords are out of bounds.
Does not work with slices.
        :param coords: The coordinates of the node to lookup.
        :return: The node at the coordinates.
        """

        x, y = coords

        # Check for within bounds
        if x < 0 or x >= self.x_size:
            raise IndexError(f"Provided x coordinate '{x}' is not within the bounds [0, {self.x_size})")
        if y < 0 or y >= self.y_size:
            raise IndexError(f"Provided y coordinate '{y}' is not within the bounds [0, {self.y_size})")

        return self.grid[y][x]

    def reset(self):
        """
Resets all nodes in the grid.
        """

        for y in range(self.y_size):
            for x in range(self.x_size):
                self.grid[y][x].reset()
