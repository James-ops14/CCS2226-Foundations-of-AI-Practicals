"""
Task 4: Breadth First Search and Depth First Search

Objective:
Write Python programs to perform:
1. Breadth First Search
2. Depth First Search

The program outputs the search path from the initial node to the goal state
and saves a graph visualization.
"""

from collections import deque
from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt


TASK_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = TASK_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def show_plots_if_interactive():
    # Show the graph only when a display window is available.
    if "agg" not in plt.get_backend().lower():
        plt.show()
    plt.close("all")


graph = {
    # This is the graph that BFS and DFS will search through.
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": [],
    "G": ["J"],
    "H": [],
    "I": ["J"],
    "J": []
}


def breadth_first_search(graph, start, goal):
    # BFS uses a queue and checks nodes level by level.
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            # Stop when the goal is found.
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                # Add this possible path to the queue.
                new_path = path + [neighbor]
                queue.append(new_path)

    return None


def depth_first_search(graph, start, goal, path=None):
    # DFS goes deep into one branch before trying the next one.
    if path is None:
        path = []

    path = path + [start]

    if start == goal:
        # Stop when the goal is reached.
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            # Continue searching from this neighbour.
            new_path = depth_first_search(graph, neighbor, goal, path)

            if new_path:
                return new_path

    return None


def visualize_graph(bfs_path, dfs_path):
    # Draw the graph and highlight the BFS and DFS paths.
    G = nx.DiGraph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 7))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        node_color="lightgray",
        font_size=12,
        font_weight="bold",
        arrows=True
    )

    bfs_edges = list(zip(bfs_path, bfs_path[1:]))
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=bfs_edges,
        edge_color="green",
        width=3,
        label="BFS Path"
    )

    plt.title("Graph Search Visualization: BFS Path Highlighted")
    bfs_output_path = OUTPUT_DIR / "bfs_path_visualization.png"
    plt.savefig(bfs_output_path, dpi=300)
    show_plots_if_interactive()

    plt.figure(figsize=(10, 7))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        node_color="lightgray",
        font_size=12,
        font_weight="bold",
        arrows=True
    )

    dfs_edges = list(zip(dfs_path, dfs_path[1:]))
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=dfs_edges,
        edge_color="red",
        width=3,
        label="DFS Path"
    )

    plt.title("Graph Search Visualization: DFS Path Highlighted")
    dfs_output_path = OUTPUT_DIR / "dfs_path_visualization.png"
    plt.savefig(dfs_output_path, dpi=300)
    show_plots_if_interactive()
    return bfs_output_path, dfs_output_path


def main():
    start_node = "A"
    goal_node = "J"

    bfs_path = breadth_first_search(graph, start_node, goal_node)
    dfs_path = depth_first_search(graph, start_node, goal_node)

    print("=" * 60)
    print("BREADTH FIRST SEARCH AND DEPTH FIRST SEARCH")
    print("=" * 60)
    print(f"Initial Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    print(f"BFS Search Path: {' -> '.join(bfs_path)}")
    print(f"DFS Search Path: {' -> '.join(dfs_path)}")

    bfs_output_path, dfs_output_path = visualize_graph(bfs_path, dfs_path)

    print("\nVisualizations saved:")
    print(f"- {bfs_output_path}")
    print(f"- {dfs_output_path}")


if __name__ == "__main__":
    main()
