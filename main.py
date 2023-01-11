import AStar
from AStar import AsciiPrinter

# ToDo: Black some nodes out so they can't be used in the path.


def main():
    grid = AStar.Grid(10, 10)

    a_star = AStar.AStar(start=grid[0, 0], end=grid[9, 9])

    path = a_star.find_path()

    print("\nNode Parents\n")
    AsciiPrinter.print_grid_node_parents(grid)

    print("\nPath Generated\n")
    AsciiPrinter.print_grid_with_path(grid, path)

    print()  # Spacing
    print(f"Passes performed {a_star.passes_performed}")
    print()  # Spacing


if __name__ == "__main__":
    main()

    input("Enter to exit")
