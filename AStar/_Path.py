from AStar import Node


class Path:
    """
Contains a path between two nodes
    """
    
    def __init__(self):
        self.start: Node
        self.end: Node

        self.path: list[Node]
