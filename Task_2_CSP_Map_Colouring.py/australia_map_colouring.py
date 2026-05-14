"""
Task 2A: Australia Map Colouring using Constraint Satisfaction Problem

Objective:
Colour Australian regions using three colours so that no two adjacent regions
have the same colour.
"""

from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt


TASK_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = TASK_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

COLORS = ["Red", "Green", "Blue"]


def show_plots_if_interactive():
    # Show the graph only when a display window is available.
    if "agg" not in plt.get_backend().lower():
        plt.show()
    plt.close("all")

australia_graph = {
    # Each region is listed together with its neighbours.
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}


def is_valid(region, color, assignment):
    # A colour is allowed if no neighbour has the same colour.
    for neighbor in australia_graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def backtrack(assignment):
    # If all regions have colours, the answer is complete.
    if len(assignment) == len(australia_graph):
        return assignment

    # Pick the next region that has not been coloured.
    unassigned = [region for region in australia_graph if region not in assignment]
    region = unassigned[0]

    for color in COLORS:
        if is_valid(region, color, assignment):
            # Try this colour first.
            assignment[region] = color

            result = backtrack(assignment)
            if result:
                return result

            # Remove the colour if it does not lead to a solution.
            del assignment[region]

    return None


def visualize_solution(solution):
    # Draw the map as a graph so the colours can be seen.
    graph = nx.Graph()

    for region, neighbors in australia_graph.items():
        for neighbor in neighbors:
            graph.add_edge(region, neighbor)

    graph.add_node("T")

    color_map = [solution[node].lower() for node in graph.nodes()]

    pos = nx.spring_layout(graph, seed=42)

    plt.figure(figsize=(9, 7))
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=color_map,
        node_size=2500,
        font_size=12,
        font_weight="bold",
        edge_color="black"
    )

    plt.title("Australia Map Colouring using CSP")
    output_path = OUTPUT_DIR / "australia_map_colouring.png"
    plt.savefig(output_path, dpi=300)
    show_plots_if_interactive()
    return output_path


def main():
    solution = backtrack({})

    print("=" * 60)
    print("AUSTRALIA MAP COLOURING CSP SOLUTION")
    print("=" * 60)

    if solution:
        for region, color in solution.items():
            print(f"{region} -> {color}")

        output_path = visualize_solution(solution)
        print(f"\nVisualization saved: {output_path}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
