from AStar._Connection import Connection
from AStar._Node import Node


class Grid:
    def __init__(self,
                 x_size: int, y_size: int,
                 direct_connections: bool = True,
                 diagonal_connections: bool = False):
        """
        :param x_size: The width of the grid.
        :param y_size: The height of the grid.
        :param direct_connections: If the nodes should be connected to their direct neighbours, up, down, left, right.
        :param diagonal_connections: If the nodes should be connected to their diagonal neighbours.
        """

        # Store size
        self.x_size: int = x_size
        self.y_size: int = y_size

        # Populate the grid
        self.grid: list[list[Node]] = [[Node(x, y) for x in range(x_size)] for y in range(y_size)]

        # Types of connections
        self.direct_connections = direct_connections
        self.diagonal_connections = diagonal_connections

        # Add direct connections
        if direct_connections:
            # Horizontal
            for y in range(y_size):
                for x in range(x_size - 1):
                    Connection.create_connection_between(self.grid[y][x], self.grid[y][x + 1], 1)
            # Vertical
            for y in range(y_size - 1):
                for x in range(x_size):
                    Connection.create_connection_between(self.grid[y][x], self.grid[y + 1][x], 1)

        # Add the diagonal connections
        if diagonal_connections:
            for a in range(y_size):
                for b in range(x_size):
                    for u in (-1, 1):
                        for v in (-1, 1):
                            # Get the x coordinate
                            x = a + u
                            if x < 0:
                                continue
                            if x >= x_size:
                                continue

                            # Get the y coordinate
                            y = b + v
                            if y < 0:
                                continue
                            if y >= y_size:
                                continue

                            # Create the connection
                            Connection.create_connection_between(
                                self.grid[a][b], self.grid[y][x], 1
                            )

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
