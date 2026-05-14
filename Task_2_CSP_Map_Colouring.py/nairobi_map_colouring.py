"""
Task 2B: Nairobi Sub-County Map Colouring using CSP

Objective:
Colour Nairobi's 17 sub-counties using the least possible number of colours
while ensuring adjacent sub-counties do not share the same colour.

Note:
This uses a simplified adjacency graph for practical simulation.
"""

from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt


TASK_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = TASK_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

COLORS = ["Red", "Green", "Blue", "Yellow"]


nairobi_graph = {
    # This is a simplified graph of Nairobi sub-counties and neighbours.
    "Westlands": ["Dagoretti North", "Starehe"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra"],
    "Dagoretti South": ["Dagoretti North", "Langata", "Kibra"],
    "Langata": ["Dagoretti South", "Kibra"],
    "Kibra": ["Dagoretti North", "Dagoretti South", "Langata", "Starehe"],
    "Roysambu": ["Kasarani", "Ruaraka"],
    "Kasarani": ["Roysambu", "Ruaraka", "Embakasi North"],
    "Ruaraka": ["Roysambu", "Kasarani", "Mathare", "Starehe"],
    "Embakasi South": ["Embakasi North", "Embakasi Central", "Embakasi East"],
    "Embakasi North": ["Kasarani", "Embakasi South", "Embakasi Central"],
    "Embakasi Central": ["Embakasi North", "Embakasi South", "Embakasi East"],
    "Embakasi East": ["Embakasi Central", "Embakasi South", "Embakasi West"],
    "Embakasi West": ["Embakasi East", "Makadara"],
    "Makadara": ["Embakasi West", "Kamukunji", "Starehe"],
    "Kamukunji": ["Makadara", "Starehe"],
    "Starehe": ["Westlands", "Kibra", "Ruaraka", "Mathare", "Makadara", "Kamukunji"],
    "Mathare": ["Ruaraka", "Starehe"]
}


def show_plots_if_interactive():
    # Show the graph only when a display window is available.
    if "agg" not in plt.get_backend().lower():
        plt.show()
    plt.close("all")


def is_valid(area, color, assignment):
    # A colour is valid if neighbouring areas do not use it.
    for neighbor in nairobi_graph[area]:
        if assignment.get(neighbor) == color:
            return False
    return True


def backtrack(assignment, colors):
    # If every sub-county has a colour, then we are done.
    if len(assignment) == len(nairobi_graph):
        return assignment

    # Pick the next sub-county that is not yet coloured.
    unassigned = [area for area in nairobi_graph if area not in assignment]
    area = unassigned[0]

    for color in colors:
        if is_valid(area, color, assignment):
            # Try this colour and continue.
            assignment[area] = color

            result = backtrack(assignment, colors)
            if result:
                return result

            # Remove the colour if it fails later.
            del assignment[area]

    return None


def find_minimum_colours():
    # Try one colour, then two, then more until it works.
    for number_of_colours in range(1, len(COLORS) + 1):
        selected_colours = COLORS[:number_of_colours]
        solution = backtrack({}, selected_colours)

        if solution:
            return solution, selected_colours

    return None, []


def visualize_solution(solution):
    # Draw the final colouring as a graph.
    graph = nx.Graph()

    for area, neighbors in nairobi_graph.items():
        for neighbor in neighbors:
            graph.add_edge(area, neighbor)

    color_map = [solution[node].lower() for node in graph.nodes()]

    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(graph, seed=7)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=color_map,
        node_size=3000,
        font_size=8,
        font_weight="bold",
        edge_color="gray"
    )

    plt.title("Nairobi Sub-County Colouring using CSP")
    output_path = OUTPUT_DIR / "nairobi_map_colouring.png"
    plt.savefig(output_path, dpi=300)
    show_plots_if_interactive()
    return output_path


def main():
    solution, used_colours = find_minimum_colours()

    print("=" * 60)
    print("NAIROBI SUB-COUNTY MAP COLOURING CSP SOLUTION")
    print("=" * 60)

    if solution:
        print(f"Minimum colours used: {len(used_colours)}")
        print(f"Colours: {used_colours}\n")

        for area, color in solution.items():
            print(f"{area} -> {color}")

        output_path = visualize_solution(solution)
        print(f"\nVisualization saved: {output_path}")
    else:
        print("No valid colouring found.")


if __name__ == "__main__":
    main()
