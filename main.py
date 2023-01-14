from AStar import AStar
from AStar import AsciiPrint
from AStar import NodeGenerator


def main():
    grid = NodeGenerator.Grid(10, 10)

    a_star = AStar(start=grid[0, 0], end=grid[9, 9])

    for x in range(grid.x_size):
        if x == 5:
            continue

        grid[x, 5].traversable = False

    print("\nInitial State\n")
    AsciiPrint.Grid.node_parents(grid, start_node=a_star.start, end_node=a_star.end)

    print("\nGenerating Paths")
    path = a_star.find_path()

    print("\nNode Parents\n")
    AsciiPrint.Grid.node_parents(grid, start_node=a_star.start, end_node=a_star.end)

    print("\nPath Generated\n")
    AsciiPrint.Grid.with_path(grid, path)

    print()  # Spacing
    print(f"Passes performed {a_star.passes_performed}")
    print(f"Path length {len(path)}")
    print()  # Spacing


if __name__ == "__main__":
    main()

    input("Enter to exit")
