from ._Node import Node


class Connection:
    def __init__(self, node1: Node, node2: Node, weight: int):
        self.node1: Node = node1
        self.node2: Node = node2

        self.weight: int = weight

    @staticmethod
    def create_connection_between(node1: Node, node2: Node, weight: int) -> None:
        """
Connects the two nodes by creating a connection class and putting it inside the connections list of both nodes.
Does nothing if there is already a connection.
        """

        # Checking for a connection
        for connection in node1.connections:
            if connection.node1 == node1 and connection.node2 == node2:
                return

            if connection.node1 == node2 and connection.node2 == node1:
                return

        # If no connection than create one
        new_connection = Connection(node1, node2, weight)

        # Add it to the nodes
        node1.connections.append(new_connection)
        node2.connections.append(new_connection)