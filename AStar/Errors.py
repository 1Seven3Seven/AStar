class PathNotFound(Exception):
    """
Used when the AStar class has no more nodes in the open list and the end node was not reached.
    """


class ConnectionNotFound(Exception):
    """
Used when looking for a connection between nodes and no connections are found.
    """
