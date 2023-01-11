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
    def __init__(self, start: Node, end: Node):
        # All
        self.open: list[Node] = []
        self.closed: list[Node] = []

        self.start: Node = start
        self.end: Node = end
