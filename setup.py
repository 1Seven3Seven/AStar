import sys

from setuptools import setup

# Make sure python 3.7 or greater
assert sys.version_info.major == 3 and sys.version_info.minor >= 7, "The AStar repo is designed to work with python 3.7 and greater.\nPlease install it."

# Get the requirements
with open("requirements.txt", 'r') as f:
    requirements = f.read().splitlines()

# Get the version
with open("AStar/version.txt", 'r') as f:
    ASTAR_VERSION = f.read().strip()

# Setup time
setup(
    name="AStar",
    version=ASTAR_VERSION,
    install_requires=requirements,
    description="An implementation of the A* pathfinding algorithm by Seven"
)
