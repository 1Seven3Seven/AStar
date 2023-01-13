import AStar
from AStar import AsciiPrint


def main():
    grid = AStar.Grid(10, 10)

    a_star = AStar.AStar(start=grid[0, 0], end=grid[9, 9])

    for x in range(grid.x_size):
        if x == 5:
            continue

        grid[x, 5].remove_all_connections()

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
    print()  # Spacing


if __name__ == "__main__":
    main()

    input("Enter to exit")
