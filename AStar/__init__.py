"""
My attempt at implementing the A* pathfinding algorithm.
"""

# Errors, huh
import AStar.Errors

# The basics, need to come first as they are used by almost everything
from ._Node import Node
from ._Connection import Connection

# Used by the algorithm so this needs to come before it
from ._Path import Path

# Ways of generating nodes
import AStar.NodeGenerator

# The algorithm
from ._AStar import AStar
