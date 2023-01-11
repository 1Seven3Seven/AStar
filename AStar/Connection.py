from .Node import Node


class Connection:
    def __init__(self, node1: Node, node2: Node, weight: int):
        self.node1: Node = node1
        self.node2: Node = node2

        self.weight: int = weight
