from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ._Connection import Connection


class Node:
    def __init__(self, x_position: int, y_position: int):
        # Position
        self.x_position = x_position
        self.y_position = y_position

        # Distance from the starting node
        self.g_cost: int | None = None
        # Distance from the end node (heuristic)
        self.h_cost: int | None = None

        # The connections to other nodes
        self.connections: list['Connection'] = []

        # The node which points to this one
        self.parent: 'Node' | None = None

    @property
    def f_cost(self):
        # G cost + H cost
        return self.g_cost + self.h_cost

    def reset(self):
        """
Resets the node's G and H costs, connections and parent.
        """

        self.g_cost = None
        self.h_cost = None
        self.connections = []
        self.parent = None

    def remove_all_connections(self):
        """
Calls remove on all connections.
        """

        for connection in self.connections:
            connection.remove()

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

    @staticmethod
    def get_all_lowest_f_cost(list_of_nodes: list['Node']) -> list['Node']:
        """
Returns a list of all nodes that have the lowest F cost in the given list.
        :param list_of_nodes: List of nodes to be handled.
        :return: List of nodes with the lowest F cost.
        """

        # Get the minimum F cost
        min_f_cost = min([node.f_cost for node in list_of_nodes])

        # Get all node with the same minimum F cost
        all_min_f_cost_nodes = [
            node for node in list_of_nodes if node.f_cost == min_f_cost
        ]

        # Return them
        return  all_min_f_cost_nodes

    @staticmethod
    def get_all_lowest_h_cost(list_of_nodes: list['Node']) -> list['Node']:
        """
Returns a list of all nodes that have the lowest H cost in the given list.
        :param list_of_nodes: List of nodes to be handled.
        :return: List of nodes with the lowest H cost.
        """

        # Get the minimum F cost
        min_h_cost = min([node.h_cost for node in list_of_nodes])

        # Get all node with the same minimum F cost
        all_min_h_cost_nodes = [
            node for node in list_of_nodes if node.h_cost == min_h_cost
        ]

        # Return them
        return  all_min_h_cost_nodes

    def __str__(self):
        return f"Node - G: {self.g_cost}, H: {self.h_cost}, F: {self.f_cost}"
