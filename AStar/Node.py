from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .Connection import Connection


class Node:
    def __init__(self):
        # Distance from the starting node
        self.g_cost: int = 0
        # Distance from the end node (heuristic)
        self.h_host: int = 0

        # The connections to other nodes
        self.connections: list['Connection'] = []

        # The node which points to this one
        self.parent: 'Node' | None = None

    @property
    def f_cost(self):
        # G cost + H cost
        return self.g_cost + self.h_host

    def get_connected_nodes(self) -> list['Node']:
        """
Returns a list of the connected nodes found in self.connections.
        """

        connected_nodes: list['Node'] = []

        for connection in self.connections:
            if connection.node1 != self:
                connected_nodes.append(connection.node1)
                continue

            connected_nodes.append(connection.node2)

        return connected_nodes

    def __str__(self):
        return f"Node - G: {self.g_cost}, H: {self.h_host}, F: {self.f_cost}"
