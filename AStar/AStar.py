# Algorithm
# Look for lowest F cost and expand on that node first
# 	In the case of same F costs for many nodes, chose the lowest H cost
# 	In the case of same H costs then go randomly
# When looking at a node, update the costs of the nodes around it
#	Mark the nodes checked
# 	Make them smaller if that is the case, else don’t change
# When you reach the end, follow the path of parents
from AStar import Node


class AStar:
    def __init__(self, start: Node | None = None, end: Node | None = None):
        # All the nodes that can be evaluated next
        self.open: list[Node] = []
        # All the nodes that have been evaluated
        # Nodes here can be updated still though
        self.closed: list[Node] = []

        # The start and end
        self.start: Node | None = start
        self.end: Node | None = end

        # If the end node has been reached
        self.end_reached: bool = False

        # Add the start to the open list
        if self.start is not None:
            self.open.append(self.start)

    def reset(self):
        """
Resets the algorithm.
        """

        self.open = []
        self.closed = []

        self.start = None
        self.end = None

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
Also calls reset
        :param node: The new ending node.
        """

        self.reset()

        self.end = node

    def _process_node(self, current_node, processing_node: Node):
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

        # Create its G costs
        # Currently just uses the sum of the x and y displacements
        x_diff = abs(self.start.x_position - processing_node.x_position)
        y_diff = abs(self.start.y_position - processing_node.y_position)
        potential_g_cost = x_diff + y_diff

        # If the g cost is smaller than the current g cost
        if (processing_node.g_cost is None) or (potential_g_cost < processing_node.g_cost):
            # Set its parent to me
            processing_node.parent = current_node

            # Give it its new G cost
            processing_node.g_cost = potential_g_cost

            # Generate and give it is new H cost
            x_diff = abs(self.end.x_position - processing_node.x_position)
            y_diff = abs(self.end.y_position - processing_node.y_position)
            new_h_cost = x_diff + y_diff
            processing_node.h_cost = new_h_cost

    def _pass(self) -> bool:
        """
Performs a pass of the algorithm.
        :return: True if the end node has been reached
        """

        # Get all nodes with the minimum F cost
        potential_nodes = Node.get_all_lowest_f_cost(self.open)

        # Get all nodes with the minimum H cost
        # Not strictly necessary
        potential_nodes = Node.get_all_lowest_h_cost(potential_nodes)

        # Get the fist index of the min H cost nodes
        node: Node = potential_nodes[0]

        # Check if it is the end node
        if node == self.end:
            return True

        # Move the node from open to closed
        self.open.remove(node)
        self.closed.append(node)

        # Get all of its connections
        connected_nodes = node.get_connected_nodes()

        # Process all the connected nodes
        for connected_node in connected_nodes:
            self._process_node(node, connected_node)

        return False
