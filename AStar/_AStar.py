from typing import Callable

from AStar import Node, Path
from AStar.Errors import PathNotFound


def _default_heuristic(end_node: Node, processing_node: Node) -> int:
    """
The default heuristic used when no heuristic is provided.
Just the sum of the x and y displacements
    :param end_node: The node the algorithm wants to meet.
    :param processing_node: The current node being processed.
    :return:
    """

    x_diff = abs(end_node.x_position - processing_node.x_position)
    y_diff = abs(end_node.y_position - processing_node.y_position)
    return x_diff + y_diff


class AStar:
    def __init__(self,
                 start: Node | None = None,
                 end: Node | None = None,
                 heuristic: Callable[[Node, Node], int] | None = None):
        # All the nodes that can be evaluated next
        self.open: list[Node] = []
        # All the nodes that have been evaluated
        # Nodes here can be updated still though
        self.closed: list[Node] = []

        # The start and end
        self.start: Node | None = start
        self.end: Node | None = end

        # The number of passes performed
        self.passes_performed: int = 0

        # If the end node has been reached
        self.end_reached: bool = False

        # Add the start to the open list
        if self.start is not None:
            self.open.append(self.start)

        # The heuristic for the H cost
        self.heuristic: Callable[[Node, Node], int] = _default_heuristic if heuristic is None else heuristic

    def reset(self):
        """
Resets the algorithm and allows for find_path to be run again.
Specifically:
    The open and closed lists.
    The number of passes performed.
    Whether the end node has been reached.
        """

        self.open = []
        self.closed = []

        self.passes_performed = 0

        self.end_reached = False

    def set_start(self, node: Node):
        """
Sets the new starting node.
Also calls reset.
        :param node: The new starting node.
        """

        self.reset()

        # New start
        self.start = node

        # New open list
        self.open.append(node)

    def set_end(self, node: Node):
        """
Sets the new ending node.
Also calls reset.
        :param node: The new ending node.
        """

        self.reset()

        self.end = node

    def _process_start_node(self):
        """
Called before _process_node should be called.
Generates the G and H costs for the starting node.
        """

        self.start.h_cost = self.heuristic(self.end, self.start)
        self.start.g_cost = 0

    def _process_node(self, current_node: Node, processing_node: Node):
        """
Processes the given node by:
    Adding it to the list of open nodes if it is not already in the open or closed lists.
    Generating and setting its G and H costs if applicable.
    Setting its parent node if applicable.
        :param current_node: The current node being handled.
        :param processing_node: Node to be processed
        """

        # If not in closed and not in open then add to open
        if processing_node not in self.closed:
            if processing_node not in self.open:
                self.open.append(processing_node)
        else:
            return

        # Find the connection between the current node and the node being processed
        connection = current_node.find_connection_with(processing_node)

        # Create its G cost
        potential_g_cost = current_node.g_cost + connection.weight

        # If the g cost is smaller than the current g cost
        if (processing_node.g_cost is None) or (potential_g_cost < processing_node.g_cost):
            # Give it its new G cost
            processing_node.g_cost = potential_g_cost

            # Set its parent to me
            processing_node.parent = current_node

            # Generate and give it is new H cost
            processing_node.h_cost = self.heuristic(self.end, processing_node)

    def _pass(self):
        """
Performs a pass of the algorithm.
If there is no nodes inside the open list then an error is raised.
        """

        # Check for open nodes
        if not self.open:
            raise PathNotFound

        # Get all nodes with the minimum F cost
        potential_nodes = Node.get_all_lowest_f_cost(self.open)

        # Get all nodes with the minimum H cost
        # Not strictly necessary
        potential_nodes = Node.get_all_lowest_h_cost(potential_nodes)

        # Get the fist index of the min H cost nodes
        node: Node = potential_nodes[0]

        # Move the node from open to closed
        self.open.remove(node)
        self.closed.append(node)

        # Check if it is the end node
        if node is self.end:
            self.end_reached = True
            self.passes_performed += 1
            return

        # Get all of its connections
        connected_nodes = node.get_connected_nodes()

        # Process all the connected nodes
        for connected_node in connected_nodes:
            self._process_node(node, connected_node)

        self.passes_performed += 1
        return

    def find_path(self):
        """
Finds a path from the start node to the end node.
If there is no nodes inside the open list then an error is raised.
        :return: Nothing in so far.
        """

        # Sanity checks
        assert self.start is not None, "Start node must be set"
        assert self.end is not None, "End node must be set"
        assert self.open, "Open list must only contain the start node"
        assert len(self.open) == 1, "Open list must only contain the start node"
        assert self.open[0] is self.start, "Open list must only contain the start node"
        assert not self.closed, "Closed list must be empty"
        assert not self.end_reached, "End condition must not start as True"
        assert self.start is not self.end, "Start must not be the end"

        # Generate the G and H costs of the starting node
        self._process_start_node()

        # Run until the end has been reached
        while not self.end_reached:
            self._pass()

        # If we get here then the end has been reached without an error being raised, create the path
        path = Path(self.start, self.end)
        path.generate_path()

        # Return the path
        return path
