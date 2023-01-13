from AStar import Node


class Path:
    """
Contains a path between two nodes.
The start and end nodes are provided upon initialisation.
The path is generated when generate_path is called.
"""

    def __init__(self, start: Node, end: Node):
        self.start: Node = start
        self.end: Node = end

        # Contains the path of nodes in order from the start to the end
        self.path: list[Node] = []

    def __getitem__(self, index):
        """
Returns the node at the index for the path.
        :param index: Index of the node to lookup.
        :return: The node at the index.
        """

        return self.path[index]

    def generate_path(self):
        """
Generates the path between the start and end nodes given during initialization.
Assumes:
    The AStar class has been used.
    There is a valid path.
    Each node in the valid path has a parent (set by the AStar class).
        """

        # Reset the path
        self.path = []

        # Add the end
        self.path.append(self.end)

        current_node = self.end

        while current_node is not self.start:
            # Get the next node
            current_node = current_node.parent
            # Add it to the list
            self.path.append(current_node)

        # Reverse the list
        self.path.reverse()
